# Requirements Document

## Introduction

This feature adds automated, event-driven citation extraction to the `dataframe-elephant` workspace. Today, the ingestion pipeline (`src/ingest_citations.py`) must be run manually after research Markdown files are added or updated. The goal is to trigger that pipeline automatically whenever a `.md` file is saved or created inside `research/raw/`, keeping `data/citations.duckdb` and `data/citation_ingestion_warnings.jsonl` continuously up to date without requiring a manual command.

The feature has two complementary delivery mechanisms:

1. **Hook-based auto-trigger** — Kiro `PostFileCreate` and `PostFileSave` hooks invoke the ingestion pipeline whenever a `.md` file under `research/raw/` changes.
2. **On-demand agent scan** — A named agent command re-runs ingestion across the full corpus at any time, useful after bulk imports or when hook output needs to be reviewed.

Both paths reuse the existing deterministic `build_database` function. No new parsing logic is introduced. All existing idempotency, warning, and provenance guarantees are preserved.

---

## Glossary

- **Ingestion_Pipeline**: The `build_database` function in `src/ingest_citations.py` that reads all Markdown files under `research/raw/`, extracts structured citation tables, and writes `data/citations.duckdb` and `data/citation_ingestion_warnings.jsonl`.
- **Hook**: A Kiro automation file stored under `.kiro/hooks/` that fires on workspace file events (`PostFileCreate`, `PostFileSave`) and executes a shell command or agent prompt.
- **Run_Record**: A row in the `ingestion_run` table that identifies a specific execution of the Ingestion_Pipeline by `run_id`, `built_at`, `parser_version`, and `input_root`.
- **Warning_Artifact**: The `data/citation_ingestion_warnings.jsonl` file produced by each Ingestion_Pipeline execution, containing one JSON object per warning with `warning_id`, `run_id`, `input_path`, `warning_type`, `message`, and `raw_value`.
- **Citation_Database**: The DuckDB file at `data/citations.duckdb` that holds all ingested documents, sources, occurrences, aliases, claims, and claim-source mappings.
- **Research_File**: Any `.md` file located anywhere under `research/raw/` (including subdirectories).
- **Internal_Evaluation_File**: A Research_File whose filename is `First-Ratings.md`; the Ingestion_Pipeline records it as `document_type = 'internal_evaluation'` and does not extract claims from it.
- **Trigger_Event**: A `PostFileCreate` or `PostFileSave` hook event raised by Kiro when a Research_File is written.
- **On_Demand_Scan**: A user-initiated agent command that re-runs the Ingestion_Pipeline over the full `research/raw/` corpus.
- **Stable_ID**: A deterministic SHA-256-derived identifier computed from content rather than insertion order, ensuring the same source or document always receives the same ID across runs.
- **Idempotent_Rebuild**: A property of the Ingestion_Pipeline whereby running it twice against an unchanged corpus produces identical row counts, identical Stable_IDs, and an identical Warning_Artifact.

---

## Requirements

### Requirement 1: Hook-Based Automatic Triggering

**User Story:** As a researcher, I want the citation database to update automatically whenever I save a research Markdown file, so that I never need to remember to run the ingestion command manually.

#### Acceptance Criteria

1. WHEN a `.md` file is created under `research/raw/`, THE Hook SHALL synchronously invoke the Ingestion_Pipeline and wait for its exit code before the hook action completes.
2. WHEN a `.md` file is saved under `research/raw/`, THE Hook SHALL synchronously invoke the Ingestion_Pipeline and wait for its exit code before the hook action completes.
3. THE Hook SHALL pass the workspace-relative paths anchored at the workspace root for `--raw-dir`, `--database`, `--warnings`, and `--schema` arguments to the Ingestion_Pipeline invocation so that no hard-coded absolute paths are required.
4. IF the Ingestion_Pipeline exits with a non-zero status code, THEN THE Hook SHALL write the full standard error output of the Ingestion_Pipeline to the hook's own stderr stream so the researcher can see what failed.
5. THE Hook SHALL NOT invoke the Ingestion_Pipeline for file save or create events outside the `research/raw/` directory tree.
6. THE Hook SHALL NOT invoke the Ingestion_Pipeline more than once per atomic save event on a single file (no duplicate triggers for the same event).

