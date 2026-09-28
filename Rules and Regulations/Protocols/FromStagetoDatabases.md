# Stage 2 → Databases Protocol (FromStagetoDatabases)

## Status

This protocol is mandatory for every person, agent, or process that imports
`research/raw/Stage 2/` into DuckDB. No Stage 2 database may be built,
rebuilt, or replaced without following this procedure.

---

## 1. Purpose

`src/ingest_citations.py` only understands two generic shapes: source tables
and claim tables with explicit `claim` + `claim type` + `confidence` columns.
`Entities.md`, `Metrics.md`, `Predicates.md`, `WorkflowMap.md`, and
`ExtractionLog.md` therefore pass through as documents but never become typed
tables in `data/citations.duckdb`.

The purpose of this protocol is to:

- Define the single supported path from Stage 2 Markdown into typed DuckDB
  tables, without changing the `citations.duckdb` contract.
- Give `Entities.md`, `Metrics.md`, `Predicates.md`, `WorkflowMap.md`,
  `Claims.md`, and `ExtractionLog.md` first-class, queryable homes.
- Preserve every uncertainty marker (`[boundary not stated in source]`,
  `[conditions not stated in source]`, `[falsifier not stated]`) as data,
  never silently dropped.
- Provide a repeatable CLI (`scripts/import_stage2.py` over
  `src/stage2_import_core.py`) that supports creating new databases via
  `--database` / `--schema` selection.
- Feed `Protocols/FollowUpResearch.md` gap scanners with structured inputs
  (`unstated boundaries`, `unstated conditions`, `missing falsifiers`,
  `open questions`).

---

## 2. Non-negotiable rules

1. **Topology is fixed (Option A):** Stage 2 data goes into a dedicated
   database, default `data/stage2.duckdb`, alongside the untouched
   `data/citations.duckdb`. Extending `citations.duckdb` in place is forbidden
   by this protocol.
2. **Claims stay in the new DB:** `Claims.md` rows live only in the Stage 2
   database. Backfilling them into `citations.duckdb` `claim`/`claim_source`
   is forbidden (two copies drift; rebuilds couple).
3. **Reject on failed gates:** if any Stage 2 file has a frontmatter gate
   other than `pass` (including `fail` or `status: draft`), the import stops
   with an error. Import-with-warnings is not permitted.
4. **Create all tables now:** all Stage 2 tables and views are created on
   every build, even for currently empty files (`Predicates.md`,
   `WorkflowMap.md`, `Claims.md`, `Metrics.md`). Zero rows is valid;
   deferring schema is forbidden.
5. **Never promote evidence class:** a `[S]` stays a `reported signal`, an
   `[I]` stays an `inference`, `low` stays `low`. Same rule as
   `Protocols/TransitionStage2.md` Gate 3.
6. **No fuzzy matching:** source linkage is by exact normalized URL or
   explicit local label only, matching `src/ingest_citations.py` behavior.
   Publisher-only URLs, multi-URL cells, truncated URLs, and unmapped
   classifications produce warnings, not guessed mappings.
7. **DuckDB dialect only:** schemas use DuckDB syntax (`CREATE TABLE IF NOT
   EXISTS`, `CREATE OR REPLACE VIEW`, `FILTER (WHERE ...)`). Do not "fix" to
   T-SQL.
8. **Derived artifacts are gitignored:** never commit `*.duckdb`, `*.jsonl`
   warnings, or passphrases.

---

## 3. Inputs and outputs

### 3.1 Inputs — Stage 2 files

| File | Table shape (per `Protocols/TransitionStage2.md` §3–4) |
| --- | --- |
| `Entities.md` | `Entity ID`, `Canonical name`, `Type`, `Boundary (what it is not)`, `Stage 1 source`, `Section`, `Confidence` |
| `Metrics.md` | `Metric ID`, `Metric name`, `Value`, `Unit`, `Scope / conditions`, `Claim type`, `Confidence`, `Source ID`, `Stage 1 source`, `Section` |
| `Claims.md` | `Claim ID`, `Claim text`, `Claim type`, `Confidence`, `Source IDs`, `Falsifier`, `Workflow stage`, `Stage 1 source`, `Section` |
| `Sources.md` | `ID`, `Source`, `URL`, `Publisher`, `Classification`, `Publication date` |
| `Predicates.md` | `Predicate`, `Subject type`, `Object type`, `Direction`, `Example (from Stage 1)`, `Stage 1 source` |
| `WorkflowMap.md` | `Stage ID`, `Stage name`, `Inputs`, `Activities`, `Outputs`, `Quality gates`, `Roles`, `Tools`, `Evidence`, `Confidence` |
| `ExtractionLog.md` | `Log ID`, `Step`, `Stage 1 source`, `Decision type`, `Description`, `Resolution` |

Every file must open with the standard Stage 2 frontmatter (`stage: 2`,
`extracted_from`, `extractor`, `gate_results` for gates 1–7).

### 3.2 Outputs — Stage 2 database

Default `data/stage2.duckdb` via `schemas/stage2.sql`, plus a warnings
artifact (default `data/stage2_ingestion_warnings.jsonl`):

