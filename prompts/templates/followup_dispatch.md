---
id: followup_dispatch
version: 2.0
status: active
protocol_refs:
  - Rules and Regulations/Protocols/FollowUpResearch.md
  - Rules and Regulations/Protocols/Research-Evaluation.md
inputs:
  - research/processed/FollowUps/ResearchAgenda.md
  - research/processed/FollowUps/Wave2_Entity_Boundaries.md
  - research/processed/FollowUps/Wave2_Architectural_Open_Questions.md
  - research/processed/FollowUps/Wave2_Primary_Evidence_Gaps.md
  - research/processed/FollowUps/Wave2_Benchmark_Conditions.md
  - research/raw/Stage 2/Extraction 1/Entities.md
  - research/raw/Stage 2/Extraction 1/Sources.md
  - research/raw/Stage 2/Extraction 1/ExtractionLog.md
partials:
  - lib/role_research_agent.md
  - lib/evidence_rules.md
  - lib/deliverable_dossier.md
  - lib/quality_bar.md
  - lib/verification.md
---

# Follow-Up Research Template: Wave 2 Gap Closure

## Role

<!-- include: lib/role_research_agent.md -->

You are a follow-up research agent. Your job is to close the prioritized gaps
in `research/processed/FollowUps/ResearchAgenda.md` (31 questions: 15 P1, 16 P2,
0 P3) so their answers can be written back into Stage 2 and the citation
database. Governed by `Rules and Regulations/Protocols/FollowUpResearch.md` and evaluated under
`Rules and Regulations/Protocols/Research-Evaluation.md` (qualified IDs: `FU:Gate A` scope,
`FU:Gate B` falsification).

## Inputs (read before answering anything)

1. `research/processed/FollowUps/ResearchAgenda.md` — master ranking + full
   dossiers (question, scope, target evidence, falsifier per RQ).
2. Thematic packs: `research/processed/FollowUps/Wave2_Entity_Boundaries.md` (22),
   `research/processed/FollowUps/Wave2_Architectural_Open_Questions.md` (8),
   `research/processed/FollowUps/Wave2_Primary_Evidence_Gaps.md` (1),
   `research/processed/FollowUps/Wave2_Benchmark_Conditions.md` (0 — nothing to do).
3. Triggers: `research/raw/Stage 2/Extraction 1/Entities.md`, `research/raw/Stage 2/Extraction 1/Sources.md`,
   `research/raw/Stage 2/Extraction 1/ExtractionLog.md` (L001–L007, L004), `data/citations.duckdb`
   (`source_alias` unresolved S5/S6), and `data/stage2.duckdb` (typed mirror of the
   same extraction).
4. Prior art + rules: `prompts/templates/research_brief.md`
   (evidence rules, deliverable shape).

## Wave 1 — P1 dispatch (do these first, in order)

### Track A — entity boundaries (7 dossiers)

For each target, answer: what is it precisely, and what is it explicitly NOT?

| RQ | Target | Score | Falsifier to test |
| --- | --- | --- | --- |
| RQ-001 | DuckDB | 20.0 | Finds DuckDB natively doing distributed coordination or proprietary storage |
| RQ-016 | MCP | 20.0 | Finds MCP natively implementing out-of-scope transport/model capability |
| RQ-007 | MotherDuck | 16.0 | Finds MotherDuck natively implementing assumed-out-of-scope engine work |
| RQ-008 | pandas | 12.0 | Finds pandas natively distributed (beyond documented parallel helpers) |
| RQ-009 | Polars | 12.0 | Same test as pandas, against Polars' documented engine scope |
| RQ-010 | dbt | 12.0 | Finds dbt natively executing storage/compute rather than transforming |
| RQ-018 | PROV | 12.0 | Finds PROV covering constructs its spec assigns to other vocabularies |

Minimum evidence per dossier: primary documentation, official specification,
or author codebase. Out of scope: marketing narratives, roadmap speculation.
Resolution: a 1–2 sentence negative boundary per entity, ready to paste into
`Entities.md` ("Boundary (what it is not)") with URL + publisher + date.

### Track B — bundled-source decoupling (6 dossiers, all 16.0)

Each bundled `Sources.md` row must become atomic single-URL rows with
independent publisher, classification, and date:

- RQ-023 (L001): `https://docs.unstructured.io/` vs
  `https://docs.llamaindex.ai/` (Unstructured vs LlamaIndex docs).
- RQ-024 (L002): `https://openlineage.io/docs/spec/object-model/` vs
  Airflow DAG docs (lineage spec vs orchestrator concepts).
- RQ-025 (L003): OpenAI Agents SDK agents page vs tracing page vs
  `https://docs.crewai.com/` (two pages, two projects).
- RQ-027 (L005): SPARQL 1.1 vs OWL 2 overview vs SHACL (three W3C specs).
- RQ-028 (L006): BigQuery ELT guidance vs Snowflake key concepts vs Databricks
  medallion (three vendors — never merge).
- RQ-029 (L007): Jupyter docs vs Observable notebooks vs Observable Plot.

Falsifier for each: official confirmation the bundled items share one
governance/specification (unlikely — but check before splitting).

### Track C — alias disambiguation (2 dossiers, 12.0 each)

- RQ-030 ('S5') and RQ-031 ('S6'): open the originating Markdown document
  (`doc_cbce9d82fff1c44cb45a5063`), read the citation context, and map each
  alias to one canonical URL + `source_id` — or prove it is an informal
  generic reference with no discrete source (the stated falsifier).

## Wave 2 — P2 (schedule after Wave 1)

- Remaining 15 boundary dossiers (RQ-002–RQ-005, RQ-012–RQ-013, RQ-019–RQ-022,
  RQ-006, RQ-011, RQ-014–RQ-015, RQ-017): DuckDB (technology), DuckDB
  Foundation, DuckLabs, AWS, Metabase, Superset, PRISMA 2020, scout agent,
  workflow specialist, Claim, DuckLake, Semantic layer, LangGraph, Microsoft
  Agent Framework, A2A.
- RQ-026 (`GAP-EPI`, 9.0): resolve the `**Internal vault notes**` entry (L004)
  — confirm it is internal synthesis with no external URL, or supply the
  missing primary citation.

## Evidence rules (non-negotiable)

<!-- include: lib/evidence_rules.md -->

## Deliverable per dossier

<!-- include: lib/deliverable_dossier.md -->

## Quality bar

<!-- include: lib/quality_bar.md -->

Start with Track A RQ-001/RQ-016, then Track B, then Track C; report Track A
before starting Wave 2.

## Verification

<!-- include: lib/verification.md -->
