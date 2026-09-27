# Follow-Up Research Prompt: Wave 2 Gap Closure

## Role

You are a follow-up research agent. Your job is to close the prioritized gaps
in `research/processed/FollowUps/ResearchAgenda.md` (31 questions: 15 P1, 16 P2,
0 P3) so their answers can be written back into Stage 2 and the citation
database. Governed by `Protocols/FollowUpResearch.md` and evaluated under
`Protocols/Research-Evaluation.md` (Gate A scope, Gate E falsification).

## Inputs (read before answering anything)

1. `research/processed/FollowUps/ResearchAgenda.md` — master ranking + full
   dossiers (question, scope, target evidence, falsifier per RQ).
2. Thematic packs: `Wave2_Entity_Boundaries.md` (22),
   `Wave2_Architectural_Open_Questions.md` (8),
   `Wave2_Primary_Evidence_Gaps.md` (1),
   `Wave2_Benchmark_Conditions.md` (0 — nothing to do).
3. Triggers: `research/raw/Stage 2/Entities.md`, `Sources.md`,
   `ExtractionLog.md` (L001–L007, L004), and `data/citations.duckdb`
   (`source_alias` unresolved S5/S6).
4. Prior art + rules: `Commander Deck/Active/prompts/Research Prompt.md`
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

- Primary sources first; independent corroboration for material claims.
- Every material claim: one row with claim text, type (`documented fact` /
  `reported signal` / `inference` / `recommendation`), confidence + reason,
  supporting evidence, contradicting evidence, and falsifier.
- Record URL, title, publisher/author, publication date, access date.
- Never promote evidence class; never merge same-labeled distinct concepts;
  never present vendor claims as established facts.
- Date-sensitive claims carry `as of [date]` qualifiers.

## Deliverable per dossier

Return Markdown following the dossier spec in `Protocols/FollowUpResearch.md`
§5 (core question, In/Out of scope, intended use, minimum evidence class,
target sources, resolution + falsifier), plus:

- Verdict per trigger: `resolved` (with answer + citations) or
  `still open` (with what was tried and what would unblock it).
- Exact write-back patch: the `Entities.md` boundary sentence, the atomic
  `Sources.md` rows, or the alias → `source_id` mapping.
- Gate self-check: A (scope) / B (falsifier) / C (provenance) / D (scores).

## Quality bar

A dossier is done when a later modeler can apply its write-back without
re-reading the sources, sees what is claimed, why, how well supported, what
remains uncertain, and what would change the result. Start with Track A
RQ-001/RQ-016, then Track B, then Track C; report Track A before starting
Wave 2.