| Table | One row per | Key columns |
| --- | --- | --- |
| `stage2_run` / `stage2_input` | build / input file | `run_id`, `built_at`, `parser_version`, `path`, `sha256` |
| `entity` | `Entities.md` row | `entity_id`, `canonical_name`, `type`, `boundary`, `boundary_stated BOOL`, `confidence`, `document_id` |
| `metric` | `Metrics.md` row | `metric_id`, `metric_name`, `value`, `unit`, `scope_conditions`, `conditions_stated BOOL`, `confidence`, `document_id` |
| `stage2_claim` | `Claims.md` row | `claim_id`, `claim_text`, `claim_type`, `confidence`, `falsifier`, `falsifier_stated BOOL`, `workflow_stage`, `document_id` |
| `source_mirror` | `Sources.md` row | verbatim Stage 2 source row plus `document_id` (mirror only; canonical citation data stays in `citations.duckdb`) |
| `predicate` | `Predicates.md` row | `predicate`, `subject_type`, `object_type`, `direction`, `example`, `document_id` |
| `workflow_stage` | `WorkflowMap.md` row | `stage_id`, `stage_name`, `inputs`, `activities`, `outputs`, `quality_gates`, `roles`, `tools`, `document_id` |
| `extraction_decision` | `ExtractionLog.md` row | `log_id`, `step`, `decision_type` (CHECK over the 11 TransitionStage2 §8 types), `description`, `resolution`, `document_id` |
| `stage2_warning` | parse/gate warning | `warning_id`, `run_id`, `input_path`, `warning_type`, `message` |

Views (all created even when empty): `unstated_boundaries`,
`unstated_conditions`, `missing_falsifiers`, `open_questions`. These are the
structured feeds for FollowUpResearch `GAP-BND` / `GAP-CND` / `GAP-FAL` /
`GAP-OPN` scanners.

---

## 4. Import process — step by step

### Step 1: Preflight (reject on failure)

1. Confirm all seven Stage 2 files exist under `--stage2-dir`
   (default `research/raw/Stage 2`).
2. Parse each file's frontmatter; every `gate_results` entry must be `pass`
   and no file may carry `status: draft`. Otherwise stop with a non-zero exit
   and name the offending file and gate. No partial database is written.

### Step 2: Parse (strict shapes, warn never guess)

1. Extract Markdown tables with the same row-splitting semantics as
   `src/ingest_citations.py` (escaped-pipe aware).
2. Match headers case-insensitively after stripping `` ` ``, `*`, `_`.
   A table missing a required column is skipped with an
   `unsupported_table_shape` warning — never column-guessed.
3. Derive BOOLs while preserving raw text: `boundary_stated`,
   `conditions_stated`, `falsifier_stated` are `FALSE` exactly when the cell
   contains `[boundary not stated in source]`, `[conditions not stated in
   source]`, or `[falsifier not stated]` respectively.

### Step 3: Assign deterministic IDs

Reuse the `stable_id(kind, value)` SHA-256 scheme from
`src/ingest_citations.py`: identical corpus ⇒ identical IDs and identical
`run_id` (`run_id` covers file paths + SHA-256 hashes + parser version).

### Step 4: Load (temp file + atomic replace)

1. Write to a temp database path, apply `schemas/stage2.sql` first so a
   broken schema leaves the existing database untouched.
2. Insert inside a single transaction: `stage2_run`, `stage2_input`, all
   content tables, then `stage2_warning`.
3. Carry forward unchanged files by SHA-256 cache (same pattern as
   `ingest_citations._load_file_cache` / `_copy_unchanged_rows`).
4. Atomically replace the target `--database` path; write the sorted warnings
   JSONL artifact.

### Step 5: Postflight

Report per-table row counts and warning counts to stdout. Creating
additional databases is the same command with different paths:

```powershell
.\.venv\Scripts\python.exe scripts/import_stage2.py `
  --stage2-dir "research/raw/Stage 2" `
  --database "data/stage2.duckdb" `
  --warnings "data/stage2_ingestion_warnings.jsonl" `
  --schema "schemas/stage2.sql"
```

---

## 5. Quality gates before a Stage 2 database is complete

| Gate | Check |
| --- | --- |
| G1 Source coverage | Every `Source ID` / `Source IDs` in Metrics/Claims resolves to `Sources.md`, else a warning names the row. |
| G2 Marker integrity | Every `[…not stated…]` marker is kept in raw text and reflected in its `*_stated` BOOL. |
| G3 Evidence-class integrity | No confidence or claim-type promotion relative to Stage 2. |
| G4 Ingestibility | Zero unexplained `unsupported_table_shape` warnings; every warning is explainable from the input. |

---

## 6. What the Stage 2 database must not contain

| Prohibited | Reason |
| --- | --- |
| Rows copied into `citations.duckdb` | Single ownership; two copies drift |
| Merged entities with unresolved naming conflicts | Destroys traceability |
| Confidence higher than Stage 2 | Fabrication without new evidence |
| Vendor metrics without preserved scope text | Decontextualised numbers mislead |
| Open questions resolved without evidence | Resolution requires new research |
| Modified Stage 2 source files | Stage 2 is immutable during import |

---

## 7. Implementation conventions

- Core logic in `src/stage2_import_core.py`, thin CLI in
  `scripts/import_stage2.py` (mirrors the `src/followup_core.py` +
  `scripts/formulate_research_questions.py` split in `AGENTS.md`).
- Run from repo root with the repo venv (`pytest.ini` sets `pythonpath=.`):
  `.\.venv\Scripts\python.exe -m pytest src/tests -q`.
- Interpreter note: plain `python` may resolve to a system interpreter
  without `duckdb`; prefer `.\.venv\Scripts\python.exe`.

---

## 8. Update triggers

Re-run this import (or add a new `--database` target) when any of the
following occurs:

- Any Stage 2 file is revised, added, or re-gated.
- `schemas/stage2.sql` changes (new table, column, or view).
- The importer introduces a new warning type affecting table structure.
- A FollowUpResearch wave resolves a gap recorded in `extraction_decision`.

When updating, preserve previous `stage2_run` rows and warnings history. Do
not silently overwrite history.

---

## 9. Final principle

The import is judged not by how clean the database looks, but by whether a
researcher who has never read Stage 1 can use the database alone to find
every established fact, its conditions and boundaries, what remains
uncertain, and what would resolve that uncertainty.
