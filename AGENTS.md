# Repository Guidelines

## Project Overview

`dataframe-elephant` is a data-research platform that processes markdown corpora, extracts citations and claims, builds DuckDB databases, and generates visualizations and follow-up research agendas. The system follows a pipeline: **Markdown → Ingestion → Database (DuckDB) → Visualization/Export → Prompt Assembly → Follow-up Research**.

## Architecture & Data Flow

### Core Modules (`src/`)
- **`viz_core.py`** – Shared visualization library for SmartHome analysis notebooks. Handles claim fetching, metric retrieval, entity lookup, and provenance rendering.
- **`stage2_import_core.py`** – Stages 2 extraction (research/raw/Stage 2/Extraction 1/2) into DuckDB. Uses `SMARTHOME_DB` environment variable pointing to `data/smarthome.duckdb`.
- **`ingest_citations.py`** – Parses Markdown tables in research documents to build the citation database (`claim`, `source`, `claim_source` and related tables per `schemas/citations.sql`).
- **`db_export_core.py`** – Exports staged data to CSV/Parquet bundles with verification roundtrips.
- **`archive_core.py`** – Encrypts and packages datasets as ECA (Encrypted Archive Containers) using AES-256-GCM + PBKDF2-HMAC-SHA256 (600k iterations).
- **`followup_core.py`** – Generates research agendas and follow-up questions from gaps in the dataset.
- **`prompt_core.py`** – Assembles prompt templates from tier-1 lint rules (R1–R5) and writes structured outputs to `research/processed/`.
- **`prompt_templates/`** – Prompt templates (`templates/`) and shared partials (`lib/`) consumed by the assembler.

### Scripts (`scripts/`)
- **Thin CLI wrappers** over core modules. All use `argparse` with `--flag` defaults pointing to repo paths.
- **`assemble_prompt.py`** – Resolves template placeholders (`{{...}}`) using templates from `src/prompt_templates/`.
- **`import_stage2.py`** – Imports Stage 2 Markdown files into DuckDB with frontmatter gating.
- **`formulate_research_questions.py`** – Scans gaps in Stage 2 data and writes `research/processed/FollowUps/`.
- **`export_databases.py`** – Bundles DBs to CSV/Parquet with optional verification.
- **`archive_stage1.py`** – Creates ECA-encrypted archives from `research/raw/Stage 1/`.
- **`restore_archive.py`** – Restores archived datasets.
- **`build_visualization_notebooks.py`** – Generates the notebook catalogue in waves: the cell contract, the bootstrap cell and wave 1's specs live here, wave 2's specs are imported from `wave2_notebook_specs.py`, and wave 3's specs from `wave3_notebook_specs.py`.
- **`wave2_notebook_specs.py`** – Spec dicts for `notebooks/2/`: claim clusters, metric ids and every code cell, importing the shared cell contract from the builder.
- **`health_check.py`** – Quick repository health check: verifies the DuckDB databases contain their expected tables and that key schemas/docs exist. Exits non-zero if any check fails.

### Configuration & Build
- **Dependencies** – All in `requirements.txt` (12 pinned-range packages: duckdb, pandas, plotly, altair, ipywidgets, cryptography, pytest, hypothesis, jupyter, nbformat, nbconvert, ipykernel).
- **Test runner** – `pytest.ini` sets `pythonpath = .` for repo-local imports.
- **Environment** – `.env` holds no secrets (`ARCHIVE_PASSPHRASE` comes from the environment or an interactive prompt); `SMARTHOME_DB` points to the staging DuckDB.
- **Schemas** – `schemas/stage2.sql` and `schemas/citations.sql` define the DuckDB schemas.
- **`notebooks/1/`** (wave 1) – SmartHome visualization notebooks, organized by workflow stage.
- **`notebooks/2/`** (wave 2) – Automation market research notebooks, organized by thematic cluster.
- **`notebooks/3/`** (wave 3) – Automation market research (Extraction 3) notebooks, organized by thematic cluster (pricing/architecture, runtime reliability, incidents, cost/labor). Spec: `scripts/wave3_notebook_specs.py` defines clusters for claims C001-C105 and metrics M1-M100.
## Key Design Patterns

1. **Deterministic Identifiers** – `stable_id(kind, value)` produces a repeatable ID (verified in `src/ingest_citations.py`). Used for claim tracking across ingestion, export, and visualization.
2. **Heuristic Linkage** – Claims are linked to metrics/entities via section/`source_ref` rather than enforced foreign keys. This allows flexible, ad-hoc relationships.
3. **Read-Only DB Access** – Most database operations use `read_only=True` except during import, export, and verification.
4. **Pre-flight Gate Checks** – `frontmatter_gate_failures()` validates Markdown structure before loading.
5. **Property-Based Testing** – `hypothesis` adds property tests for URL normalization, stable-ID determinism, classification membership, and table parsing.
6. **Round-Trip Verification** – Export and import pipelines include verification steps comparing schema, contents, and views.

## Important Files

