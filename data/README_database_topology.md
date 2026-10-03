# Database Topology

Five DuckDB files; relationships:

- `citations.duckdb`: Source citations, claims, metrics (extracted from `research/raw/` Markdown).
- `stage2.duckdb`: Stage 2 Extraction 1 data (`research/raw/Stage 2/Extraction 1`).
- `smarthome.duckdb`: Stage 2 Extraction 2 (Smart Homes) — `data/smarthome.duckdb`.
- `AutomationResearch.duckdb`: Stage 2 Extraction 3 (Automation Market Research).
- `fusion_energy.duckdb`: Stage 2 Fusion Energy extraction (`research/raw/Stage 2/Fusion Energy`).

`stage2.duckdb`, `smarthome.duckdb`, `AutomationResearch.duckdb`, and `fusion_energy.duckdb` share the same `schemas/stage2.sql` schema. `citations.duckdb` uses `schemas/citations.sql`.
