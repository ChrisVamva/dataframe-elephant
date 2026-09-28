# Report 1: Citation Intelligence Database review

**Date:** 2026-09-27
**Reviewer:** automated review pass, run at the project owner's request
**Scope:** `src/ingest_citations.py`, `src/tests/test_ingest_citations.py`, `schemas/citations.sql`, `analysis/citation_evaluator.sql`, the generated artifacts in `data/`, and the setup documentation around them
**Environment:** conda environment `datascience` (Miniforge), DuckDB 1.5.5, pytest 9.1.1
**Out of scope:** the quality of the research content itself, which is governed by `Protocols/Research-Evaluation.md`

## Status

The pipeline works today. The build completes, `python -m pytest src/tests -q` is 7 of 7 green, `schemas/citations.sql` applies cleanly, and all 9 statements of `analysis/citation_evaluator.sql` run against DuckDB without error. Nothing in this report claims the current snapshot is wrong.

What this report does claim:

- two latent ways the build can destroy its own artifact (F1, F2);
- one instance of source-file corruption (F3);
- one path where a recorded classification is dropped with no warning (F4);
- three places where the review workflow does not surface what it claims to (F5, F6, F7);
- hygiene, documentation, and coverage gaps (F8 to F15).

Snapshot measured during this review: 15 documents, 207 sources, 455 citation occurrences (215 resolved, 197 unresolved, 43 ambiguous), 455 aliases (215 matched by canonical URL, 240 unresolved), 0 claims, 0 claim-source mappings, 604 ingestion warnings.

## Method

- Read `src/ingest_citations.py` and `src/tests/test_ingest_citations.py` in full.
- Executed both SQL files against DuckDB: the schema first, then each evaluator statement.
- Queried the built snapshot and the warnings artifact for counts and for every field the views expose.
- Reproduced each suspected defect with a minimal synthetic input in a temporary directory.
- Byte-scanned `src/` for encoding damage and control characters.

## Findings summary

| ID | Severity | Finding | Location |
| --- | --- | --- | --- |
| F1 | High | A failed build leaves the database emptied rather than unchanged | `build_database` delete/insert block |
| F2 | High | Two claim rows whose text normalizes to the same value abort the build | `_parse_claim_row` claim identifier |
| F3 | Medium | A raw control character plus a dead duplicate line in `normalize_url` | `src/ingest_citations.py` line 49 |
| F4 | Medium | An unmapped classification is dropped silently, and its warning is unreachable | `_source_row_data` |
| F5 | Medium | The "unknown status" triage query matches 207 of 207 sources | `_source_row_data`, evaluator query 4 |
| F6 | Medium | All 15 documents carry NULL evaluation metadata although the decisions exist | `_document_metadata`, `_metadata_value`, corpus layout |
| F7 | Medium | 604 warnings and 240 unresolved aliases are unreachable from the evaluator queries | `analysis/citation_evaluator.sql` |
| F8 | Low | Bare `pytest` fails with `ModuleNotFoundError: No module named 'src'` | no pytest configuration |
| F9 | Low | No git repository and no `.gitignore` for large regenerable artifacts | repository root |
| F10 | Low | `.venv/` is stale and cannot import DuckDB | `.venv/` |
| F11 | Low | Root `README.md` structure tree and directory guide are out of date | `README.md` |
| F12 | Low | Documentation conflict about where `First-Ratings.md` belongs | `data/README.md`, `Plans and Actions/` |
| F13 | Low | Every rebuild discards the previous run record | `build_database` delete order |
| F14 | Low | Several warning types and failure branches have no test coverage | `src/tests/` |
| F15 | Low | A "status" column is mapped to claim type | `_claim_columns` |

## F1 - High - A failed build empties the database

**Evidence.** The rebuild is not atomic. `build_database` deletes the tables in three separate transactions, each followed by its own `COMMIT`, and only then opens a fourth transaction to insert the new rows. If any insert raises, the `ROLLBACK` in the exception handler can only undo that fourth transaction; the three delete transactions are already durable. The warnings file is written after the database work, so a failed build also leaves `data/citation_ingestion_warnings.jsonl` describing a state that no longer matches the database.

