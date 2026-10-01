# Hook-Based Auto-Trigger Extraction Protocol

## Status

This protocol governs every hook-triggered and on-demand execution of the citation ingestion pipeline in this workspace. It applies to the Kiro automation layer, the `build_database` function in `src/ingest_citations.py`, and any process that reads or writes `data/citations.duckdb` or `data/citation_ingestion_warnings.jsonl`.

---

## 1. Purpose

Define the end-to-end extraction process so that:

- The citation database stays continuously up to date without manual intervention.
- Every ingestion run is traceable, auditable, and reproducible.
- Failures are visible and recoverable, never silent.
- The database is never left in a corrupt or partial state.

---

## 2. Trigger Mechanisms

The extraction pipeline can be started in two ways.

### 2.1 Hook-Based Auto-Trigger (primary path)

A Kiro hook defined at `.kiro/hooks/ingest-citations.json` watches the `research/raw/` directory tree.

**Trigger events:**

| Event | Condition |
| --- | --- |
| `PostFileCreate` | A new `.md` file is created anywhere under `research/raw/` |
| `PostFileSave` | An existing `.md` file is saved anywhere under `research/raw/` |

**File path filter:** The hook `matcher` field restricts firing to paths matching the regular expression `research/raw/.*\.md`. Events outside `research/raw/` do not trigger extraction.

**Execution model:** The hook runs synchronously. It invokes the pipeline and waits for the process exit code before completing. If the pipeline exits non-zero, the hook writes the full stderr output to its own stderr stream so the error is visible in the Kiro session.

**Python interpreter:** The hook invokes `.venv/Scripts/python` on Windows or `.venv/bin/python` on POSIX. It does not use a bare `python` or `python3` system executable.

**Arguments passed:** The hook passes all required paths as workspace-relative arguments:

```
.venv/Scripts/python src/ingest_citations.py \
  --raw-dir research/raw \
  --database data/citations.duckdb \
  --warnings data/citation_ingestion_warnings.jsonl \
  --schema schemas/citations.sql
```

No hard-coded absolute paths are used.

### 2.2 On-Demand Full-Corpus Scan (secondary path)

A researcher or agent can trigger a full rebuild at any time without supplying arguments. This is the recovery path after bulk imports, missed triggers, or database verification needs.

**When to use on-demand scan:**

- After adding multiple research files at once without saving them individually.
- After restoring or replacing the `research/raw/` directory from backup.
- To verify the database reflects the current corpus state.
- When reviewing the warning output after a large batch of edits.

**Output:** On successful completion, the pipeline prints counts to standard output:

```
documents:           N
sources:             N
citation_occurrences: N
claims:              N
claim_source_links:  N
warnings:            N
```

---

## 3. Extraction Process — Step by Step

### Step 1: File Discovery

The pipeline scans `research/raw/` recursively for all `.md` files. Files are sorted by workspace-relative path, case-folded, so processing order is deterministic across operating systems.

For each discovered file, the pipeline records:

- Workspace-relative path
- SHA-256 content hash
- Last-modified timestamp (nullable if the OS does not report it)

The sorted list of `path\0sha256` pairs plus the `PARSER_VERSION` string is hashed to produce the `run_id`. An unchanged corpus always produces the same `run_id`.

### Step 2: Document Classification

Each `.md` file is assigned a document type before any tables are parsed.

| Condition | `document_type` | `is_internal` |
| --- | --- | --- |
| Filename is `First-Ratings.md` (case-sensitive) anywhere | `internal_evaluation` | `TRUE` |
| Filename is `Citation.md` | `citation_registry` | `FALSE` |
| Filename is `Report.md` under a `Citations/` directory | `source_quality_report` | `FALSE` |
| Title contains `Structured Research` or `Research Brief` | `research_brief` | `FALSE` |
| All other files | `research_note` | `FALSE` |

Internal evaluation files (`is_internal = TRUE`) are ingested as document rows but **no citation occurrences or claims are extracted from them**. They are excluded from the `source_recurrence` view's `distinct_documents` and `total_occurrences` counts.

### Step 3: Table Parsing

For each non-internal document, the pipeline parses every Markdown table. A valid table requires:

- A header row containing `|`-separated column names.
- A separator row immediately below it (cells matching `:?---+:?`).
- One or more data rows.

Two table kinds are recognised:

**Source tables** — identified by the presence of a title/citation/source column plus at least one of: a URL column, a publisher column, or a classification column.

