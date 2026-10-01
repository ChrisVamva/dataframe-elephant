# Database Topology

Four DuckDB files; relationships:

- `citations.duckdb`: Source citations, claims, metrics (extracted from `research/raw/` Markdown).
- `stage2.duckdb`: Stage 2 Extraction 1 data (`research/raw/Stage 2/Extraction 1`).
- `smarthome.duckdb`: Stage 2 Extraction 2 (Smart Homes) — `data/smarthome.duckdb`.
- `AutomationResearch.duckdb`: Stage 2 Extraction 3 (Automation Market Research).

`stage2.duckdb` and `smarthome.duckdb` share the same `schemas/stage2.sql` schema. `citations.duckdb` uses `schemas/citations.sql`.