**Reproduction.** A temporary corpus containing a single document with two claim rows (see F2) produced:

```
BUILD FAILED: ConstraintException: PRIMARY KEY or UNIQUE constraint violation: duplicate key "clm_897826b5607ec4d4a0fa8c1e"
post-failure row counts:
  ingestion_run 0   ingestion_input 0   research_document 0   source 0
  citation_occurrence 0   claim 0   claim_source 0   ingestion_warning 0
```

**Impact.** One bad row in the corpus turns the snapshot into an empty database, and the previous snapshot is not recoverable from the file. The promise in `data/README.md` that a rebuild "replaces the derived tables ... rather than appending duplicate rows" holds only on the success path. Because claim ingestion is the stated next step, the probability of a first failure is not low.

**Smallest corrective action.** Perform the deletes and the inserts in a single transaction, keeping the existing child-before-parent delete order:

```python
try:
    connection.execute("BEGIN TRANSACTION")
    for table in (
        "claim_source", "source_alias", "citation_occurrence", "ingestion_warning",
        "ingestion_input", "claim", "source", "research_document", "ingestion_run",
    ):
        connection.execute(f"DELETE FROM {table}")
    _insert_rows(connection, "ingestion_run", [...])
    _insert_rows(connection, "ingestion_input", [...])
    _insert_rows(connection, "research_document", document_rows)
    _insert_rows(connection, "source", list(source_records.values()))
    _insert_rows(connection, "citation_occurrence", occurrence_rows)
    _insert_rows(connection, "source_alias", alias_rows)
    _insert_rows(connection, "claim", claim_rows)
    _insert_rows(connection, "claim_source", claim_source_rows)
    _insert_rows(connection, "ingestion_warning", warnings)
    connection.execute("COMMIT")
except Exception:
    connection.execute("ROLLBACK")
    raise
```

A stronger variant builds into a temporary database file and replaces the target only after a successful commit, which also protects the artifact if the process is killed mid-transaction.

**Verification.** Repeat the F2 reproduction and confirm the build still raises while the pre-existing row counts in `data/citations.duckdb` are unchanged.

## F2 - High - Claim rows that normalize to the same text abort the build

**Evidence.** The claim identifier is content-derived: `stable_id("clm", document_id + NUL + _normalized_text(claim_text))`, and `_normalized_text` collapses whitespace and case-folds. Two rows that differ only in case or spacing therefore produce the same primary key. Nothing de-duplicates, merges, or warns before the insert, and `_insert_rows` performs a plain multi-row insert.

**Reproduction.** Two claim rows in one document, `The tool is fast` and `the tool is FAST`, both typed `documented fact` at `high` confidence against the same source, abort the build with the duplicate-key error quoted in F1.

**Impact.** The claim path currently has no real-data coverage (0 claims in the snapshot), so this surfaces exactly when the planned claim curation begins. Combined with F1, the first malformed claim table can empty the database.

**Smallest corrective action.** De-duplicate claim rows by `claim_id` before the insert and choose a policy: merge the two rows' `claim_source` entries and emit a warning, or make the identifier include the claim type, confidence, and source row so that near-duplicates remain separate and visible. A merge-only fix must also de-duplicate mapping rows: `claim_source_id` is built from claim, source, relationship, and locator, and the locator cell is normally empty, so merging two claims while keeping both mappings recreates the same collision in `claim_source`.

**Verification.** The reproduction builds successfully; the snapshot holds the number of claims and mappings the chosen policy predicts; a regression test covers the collision; the existing 7 tests stay green.

## F3 - Medium - Control character and dead duplicate line in `normalize_url`

**Evidence.** Line 49 of `src/ingest_citations.py` is:

```python
    value = raw_url.strip().strip("<>").rstrip(".,;:)d}")
```

The character between `)` and `d` is a raw `0x05` (ENQ) control byte rather than a printable character; the intended set was `".,;:)]}"`. Line 50 assigns the same variable again using the correct set, so line 49 is dead code. Byte 1322 of the file is `0x05`, and a byte scan of the whole `src/` tree found no other control character; the only other non-ASCII bytes are legitimate typographic quotes on line 356.

