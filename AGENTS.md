# AGENTS.md — dataframe-elephant

## Project Overview
Data-research workspace: Markdown corpus in `research/raw/` → DuckDB citation intelligence in `data/` → follow-up agenda in `research/processed/`, plus an encrypted-archive (ECA) pipeline. Core logic in `src/*_core.py`, thin CLIs in `scripts/`.

## Critical Entry Points

### Interpreter (Windows)
- **Use the repo venv**: `.\.venv\Scripts\python.exe` (system 3.13 lacks deps like duckdb)
- **Install deps**: `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` (duckdb, pytest, hypothesis, cryptography)
- **Test setup**: `.\.venv\Scripts\python.exe -m pytest src/tests -q`

### Monorepo Structure
- **Entrypoint files**:
  - `src/ingest_citations.py` - Stage 1 ingestion to citations.duckdb
  - `src/stage2_import_core.py` - Stage 2 import (per extraction folder) to stage2.duckdb / smarthome.duckdb  
  - `src/archive_core.py` - Core ECA encryption/compression library
  - `src/db_export_core.py` - Native DuckDB export bundles
  - `src/viz_core.py` - Read-only query/provenance helpers shared by the notebooks in `notebooks/`
- **Scripts directory**: Thin CLIs that import core modules (mirroring `src/*_core.py` pattern)

## Essential Commands

### Database Operations
- **Citation DB**: `.\.venv\Scripts\python.exe src/ingest_citations.py`
- **Stage 2 DB (Extraction 1)**: `.\.venv\Scripts\python.exe scripts/import_stage2.py --stage2-dir "research/raw/Stage 2/Extraction 1" --database "data/stage2.duckdb" --warnings "data/stage2_ingestion_warnings.jsonl" --schema "schemas/stage2.sql"`
- **Smart-home DB (Extraction 2)**: `.\.venv\Scripts\python.exe scripts/import_stage2.py --stage2-dir "research/raw/Stage 2/Extraction 2" --database "data/smarthome.duckdb" --warnings "data/smarthome_ingestion_warnings.jsonl" --schema "schemas/stage2.sql"`
- **Archive (Stage 1 Wave 1)**: `.\.venv\Scripts\python.exe scripts/archive_stage1.py --dry-run` (ALWAYS start with dry-run!)
- **Restore archive**: `.\.venv\Scripts\python.exe scripts/restore_archive.py --archive <file>.tar.gz.enc --dest "research/raw/Stage 1/Wave 1"` (use `--list` to inspect without extracting; Commander Deck archives need `--dest "Rules and Regulations/Commander Deck/Archive_restored"`)

### Prompt Library
- **Assemble a prompt**: `.\.venv\Scripts\python.exe scripts/assemble_prompt.py --template followup_dispatch --out prompts/dispatch/<date>_wave2.md`
- **Follow-up agenda**: `.\.venv\Scripts\python.exe scripts/formulate_research_questions.py --stage2-dir "research/raw/Stage 2/Extraction 1" --output-dir "research/processed/FollowUps"`

### Visualization Notebooks
- **Rebuild notebooks**: `.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py` (the `.ipynb` files are generated; edit the generator, not the notebooks)
- **Verify notebooks match the generator**: `.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py --check`
- **Notebook focus**: `.\.venv\Scripts\python.exe -m pytest src/tests/test_viz_notebooks.py -q` (executes every notebook headless in a real Jupyter kernel)
- **Shared library focus**: `.\.venv\Scripts\python.exe -m pytest src/tests/test_viz_core.py -q`

### Testing
- **Full suite**: `.\.venv\Scripts\python.exe -m pytest src/tests -q`
- **Export focus**: `.\.venv\Scripts\python.exe -m pytest src/tests/test_export_databases.py -q`
- **Archive focus**: `.\.venv\Scripts\python.exe -m pytest src/tests/test_archive_roundtrip.py -q`
- **Prompt lint**: `.\.venv\Scripts\python.exe -m pytest src/tests/test_prompts.py -q` (Tier 1 rules R1–R5; R5 asserts prompt commands match AGENTS.md verbatim — keep commands in sync)
- **No linter/typechecker**: there is no `ruff`/`mypy` config; the only automated checks are pytest + the prompt lint rules.

### Export Protocol
- **Full export**: `.\.venv\Scripts\python.exe scripts/export_databases.py`
- **Partial options**: `--which all|citations|stage2|smarthome` `--formats csv,parquet` `--overwrite` `--no-verify` `--timestamp <ts>` (diagnostics only)

## Gotchas That Will Bite

### Archive Operations
- **Delete risk**: `archive_stage1.py` **deletes source `.md` files** after verified roundtrip unless `--keep-originals` or `--dry-run`
- **Passphrase order**: `--passphrase` → `$ARCHIVE_PASSPHRASE` env → `.env` → interactive prompt (archive prompts twice!)
- **ECA slowness**: 600k PBKDF2 iterations make archive/encrypt tests expensive

### Data Integrity
- **Source preservation**: `build_database` uses temp file + atomic replace, carries forward unchanged files by SHA-256 cache
- **Schema safety**: Broken schema leaves existing DB untouched (rollback test covers this)
- **CSV vs Parquet**: CSV collapses empty strings to NULL in nullable columns; Parquet preserves NULL-vs-empty exactly