| Path | Purpose |
|------|----------|
| `src/viz_core.py` | Visualization helpers, claim/metric/entity fetchers |
| `src/stage2_import_core.py` | Stage 2 Markdown → DuckDB import |
| `src/ingest_citations.py` | Citation extraction from Markdown tables |
| `src/db_export_core.py` | CSV/Parquet bundle export with verification |
| `src/archive_core.py` | ECA encryption & archiving |
| `src/followup_core.py` | Gap detection and follow-up question generation |
| `src/prompt_core.py` | Prompt template assembly and linting (R1–R5) |
| `src/prompt_templates/` | Prompt templates and shared `lib/` partials |
| `schemas/stage2.sql` | DuckDB schema for Stage 2 data |
| `schemas/citations.sql` | DuckDB schema for citation data |
| `scripts/assemble_prompt.py` | Template substitution for prompt generation |
| `scripts/import_stage2.py` | Stage 2 data ingestion with frontmatter validation |
| `scripts/formulate_research_questions.py` | Research agenda formation |
| `scripts/export_databases.py` | Bulk DB export with manifest auditing |
| `scripts/archive_stage1.py` | Archive creation (ECA) |
| `scripts/restore_archive.py` | Archive restoration |
| `scripts/build_visualization_notebooks.py` | Notebook generation from claim clusters (all three waves) |
| `scripts/wave2_notebook_specs.py` | Wave-2 notebook specs (`notebooks/2/`) |
| `scripts/wave3_notebook_specs.py` | Wave-3 notebook specs (`notebooks/3/`): 4 thematic clusters for claims C001-C105 and metrics M1-M100 from Extraction 3 |
| `pytest.ini` | Test configuration (`pythonpath = .`) |
| `requirements.txt` | 12-package dependency list |
| `.gitignore` | Excludes venv, duckdb dumps, ECA archives, exported artifacts |

## Development Commands

```bash
# Install dependencies (uses repo venv)
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# Run full test suite
.\.venv\Scripts\python.exe -m pytest src/tests -q

# Run specific test groups
.\.venv\Scripts\python.exe -m pytest src/tests/test_viz_notebooks.py -q          # visualization notebooks
.\.venv\Scripts\python.exe -m pytest src/tests/test_archive_roundtrip.py -q     # archive/ECA tests
.\.venv\Scripts\python.exe -m pytest src/tests/test_export_databases.py -q     # export tests
.\.venv\Scripts\python.exe -m pytest src/tests/test_prompts.py -q               # prompt lint rules (R1-R5)

# Build notebooks (all waves: notebooks/1/, notebooks/2/, notebooks/3/)
.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py               # all waves

# Stage 2 import (Extraction 2 -> data/smarthome.duckdb)
.\.venv\Scripts\python.exe scripts/import_stage2.py --stage2-dir "research/raw/Stage 2/Extraction 2" --database "data/smarthome.duckdb" --warnings "data/smarthome_ingestion_warnings.jsonl" --schema "schemas/stage2.sql"

# Citation ingestion
.\.venv\Scripts\python.exe src/ingest_citations.py

# Build notebooks (all waves: notebooks/1/, notebooks/2/, notebooks/3/)
.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py               # all waves
.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py --wave 2   # one wave only
.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py --check    # fail if on-disk files are stale

# Assemble a prompt
.\.venv\Scripts\python.exe scripts/assemble_prompt.py

# Follow-up research agenda
.\.venv\Scripts\python.exe scripts/formulate_research_questions.py

# Export databases
.\.venv\Scripts\python.exe scripts/export_databases.py

# Archive Stage 1 (dry-run first!)
.\.venv\Scripts\python.exe scripts/archive_stage1.py --dry-run

# Restore archive
.\.venv\Scripts\python.exe scripts/restore_archive.py --archive <file>.tar.gz.enc --dest "research/raw/Stage 1/Wave 1"
```

## Code Conventions

- **Language**: Python (repo venv recommended).
- **Style**: Type hints throughout; `from __future__ import annotations` is used in some files.
- **Error Handling**: Custom exceptions (`Stage2ImportError`, `ExportError`, `PromptRenderError`, `ArchiveError`) raised on failures; loud failures prevent silent corruption.
- **Async**: Minimal async usage; most I/O is synchronous via DuckDB's blocking driver.

## Testing & QA

- **Unit tests** – `src/tests/` contains 8 test files covering visualization, export, archive, prompts, stage2 import, follow-up research, citation ingestion, and notebooks.
- **Notebook gate** – `test_viz_notebooks.py` parametrizes over all three waves: every notebook is checked against the generator, executed headless in a Jupyter kernel (must produce a Plotly figure and no cell errors), and every `C###` / `M###` id it mentions is verified against the database.
- **Integration tests** – Use real DuckDB instances (via `pytest.ini` pythonpath) and real ECA archives.
- **Property-based** – `hypothesis` adds non-deterministic coverage for string parsing and numeric extraction.
- **Coverage expectation** – Full suite (`src/tests -q`) runs daily; critical paths (archive roundtrip, citation ingestion) are marked as high priority.

## Maintenance Notes

- **Never commit** derived artifacts: `.duckdb` dumps, ECA archives (`.tar.gz.enc`), exported CSVs/Parquets, notebook outputs, and prompt templates. `data/exports/` is gitignored.
- **Always use `--dry-run`** on archive creation and export operations.
- **Keep `SMARTHOME_DB`** consistent across environments; rotate passphrases via environment variables or interactive prompts.
- **Review `AGENTS.md`** before making structural changes; it captures the current architecture and coding standards.