---

### Requirement 2: On-Demand Full-Corpus Scan

**User Story:** As a researcher, I want to be able to re-run citation extraction across the entire corpus on demand, so that I can recover from a missed trigger, rebuild after a bulk import, or verify the current state of the database.

#### Acceptance Criteria

1. WHEN the researcher invokes the On_Demand_Scan command, THE Ingestion_Pipeline SHALL process every `.md` file under `research/raw/` including subdirectories.
2. WHEN the On_Demand_Scan completes successfully, THE Ingestion_Pipeline SHALL report the exact counts of documents, sources, citation occurrences, claims, claim-source mappings, and warnings written during that run to the researcher on standard output.
3. THE Ingestion_Pipeline SHALL complete the On_Demand_Scan without requiring the researcher to supply file paths or arguments beyond invoking the command.
4. IF a previous Citation_Database already exists at `data/citations.duckdb`, THEN THE Ingestion_Pipeline SHALL delete it and create a new database at the same path rather than appending rows to the existing file.
5. IF the On_Demand_Scan fails before producing a complete new Citation_Database, THEN THE Ingestion_Pipeline SHALL leave the pre-existing `data/citations.duckdb` file unchanged.
6. IF the Ingestion_Pipeline encounters a parse error for a single Research_File during the On_Demand_Scan, THEN THE Ingestion_Pipeline SHALL record a warning for that file and continue processing the remaining files rather than aborting the scan.

---

### Requirement 3: Idempotency and Stable Identifiers

**User Story:** As a researcher, I want repeated ingestion runs against unchanged files to produce the same database content, so that I can rebuild without accumulating duplicate rows or changing existing IDs.

#### Acceptance Criteria

1. WHEN the Ingestion_Pipeline is run twice against the same set of Research_Files with no content changes between runs, THE Ingestion_Pipeline SHALL produce identical row counts in every table.
2. WHEN the Ingestion_Pipeline is run twice against the same set of Research_Files with no content changes between runs, THE Ingestion_Pipeline SHALL assign identical Stable_IDs to every document, source, occurrence, alias, claim, and claim-source row.
3. WHEN the Ingestion_Pipeline is run twice against the same set of Research_Files with no content changes between runs, THE Warning_Artifact SHALL contain identical warning records (same `warning_id` values, same order by `input_path` ascending then `warning_id` ascending).
4. THE Ingestion_Pipeline SHALL NOT use insertion-order, timestamps, or random values as inputs when computing Stable_IDs.
5. THE Ingestion_Pipeline SHALL derive each Stable_ID exclusively from the byte content of the source Research_File and the structural position of the element within that file (e.g., table index, row index, column name), so that the same element in the same file always yields the same ID.
6. WHEN the Ingestion_Pipeline processes a Research_File whose path and byte content are identical to a file processed in a previous run, THE Ingestion_Pipeline SHALL produce identical output rows for that file without re-parsing or re-inserting any data that would change existing row values.

---

### Requirement 4: Atomic Database Write

**User Story:** As a researcher, I want the citation database file to remain readable and consistent even if the ingestion run fails partway through, so that a failed build never corrupts the last good snapshot.

#### Acceptance Criteria

1. THE Ingestion_Pipeline SHALL write all new data to a temporary database file located in the same directory as the Citation_Database before replacing the live Citation_Database.
2. WHEN the Ingestion_Pipeline completes all inserts and commits successfully, THE Ingestion_Pipeline SHALL replace the existing Citation_Database with the temporary file in a single atomic rename operation such that no intermediate state is observable to concurrent readers.
3. IF the Ingestion_Pipeline encounters any error before the commit, THEN THE Ingestion_Pipeline SHALL leave the existing Citation_Database file byte-for-byte unchanged.
4. IF the Ingestion_Pipeline encounters any error before the commit, THEN THE Ingestion_Pipeline SHALL delete the temporary database file before exiting, leaving no partial temporary file on disk.
5. IF the rename operation in criterion 2 fails, THEN THE Ingestion_Pipeline SHALL retain the temporary database file undeleted and emit an error message indicating the Citation_Database was not replaced, so the operator can recover the completed temporary file manually.