**Claim tables** — identified by the presence of a `claim`, `claim text`, or `assertion` column.

All other tables are skipped.

### Step 4: Source Extraction

For each row in a source table:

1. The raw cell text of the entire row is captured verbatim as `raw_citation_text` (pipe-joined concatenation of all cell values).
2. URL candidates are extracted from the URL column and the title column using a URL pattern regex. Tracking parameters (`utm_*`, `fbclid`, `gclid`, `mc_cid`, `mc_eid`) are stripped and URLs are canonicalised.
3. **Resolution logic:**

| URL candidates found | `resolution_status` | `source_id` |
| --- | --- | --- |
| Exactly 1 | `resolved` | SHA-256-derived stable ID |
| More than 1 | `ambiguous` | NULL |
| 0 | `unresolved` | NULL |

4. For resolved sources, a `source` row is created. If the same source (by canonical URL or by publisher+title identity) appears in multiple files, its metadata is merged: the `evidence_class` is preserved if consistent, or set to NULL if conflicting.
5. A `citation_occurrence` row is written for every source table row regardless of resolution status.
6. Exactly one `source_alias` row is written per occurrence. The alias value is the local label (e.g. `S1`) if present, otherwise the source title. The `match_method` is `canonical_url` for resolved sources and `unresolved` for all others.

### Step 5: Claim Extraction

Claim extraction runs only for documents where `is_internal = FALSE`.

For each row in a claim table, the pipeline checks for three required fields: `claim` (or `claim text` / `assertion`), `claim type`, and `confidence`. If any required field is absent or unrecognised:

- A warning of type `unsupported_table_shape` is written.
- The row is **skipped** — no partial claim row is inserted.

For valid claim rows, a `claim` row is inserted and one or more `claim_source` rows are created by resolving local source labels (e.g. `S1`) against the document's local alias map.

### Step 6: Stable ID Assignment

All primary keys are deterministic SHA-256-derived identifiers. No auto-increment, timestamp, or random component is used.

| Entity | Identity input |
| --- | --- |
| `document` | Workspace-relative path (case-folded) |
| `source` | `url:<canonical_url>` or `publisher:<host>\|title:<normalised_title>` |
| `citation_occurrence` | `document_id + row_index + raw_row` |
| `source_alias` | `document_id + row_index + alias_value` |
| `claim` | `document_id + claim_type + confidence + normalised_claim_text` |
| `claim_source` | `claim_id + source_id + relationship + evidence_locator` |
| `warning` | `run_id + input_path + warning_type + message + raw_value` |
| `run` | Sorted `path\0sha256` pairs + `PARSER_VERSION` |

Running the pipeline twice against an identical corpus always produces the same IDs.

### Step 7: Atomic Database Write

The pipeline never writes directly to `data/citations.duckdb` during a run.

1. All data is written to a temporary file in `data/` named `citations.tmp.<hash>.duckdb`.
2. On successful commit of all tables in a single transaction, the temporary file is renamed to `citations.duckdb` in one atomic operation.
3. If any error occurs before the commit, the temporary file is deleted and the existing `citations.duckdb` is left byte-for-byte unchanged.
4. If the rename itself fails, the temporary file is retained and an error is emitted so the completed data can be recovered manually.

### Step 8: Warning and Provenance Recording

On completion of every run, the pipeline writes:

**To the database (same transaction as all ingestion data):**

- One `ingestion_run` row: `run_id`, `built_at`, `parser_version`, `input_root`.
- One `ingestion_input` row per processed file: workspace-relative path, SHA-256 hash, last-modified timestamp.

**To `data/citation_ingestion_warnings.jsonl`:**

One JSON object per line, sorted by `input_path` ascending then `warning_id` ascending. The file is replaced on every run — it is never appended to.

Each warning object contains exactly:

```json
{
  "warning_id": "warn_<24-char hex>",
  "run_id": "run_<24-char hex>",
  "input_path": "research/raw/...",
  "warning_type": "<type>",
  "message": "Human-readable description",
  "raw_value": "The raw cell text or value that triggered the warning"
}
```

---

## 4. Warning Types Reference

