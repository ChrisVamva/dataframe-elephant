# Index — Critical Minerals and Semiconductor Supply Chains (Wave 5)

_Status tracker. Date-stamp every status change._

| Date | Item | Status |
|------|------|--------|
| 2026-10-04 | NR3 brainstorming session completed; domain 7 / Subject G ranked | Done |
| 2026-10-06 | Subject selected by user (domain 7: critical-minerals & semiconductor supply chains) | Done |
| 2026-10-06 | Wave 5 skeleton created | Done |
| 2026-10-06 | Research pass: 4 agent runs (export controls + laundering; import regimes; tracing tech; concentration) + inline gap-fill (OECD framework, UFLPA FY2025) | Done |
| 2026-10-06 | Source register built (S01–S75) | Done |
| 2026-10-06 | Notes filled: 01_Background (Regimes, Concepts), 02_Origin_Evidence, 03_Laundering_Cases (6-step taxonomy), 04_Tracing_Technologies (+Concentration), 05_Origin_Record_Design v0 | Done |
| 2026-10-06 | Synthesis (RQ1–RQ5 + falsifiers) written | Done |
| 2026-10-06 | Article brainstorm delivered: `Artifacts/Article Ideas/5/SemiconductorBrainstorm.md` + `IdeasSemiconductorsEvaluation.md` | Done |
| 2026-10-07 | Stage 2 promotion completed: `research/raw/Stage 2/Extraction 5/` (7 contract files; Sources S01–S76, Entities E001–E050, Claims C001–C064, Metrics M001–M070, Predicates 14, Workflow W01–W07, ExtractionLog L001–L022; all 7 gates pass). Ingested into `data/citations.duckdb` (full Stage 2 run: 35 documents / 291 sources / 349 claims); warnings explained in ExtractionLog L021 | Done |
| 2026-10-07 | DuckDB created: `data/Semiconductors.duckdb` (0 warnings; 50 entities / 70 metrics / 64 claims / 76 sources / 14 predicates / 7 workflow stages / 22 decisions; gap views live). Registered as `semiconductors` in `PRODUCTION_DATABASES`, `export_databases.py --which`, `data/README.md`, `ExportDatabase.md` §3.1–§3.2. Export pipeline verified (`--which semiconductors`, with verification roundtrip); `health_check.py` passes | Done |
| 2026-10-07 | First article drafted: `Artifacts/Article Ideas/5/Draft/Russian gold.md` (idea 1.1, per ArticleCreation.md; all anchors verified against `Semiconductors.duckdb`; C020 kept at reported signal/low) | Done |

## Open Follow-ups (from 06_Evidence/Findings.md)

- Verify BIS FY2025 penalty figures (~$324M) against the BIS annual report [S13].
- Named Ga/Ge transshipment enforcement cases with quantities [S32 area].
- Citable 2025-26 tracker release for TSMC's sub-7nm share (~90% is UNVERIFIED-BACKGROUND) [S63].
- WCO global misdeclared-origin seizure statistics — none surfaced.
- China official export-license approval rate — none published; ~25% Jun 2025 is journalistic [S10].
- October 2026 status of the Nov 10, 2026 truce-suspension expiry [S10].
- Perth Mint / Iran sanctions element — needs AFR/Reuters archive pull [S40].
- Re|Source: confirmed commercial operation or folded? [S42]
- SIA/BCG "160+ weak links / 50+ concentration points" — verify against report PDF [S65].