---

### Requirement 5: Warning and Provenance Capture

**User Story:** As a researcher, I want every ingestion run to record its provenance and surface all parsing problems, so that I can audit which files were processed and track down incomplete citations.

#### Acceptance Criteria

1. WHEN the Ingestion_Pipeline completes a run, THE Ingestion_Pipeline SHALL write a Run_Record to the `ingestion_run` table containing the `run_id`, `built_at` timestamp, `parser_version`, and `input_root`.
2. WHEN the Ingestion_Pipeline completes a run, THE Ingestion_Pipeline SHALL write one `ingestion_input` row per Research_File processed, recording the workspace-relative path, SHA-256 content hash, and last-modified timestamp; IF the operating system does not report a last-modified timestamp for a file, THEN THE Ingestion_Pipeline MAY store NULL for that field.
3. WHEN a source row lacks a resolvable direct URL, THE Ingestion_Pipeline SHALL write a warning object containing the fields `warning_id`, `run_id`, `input_path`, `warning_type` set to `source_rows_lacking_direct_urls`, `message`, and `raw_value` to the Warning_Artifact.
4. WHEN a source row has multiple URL candidates that cannot be disambiguated, THE Ingestion_Pipeline SHALL write a warning of type `duplicate_candidate` to the Warning_Artifact and set `resolution_status = 'ambiguous'` on the corresponding occurrence row.
5. WHEN a claim-like table row lacks an explicit `claim_type` or `confidence` value, THE Ingestion_Pipeline SHALL write a warning of type `unsupported_table_shape` to the Warning_Artifact and SHALL NOT insert a row into the `claim` table for that row.
6. THE Ingestion_Pipeline SHALL write the Warning_Artifact to `data/citation_ingestion_warnings.jsonl`, with each warning object containing the fields `warning_id`, `run_id`, `input_path`, `warning_type`, `message`, and `raw_value`, sorted by `input_path` ascending then `warning_id` ascending, with one JSON object per line.
7. IF a Warning_Artifact already exists at `data/citation_ingestion_warnings.jsonl` when a run begins, THEN THE Ingestion_Pipeline SHALL overwrite it with the new run's warnings rather than appending to it.
8. THE Ingestion_Pipeline SHALL commit all ingestion data rows, provenance rows (`ingestion_run`, `ingestion_input`), and warning rows to the database in a single transaction, so that either all records from a run are present or none are.

---

### Requirement 6: Research_File Scope and Classification

**User Story:** As a researcher, I want the ingestion pipeline to correctly classify each Markdown document type so that internal evaluation files are never counted as independent external evidence.

#### Acceptance Criteria

1. THE Ingestion_Pipeline SHALL ingest every `.md` file found under `research/raw/` at any subdirectory depth as a `research_document` row with `document_type = 'research_document'` and `is_internal = FALSE`, unless overridden by a classification rule.
2. WHEN a Research_File's filename matches `First-Ratings.md` (case-sensitive), THE Ingestion_Pipeline SHALL set `document_type = 'internal_evaluation'` and `is_internal = TRUE` on its `research_document` row.
3. IF a `research_document` row has `is_internal = TRUE`, THEN THE Ingestion_Pipeline SHALL NOT create any `citation_occurrence` rows linked to that document, and SHALL leave any previously extracted claim rows for that document unchanged.
4. THE `source_recurrence` view SHALL compute `distinct_documents` as the count of distinct `research_document` identifiers and `total_occurrences` as the count of `citation_occurrence` rows, restricted in both cases to documents where `is_internal = FALSE`.
5. WHEN a Markdown file is located under `analysis/` and its filename matches `First-Ratings.md` (case-sensitive), THE Ingestion_Pipeline SHALL ingest it as a `research_document` row with `document_type = 'internal_evaluation'` and `is_internal = TRUE`.