**Impact.** There is no runtime effect today, because line 50 overwrites the value. The risk is latent and specific: if the duplicate line is ever removed as obvious duplication, the surviving `rstrip` set strips trailing `d`, `)`, `}`, and `;`. Verified behaviour of that exact set, executed directly:

```
'https://example.org/docs/download'.rstrip(...)  ->  'https://example.org/docs/downloa'
'https://example.org/docs/x}'.rstrip(...)        ->  'https://example.org/docs/x'
'https://example.org/docs/x]'.rstrip(...)        ->  'https://example.org/docs/x]'
```

The corrupted set both truncates URLs ending in `d` and fails to strip the `]` it was meant to remove. The stray control byte also signals that some tool wrote this file with a broken encoding.

**Smallest corrective action.** Delete line 49 and keep line 50. Add a regression test for trailing punctuation stripping, and ideally a repository check that rejects control characters in source files.

**Verification.** `python -m pytest src/tests -q` stays green, and `normalize_url("https://example.org/docs/download")` returns the URL unchanged.

## F4 - Medium - An unmapped classification is dropped silently

**Evidence.** In `_source_row_data` the classification check sits inside the final `else` branch, which is reached only when a row yields *no* URL candidate. A row that resolves to a source through exactly one candidate never reaches it. Reproduction: a source table row with URL `https://example.org/docs/x` and classification `Mixed` produced exactly one source with `evidence_class = NULL` and **zero warnings**.

The same pattern is present in the real snapshot: 22 of 207 sources have NULL `evidence_class` (21 of them because the classification cell is empty, and 1 with the composite value `Mixed (Superset docs = Primary; metabase.com LP = Secondary)`), while the 604-line warnings artifact contains **zero** `weak_source_classification` entries.

**Impact.** An unmapped or composite classification disappears without a trace. Those 22 sources can never appear in the primary-evidence filter used by `source_reputation` and by evaluator query 2 (`authority_class = 'primary'`), and the reviewer is never told that a recorded classification was discarded. `Protocols/Research-Evaluation.md` requires conflicting and missing evidence to be recorded, and evidence class is one of the declared dimensions of the data contract.

**Smallest corrective action.** Move the classification check out of the `else` branch so that it fires whenever a non-empty classification maps to no evidence class, regardless of whether a URL resolved. Keep the existing `classification_conflict` warning for the name-merge path in `_merge_source_metadata`. Rows with an empty classification cell should stay silent, since there is nothing recorded to warn about.

**Verification.** The reproduction emits one `weak_source_classification` warning; a full rebuild raises that warning type from 0 to the number of unmapped rows (at least 1 for the composite value above); the suite stays green.

## F5 - Medium - The completeness triage query matches every source

**Evidence.** `_source_row_data` writes sentinel values for the quality dimensions it cannot derive: `status: "unknown"`, `directness: "unknown"`, `bias_notes: None`, `author: None`. Nothing later updates them. Measured in the snapshot: `status = 'unknown'` for all 207 sources, `directness = 'unknown'` for all 207, and `bias_notes` NULL for all 207.

The evaluator query documented as "Locate incomplete, weakly classified, unknown-status, or old source records" includes the predicate `lower(status) = 'unknown'` inside a seven-way `OR`. Because that predicate is true for every row, the query selects **207 of 207** sources (verified by running it against the snapshot), so it cannot be used to find anything.

**Impact.** The only data-completeness query in the review pack returns the whole table, which trains the reviewer to ignore it. Two dimensions the plan committed to keeping separate, status and directness, carry no information at all, and `source_reputation` exposes three constant columns. The distinction between "the source does not record a status" and "the source records that the status is unknown" has been lost at ingest time.

**Smallest corrective action.** Treat the two cases differently and re-scope the query:

- stop writing sentinels, leaving `status` and `directness` NULL when the source text does not state them, so "not recorded" stays distinguishable from "recorded as unknown";
- rewrite the triage query to target named gaps rather than any of seven conditions, for example one query for sources with no evidence class, one for sources with no usable page URL, and one for sources whose text explicitly says the status is unknown;
- populate `status`, `directness`, and `bias_notes` from the raw register columns in a later curation pass, when those values are actually present.

Clearing the sentinels alone does not fix the query: with NULL values the `status IS NULL` clause would then match everything instead. The query rewrite is the substantive part of the fix.

**Verification.** The triage queries return fewer rows than the source count, and every returned row can be explained by the specific gap named in its query.

## F6 - Medium - Evaluation metadata is empty for all 15 documents

**Evidence.** In the snapshot, `select count(*), count(evaluation_date), count(evaluation_decision), count(quality_rating) from research_document` returns `(15, 0, 0, 0)`, and the per-document listing shows NULL for all three columns on every row. There are two independent causes.

1. **Placement.** The document-level decisions live in `analysis/On Research/First-Ratings.md`, which contains 15 bold `Decision` lines and 15 bold `Research question` lines, one per ingested document. That path is outside the ingest root, so the file is never read: `is_internal` is 0 for every document in the snapshot, and the existing internal-artifact test only exercises a synthetic fixture. `Plans and Actions/Plan First Citation Intelligence Database.md` expected the file at `research/raw/First-Ratings.md`.
2. **Label style.** `_metadata_value` matches only a line-leading `Key: value` with an optional `-` or `*` bullet. Verified against the real function:

```
_metadata_value('Decision: Revise', ...)              ->  'Revise'
_metadata_value('- Decision: Revise', ...)            ->  'Revise'
_metadata_value('**Decision:** **Revise.**', ...)     ->  ''
_metadata_value('**Evaluation date:** 2026-09-27', ...) ->  ''
```

The project's evaluation records use the bold style, so even after the file is ingested, its decisions and dates would not be read.

**Impact.** Four schema columns, and the whole evaluation half of the data contract, are inert. The database cannot answer "which documents were accepted, revised, or rejected" even though `Protocols/Research-Evaluation.md` makes the decision a required field of every evaluation record.

**Smallest corrective action.** Extend `_metadata_value` to tolerate bold labels (strip a leading `**` or `__` and trailing `**`/`__` around the key), and add a test built from the bold style found in `First-Ratings.md`. Then choose how the file reaches the ingest root, either by moving a copy to `research/raw/` or by adding a second input root, so its 15 decisions land as an internal artifact with `is_internal = TRUE` and are excluded from external recurrence by the existing view logic.

**Verification.** A test asserting that a bold-labelled fixture yields the expected `evaluation_decision`, `evaluation_date`, and `quality_rating`; after ingesting the file, `count(evaluation_decision)` equals 15 and the internal document is flagged.

## F7 - Medium - The review queue is not reachable from the evaluator queries

**Evidence.** `analysis/citation_evaluator.sql` holds 9 statements and references `ingestion_warning` and `source_alias` zero times, although both tables exist in `schemas/citations.sql` and between them hold the material the plan describes as the review queue:

- 604 warnings: `source_rows_lacking_direct_urls` 335, `unresolved_alias` 225, `duplicate_candidate` 43, `unsupported_table_shape` 1;
- 240 alias rows with `match_method = 'unresolved'`, against 215 resolved by canonical URL.

**Impact.** The evaluator pack reports recurrence, reputation, coverage, conflicts, and next research candidates, but not the two largest data-quality signals in the snapshot. `data/README.md` tells the reader to use this file "for the initial review queries", yet the step the README itself names as the next curation task, reviewing unresolved source aliases, has no query. A reviewer must hand-write SQL against the JSONL or the tables to see any of it.

**Smallest corrective action.** Add two sections to `analysis/citation_evaluator.sql`: warnings grouped by `warning_type` and by input document with counts and one sample message, and unresolved aliases grouped by document and local label, ordered by document so the register can be corrected document by document. Both are DuckDB SQL over tables that already exist, so no ingestion change is needed.

**Verification.** Running the file returns those result sets, and both are non-empty against the current snapshot (604 and 240 rows respectively before grouping).