| `warning_type` | Meaning | Action required |
| --- | --- | --- |
| `source_rows_lacking_direct_urls` | Source has a publisher-domain URL only, no page path | Review and add a direct URL if available |
| `duplicate_candidate` | Multiple URL candidates found in one row; source left ambiguous | Disambiguate by cleaning the URL or splitting into separate rows |
| `missing_title` | Source row has no title cell | Add a title to the Markdown table row |
| `unsupported_table_shape` | Claim-like table row missing `claim_type` or `confidence` | Fix the table structure or remove the row |
| `truncated_url` | URL appears cut off or incomplete | Replace with the full URL |
| `weak_source_classification` | Classification value does not map to `primary`, `secondary`, or `internal` | Correct the classification column value |
| `classification_conflict` | Same source appears with conflicting evidence classes across files | Reconcile the classification in the source files |
| `unresolved_alias` | A local label used in a claim row does not map to exactly one source | Ensure the label appears in the source table with a resolvable URL |

---

## 5. Correctness Properties

The following properties must hold after every run. They can be verified programmatically.

1. **Idempotency** — Running the pipeline twice against an unchanged corpus produces identical row counts in every table, identical Stable_IDs, and an identical Warning_Artifact.
2. **No partial writes** — `data/citations.duckdb` is either the previous complete snapshot or the new complete snapshot. It is never in an intermediate state.
3. **No claim rows from internal files** — No `citation_occurrence` or `claim` row has a `document_id` whose corresponding `research_document.is_internal` is `TRUE`.
4. **One alias per occurrence** — Every `citation_occurrence` row has exactly one corresponding `source_alias` row.
5. **Warning completeness** — Every row that triggered a warning during parsing has a corresponding warning entry in `data/citation_ingestion_warnings.jsonl`.
6. **Provenance completeness** — Every file discovered during a run has a corresponding `ingestion_input` row in the same transaction.
7. **Source recurrence view accuracy** — `source_recurrence.distinct_documents` and `total_occurrences` count only rows linked to documents where `is_internal = FALSE`.

---

## 6. Failure and Recovery Procedures

### Pipeline exits non-zero during hook trigger

1. Read the stderr output surfaced by the hook.
2. Check whether `data/citations.duckdb` is intact — it should be unchanged from the previous run.
3. Correct the cause (malformed Markdown, missing schema file, import error).
4. Re-save the research file to re-trigger the hook, or run the on-demand scan.

### Hook does not fire on file save

1. Confirm `.kiro/hooks/ingest-citations.json` exists and is not listed in `.gitignore`.
2. Verify the `matcher` regex (`research/raw/.*\.md`) covers the saved file's path.
3. Confirm the virtual environment exists at `.venv/` and the Python interpreter is present.
4. Run the on-demand scan manually as a fallback.

### Temporary file left on disk

If a file matching `data/citations.tmp.*.duckdb` exists after a failed run, it means the rename step failed after a successful commit. The file contains a complete, valid database. To recover:

```powershell
Move-Item -Force data\citations.tmp.<hash>.duckdb data\citations.duckdb
```

### Warning count unexpectedly high

1. Open `data/citation_ingestion_warnings.jsonl` and group by `warning_type`.
2. Use the Warning Types Reference in section 4 to identify the required action for each type.
3. Fix the source files, then re-trigger extraction.

---

## 7. Hook Configuration Reference

The hook file at `.kiro/hooks/ingest-citations.json` must conform to the Kiro hook schema:

```json
{
  "version": "v1",
  "hooks": [
    {
      "name": "Auto-ingest citations",
      "trigger": "PostFileSave",
      "matcher": "research/raw/.*\\.md",
      "action": {
        "type": "command",
        "command": ".venv/Scripts/python src/ingest_citations.py --raw-dir research/raw --database data/citations.duckdb --warnings data/citation_ingestion_warnings.jsonl --schema schemas/citations.sql"
      }
    },
    {
      "name": "Auto-ingest citations (new file)",
      "trigger": "PostFileCreate",
      "matcher": "research/raw/.*\\.md",
      "action": {
        "type": "command",
        "command": ".venv/Scripts/python src/ingest_citations.py --raw-dir research/raw --database data/citations.duckdb --warnings data/citation_ingestion_warnings.jsonl --schema schemas/citations.sql"
      }
    }
  ]
}
```

This file must not be excluded by `.gitignore` so that the automation is reproducible for any collaborator or agent working in the same workspace.

---

## 8. Update Triggers

Re-review this protocol when any of the following occurs:

- The `build_database` function signature or argument names change.
- New document types are added to the classification logic.
- New warning types are introduced in `src/ingest_citations.py`.
- The DuckDB schema in `schemas/citations.sql` is modified.
- The Kiro hook schema or trigger event names change.
- The virtual environment path or Python version requirement changes.
