# Citation Database

Build the local DuckDB snapshot from all Markdown documents under `research/raw/`:

```powershell
conda activate datascience
python -m pip install -r requirements.txt
python src/ingest_citations.py
python -m pytest src/tests -q
```

The project uses the `datascience` conda environment (Miniforge) as its interpreter, and this workspace already selects it through `python-envs.defaultEnvManager` in `.vscode/settings.json`. If `conda activate` is unavailable in a fresh PowerShell session, run `conda init powershell` once, or call the environment interpreter directly:

```powershell
& "$env:USERPROFILE\miniforge3\envs\datascience\python.exe" src/ingest_citations.py
```

The build writes `data/citations.duckdb` and `data/citation_ingestion_warnings.jsonl`. Each input Markdown file is recorded with its workspace-relative path, SHA-256 content hash, and modification timestamp. The run record includes the build timestamp and parser version. Document, source, occurrence, alias, and claim IDs are deterministic for the same paths and contents; rebuilding replaces the derived tables and warning artifact rather than appending duplicate rows.

The parser only links sources by an exact normalized URL or an explicit source label in a structured claim table. Publisher-only URLs, grouped references, truncated URLs, unsupported table shapes, and classification conflicts remain visible as unresolved records or warnings. Fuzzy matching is intentionally not performed. `First-Ratings.md`, if added later, is recorded as an internal evaluation artifact; it is not treated as independent external evidence. It is currently absent from the input corpus.

The current corpus has no claim table with the required explicit claim type and confidence fields, so the first snapshot contains zero claims and zero claim-source mappings. Inline prose references are not converted into claim links. The next curation step is to review unresolved source aliases and add explicit, typed claim/evidence-span rows for the research briefs; do not infer those mappings from surrounding prose.

`source_recurrence` reports appearances by distinct documents and total occurrences. `source_reputation` is a profile of separate recorded dimensions: evidence class (authority proxy), directness, dates, status, documented independence groups, limitations, and recurrence. When the source text does not state a status or directness, those values remain NULL rather than being forced to `unknown`; that preserves the distinction between "not recorded" and "explicitly recorded as unknown." Use `analysis/citation_evaluator.sql` for the initial review queries, including the warning stream and unresolved alias review.

## Stage 2 database

The typed Stage 2 mirror is built separately per `Protocols/FromStagetoDatabases.md` (Option A: dedicated database, `citations.duckdb` untouched):

```powershell
.\.venv\Scripts\python.exe scripts/import_stage2.py
```

This writes `data/stage2.duckdb` and `data/stage2_ingestion_warnings.jsonl` from the seven `research/raw/Stage 2/` files via `schemas/stage2.sql`. All frontmatter gates must be `pass` or the import is rejected. Uncertainty markers are preserved as `*_stated` BOOLs; gap views (`unstated_boundaries`, `unstated_conditions`, `missing_falsifiers`, `open_questions`) feed the FollowUpResearch scanners.