---

### Requirement 7: Source Resolution and Alias Preservation

**User Story:** As a researcher, I want every citation occurrence to preserve its raw text and resolution status, so that I can review unresolved aliases and fix them without losing the original data.

#### Acceptance Criteria

1. THE Ingestion_Pipeline SHALL retain in `raw_citation_text` the pipe-joined concatenation of all cell values in the Markdown table row that produced the occurrence, unchanged from the parsed Markdown source.
2. WHEN a source row resolves to exactly one canonical URL, THE Ingestion_Pipeline SHALL set `resolution_status = 'resolved'` on the occurrence row and store the `source_id`.
3. WHEN a source row resolves to zero canonical URLs, THE Ingestion_Pipeline SHALL set `resolution_status = 'unresolved'` on the occurrence row and leave `source_id` as NULL.
4. WHEN a source row contains multiple URL candidates, THE Ingestion_Pipeline SHALL set `resolution_status = 'ambiguous'` on the occurrence row and leave `source_id` as NULL.
5. THE Ingestion_Pipeline SHALL write exactly one `source_alias` row per `citation_occurrence` row, recording the alias value as the occurrence's local label if present, otherwise the source title; the `match_method` field SHALL be set to `'exact'` for resolved occurrences and `'none'` for unresolved or ambiguous occurrences; and the `resolution_status` field SHALL mirror the value set on the corresponding occurrence row.
6. THE Ingestion_Pipeline SHALL NOT perform fuzzy matching to auto-merge ambiguous or unresolved sources; unresolved aliases SHALL remain visible in the `source_alias` table for manual review.

---

### Requirement 8: Hook Configuration and Discoverability

**User Story:** As a researcher, I want the hook configuration to be stored in the workspace so that the automation is reproducible and visible to anyone working in the same project.

#### Acceptance Criteria

1. THE Hook SHALL be defined as a JSON file named `ingest-citations.json` under `.kiro/hooks/`, containing at minimum the fields `triggers`, `matcher`, `actionType`, and `command`, with `triggers` set to include both `PostFileCreate` and `PostFileSave`.
2. THE Hook SHALL use a `matcher` field containing a regular expression that restricts firing to file paths matching `research/raw/.*\.md`.
3. THE Hook configuration file SHALL be tracked by version control, meaning the path `.kiro/hooks/ingest-citations.json` is not excluded by `.gitignore` or any nested ignore file in the workspace.
4. THE Hook SHALL set `actionType` to `command` and set `command` to invoke the Python interpreter using the relative path `.venv/Scripts/python` on Windows or `.venv/bin/python` on POSIX systems, rather than a bare `python` or `python3` executable name.

---

### Requirement 9: Incremental File Cache

**User Story:** As a researcher, I want the ingestion pipeline to skip re-parsing files that have not changed since the last run, so that hook-triggered builds complete quickly even as the corpus grows.

#### Acceptance Criteria