## F8 - Low - Bare `pytest` cannot collect the suite

**Evidence.**

```
pytest src/tests -q            ->  ModuleNotFoundError: No module named 'src'
python -m pytest src/tests -q  ->  7 passed
```

The import `from src.ingest_citations import ...` needs the repository root on `sys.path`. `python -m pytest` adds the current directory implicitly; the `pytest.exe` console script does not.

**Impact.** `data/README.md` documents the working form, so the project is not broken and the owner is not blocked. However any reviewer, task runner, editor integration, or CI job that invokes `pytest` directly gets a collection error that looks like a broken test suite. This was observed in practice during this review.

**Smallest corrective action.** Add a `pyproject.toml` with `[tool.pytest.ini_options]` and `pythonpath = ["."]`, or the equivalent `pytest.ini`. This makes both invocation styles work from the repository root without changing the tests.

**Verification.** Both `pytest src/tests -q` and `python -m pytest src/tests -q` report 7 passed.

## F9 - Low - No repository, and no ignore rules for regenerable artifacts

**Evidence.** There is no `.git` directory at the repository root. The only `.gitignore` files present are the ones generated inside `.pytest_cache/` and `.venv/`. Unguarded generated or machine-specific artifacts: `data/citations.duckdb` (12,595,200 bytes), `data/citation_ingestion_warnings.jsonl` (189,461 bytes), `.pytest_cache/`, and `.venv/` (498 files).

**Impact.** A first `git init` followed by `git add .` would stage a 12 MB binary database, a 185 KiB derived warning log, and a broken virtual environment, after which every rebuild would appear as a large binary diff.

**Smallest corrective action.** Initialise the repository and add a `.gitignore` excluding `.venv/`, `.pytest_cache/`, `data/citations.duckdb`, and `data/citation_ingestion_warnings.jsonl`. `data/README.md` states these artifacts are regenerable, so excluding them is the consistent default; if a specific snapshot should be preserved, commit it deliberately as a release artifact rather than as build output.

**Verification.** `git status --short` lists no `.duckdb`, `.jsonl`, `.venv`, or `.pytest_cache` entries.

## F10 - Low - The stale virtual environment contradicts the documented setup

**Evidence.** `.venv/` contains 498 files, but `import duckdb` fails inside it, while `data/README.md` now directs users to the `datascience` conda environment and `.vscode/settings.json` pins conda as the workspace default.

**Impact.** A reader who notices `.venv/` on disk and activates it, which is the instinct the previous documentation trained, gets `ModuleNotFoundError: No module named 'duckdb'` and may conclude that the project is broken.

**Smallest corrective action.** Either delete `.venv/`, or install `requirements.txt` into it and keep both environments working. Deleting it is the smaller change and matches the documented setup.

**Verification.** `.venv/` no longer exists, or `.venv/Scripts/python.exe -c "import duckdb"` succeeds.

## F11 - Low - The root README does not describe the current repository

**Evidence.** The structure tree and the directory guide in `README.md` omit `Plans and Actions/`, `Protocols/`, `Problems/`, `requirements.txt`, and `.vscode/`. They describe `schemas/` as "JSON schemas, data contracts, validations, types" although it holds the DuckDB DDL, and `analysis/` as "notebooks, reports, explorations" although it holds `citation_evaluator.sql` and the evaluation notes. There is no pointer to `data/README.md`, which is the only place the build is documented.

**Impact.** The root README is the entry point to the project, and following it does not lead to a reproducible build.

**Smallest corrective action.** Update the tree and directory guide to match the directories that exist, describe `schemas/` and `analysis/` accurately, and add a short build section linking to `data/README.md` and `Protocols/Research-Evaluation.md`.

**Verification.** Every directory named in the tree exists, and every top-level directory that exists is named.

## F12 - Low - Documentation conflict about `First-Ratings.md`

**Evidence.** `data/README.md` states that `First-Ratings.md` "if added later, is recorded as an internal evaluation artifact" and "is currently absent from the input corpus". `Plans and Actions/Plan First Citation Intelligence Database.md` lists it as a relevant file and its step 10 covers ingesting it as an internal artifact. The file exists at `analysis/On Research/First-Ratings.md`, so it is absent from the input corpus but present in the repository.