### DuckDB Specifics
- **Dialect only**: `schemas/*.sql` uses DuckDB syntax (`CREATE OR REPLACE VIEW`, `FILTER (WHERE ...)`, `ADD COLUMN IF NOT EXISTS`)
- **Parsing rules**: No fuzzy matching by design: publisher-only URLs, multi-URL cells, truncated URLs, unmapped classifications produce `unresolved`/`ambiguous` rows + `ingestion_warning` entries
- **Claim requirement**: Claim tables require `claim` + `claim type` + `confidence` columns or they are skipped with `unsupported_table_shape` warning
- **No claim→metric FK**: `schemas/stage2.sql` links claims to metrics only by shared `section` or `source_ref`. `viz_core` derives those links heuristically and labels the reason in a `linkage` column; never present that linkage as a stored relationship
- **Value cells are authored strings**: `metric.value` holds `"3-5"`, `"1.4, 1.4.2, 1.5, 1.6"`, `"760 (45%)"`. Use `viz.parse_numbers` / `viz.range_value`; never assume a typed number
- **Internal evaluation**: `First-Ratings.md` excluded from external recurrence/claims; `source.status`/`directness` stay `NULL` when unrecorded

### Environment & Testing
- **pytest.ini**: Sets `pythonpath=.` - always run from repo root
- **Monkeypatching**: Tests monkeypatch `ingest_citations.ROOT` to isolate `analysis/**/*.md` ingestion
- **ECA tests**: Hypothesis roundtrip tests (`test_archive_roundtrip.py`, `test_ingest_citations.py` Wave 6) are the expensive suite

## Architecture Notes

### Multi-Database Topology
- **Option A (fixed)**: Stage 2 data goes into dedicated databases, one per extraction folder, alongside untouched `data/citations.duckdb`: `data/stage2.duckdb` (Extraction 1) and `data/smarthome.duckdb` (Extraction 2)
- **Extraction folders**: `research/raw/Stage 2/Extraction 1/`, `research/raw/Stage 2/Extraction 2/` — the importer does not recurse, so `--stage2-dir` must name the leaf folder holding the seven contract files
- **Stage 2 contents**: `Entities.md`, `Metrics.md`, `Claims.md`, `Sources.md`, `Predicates.md`, `WorkflowMap.md`, `ExtractionLog.md` (identical contract for every extraction; `schemas/stage2.sql` is shared, never forked)

### Export Protocol
- **Sources of truth**: `data/citations.duckdb`, `data/stage2.duckdb` and `data/smarthome.duckdb` only
- **Export quality gates**: 8 gates (G1-G8) with specific failure modes and recovery steps
- **Verification**: Every bundle re-imports into fresh temp database and compares schema, contents, views, FK checks

### File Structure Ownership
- **research/raw/** → Raw Markdown files, Stage 1 archives
- **research/processed/** → Cleaned research for analysis  
- **data/** → Dataset snapshots (input/output, fixtures)
- **schemas/*.sql** → DuckDB-only canonical table/view definitions
- **analysis/*.sql** → DuckDB-only analysis queries and reports

## Development Workflow

### Command Order Matters
1. **Validate first**: Always start archive operations with `--dry-run`
2. **Test flow**: `test_export_databases.py` + `test_archive_roundtrip.py` + `test_viz_notebooks.py` → full suite (`src/tests`) → export. There is no lint/typecheck step (no ruff/mypy config).
3. **Testing**: Run focused tests before full suite (`test_export_databases.py`, `test_archive_roundtrip.py`, `test_viz_core.py`, `test_viz_notebooks.py`)

### Environment Setup
- **Prefer repo venv**: `.\.venv\Scripts\python.exe` over system python
- **if conda**: `conda activate datascience` is documented in `data/README.md` but `.venv` is verified working

### Derived Artifacts
- **Gitignored**: `*.duckdb`, `*.jsonl`, `.env`, `data/exports/`
- **Source of truth**: Only `data/citations.duckdb`, `data/stage2.duckdb` and `data/smarthome.duckdb` are authoritative
- **Exports**: One timestamped run directory per export, with `manifest.json` audit trail

## What to Avoid

### Common Mistakes
- Running plain `python` instead of repo venv interpreter
- Forgetting `--dry-run` on archive operations
- Treating exports as source of truth
- Converting DuckDB SQL to T-SQL
- Editing hand-generated CSV/Parquet payloads
- Running production databases with multiple writers

### Protocol Violations
- Don't run archive against real data without `--keep-originals` or `--dry-run`
- Don't edit production databases to suit exports
- Don't present view snapshots as source tables
- Don't commit derived artifacts (`data/exports/`, `*.duckdb` files)
- Don't use automatic ECA encryption for exports by default
- Don't hand-edit `notebooks/*.ipynb`; they are generated by `scripts/build_visualization_notebooks.py`
- Don't chart a number the corpus does not record (e.g. inventing Matter release dates, an ecosystem device-type parity matrix, or per-control security scorecard results) — the notebooks state what is missing instead