1. WHEN the Ingestion_Pipeline starts and a Citation_Database already exists at `data/citations.duckdb`, THE Ingestion_Pipeline SHALL read the most recent `ingestion_run` record and its associated `ingestion_input` rows to build a cache of `{workspace-relative-path: sha256}` entries from that run.
2. WHEN a Research_File's workspace-relative path and SHA-256 content hash both match an entry in the file cache, THE Ingestion_Pipeline SHALL classify that file as unchanged and SHALL NOT re-parse it.
3. WHEN a Research_File is classified as unchanged, THE Ingestion_Pipeline SHALL copy its existing `research_document`, `source`, `citation_occurrence`, `source_alias`, `claim`, and `claim_source` rows from the previous Citation_Database into the new temporary database rather than re-deriving them.
4. WHEN a Research_File is classified as unchanged, THE Ingestion_Pipeline SHALL still write a new `ingestion_input` row for that file under the current `run_id`, recording its path, SHA-256, and last-modified timestamp.
5. WHEN a Research_File's SHA-256 content hash differs from the cached value, or when the file has no cache entry, THE Ingestion_Pipeline SHALL classify that file as changed and SHALL re-parse it in full.
6. THE Ingestion_Pipeline SHALL produce, in the `research_document`, `source`, `citation_occurrence`, `source_alias`, `claim`, and `claim_source` tables, row sets identical to a full rebuild for the same set of Research_Files regardless of whether the incremental cache was used; `ingestion_run` and `ingestion_input` rows are exempt from this constraint.
7. IF the Citation_Database does not exist, cannot be opened for reading, or contains no `ingestion_run` rows when the Ingestion_Pipeline starts, THE Ingestion_Pipeline SHALL fall back to a full rebuild without error.
8. WHEN a source row carried forward from an unchanged file has the same `source_id` as a source row produced by parsing a changed file, and both have non-null `evidence_class` values that differ, THE Ingestion_Pipeline SHALL set `evidence_class = NULL` on the merged source row and write a warning of type `classification_conflict` to the Warning_Artifact.
9. WHEN the Ingestion_Pipeline carries forward rows from unchanged files, THE Ingestion_Pipeline SHALL also carry forward all `ingestion_warning` rows associated with those files' paths from the previous run, so that the warning log reflects all known issues in the corpus regardless of which files were re-parsed.

---

### Requirement 10: Source Domain Categorisation and Evidence Tier

**User Story:** As a researcher, I want every extracted source and citation occurrence to carry a structured category label at extraction time, so that I can filter and compare citations by topic domain and evidence strength without manual tagging.

#### Acceptance Criteria

1. THE Ingestion_Pipeline SHALL assign a `domain_category` value to every `source` row at extraction time using the source's `canonical_url`, `title`, and `publisher` fields as inputs.
2. THE `domain_category` field SHALL be drawn from a closed enumeration: `compliance_regulation`, `ai_ml_technology`, `workflow_process`, `market_research`, `technical_standard`, `academic_research`, `organizational`, `uncategorised`.
3. IF `canonical_url`, `title`, and `publisher` are all null, empty, or match no classification rule, THEN THE Ingestion_Pipeline SHALL assign `domain_category = 'uncategorised'`.
4. THE Ingestion_Pipeline SHALL assign an `evidence_tier` value to every `citation_occurrence` row at extraction time by performing a case-insensitive string match of the occurrence's `recorded_classification` field against the values `primary`, `secondary`, and `internal`.
5. THE `evidence_tier` field SHALL be drawn from a closed enumeration: `tier_1_primary`, `tier_2_secondary`, `tier_3_tertiary`, `unclassified`.
6. IF `recorded_classification` contains the substring `primary` (case-insensitive), THEN THE Ingestion_Pipeline SHALL set `evidence_tier = 'tier_1_primary'`.
7. IF `recorded_classification` contains the substring `secondary` (case-insensitive), THEN THE Ingestion_Pipeline SHALL set `evidence_tier = 'tier_2_secondary'`.
8. IF `recorded_classification` contains the substring `internal` (case-insensitive), THEN THE Ingestion_Pipeline SHALL set `evidence_tier = 'tier_3_tertiary'`.
9. IF `recorded_classification` is absent, empty, or does not contain any of the substrings `primary`, `secondary`, or `internal`, THEN THE Ingestion_Pipeline SHALL set `evidence_tier = 'unclassified'`.
10. THE `domain_category` and `evidence_tier` values SHALL be stored as columns in the `source` and `citation_occurrence` tables respectively, and SHALL be queryable without joining to any other table.
11. WHEN the Ingestion_Pipeline carries forward unchanged rows from the file cache (Requirement 9), THE `domain_category` and `evidence_tier` values from the previous run SHALL be preserved unchanged in the copied rows.
12. WHEN classifying `domain_category` and multiple fields match different category rules, THE Ingestion_Pipeline SHALL apply precedence in the order `canonical_url` first, then `publisher`, then `title`, and SHALL assign the category matched by the highest-precedence field.