**Impact.** A reader cannot tell whether ingesting the file is the intended next step, an optional variant, or forbidden. The snapshot carries no evaluation metadata at all (F6), which is exactly what this file would supply.

**Smallest corrective action.** Decide the policy once, record it in `data/README.md`, and align the plan: either ingest the file (move or copy it under `research/raw/`, or extend the build with a second input root) or state explicitly that it stays outside the corpus and why. Then correct the sentence that says the file is absent, since it now misdescribes the repository.

**Verification.** `data/README.md` and the plan make the same statement about the same path, and the snapshot either contains the internal document or states why it does not.

## F13 - Low - Each rebuild discards the previous run record

**Evidence.** `build_database` deletes `ingestion_run` and `ingestion_input` in its third delete transaction before inserting the new run. The snapshot contains exactly 1 row in `ingestion_run`. Because `run_id` is derived from the inputs plus `PARSER_VERSION`, rebuilding identical inputs reproduces the same identifier, but rebuilding after any corpus edit destroys the previous run provenance. `built_at` records the current time, so the database file is not byte-reproducible even when `run_id` is stable.

**Impact.** The artifact can describe only the newest build. Comparing two snapshots, or answering "what did the corpus look like when this claim was recorded", is impossible from the database. `Protocols/Research-Evaluation.md` section 9 asks that an update preserve the previous evaluation date, decision, and evidence trail and that history not be silently overwritten, which this behaviour contradicts.

**Smallest corrective action.** Choose one behaviour and document it: retain run rows, by not deleting `ingestion_run` and `ingestion_input` or by writing history into a separate table, so builds accumulate; or keep the single-snapshot behaviour and state in `data/README.md` that the artifact deliberately describes only the latest run, with the warnings file and the recorded input hashes as the audit trail.

**Verification.** Either `select count(*) from ingestion_run` grows across builds with distinct identifiers, or the documenting sentence exists.

## F14 - Low - Warning types and failure branches without test coverage

**Evidence.** The parser can emit at least seven warning types; the corpus exercises four (`source_rows_lacking_direct_urls`, `unresolved_alias`, `duplicate_candidate`, `unsupported_table_shape`). `truncated_url`, `missing_title`, and `weak_source_classification` never occur in the snapshot, and `classification_conflict` never occurs.

The 7 tests cover URL normalization, stable identifiers, the table parser with escaped pipes, URL-linked sources, the structured register header, ambiguous labels with explicit claim links, and internal-artifact behaviour. Not covered: the duplicate-claim collision (F2), trailing punctuation in URLs (F3), the unmapped-classification path (F4), the truncated-URL and missing-title branches, the classification-conflict merge path, claim label resolution failure, and the `document_citation_coverage` and `source_conflicts` views with non-empty claims, which is currently impossible because there are no claims.

**Impact.** The suite is green but silent about the paths most likely to be exercised during the next step, claim curation. The three defects found by construction in this report (F2, F3, F4) were all in uncovered code.

**Smallest corrective action.** Add one focused test per branch, starting with the three reproductions already recorded in F2, F3, and F4, so that each has a failing case before its fix and a passing case after.

**Verification.** Each new test fails against the current code for the defect it names, and passes once the matching fix is applied.

## F15 - Low - A "status" column is mapped to claim type

**Evidence.** `_claim_columns` resolves the claim-type column from the header set `{"claim type", "type", "status"}`. A claim table that contained a Status column would have that column read as the claim type. Such a table is recognised as claims whenever a header matches `{"claim", "claim text", "assertion"}`, so it would be parsed as claims rather than left alone.

**Impact.** Low today, because the snapshot holds no claims. It becomes a silent mis-typing risk in exactly the tables that are about to be authored: a row whose status is `reviewed` would fail the type lookup and drop the row with an `unsupported_table_shape` warning, and a status value that happened to match a claim-type phrase would be recorded as a claim type instead.

**Smallest corrective action.** Remove `status` from the claim-type header set and keep the explicit `claim type` and `type` headers, relying on the existing warning to surface any table whose type column is not recognised.

**Verification.** A fixture with `Claim | Status | Confidence` columns produces the unsupported-shape warning instead of a parsed claim.

## Verified clean, no action required

- **SQL dialect.** `schemas/citations.sql` and `analysis/citation_evaluator.sql` are valid DuckDB and must not be rewritten to satisfy a T-SQL parser. The editor-level false positives are already resolved by `mssql.autoDisableNonTSqlLanguageService: true` in `.vscode/settings.json`, and both files carry a dialect header comment.
- **Dependency manifest.** `requirements.txt` (`duckdb>=1.4,<2.0`, `pytest>=8,<10`) matches the working environment (DuckDB 1.5.5, pytest 9.1.1); `pip install --dry-run -r requirements.txt` is a no-op.
- **URL extraction.** No false-positive hosts were found. The 207 sources resolve to 119 distinct hosts, all plausible, with no version-string or `node.js` style hosts, and 69 sources carry a real page path; the remaining publisher-level URLs are recorded as warnings by design.
- **Identifier stability.** `run_id` is derived from input paths, input hashes, and `PARSER_VERSION`, and the existing test asserts that two consecutive builds return identical results.
- **Constraint enforcement.** The schema's checks work: the existing test asserts that an invalid `evidence_class` is rejected by DuckDB.
- **Retention of unresolved records.** Keeping 197 unresolved and 43 ambiguous occurrences, and 240 unresolved aliases, is intended by the plan and stated in `data/README.md`; this report treats it as correct behaviour, not as a defect.
- **Internal-artifact handling.** The `is_internal` branch, the internal-artifact test, and the exclusion of internal documents from `source_recurrence` all exist and pass.
- **Setup documentation.** No references to the previous `venv` workflow remain anywhere in the repository, and `python -m pytest` and `python src/ingest_citations.py` both run exactly as documented.

## Deliberately deferred, not defects

- **Zero claims and zero claim-source mappings.** Consequently `source_conflicts` and `next_research_candidates` return no rows, and `document_citation_coverage.claims_without_source_mappings` cannot be meaningfully validated. The plan defers claim extraction until mapping is reliable, and `data/README.md` states the zero-claim snapshot honestly. F2, F14, and F15 are the reason this matters: the claim path is entirely unexercised.
- **No fuzzy matching, no LLM, no probabilistic extraction.** Stated in the plan and in `data/README.md`.
- **Single-file local DuckDB, no server, dbt, graph store, or vector store.** Stated in the plan.
- **`built_at` makes the database bytes differ between builds while identifiers stay stable.** Recorded under F13 as a policy question rather than a defect.

## Recommended order of work

1. **F1 and F2 together.** They interact: F2 is one of the ways F1 is triggered, and both sit on the path the project is about to exercise.
2. **F3 and F4.** Small, self-contained, and each has a reproduction already written here.
3. **F5, F6, F7.** These make the review workflow surface the gaps it claims to surface; F6 also unlocks the evaluation metadata the protocol requires.
4. **F8, F9, F10, F11, F12.** Setup, hygiene, and documentation.
5. **F13, F14, F15.** Policy decision, coverage, and a latent header mapping.

## Verification commands

```powershell
conda activate datascience
python -m pytest src/tests -q
python src/ingest_citations.py
python -c "import duckdb; con = duckdb.connect('data/citations.duckdb', read_only=True); print(con.execute('select count(*) from source').fetchone())"
```

After applying F1 and F2, re-run the duplicate-claim reproduction recorded in F1 as the regression check: the build should fail loudly while the existing snapshot keeps its row counts.

## Open status

Findings F1 to F15 are open. This report applies no code change, no documentation change, and no data change: it records evidence, impact, and the smallest corrective action for each item, so that each fix can be made and verified independently. The falsifier for the whole review is the next build over a corpus that contains an explicit claim table plus the placement of `First-Ratings.md` inside the ingest root; re-run this review after that step, since F2, F4, F6, F14, and F15 all change behaviour on that path.
