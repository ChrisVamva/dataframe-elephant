---
title: Research-to-Data Capability Atlas — Results
aliases:
  - Research.Results
  - Research-to-Data Results
  - Research-to-Data Capability Cluster (results)
created: 2026-09-27
modified: 2026-09-27
status: consolidated results (evidence-grounded)
parent: "[[Research Prompt]]"
scope: "[[The components to investigate]]"
sources_access_date: 2026-09-27
related_notes:
  - "[[ANT GP H]]"
  - "[[C]]"
  - "[[DPS]]"
  - "[[FAI]]"
  - "[[Q]]"
  - "[[OP MS 1.3F]]"
  - "[[DC L5.6]]"
  - "[[CP L6]]"
  - "[[G0]]"
  - "[[G1]]"
  - "[[G2]]"
  - "[[G3]]"
  - "[[Citations/Citation]]"
  - "[[Citations/Report]]"
---

# Research-to-Data Capability Atlas — Results

**Result type:** consolidated research brief — Sections 1–7 follow the deliverable spec in [[Research Prompt]]; §0 (method), §8 (modeling handoff) and §9 (verification) are added for auditability and reuse.
**Workflow under study:** Research → Evidence → Extraction → Structured representation → Normalization → Database → Query → Analysis → Visualization → Interpretation → New research → Agent iteration.
**Target of this note:** a *deduplicated, modeling-ready* result set — stable names, explicit boundaries, typed claims, entities and relationships ready to load into `schemas/`, `data/`, and `analysis/`.

> **Relationship to prior vault notes.** This vault already contains eleven overlapping passes over the same cluster ([[ANT GP H]], [[C]], [[DPS]], [[FAI]], [[Q]], [[OP MS 1.3F]], [[DC L5.6]], [[CP L6]], [[G0]]–[[G3]], plus the citation audit in [[Citations/Citation]] and [[Citations/Report]]). `Research.Results.md` is the **consolidation layer**: it de-duplicates those passes, resolves their naming conflicts into a single register (§8.1), and adds a fresh primary-source verification pass dated 2026-09-27 (§7). Where this note disagrees with an earlier note, the earlier note is named.

---

## 0. Method, evidence classes, and how to read this note

### 0.1 What was done

1. **Internal consolidation.** All eleven existing `research/raw` notes plus the two `Citations/` audit notes were inventoried (headings, entity rows, comparison tables, source lists) and reconciled. Contradictions are recorded, not silently resolved.
2. **Targeted primary-source verification (2026-09-27).** Because the cluster is unusually version-sensitive, a verification pass fetched first-party pages for the most volatile claims: DuckDB/DuckLabs governance, DuckLake, pandas 3.0, Polars 2.0, MCP specification, Microsoft Agent Framework, LangGraph v1, dbt, BI tool releases, provenance and review standards.
3. **Claim typing and confidence.** Every non-obvious finding carries a claim label and a lens-level confidence value. §4 rows carry their own confidence.
4. **Modeling handoff.** §8 converts the findings into candidate tables, a canonical-name register, a predicate register, and a time-sensitivity register so the atlas can become data rather than prose.

### 0.2 Evidence classes (used inline as short tags)

| Tag | Class | Meaning in this note |
| --- | --- | --- |
| `[F]` | **documented fact** | Directly stated by a primary source (official documentation, specification, standards body, first-party release announcement). Scope is limited to what that source documents. |
| `[S]` | **reported signal** | Job postings, vendor positioning, secondary comparisons, market material. Useful, biased, and usually time-sensitive. |
| `[I]` | **inference** | Synthesis across two or more sources; not stated by any single source. |
| `[R]` | **recommendation** | Proposed design or operating choice for this atlas and its data model. |

Confidence scale per lens: **High** = primary documentation or a stable standard; **Medium** = multiple convergent secondary sources, or primary documentation for a moving target; **Low** = single-source, vendor-only, or emergent/naming-unstable.

### 0.3 Standing caveats carried from the prior passes

- Vendor comparison pages (e.g. Metabase-vs-Superset, parser benchmarks, "best agent framework" roundups) are **positioning artifacts**. They are cited as `[S]` and never promoted to `[F]`.
- Official documentation is strong evidence for *what a tool does* and weak-to-no evidence for *how well it performs, what it costs, or how widely it is adopted*. Benchmark magnitudes in the prior notes (e.g. "11.4× pandas", "3.89 s vs 365 s") are `[S]`, hardware- and version-bound.
- Occupational sources (BLS, O*NET) classify *occupations*, not employer title semantics. Employer titles drift faster than the taxonomy.
- Any bullet that depends on a product version, release status, or corporate structure is flagged in the **time-sensitivity register** (§8.4).

### 0.4 What would falsify the main conclusions

| Conclusion | Falsifier that would overturn it |
| --- | --- |
| Roles are non-interchangeable bundles, not equivalent labels | A large posting sample showing one title covering research synthesis, ontology design, and dashboard delivery with identical skill weights |
| Extraction is the highest-variance stage | Measured per-stage error budgets showing extraction error is dominated by upstream research-selection error |
| Evidence↔structured-data boundary is the main modeling fault line | A dominant practice where claims are stored without source spans and still pass downstream audit |
| Provenance is a governance gap, not a tooling gap | Broad adoption of claim-level provenance in mainstream BI/semantic layers with no bespoke engineering |
| Agent error is multiplicative across stages | Stage-isolated evaluations showing downstream stages reconverge after upstream hallucination |

---

## 1. Executive synthesis

1. **The cluster is a socio-technical pipeline, not a profession, a vendor, or a tool category.** Twelve stages, four entity families (capability, artifact, actor, governance), one loop. Modelling it as a single "data work" label is the most common and most costly collapse in the prior notes `[I]`. Confidence: High.
2. **The load-bearing boundary is evidence → structured data.** A citation, a PDF, and a claim are not records. A record needs at minimum: subject, predicate, object, source span, extraction method, schema version, uncertainty, and provenance. Everything downstream (query, analysis, visualization) inherits this stage's errors `[I/R]`. Confidence: High.
3. **DuckDB is no longer only "in-process".** Its own documentation now describes a **Quack protocol** that steps the engine out of purely embedded operation, alongside single-file storage, DuckLake lakehouse formats scaling to petabytes, DuckDB-Wasm in browsers, and 41.7k GitHub stars `[F]`. **DuckLabs (the >30-person Amsterdam company behind DuckDB) joined AWS effective 2026-09-01 (announced 2026-08-26); DuckDB, DuckLake and Quack remain MIT-licensed and the nonprofit DuckDB Foundation continues stewardship** `[F]`. Any note written before 2026-08 that lists DuckDB Labs as an independent bootstrapped vendor is now stale. Confidence: High for governance facts.
4. **DuckLake 1.0 (2026-04-13) reframes the lakehouse as SQL metadata, not files.** The catalog is any SQL database with primary keys (SQLite/PostgreSQL/DuckDB in the reference implementation); the spec is production-ready with backward-compatibility guarantees; the `ducklake` extension ships in DuckDB v1.5.2 and is a top-10 core extension by downloads `[F]`. "Database" versus "file format" becomes a design axis rather than a binary `[I]`. Confidence: High.
5. **The local analytics stack re-baselined in 2026 and the prior notes understate it.** pandas **3.0.0 (2026-01-21)** makes the dedicated `str` dtype the default (pyarrow-backed when available, not required) and Copy-on-Write the only mode, removing chained assignment and `SettingWithCopyWarning` `[F]`; **Polars 2.0 (first RC 2026-09-02)** makes the streaming engine the default for `LazyFrame.collect`, expects roughly 5× aggregate improvement, drops row-order guarantees for `join`/`group_by`/`unpivot` unless `maintain_order` is set, and removes lossy implicit casts `[F]`. "pandas is single-threaded and OOMs" and "Polars needs manual lazy wiring" are both now version-stale `[I]`. Confidence: High for release facts; Medium for magnitudes.
6. **Polars 2.0 is explicitly designed for AI-driven development.** The announcement justifies strictness partly because *agents* can call `collect_schema()` to validate query structure without materializing data, and adds typed `AttributeRemovedError`/`ArgumentRemovedError` so an agent can recover `[F]`. This is the clearest 2026 example of a data library optimizing for agent consumers, not only humans `[I]`. Confidence: High for the quote; Medium for generality.
7. **Agent infrastructure standardized around two protocol layers and one orchestration layer.** MCP's **2026-07-28** revision (final, LF Projects governance) moves to a **stateless core**, retires `initialize`/`Mcp-Session-Id`, adds `server/discover`, `Mcp-Method`/`Mcp-Name` header routing, cacheable list results, Multi Round-Trip Requests for sampling/elicitation, authorization hardening, an extensions framework (Tasks, MCP Apps, EMA), and a 12-month deprecation policy `[F]`. **Microsoft Agent Framework 1.0 (2026-04-03)** unifies Semantic Kernel + AutoGen into one open-source .NET/Python SDK with A2A and MCP interop plus an LTS commitment `[F]`. **LangGraph v1** keeps graph/state primitives unchanged and makes durable execution, checkpointing, streaming and human-in-the-loop first-class, deprecating `create_react_agent` for LangChain's `create_agent` `[F]`. Framework churn is the least stable part of the atlas `[I]`. A second, quieter convergence: **both major open-source BI tools now ship MCP servers** (Metabase 63, 2026-07-21; Apache Superset 6.1.0, 2026-06-11), which pulls the visualization and interpretation stages into the same agent-interaction surface as extraction and orchestration `[F]`. Confidence: High.
8. **Provenance and research-method standards exist, are stable, and remain largely unimplemented in the BI/data path.** W3C PROV (`Entity`/`Activity`/`Agent`) and PRISMA 2020 (27-item checklist + flow diagram; PRISMA-P for protocols) are stable primary standards `[F]`, while mainstream BI lineage is coarser and semantic layers rarely carry claim-level support/conflict `[I]`. The gap is organizational and modelling discipline, not the absence of a specification `[I/R]`. Confidence: High for standards; Medium for adoption.
9. **Roles differ by *output artifact*, not by tool list.** Data/BI analyst output = metric/dashboard; research analyst output = briefing/forecast; knowledge engineer output = computable model (ontology/graph/semantic layer); research engineer output = pipeline/eval harness; information architect output = taxonomy/metadata structure `[S]` — with all five using SQL and Python somewhere `[I]`. Title-based entity keys should be replaced by capability+output keys (§4.3) `[R]`. Confidence: Medium-High.
10. **The most defensible atlas design is claim-centric with graph projections.** A relational core (`source`, `claim`, `evidence`, `entity`, `relation`, `artifact`, `activity`, `quality_check`) plus optional RDF/graph and DuckDB/SQL projections satisfies provenance, query, and analysis needs together, and is compatible with both nanopublication-style atomic claims `[F]` and a PostgreSQL-style analytics path `[F]`. Confidence: Medium (design synthesis, not a documented standard).

**Open questions carried forward:** where the "analyst" boundary sits once agents generate dashboards; whether claim-level provenance can reach mainstream semantic layers; how per-stage error budgets should be measured; and which artifact type the emerging "AI/agent workflow specialist" actually produces `[I]`.

---

## 2. Lens findings

### 2.1 Skills

**Definition and scope.** A *skill* is a repeatable human or agent capability that transforms one artifact class into another. Skills are not tools (`SQL` is a skill; `DuckDB` is software) and not titles (a title bundles several skills). Eleven skills are in scope `[F, per [[The components to investigate]]]`.

| Skill | Boundary (what it is *not*) | Workflow stage | Artifact transformed | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| Research synthesis | Not literature search; synthesis appraises and combines, and reports method (PRISMA) | Research → Interpretation | Source set → appraisal + findings narrative | `[F]` PRISMA 2020 | High |
| Information extraction | Not summarization; extraction emits typed fields per a declared schema | Extraction | Unstructured span → typed record | `[F]` extraction tool docs | High |
| Data modeling | Not table creation; modeling chooses grain, keys, facts/dims, DAG shape | Structured representation → Normalization | Requirements → model spec | `[F]` dbt docs | High |
| Ontology design | Not schema-by-example; requires declared classes, relations, constraints (OWL/SHACL) | Structured representation | Domain → formal conceptualization | `[F]` W3C OWL/SHACL | High |
| Normalization | Not extraction; normalization reconciles units, vocabularies, and identity across sources | Normalization | Raw records → comparable records | `[F]` ELT/dbt docs | High |
| SQL | Not a database product; a declarative query/transformation language | Database → Analysis | Tables → result sets | `[F]` DuckDB/SQL docs | High |
| DuckDB operation | Not pandas manipulation; file/table-centric, out-of-core, SQL-first | Database → Query | Files/tables → aggregates | `[F]` DuckDB docs | High |
| pandas / Polars DataFrame work | Not SQL-first; programmatic, script/notebook-centric computation | Normalization → Analysis | DataFrames → results/models | `[F]` pandas 3.0 / Polars 2.0 docs | High |
| Visualization | Not chart rendering alone; makes encodings readable and defensible | Visualization | Result sets → encodings/dashboards | `[F]` Plot/BI docs | High |
| Provenance | Not logging; records entities/activities/agents and derivation at claim granularity | Cross-cutting | Runs + claims → derivation graph | `[F]` PROV-DM/PROV-O | High |
| Agent orchestration | Not prompt writing; owns state, handoffs, retries, gates, budgets, evals | Agent iteration | Goal → bounded multi-step execution | `[F]` LangGraph v1 / MAF 1.0 | Medium-High |

**Position in workflow.** Skills are cross-cutting but unevenly distributed: extraction and normalization dominate error variance, provenance is the only skill required at *every* stage, and orchestration only becomes necessary once stages are delegated to non-deterministic actors `[I]`.

**Relationships to other lenses.** `Skill used_in Workflow`; `Skill required_by Market Position`; `Skill implemented_by Software`; `Skill governed_by Methodology`; `Agent performs WorkflowStep` and `requires Skill`.

**Trade-offs and failure modes.** (a) Skill substitution without output change — a summarizer asked to extract emits prose shaped like data `[I]`. (b) Tool-skill conflation — "knows pandas" treated as "can model data" `[I]`. (c) Provenance treated as documentation rather than data capture, so it cannot be queried `[I/R]`. (d) A missing orchestration skill misdiagnosed as a framework-selection problem `[I]`.

**Confidence: High** for the skill list and for boundaries resting on standards/documentation; **Medium** for the error-variance ordering (inference across prior passes, unmeasured).

### 2.2 Market positions

**Definition and scope.** A *market position* is an employer- or market-level label that bundles skills, workflow stages, and expected output artifacts. These labels are **not synonyms**: several prior passes converge on the finding that "analyst" spans everything from Excel reporting to ontology engineering `[S]`.

| Position | Output artifact (primary) | Distinct skill/tool signal | Workflow locus | Definitional maturity |
| --- | --- | --- | --- | --- |
| Data analyst | Dashboard, KPI set, ad-hoc answer | SQL + BI semantics + storytelling | Query → Interpretation | Mature, broad |
| Data/BI analyst | Governed metric layer + dashboards | + semantic layer, metric definitions, row-level security | Storage → Visualization | Mature |
| Research analyst | Briefing, market/sector forecast | Surveys, domain expertise, statistics; Excel/SPSS | Research → Interpretation | Mature, largely non-technical |
| Knowledge engineer | Ontology, knowledge graph, semantic/RAG grounding | RDF/SPARQL/OWL/SHACL, graph DBs | Representation → Normalization | Mature concept, inflated usage |
| Information architect | Taxonomy, metadata/navigation model | Content/schema modelling, metadata standards | Representation (broader than graphs) | Stable |
| Research engineer | Pipeline, evaluation harness, prototype system | Python, infra, experimentation, scraping | Research → Iteration | Mature |
| Data engineer (boundary role) | Pipelines, warehouse/lake, contracts | Orchestration, ingestion, quality/scale | Extraction → Storage | Mature |
| Automation specialist | Automations (RPA/script/API glue) | Scripting, integrations, workflow platforms | Any repetitive stage | Weak/emergent |
| AI/agent workflow specialist | Agent graph, tool/MCP wiring, eval suite | Orchestration frameworks, MCP/A2A, tracing | Agent iteration | Emergent, vendor-driven |
| BI developer (adjacent) | Semantic models + embedded analytics | Warehouse SQL, BI modelling | Storage → Visualization | Mature |

**Position in workflow.** Positions cluster at different stages — which is *why* they are not interchangeable: dashboards and briefings both end in "insight" but start from different evidence classes under different quality tests `[I]`.

**Relationships to other lenses.** `Market Position performs Workflow`; `requires Skill`; `produces Artifact`; `appears_in Company (hiring)`; `uses Software`.

**Trade-offs and failure modes.** Title inflation; "knowledge engineer" rebranded for RAG without logic/ontology training, producing shallow ontologies `[I]`; automation and agent titles lacking a hiring taxonomy `[S]`; one title spanning Excel to ML inside a single market `[S]`.

**Confidence: High** for analyst/engineer/knowledge-engineer/information-architect boundaries; **Low-Medium** for automation and AI-agent workflow titles (emergent, vendor-shaped, thin samples in prior passes).

### 2.3 Technology

**Definition and scope.** A *technology* is a durable technical substrate or standard. It is distinct from the software implementing it (`SQL` vs a database engine), the product packaging it (an engine vs a hosted service), and the company stewarding it.

| Technology | Boundary note | Workflow stage | Representative implementations | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| Python | General language, not a data tool | Cross-cutting | pandas, Polars, Playwright, agent SDKs | `[F]` docs | High |
| SQL | Language/standard, not an engine | Query, Analysis | DuckDB, PostgreSQL, warehouses | `[F]` duckdb.org | High |
| Columnar file formats | File-level, not a warehouse | Storage | Parquet, Arrow IPC | `[F]` DuckDB/Polars docs | High |
| Apache Arrow (in-memory) | Memory layout/interchange, not storage | Cross-cutting (zero-copy boundaries) | pandas 3.0 `str` via pyarrow, Polars, DuckDB | `[F]` pandas 3.0 blog | High |
| In-process OLAP | Single-node embedded engine, not distributed MPP | Database, Query | DuckDB, DuckDB-Wasm | `[F]` duckdb.org | High |
| Lakehouse table format | Metadata layer over object storage, not a DBMS | Storage | DuckLake 1.0, Iceberg, Delta | `[F]` DuckLake 1.0 | High |
| Notebook-computational narrative | Execution environment, not a file format | Analysis, Visualization | Jupyter, Observable, marimo | `[F]` Jupyter/Observable docs | High |
| HTTP APIs / web scraping | Ingest mechanism, not extraction semantics | Research → Extraction | HTTP clients; extraction services | `[S]` tool docs (+ legal caveat) | Medium-High |
| Browser automation | Controls a browser, not a site's schema | Extraction | Playwright, Skyvern | `[S]` docs + vendor | Medium |
| LLMs / embeddings | Probabilistic substrate; neither a database nor a correctness guarantee | Extraction, Interpretation, Agent iteration | Provider APIs, local models | `[F]` MCP/agent docs | Medium-High |
| Graph technologies | Model choice (RDF/SPARQL, property graph), not merely a store | Representation, Query | RDF+SPARQL+OWL/SHACL, Cypher | `[F]` W3C, Neo4j | High |
| Provenance model (PROV) | Vocabulary/standard, not a logging library | Cross-cutting | PROV-DM, PROV-O, PROV-N | `[F]` W3C REC | High |
| Agent interaction protocols | Wire contracts, not frameworks | Agent iteration | MCP 2026-07-28, A2A | `[F]` MCP spec, MAF 1.0 | High |
| Constraint/validation languages | Constraint semantics, not a pipeline | Structured representation → Normalization | JSON Schema, SHACL, dbt tests | `[F]` specs/docs | High |

**Position in workflow.** Python/pandas/Polars → Normalization/Analysis; SQL/DuckDB/lakehouse → Storage/Query; APIs/scraping/browser automation → Research/Extraction; LLMs/embeddings → Extraction/Interpretation/Agent iteration; graphs → Representation/Query; PROV and validation languages → cross-cutting governance `[I]`.

**Relationships to other lenses.** `Technology implemented_by Software`; `used_by Workflow`; `supports Agent`; `defined_by Standard`; `Software produced_by Company`.

**Trade-offs and failure modes.** Scraping fragility plus legal/ToS exposure `[S]`; embeddings lose exactness and weaken provenance `[I]`; graph modelling carries upfront ontology cost and a skill scarcity `[I]`; probabilistic extraction produces **silent** schema drift rather than a parsing crash `[I]` — the highest-cost failure mode in the cluster `[I/R]`.

**Confidence: High** for substrate boundaries and standards; **Medium** for comparative robustness claims; scraping legality is jurisdiction-dependent.

### 2.4 Software

**Definition and scope.** *Software* is an installable or hosted executable artifact. Maintaining a five-way distinction `Technology → Software → Product → Company → Standard` prevents the atlas from collapsing DuckDB-the-engine, the DuckDB binary, a hosted DuckDB service, DuckLabs, and the DuckDB Foundation into one node `[R]`.

| Software | Core job | Strength | Boundary / limitation | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| DuckDB | in-process analytical SQL | SQL over files+tables, no external deps, ACID/MVCC, extensions, browser build; Quack adds remote access | not a multi-tenant warehouse control plane | `[F]` duckdb.org | High |
| pandas 3.0 | Python tabular manipulation | ecosystem breadth; default `str` dtype; Copy-on-Write only | migration cost: chained assignment and `SettingWithCopyWarning` gone | `[F]` pandas 3.0 blog/whatsnew | High |
| Polars 2.0 | DataFrame/query engine | streaming by default (≈5× expected), strictness, `collect_schema()` for agents | row order not guaranteed for `join`/`group_by`/`unpivot` unless requested | `[F]` pola.rs 2.0 RC post | High |
| DuckLake | lakehouse format (SQL catalog + object storage) | production-ready v1.0, backward compatibility, catalog = SQLite/Postgres/DuckDB | young ecosystem vs Iceberg/Delta | `[F]` ducklake.select v1.0 | High |
| Jupyter | interactive notebook environment | ubiquity, kernel ecosystem, narrative + code | execution order, environment drift, hidden state | `[F]` docs; `[I]` limits | High |
| dbt (Core/Cloud) | SQL/Python transformation in a project | modular models, DAG, tests, docs, CI | depends on an execution backend; not a source-research tool | `[F]` docs.getdbt.com | High |
| Metabase | BI questions, models, dashboards, embedding | low-friction self-serve; v63 (2026-07-21) adds treemaps, 2FA, PDF subscriptions, custom viz, and an **MCP server with authorization audit logs** | governance/semantic depth limited at lower tiers; MCP dynamic client registration off by default | `[F]` metabase.com/releases/metabase-63 | Medium-High |
| Apache Superset | open-source BI exploration + dashboards | broad viz/DB connectivity, SQL Lab; **6.1.0 (2026-06-11)** adds an Extensions framework with stable APIs, a Global Task Framework, and an **MCP service** for AI assistants | heavier ops; semantic consistency needs setup | `[F]` release post + ASF 6.1.0 downloads; `[S]` vendor-affiliated author | Medium-High |
| Observable / Plot | reactive notebook + grammar-of-graphics viz | authoring-grade interactive visual narrative | not an ingestion/storage/governance layer | `[F]` docs | High |
| Airflow | scheduled DAG orchestration | explicit tasks, dependencies, backfills | orchestration is not quality or semantics | `[F]` docs | High |
| Playwright | browser automation | multi-browser control + assertions, agent-drivable | selector/auth/site-change brittleness | `[F]` docs | High |
| OpenLineage | lineage event model | dataset/job/run vocabulary | metadata does not verify values | `[F]` spec docs | High |
| Unstructured / LlamaParse+LlamaExtract | document → structured output | layout/table handling, schema-constrained extraction, item citations/confidence | probabilistic fill; cost and format-coverage limits | `[F]` tool docs; `[S]` benchmarks | Medium-High |
| LangGraph v1 | stateful agent graph runtime | durable execution, checkpointing, streaming, HITL first-class | graph programming model; framework churn | `[F]` LangGraph v1 docs | High |
| Microsoft Agent Framework 1.0 | multi-agent orchestration SDK | .NET+Python, A2A/MCP interop, LTS, unifies AutoGen+Semantic Kernel | new surface; migration needed from AutoGen/SK | `[F]` MS devblog 2026-04-03 | High |
| CrewAI | role/task agent teams | fast start for sequential collaboration | token cost; weaker state control than graph runtimes | `[S]` third-party | Medium |
| OpenAI Agents SDK | agents + tools + handoffs + guardrails + tracing | compact, typed, provider-aligned | provider-centric ecosystem | `[F]` docs | Medium-High |

**Position in workflow.** The same software can occupy several stages (a notebook is Analysis *and* Visualization authoring), so `Software appears_in WorkflowStep` must be many-to-many `[R]`.

**Trade-offs and failure modes.** Silent memory blow-up from legacy pandas patterns; Polars 2.0 migration breakage; DuckDB single-node scaling ceiling; BI semantic drift under self-serve; orchestration mistaken for quality; parser output that satisfies a schema while being false `[I]`.

**Confidence: High** for documented capabilities; **Medium** for BI limits and all benchmark magnitudes.

### 2.5 Companies

**Definition and scope.** *Company* covers four roles that must not be merged: **employers** (hire the positions), **vendors** (sell and support products), **open-source foundations/projects** (steward code and standards), and **research organizations/consultancies** (produce methods and client systems) `[F]`.

| Category | Entity | What it is | Evidence | Confidence |
| --- | --- | --- | --- | --- |
| Vendor (absorbed into Big Tech) | DuckLabs (DuckDB Labs) | >30-person Amsterdam team behind DuckDB; bootstrapped and founder-owned until joining **AWS effective 2026-09-01** (announced 2026-08-26, completed 2026-08-31) | `[F]` first-party announcement; founders Mark Raasveldt & Hannes Mühleisen | High |
| Nonprofit foundation | DuckDB Foundation (Amsterdam, NL) | Continues stewardship of DuckDB/DuckLake/Quack; plans a technical advisory board; MIT licence retained | `[F]` ducklabs.com announcement; duckdb.org footer © 2026 DuckDB Foundation | High |
| Vendor (product company) | MotherDuck | Hosted DuckDB positioning + hosted DuckLake service; CEO quoted endorsing the AWS move | `[F]` DuckLake 1.0 adoption section; `[S]` prior-note funding details | Medium-High |
| Standards body (foundation) | Model Context Protocol (a Series of LF Projects, LLC) | Governs the MCP specification and Tier-1 SDKs; 2026-07-28 revision; 12-month deprecation policy | `[F]` MCP blog | High |
| Vendor (framework + observability) | LangChain, Inc. | LangGraph / LangChain / LangSmith: agent runtime plus evaluation tooling | `[F]` LangGraph v1 docs | High |
| Vendor (platform) | Microsoft | Microsoft Agent Framework 1.0 unifying AutoGen + Semantic Kernel; Azure/Foundry distribution | `[F]` devblog 2026-04-03 | High |
| Vendor (data platform) | dbt Labs | dbt Core/Cloud; defines the reference ELT "T" with tests, docs, lineage | `[F]` docs.getdbt.com | High |
| Vendor (BI) | Metabase, Inc. | Open-source + commercial BI and embedding | `[F]` project docs/releases; `[S]` positioning | Medium-High |
| Foundation/project | Apache Software Foundation | Stewards Apache Superset (and Airflow) | `[F]` project sites | High |
| Vendor (managed OSS) | Preset | Managed Superset hosting | `[S]` prior-note sources | Medium |
| Vendors (extraction) | Unstructured; LlamaIndex | Document parsing/extraction products and SDKs | `[F]` tool docs; `[S]` comparisons | Medium-High |
| Vendor (graph) | Neo4j | Property-graph database plus graph-analytics ecosystem | `[F]` product docs | High |
| Research organizations | CWI Amsterdam (Database Architectures); Universität Tübingen (database systems) | Origin research group for DuckDB; public endorsements of continued open-source governance | `[F]` quotes in the DuckLabs announcement (Peter Boncz, CWI; Torsten Grust, Tübingen) | High |
| Employers (role demand) | Banks, insurers, asset managers, consultancies, tech firms | Hire research analysts, data/BI analysts, knowledge engineers, research engineers | `[S]` job postings in prior notes (e.g. Accenture knowledge-engineer postings) | Medium |
| Sector research firms | Gartner, Forrester, Wood Mackenzie and equivalents | Research-analyst employers producing forecasts/briefings | `[S]` prior notes; weak samples | Low-Medium |

**Position in workflow.** Vendors concentrate in Extraction, Storage, Query, Visualization and Agent iteration (the monetizable stages); foundations sit on formats/protocols/standards; research organizations supply the method layer and much of the technology lineage `[I]`.

**Relationships to other lenses.** `Company produces Product`; `employs Market Position`; `stewards Software/Standard`; `acquired_by Company`; `sponsors Research`.

**Trade-offs and failure modes.** Consolidation risk (an engine steward absorbed by a hyperscaler changes incentives even when the licence does not) `[I]`; vendor-authored comparisons; stale funding/headcount data in earlier notes; role-demand inference from small posting samples `[I]`.

**Confidence: High** for entity classification and the 2026 governance change; **Medium** for employer/sector mapping; **Low** for market-sizing (no sizing claims are made here).

### 2.6 Products

**Definition and scope.** A *product* is a packaged offering aimed at a user problem, positioned at a workflow stage, with a differentiating capability. Definition template used below: `problem → stage → differentiator → boundary` `[R]`.

| Product (pattern) | User problem | Workflow position | Differentiating capability | Boundary |
| --- | --- | --- | --- | --- |
| Embedded analytical database (DuckDB, DuckDB-Wasm) | Analyse local or remote files/tables without infrastructure | Database → Query | SQL + ACID in-process, zero deps, Arrow/Parquet, browser deployment | not multi-tenant governance or scale-out |
| Hosted analytical service (MotherDuck and peers) | Shared team DuckDB without running servers | Storage → Query | managed engine, concurrency/isolation model, hosted lakehouse | lock-in and cost model |
| Lakehouse format + catalog (DuckLake 1.0) | Data on object storage, queryable as a database | Storage | SQL-database catalog, backward-compatible spec, inlining, deletion vectors | ecosystem age vs Iceberg/Delta |
| Transformation framework (dbt Core/Cloud) | Repeatable, tested, documented transformations | Normalization → Storage | models-as-SELECT, DAG, tests, docs, environments | needs an execution backend |
| Semantic/metric layer (dbt semantic models/MetricFlow and peers) | One definition of a metric across tools | Storage → Visualization | metric definitions in version control | adoption and engine coupling `[S/I]` |
| BI product (Metabase, Superset, Preset) | Self-serve questions and dashboards | Visualization → Interpretation | question builder, sharing/embedding, open-source deploy, and (since 2026) an **MCP server exposing governed data to AI clients** | semantic correctness inherits the model |
| Notebook product (Jupyter, Observable, marimo) | Exploration with narrative and interactivity | Analysis → Visualization | reproducible narrative; reactive updates; exportable artifacts | weak governance/ingestion story |
| Document extraction product (Unstructured, LlamaParse/LlamaExtract) | Turn PDFs/HTML into schema-valid records | Extraction → Structured representation | layout/table awareness, schema-constrained output, per-item citations and confidence | probabilistic; cost; format gaps |
| Research agent product (deep-research style assistants) | Multi-source synthesis with citations | Research → Evidence → Interpretation | search breadth and summarization speed; reproducible artifacts in at least one studied case | citation fidelity, paywalls, non-reproducibility; peer-reviewed feasibility study of Elicit found ≈86% value accuracy but far weaker stability of the *supporting quotes* `[F]` |
| Agent runtime/framework (LangGraph, Microsoft Agent Framework, CrewAI, OpenAI Agents SDK) | Reliable multi-step tool use | Agent iteration | durable state/checkpoints, handoffs, guardrails, tracing | framework churn; probabilistic execution |
| Knowledge/RAG system (graph, vector, hybrid) | Ground answers in a curated corpus | Representation → Query | semantic retrieval plus relation traversal | ontology upkeep; retrieval opacity |
| Observability/eval product (LangSmith and peers) | Know whether the pipeline works | Agent iteration | traces, datasets, evals, HITL review | measures only what it instruments |

**Position in workflow.** Products cluster where value is billable: extraction, storage/query, and agent iteration. **No verified product owns the evidence → structured-data boundary end-to-end**, which is the cluster's structural gap `[I/R]`.

**Trade-offs and failure modes.** Products promising "research in, insight out" hide schema and provenance work; products promising "data platform" hide source-selection work; the seam between them is where projects fail `[I/R]`.

**Confidence: High** for product-category boundaries; **Medium** for differentiator claims; **Low** for any single vendor's superiority claim.

### 2.7 Methodologies

**Definition and scope.** A *methodology* is a documented, repeatable procedure that governs how a workflow stage is performed and how its output is judged. Methodologies are the *rules*, including the required reports — distinct from both tools and skills.

| Methodology | Governs | Required artifact / gate | Status | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| Systematic review protocol (PRISMA 2020) | Research → Evidence → Interpretation | 27-item checklist + flow diagram; PRISMA-P for protocols | Stable standard; explicitly **not** a quality-appraisal instrument | `[F]` BMJ PRISMA 2020 | High |
| Evidence-appraisal / certainty frameworks (GRADE-class) | Evidence → Interpretation | Certainty-of-evidence summary | Stable in health evidence synthesis; rare in data work | `[I]` prior notes | Medium |
| Provenance model (W3C PROV) | Cross-cutting | Entity/Activity/Agent derivations | W3C Recommendation, stable | `[F]` PROV-DM/PROV-O | High |
| Nanopublication model | Structured representation → Database (claims) | Atomic claim + assertion/provenance/publication-info graphs; immutable content-hash identifier | Spec/guidelines available; niche adoption | `[F]` nanopub guidelines ([[G1]]–[[G3]]) | Medium-High |
| ETL (extract-transform-load) | Extraction → Normalization → Database | Transform before load; constrained by target load step | Legacy-dominant; still valid for constrained targets | `[F]` warehouse docs ([[CP L6]]) | High |
| ELT (extract-load-transform) | Extraction → Database → Normalization | Load raw, transform in place; version-controlled models | Current default in cloud analytics | `[F]` dbt/warehouse docs | High |
| Dimensional/relational modelling | Structured representation → Normalization | Facts, dimensions, grain, keys | Mature; still the BI default | `[F]` warehouse/dbt docs | High |
| Medallion layering (bronze/silver/gold) | Storage → Normalization | Raw retention, validation/cleaning, business models | Vendor-recommended pattern, not mandatory | `[F]` Databricks docs ([[CP L6]]) | Medium-High |
| Semantic/metric layer definition | Storage → Visualization → Interpretation | Governed metric definitions | Converging practice, engine-coupled | `[S]` vendor docs | Medium |
| Schema-first extraction protocol | Extraction → Structured representation | Declared schema + validation + per-field citation/confidence | Emergent de facto method in extraction products | `[F]` extraction tool docs | Medium-High |
| Test-and-contract pattern | Normalization → Storage | Asserted tests on models; failing-row semantics | Mature in dbt-style projects; often absent in ad-hoc pipelines | `[F]` dbt tests docs | High |
| Notebook narrative + parameterization | Analysis → Visualization | Executable narrative; parameterized reruns | Widely practised, weakly governed | `[F]` Jupyter/Observable docs; `[I]` limits | Medium-High |
| Agent evaluation protocol (traces + datasets + graders + HITL) | Agent iteration | Per-step traces, eval sets, review gates, budgets | Emergent; tooling-led, no standard | `[F]` LangGraph/LangSmith + MAF docs; `[I]` | Medium |
| Data governance/access control | Cross-cutting (Storage → Visualization) | RBAC, masking, audit, lineage | Mature in warehouses; rarely claim-level | `[F]` warehouse docs ([[CP L6]]) | High |

**Position in workflow.** Methodologies are the strongest constraint available *before* execution: PRISMA vs ad-hoc review, ETL vs ELT, and schema-first vs heuristic extraction determine which quality gates are even possible `[I]`.

**Relationships to other lenses.** `Methodology governs Workflow`; `requires Artifact/Gate`; `implemented_by Software`; `applied_by Market Position`; `encoded_in Standard`.

**Trade-offs and failure modes.** Methodology theatre — a PRISMA flow diagram attached to an unstructured LLM review `[I]`; ETL/ELT chosen by fashion rather than target constraints `[I]`; provenance vocabulary adopted without per-claim capture `[I]`; governance applied to storage but not to extracted claims `[I/R]`.

**Confidence: High** for standards and warehouse/dbt methods; **Medium** for emergent extraction/agent protocols.

### 2.8 Workflows

**Definition and scope.** A *workflow* is a named, repeatable sequence of stages with declared inputs, outputs, decisions, and quality gates. The generic cluster workflow is given in [[The components to investigate]]; the archetypes below are the instances practitioners actually run `[F for named practice; I for the mapping]`.

| Workflow archetype | Trigger | Inputs | Outputs | Gates that matter | Typical tool path |
| --- | --- | --- | --- | --- | --- |
| Ad-hoc question answering | A decision needs a number | One or two sources/tables | A number with a screenshot | Source legitimacy; metric definition | SQL/BI |
| Evidence-backed dataset build | A dataset must be assembled from documents and web sources | Source corpus + target schema | Normalized, queryable dataset + provenance | Schema validation; duplicate/entity resolution; spot-check audit | Scrape/API → extraction → pandas/Polars → DuckDB → notebook |
| Research brief / market scan | A decision needs a synthesized view | Source set (reports, filings, interviews) | Briefing with citations and stated limits | Source appraisal (PRISMA-like); claim-level citation | Research tools → notes → synthesis |
| Living review / monitored corpus | The evidence base changes over time | Monitored sources + prior claims | Updated claims + change log | Re-extraction consistency; supersession handling | Scheduler → extraction → versioned store |
| Analytics engineering pipeline | A metric must be trustworthy and reusable | Raw loads + business definitions | Modeled tables + tested metrics + dashboards | Model tests; metric definitions; code review | dbt + warehouse/DuckDB → BI |
| Notebook analysis cycle | An exploratory question | DataFrames/tables | Analysis + visualization + narrative | Reproducibility; parameterization | pandas/Polars/Jupyter/Observable |
| Agent-orchestrated research loop | A recurring research/extraction process | Tools + schema + budgets | Extracted records + eval report | Per-step verification; budget; HITL escalation | Agent runtime + MCP tools + traces |

**Position in workflow.** Workflows *are* the pipeline instantiated with a purpose: methodologies govern them, software implements them, roles execute them, and agents partially automate them `[I]`.

**Relationships to other lenses.** `Workflow uses Technology/Software`; `governed_by Methodology`; `appears_in Market Position`; `produces Artifact`; `has WorkflowStep`; `Agent performs WorkflowStep`; `WorkflowRun produces Artifact`.

**Trade-offs and failure modes.** (a) Skipping a gate to save time moves the cost downstream, where diagnosis is harder `[I]`. (b) Picking a workflow archetype by tool preference rather than by evidence class `[I]`. (c) Iteration without versioning produces "which number is right?" drift `[S]`.

**Confidence: Medium-High** — archetypes are inferred from cited tool/method documentation plus prior-pass signals; no field study was conducted.

### 2.9 Agents

**Definition and scope.** An *agent* is a bounded software actor with a goal, tool access, state, an output contract, and a verification expectation. Excluded by definition: single-shot prompt calls with no tools and no state (those are model invocations) `[R]`.

| Agent | Task | Required tools / state | Handoff and verification | Failure modes |
| --- | --- | --- | --- | --- |
| Research / scout | Find and rank candidate sources for a question | Search/scrape tools, source register, dedupe state | Hands candidate set + rationale to extraction; verified by source-quality rubric + human sampling | Paywall/SEO bias; fabricated citations; stale sources; runaway breadth |
| Extraction | Convert documents/pages into schema-valid records | Parsers, model provider, JSON Schema, span locators | Hands typed records to normalization; verified by schema check + span spot-check | Silent schema drift; hallucinated fills; unit/period misreads; table-flattening errors |
| Entity resolution / normalization | Reconcile identity, units, vocabularies across sources | Reference lists, blocking/fuzzy tools, rules | Hands canonical records to storage; verified by duplicate-rate and conflict counts | Over-merging distinct entities; unit confusion; locale/date errors |
| Data cleaning | Repair nulls, types, outliers, encodings | DataFrame/SQL engine, rule set | Hands clean tables + change log; verified by rule tests + before/after diff | Lossy irreversible edits; "fixing" legitimate outliers; unlogged changes |
| Coding | Write/modify pipeline, SQL, notebook code | Repo access, test runner, linter, schema | Hands runnable code; verified by tests, review, reproducibility rerun | Invented APIs; tests that assert the bug; dependency drift |
| Analytical | Compute statistics/aggregations and interpret | Query engine, notebook kernel, chart lib | Hands results + interpretation; verified by recomputation and alternative specification | Metric substitution; specification searching; over-claiming causality |
| Visualization | Produce encodings from result sets | Plot/chart library, style rules | Hands figures + alt text; verified against data and audience test | Misleading scales; decorative encodings; accessibility gaps |
| Orchestrator / coordinator | Plan, route, budget, retry, escalate | Workflow runtime, state store, budget/policy config | Owns handoffs and gates; verified by per-step traces and eval sets | Cross-stage error amplification; context overflow; loops; memory poisoning; budget burn |
| Verifier / critic | Attack claims and outputs independently | Retrieval over sources, rules, checklists | Emits pass/fail + evidence; feeds gates and re-planning | Rubber-stamping; correlated blind spots with the producer; false confidence |

**Position in workflow.** Agents are strongest as *stage-local operators* with typed outputs and explicit gates, and weakest as end-to-end replacements for research design, schema design, and interpretation `[I/R]`. Verification must be **per stage**: an end-to-end score hides which stage introduced the error `[I/R]`.

**Required state and handoff contract.** Minimum viable handoff = input artifact reference + schema version + output contract + provenance record + confidence + escalation rule. Without a schema version in state, an agent cannot detect drift it caused itself `[R]`.

**Relationships to other lenses.** `Agent performs WorkflowStep`; `requires Tool`; `produces Artifact`; `constrained_by Budget/Policy`; `governed_by Methodology`; `verified_by Verifier/Human`; `traced_by Observability Product`.

**Trade-offs and failure modes.** Errors are multiplicative, not additive: a hallucinated source becomes an extracted record, a normalized fact, a chart, and a conclusion `[I]`. Claimed failure classes across the verified documentation set: hallucination, context overflow, reasoning loops, memory poisoning, provenance loss, framework-version breakage `[F for mechanisms; S for severity rankings]`. Verified 2026 mitigation primitives: durable checkpointing + HITL (LangGraph v1), stateless MCP requests with header-based routing and cacheable tool catalogs (MCP 2026-07-28), pre-materialization schema validation (Polars `collect_schema()`), guardrails plus A2A/MCP interop (Microsoft Agent Framework 1.0) `[F]`.

**Confidence: Medium** for the taxonomy (synthesis); **High** for tool/protocol capabilities; **Low** for general superiority claims about any agent architecture.

---

## 3. Workflow map

Stage-by-stage map. **Decision** = the choice made at that stage; **Gate** = the check that must pass before proceeding `[I/R for framing; F for the cited tool capabilities]`.

### 3.1 Stages 1–6

| # | Stage | Inputs | Activities / decisions | Outputs | Quality gate | Likely tools | Suitable agent role |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Research (question + protocol)** | Goal, stakeholder question, prior work | Frame question; scope and inclusion/exclusion; time window; declare method; decide review vs scan vs experiment | Protocol / question spec + scope + success criteria | Is the question answerable with available evidence classes? Was the method declared *before* collection? | Protocol templates, notes, issue trackers | *Research/scout* drafts candidates and prior work; **human owns the protocol** |
| 2 | **Evidence (collection + appraisal)** | Protocol; source candidates | Acquire sources (PDF/HTML/API); record metadata; appraise authority, recency, bias; deduplicate; capture spans | Source register (URL/date/publisher/spans) + appraisal notes | Provenance captured per source; licence/ToS/paywall cleared; duplicates removed | Browser automation, HTTP clients, parsers, reference managers | *Research/scout* + *verifier* applying a source-quality rubric |
| 3 | **Extraction** | Sources + target schema | Define schema first; convert spans to typed fields; handle tables/layout; record confidence + locator | Typed records + extraction log (tool/model, prompt or rule version, locator) | Schema validation; span spot-check; unit/period sanity; extraction version recorded | Document extraction products, LLM structured outputs, regex, DataFrame parsers | *Extraction agent*; *verifier* samples spans |
| 4 | **Structured representation** | Typed records + domain model | Choose representation (relational/document/graph/claim-graph); define entities, keys, relations, cardinality; declare ontology or schema | Schema/ontology + entity definitions + JSON Schema/SHACL constraints | Can every required claim be expressed? Are keys stable? Are relations typed? | JSON Schema, RDF/OWL/SHACL, ER modelling, DuckDB DDL | *Coding agent* implements the declared schema; **human owns ontology decisions** |
| 5 | **Normalization** | Raw typed records | Canonicalize units, currencies, dates, locales, vocabularies; resolve entities; deduplicate; reconcile conflicts; log transformations | Comparable, deduplicated records + transformation/provenance log | Duplicate-rate and conflict counts within threshold; transformations logged or reversible; no silent losses | pandas 3.0, Polars 2.0, SQL/DuckDB, entity-resolution tooling | *Entity-resolution* and *data-cleaning* agents; *verifier* audits changes |
| 6 | **Database (storage + load)** | Normalized records | Choose store (single-file DuckDB / lakehouse catalog / warehouse / graph); load; version; apply constraints, indexes, partitioning; set access control | Queryable store + version/snapshot + load log + access policy | Load idempotency; constraints applied; snapshot recoverable; access policy set before sharing | DuckDB (file or DuckLake catalog), warehouses, graph DBs, Parquet/Arrow, OpenLineage events | *Coding agent* runs loads; *orchestrator* enforces schedule and rollback |

### 3.2 Stages 7–12

| # | Stage | Inputs | Activities / decisions | Outputs | Quality gate | Likely tools | Suitable agent role |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | **Query** | Queryable store + question | Translate question into query; choose grain/joins/filters; manage cost and correctness; parameterize for reuse | Result sets / views / models | Does the query answer the declared question? Are joins non-duplicating? Is the metric the governed definition? | SQL, DuckDB, dbt models + tests, semantic layer | *Coding agent* writes and repairs queries; **human reviews metric definitions** |
| 8 | **Analysis** | Result sets | Aggregate, compare, test, model; quantify uncertainty; check alternative specifications and sensitivity | Findings + uncertainty + method notes | Recomputable from stored data; assumptions stated; sensitivity checked; no unstated substitutions | pandas/Polars, notebooks, statistics libraries | *Analytical agent*; *verifier* recomputes independently |
| 9 | **Visualization** | Findings | Choose encoding and granularity; design for audience; annotate caveats; ensure accessibility | Charts, dashboards, interactive artifacts | Encoding matches the claim (no truncated/misleading axes); caveats visible; accessible text present | Plot/Observable, Metabase/Superset, notebooks | *Visualization agent*; **human** for audience judgment |
| 10 | **Interpretation** | Findings + visualizations + context | Decide what it means; state limits; separate observation from inference; recommend decisions | Report/briefing with claims, confidence, limits, citations | Every claim traceable to data + source; limits and counter-evidence stated; reviewer sign-off | Notes, BI shares, publication tooling | **Human-owned**; *verifier/critic* challenges claims |
| 11 | **New research** | Gaps, contradictions, limits | Reformulate questions; update protocol; extend or supersede claims; register the next iteration | Updated protocol / question backlog + supersession records | Changed claims versioned against predecessors; new gaps captured as first-class entities | Versioned notes, claim store, scheduler | *Research/scout* proposes; **human prioritizes** |
| 12 | **Agent iteration** | Traces, eval results, failure reports | Replay failures; patch prompts/tools/schemas; rerun evals; adjust budgets and gates; checkpoint improvements | Updated agent config + eval report + changelog | Per-step traces recorded; evals rerun after changes; regressions detected; human approval for autonomy changes | LangGraph + LangSmith, MAF + observability, MCP tool catalogs | *Orchestrator* runs the loop; **human** approves autonomy and gate changes |

### 3.3 Feedback loops and the gates that matter

- **10 → 1 evidence update:** interpretation exposes a weak or missing source class → protocol revised `[I]`.
- **11 → 3 schema repair:** new claims don't fit the schema → schema version bumped, extraction rerun over affected spans `[I/R]`.
- **12 → any agent revision:** an eval failure patches the responsible stage rather than the whole pipeline `[R]`.
- **9 → 7 viz exposes query error:** a chart makes a join error visible → fix the query before anything downstream proceeds `[I]`.
- **Load-bearing gates:** protocol declared → provenance captured → schema validated → duplicates/conflicts bounded → constraints applied → question-to-query match → recomputability → encoding honesty → claim traceability → versioned supersession → trace-level evaluation `[R]`. Skipping an early gate cannot be compensated later `[I]`.

---

## 4. Entity and relationship candidates

One row per distinct entity or relationship. Stable names; no merging of distinct concepts. Source IDs (`S1`–`S27`) resolve in §7. This table is designed to be loaded directly into the `schemas/` + `data/` layers `[R]`.

### 4.1 Skills and market positions

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Skill | Research synthesis | Appraises and combines a source set into findings under a declared method | Research → Interpretation | PRISMA 2020, Research Analyst | governed_by, appears_in | S14 | High |
| Skill | Information extraction | Converts spans into typed fields per a declared schema | Extraction | JSON Schema, Extraction Agent | implemented_by, requires | S18 | High |
| Skill | Data modeling | Chooses grain, keys, facts/dims and the transformation DAG | Structured representation → Normalization | dbt, DuckDB, Data Engineer | implemented_by, appears_in | S10 | High |
| Skill | Ontology design | Declares classes, relations, constraints for computable meaning | Structured representation | OWL, SHACL, Knowledge Engineer | implemented_by, appears_in | S24 | High |
| Skill | Normalization | Reconciles units, vocabularies and identity across sources | Normalization | pandas, Polars, Data Cleaning Agent | implemented_by, required_by | S4, S6 | High |
| Skill | SQL | Declarative query/transformation language | Database → Analysis | DuckDB, dbt, Metabase | uses | S1, S10 | High |
| Skill | DuckDB operation | Tuning in-process/file-centric OLAP queries and extensions | Database → Query | DuckDB, Parquet, DuckLake | implemented_by | S1, S3 | High |
| Skill | pandas DataFrame work | Programmatic tabular manipulation with the 3.0 semantics (`str` dtype, CoW) | Normalization → Analysis | pandas, Jupyter | implemented_by | S4, S5 | High |
| Skill | Polars DataFrame work | Lazy/streaming expression-based querying and transformation | Normalization → Analysis | Polars, Arrow | implemented_by | S6 | High |
| Skill | Visualization | Selects and defends encodings; designs for audience and accessibility | Visualization | Plot, Metabase, Superset | implemented_by | S11, S12 | High |
| Skill | Provenance capture | Records entities/activities/agents and derivations at claim granularity | Cross-cutting | PROV-O, OpenLineage, Evidence | governed_by, produces | S13, S20 | High |
| Skill | Agent orchestration | Owns state, handoffs, retries, gates, budgets and evaluations | Agent iteration | LangGraph, MAF, MCP | implemented_by | S7, S8, S9 | Medium-High |
| Market Position | Data analyst | Turns modeled internal data into decisions via dashboards/answers | Query → Interpretation | SQL, Metabase, Metric | uses, produces | S22, S17 | High |
| Market Position | Data/BI analyst | Adds governed metric definitions, semantic layer, access control | Storage → Visualization | Semantic Layer, dbt, dbt tests | uses, produces | S10, S22 | Medium-High |
| Market Position | Research analyst | Produces briefings/forecasts from external unstructured evidence | Research → Interpretation | Source Register, Research synthesis | performs, produces | S22, S17 | Medium-High |
| Market Position | Knowledge engineer | Builds ontologies, knowledge graphs and semantic/RAG grounding | Structured representation | Ontology design, Neo4j, RDF | performs, produces | S24, S26, S22 | High |
| Market Position | Information architect | Designs taxonomies, metadata and navigation across systems | Structured representation | Taxonomy, Metadata, Schema | produces, supports | S22 | Medium |
| Market Position | Research engineer | Industrializes research: pipelines, tooling, evaluation harnesses | Research → Iteration | Python, Pipeline, Evaluation | produces, uses | S22 | Medium-High |
| Market Position | Data engineer (boundary) | Builds ingestion/storage pipelines and contracts at scale | Extraction → Storage | Airflow, Warehouse, OpenLineage | produces, uses | S20, S25, S22 | High |
| Market Position | Automation specialist | Automates repetitive operational workflows with rules/scripts/integrations | Any repetitive stage | RPA, APIs, Workflow platform | performs | S22 | Low-Medium |
| Market Position | AI/agent workflow specialist | Designs agent graphs, tool/MCP wiring, evals and human gates | Agent iteration | LangGraph, MAF, MCP, Evaluation | performs, produces | S7, S8, S9 | Low-Medium |
| Market Position | BI developer (adjacent) | Builds semantic models and embedded analytics surfaces | Storage → Visualization | dbt, Superset embedding, Semantic Layer | produces, uses | S11, S12 | Medium-High |

### 4.2 Technologies and software

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Technology | SQL | Declarative relational query language and standard | Query, Analysis | DuckDB, dbt, BI tools | uses, implemented_by | S1, S10 | High |
| Technology | In-process OLAP engine | Embedded analytical DBMS optimizing long aggregate/join workloads | Database, Query | DuckDB, DuckDB-Wasm | implemented_by | S1 | High |
| Technology | Columnar storage (Parquet) | Column-oriented file format for analytical scans | Storage | DuckDB, Polars, DuckLake | uses, implemented_by | S1, S6 | High |
| Technology | Apache Arrow | In-memory columnar layout enabling zero-copy interchange | Cross-cutting | pandas 3.0 `str`, Polars, DuckDB | uses | S4 | High |
| Technology | Lakehouse table format | Metadata protocol making object storage behave like a database | Storage | DuckLake, Iceberg, Delta | implemented_by | S3 | High |
| Technology | Notebook-computational narrative | Executable document mixing code, output and prose | Analysis, Visualization | Jupyter, Observable | implemented_by | S22, S27 | High |
| Technology | Browser automation | Programmatic control of a browser for data acquisition | Extraction | Playwright, extraction agents | uses, implemented_by | S19 | High |
| Technology | LLM structured output | Schema-constrained generation used as an extractor | Extraction | JSON Schema, Extraction Agent | uses | S18 | Medium-High |
| Technology | Embeddings / vector retrieval | Semantic similarity retrieval over text and objects | Representation, Query | RAG system, Knowledge graph | uses | S22 | Medium |
| Technology | RDF/SPARQL/OWL/SHACL | Graph data model, query language, ontology and constraint stack | Representation, Query | Knowledge graph, Nanopublication | uses, implements | S24 | High |
| Technology | Provenance vocabulary (PROV) | W3C Entity/Activity/Agent derivation model | Cross-cutting | Evidence, Claim, Activity | governs | S13 | High |
| Technology | MCP (agent tool protocol) | Stateless request/response protocol exposing tools, resources, prompts | Agent iteration | Agent Runtime, BI MCP server | uses, implemented_by | S7 | High |
| Technology | A2A (agent-to-agent interaction) | Cross-runtime agent interoperability surface | Agent iteration | Microsoft Agent Framework | uses | S8 | Medium-High |
| Software | DuckDB | In-process analytical SQL engine; single-file storage plus lakehouse access | Database, Query | Parquet, DuckLake, MotherDuck | implements, produced_by | S1, S3 | High |
| Software | DuckLake extension | Reference implementation of the DuckLake specification (DuckDB ≥ v1.5.2) | Storage | DuckDB, catalog DB | implements, produced_by | S3 | High |
| Software | pandas 3.0 | Python DataFrame library; `str` dtype default, Copy-on-Write only | Normalization, Analysis | Python, Arrow, Jupyter | implements, produced_by | S4, S5 | High |
| Software | Polars 2.x | DataFrame/query engine with streaming engine as default | Normalization, Analysis | Python/Rust, Arrow | implements, produced_by | S6 | High |
| Software | Jupyter | Notebook environment and kernel ecosystem | Analysis, Visualization | Notebook narrative | implements, produced_by | S22, S27 | High |
| Software | dbt (Core/Cloud) | Transformation project runner: models, DAG, tests, docs | Normalization, Storage | SQL, dbt tests, Warehouse | implements, produced_by | S10 | High |
| Software | Metabase | BI questions/models/dashboards; MCP server; embedded analytics | Visualization, Interpretation | Warehouse, Metric, MCP | implements, produced_by | S11 | High |
| Software | Apache Superset | Open-source BI with Extensions framework and MCP service | Visualization, Interpretation | Preset, Warehouse, MCP | implements, stewarded_by | S12 | High |
| Software | Observable / Plot | Reactive notebook plus grammar-of-graphics visualization library | Analysis, Visualization | Notebook narrative, encodings | implements, produced_by | S27 | High |
| Software | Playwright | Browser automation with assertions | Extraction | Browser automation, agents | implements | S19 | High |
| Software | Unstructured; LlamaParse/LlamaExtract | Document → structured output with schema and citation support | Extraction, Structured representation | JSON Schema, Extraction Agent | implements, produced_by | S18 | Medium-High |
| Software | LangGraph v1 | Stateful agent graph runtime with durability, HITL and streaming | Agent iteration | LangSmith, MCP | implements, produced_by | S9 | High |
| Software | Microsoft Agent Framework 1.0 | Multi-agent orchestration SDK (.NET/Python) with A2A/MCP | Agent iteration | AutoGen, Semantic Kernel | implements, produced_by | S8 | High |
| Software | OpenAI Agents SDK; CrewAI | Agent SDK with handoffs/guardrails/tracing; role-based agent teams | Agent iteration | Model provider, tools | implements, produced_by | S21 | Medium-High |
| Software | OpenLineage | Lineage event standard and object model | Storage, Cross-cutting | Dataset, Run, Job | implements, governs | S20 | High |
| Software | Airflow | Scheduled DAG orchestration | Extraction → Storage | Pipeline, Scheduler | implements | S20 | High |

### 4.3 Companies, products, methodologies

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Company | DuckLabs | Steward company of DuckDB; joined AWS effective 2026-09-01 | Vendor | DuckDB, DuckLake, AWS | stewards, employed_by | S2 | High |
| Company | DuckDB Foundation | Nonprofit steward of DuckDB/DuckLake/Quack (MIT); advisory board planned | Governance | DuckDB, DuckLake, Quack | stewards, governs | S1, S2 | High |
| Company | MotherDuck | Hosted DuckDB + hosted DuckLake vendor | Vendor | DuckDB, DuckLake | produces, supports | S3, S22 | Medium-High |
| Company | dbt Labs | Vendor of dbt Core/Cloud and semantic layer | Vendor | dbt, Metric | produces, stewards | S10 | High |
| Company | Metabase, Inc. | Vendor of Metabase BI (open source + commercial) | Vendor | Metabase, MCP server | produces, stewards | S11 | High |
| Company | Apache Software Foundation | Foundation stewarding Superset and Airflow | Foundation | Superset, Airflow | stewards, governs | S12, S20 | High |
| Company | Preset | Managed Superset vendor | Vendor | Superset, Preset MCP | produces, supports | S12 | Medium-High |
| Company | LangChain, Inc. | Vendor of LangGraph/LangChain/LangSmith | Vendor | LangGraph, LangSmith | produces, stewards | S9 | High |
| Company | Microsoft | Vendor of Agent Framework; unifies AutoGen + Semantic Kernel | Vendor | MAF, A2A, Azure | produces, stewards | S8 | High |
| Company | MCP / LF Projects, LLC | Standards body governing the MCP specification | Standards body | MCP, SDKs | governs, stewards | S7 | High |
| Company | Neo4j | Graph database vendor | Vendor | Knowledge graph, Cypher | produces | S26 | High |
| Company | Unstructured; LlamaIndex | Extraction product vendors | Vendor | Extraction software, schema | produces | S18 | Medium-High |
| Company | CWI Amsterdam; Universität Tübingen | Research organizations behind/around DuckDB | Research org | DuckDB, DuckDB Foundation | employs, sponsors | S2 | High |
| Product | DuckDB (embedded analytical database) | Zero-dependency embedded SQL analytics over files/tables | Database, Query | DuckDB software, Parquet | produced_by, implements | S1 | High |
| Product | Hosted lakehouse on DuckLake | Object storage + SQL catalog as a managed service | Storage | DuckLake spec, MotherDuck | produced_by, implements | S3 | High |
| Product | dbt Cloud | Managed transformation with tests, docs, scheduling | Normalization | dbt, Warehouse | produced_by | S10 | High |
| Product | Metabase (BI product) | Self-serve and embedded BI with AI/MCP surface | Visualization, Interpretation | Warehouse, MCP, Metric | produced_by | S11 | High |
| Product | Preset / Apache Superset | Open-source-first BI with extensions and MCP | Visualization, Interpretation | Superset, Preset | produced_by | S12 | High |
| Product | LangGraph runtime + LangSmith | Agent runtime plus observability and evaluation | Agent iteration | LangGraph, traces, evals | produced_by | S9 | Medium-High |
| Product | Document extraction service | Schema-first document → records with locators and confidence | Extraction, Structured representation | Extraction agent, schema | produced_by | S18 | Medium-High |
| Product | Research assistant (Elicit-class) | Literature search plus assisted data extraction | Research, Extraction | Systematic review, Evidence | produced_by, evaluated_by | S15 | Medium-High |
| Methodology | PRISMA 2020 | Reporting standard for systematic reviews: 27-item checklist + flow diagram | Research → Interpretation | Research synthesis, Evidence | governs, requires | S14 | High |
| Methodology | ELT | Load raw, transform in place with version-controlled models | Extraction → Normalization | dbt, Warehouse | governs, implemented_by | S10, S25 | High |
| Methodology | ETL | Transform before load; used where target systems constrain transformations | Extraction → Database | Warehouse, Pipeline | governs, implemented_by | S25 | High |
| Methodology | Dimensional/relational modelling | Grain, keys, facts, dimensions | Structured representation | Data modeling, Metric | governs | S25 | High |
| Methodology | Medallion layering | Bronze/silver/gold progressive refinement | Storage → Normalization | Warehouse, Quality Gate | governs | S25 | Medium-High |
| Methodology | Schema-first extraction | Declare schema, validate, attach locator and confidence per field | Extraction → Structured representation | Extraction Agent, JSON Schema | governs, requires | S18 | Medium-High |
| Methodology | Test-and-contract | Assert model tests and failing-row semantics before promotion | Normalization → Storage | dbt tests, Quality Gate | governs, requires | S10 | High |
| Methodology | PROV-based lineage capture | Record entity/activity/agent derivations per artifact and claim | Cross-cutting | PROV-O, OpenLineage, Evidence | governs, requires | S13, S20 | High |
| Methodology | Nanopublication claim packaging | Atomic claim + provenance + publication info in immutable graphs | Structured representation → Database | Claim, Evidence, Trusty URI | governs | S23 | Medium-High |
| Methodology | Agent evaluation protocol | Per-step traces, eval sets, graders, HITL review, budget limits | Agent iteration | Agent, Trace, Evaluation | governs, requires | S9, S8, S21 | Medium |

### 4.4 Workflows, agents, and supporting entity types

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Workflow | Evidence-backed dataset build | Sources → extraction → normalization → store → query → analysis | Extraction → Visualization | WorkflowRun, Artifact | has WorkflowStep | S22 | Medium-High |
| Workflow | Research brief / market scan | Source appraisal → synthesis → briefing | Research → Interpretation | Source Register, Report | has WorkflowStep | S14, S22 | Medium-High |
| Workflow | Living review / monitored corpus | Scheduled re-extraction with explicit claim supersession | Research → Database | Scheduler, Claim | has WorkflowStep | S22 | Medium |
| Workflow | Analytics engineering pipeline | Load → transform → test → serve governed metrics | Extraction → Visualization | dbt, Warehouse, Metric | has WorkflowStep | S10, S25 | High |
| Workflow | Agent-orchestrated research loop | Bounded agents + tools + gates + eval-driven revision | Research → Agent iteration | Agent, Trace, Budget | has WorkflowStep | S7, S8, S9 | Medium |
| Agent | Research/scout agent | Finds and ranks candidate sources for a question | Research, Evidence | Search tools, Source Register | performs, produces | S22, S21 | Medium |
| Agent | Extraction agent | Converts sources into schema-valid records | Extraction | Parsers, Schema, Locator | performs, produces | S18, S15 | Medium-High |
| Agent | Entity-resolution agent | Reconciles identity, units and vocabularies across sources | Normalization | Reference lists, Rules | performs, produces | S22 | Medium |
| Agent | Data-cleaning agent | Repairs nulls/types/outliers with a logged change set | Normalization | DataFrame engine, Rule set | performs, produces | S22 | Medium |
| Agent | Coding agent | Writes pipeline/SQL/notebook code against the declared schema | Structured representation → Query | Repo, Tests, Schema | performs, produces | S9, S21 | Medium-High |
| Agent | Analytical agent | Computes aggregates/statistics and drafts interpretation | Analysis | Query engine, Notebook | performs, produces | S21, S15 | Medium |
| Agent | Visualization agent | Produces encodings and accessible text from result sets | Visualization | Plot library, Style rules | performs, produces | S27 | Low-Medium |
| Agent | Orchestrator/coordinator agent | Plans, routes, budgets, retries, escalates across stages | Agent iteration | Runtime, State store, Budget | performs, governs | S7, S8, S9 | Medium |
| Agent | Verifier/critic agent | Independently challenges claims and outputs; emits pass/fail + evidence | Cross-cutting gates | Source retrieval, Checklists | performs, verifies | S15, S22 | Medium |
| Source | Source record | Identity + metadata + appraisal of an evidence artifact | Evidence | Evidence, Claim | supports, appears_in | S22 | High |
| Evidence | Evidence span | Locatable quotation or region inside a source supporting a claim | Evidence | Claim, Source record | supports, conflicts_with | S13, S15 | High |
| Claim | Claim | Typed assertion about an entity with status, confidence and supersession | Cross-cutting | Evidence, Entity, Relation | described_by, supported_by | S23, S13 | High |
| Schema | Schema / ontology | Declared entities, keys, relations and constraints at a version | Structured representation | Claim, Quality Gate | governs, validates | S24, S18 | High |
| Metric | Metric definition | Governed, versioned computation answering a named business question | Storage → Interpretation | Data/BI analyst, BI tool | governs, appears_in | S10, S11 | Medium-High |
| Quality Gate | Quality check | Named, executable assertion an artifact must pass before promotion | Cross-cutting | Methodology, Artifact | validates, governs | S10 | High |
| Artifact | Artifact | Any produced or consumed object (dataset, report, chart, model, trace) | Cross-cutting | Activity, Provenance | produced_by, used_by | S13 | High |
| Dataset | Dataset | Versioned, queryable collection of normalized records | Database | Schema, Artifact | conforms_to, produced_by | S20 | High |
| Activity | Activity / run | An execution of a workflow or agent step with inputs and outputs | Cross-cutting | Agent, Artifact, Provenance | performed_by, produced | S13 | High |
| Standard | Standard | Published specification constraining formats or reporting | Cross-cutting | Methodology, Schema | governs, implemented_by | S13, S14 | High |
| Evaluation | Evaluation | Dataset + graders + thresholds measuring a workflow or agent | Agent iteration | Agent, Trace, Quality Gate | measures, governs | S9, S8 | Medium |

### 4.5 Relationship predicate register

Used to keep edges consistent and machine-loadable `[R]`.

| Predicate | Subject → Object | Meaning | Example |
| --- | --- | --- | --- |
| `used_in` | Skill → Workflow | Skill required by a workflow | Research synthesis used_in Research brief |
| `uses` | Workflow/Agent → Technology/Software | Execution dependency | Evidence-backed dataset build uses DuckDB |
| `implemented_by` | Technology → Software | Concrete implementation | SQL implemented_by DuckDB |
| `produced_by` | Software/Product → Company | Producer or owner | DuckDB produced_by DuckLabs |
| `stewards` | Company/Foundation → Software/Standard | Governance responsibility | DuckDB Foundation stewards DuckLake |
| `employed_by` | Company → Company | Absorption/acquisition | DuckLabs employed_by AWS (2026-09-01) |
| `governs` | Methodology/Standard → Workflow/Schema | Constraint relation | PRISMA 2020 governs Research brief |
| `requires` | Methodology → Artifact/Gate | Mandatory output | ELT requires tested models |
| `performs` | Agent/Market Position → WorkflowStep | Execution assignment | Extraction agent performs Extraction |
| `produces` | Agent/Workflow/Position → Artifact | Output relation | Coding agent produces pipeline code |
| `supports` | Source/Evidence → Claim | Evidence relation | Source record supports Claim |
| `conflicts_with` | Evidence → Evidence | Contradictory support | Retracted study conflicts_with verified study |
| `appears_in` | Skill/Workflow → Market Position | Bundling relation | Data modeling appears_in Data engineer |
| `validates` | Quality Gate → Artifact | Enforcement relation | Schema check validates extracted records |
| `supersedes` | Claim → Claim | Versioning relation | New claim supersedes prior claim |
| `traced_by` | Activity → Trace | Observability relation | Agent step traced_by Trace record |
| `measured_by` | Workflow/Agent → Evaluation | Assessment relation | Extraction pipeline measured_by Evaluation |

---

## 5. Comparison tables

Criteria used throughout: purpose, users, inputs, outputs, integration surface, maturity, cost, openness, limitations. All comparative cells are `[I]` synthesis unless a source is cited.

### 5.1 Market positions

| Position | Purpose | Primary users | Inputs | Outputs | Integration surface | Maturity (role definition) | Limitations / failure |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Data analyst | Answer business questions from modeled data | Internal stakeholders | Tables/metrics | Dashboards, answers | BI tools, SQL, tickets | High | Cannot fix semantic or source-quality defects upstream |
| Data/BI analyst | Govern definitions + serve analytics | Analytics org | Models + metric requirements | Semantic layer, dashboards | dbt/semantic layer, BI | High | Scope creep into engineering without pipeline ownership |
| Research analyst | Produce external evidence syntheses | Leadership, clients | Reports, filings, interviews | Briefings, forecasts | Documents, spreadsheets | High | Evidence chain often unversioned/untraceable |
| Knowledge engineer | Make domain meaning computable | Product, search, AI teams | Domain expertise, corpora | Ontology, KG, RAG grounding | Graph DB, SPARQL, embeddings | Medium-High | Title inflation without formal ontology method |
| Information architect | Structure metadata/navigation | Enterprise IT, content teams | Systems inventory, taxonomies | Taxonomy, metadata model | Catalogs, MDM | High | Detached from actual query/analysis use |
| Research engineer | Industrialize research workflows | Research teams | Prototypes, tooling needs | Pipelines, eval harnesses | Repos, cloud, notebooks | High | Over-engineering ahead of a stable schema |
| Data engineer | Move and protect data at scale | Platform teams | Sources, contracts | Pipelines, stores, contracts | Orchestrators, warehouses, lineage | High | Optimizes throughput over semantics |
| Automation specialist | Remove repetitive manual steps | Ops/back office | Process maps | Automations | RPA/scripts/APIs | Low-Medium | Brittle, unversioned, no data quality guarantees |
| AI/agent workflow specialist | Make multi-step AI reliable | Product/AI teams | Goals, tools, schemas | Agent graphs, evals, guardrails | MCP/A2A, runtimes, tracing | Low-Medium | Framework churn; measures its own instrumentation |
| BI developer | Build semantic/embedded analytics products | Product, customers | Warehouse models | Embedded dashboards, models | BI SDK, warehouse | Medium-High | Coupled to one BI engine |

### 5.2 Local analytical stack and storage choices

| Option | Nature | Best fit | Cost / openness | Maturity | Key limitation |
| --- | --- | --- | --- | --- | --- |
| pandas 3.0 | In-memory DataFrame library | Ecosystem-rich analysis, ML handoff, small/medium data | Open source (BSD); wide ecosystem | Very high | Pre-3.0 patterns break (chained assignment removed); single-process |
| Polars 2.x | Lazy/streaming DataFrame engine | Large ETL/transformation, strict schemas, agent-authored queries | Open source (MIT); smaller ecosystem | High, changing fast | Engine-default change alters row-order expectations; API migration |
| DuckDB | Embedded analytical SQL engine | Ad-hoc SQL over files/tables, joins, out-of-core | Open source (MIT); zero deps | Very high | Single-node; no built-in multi-user control plane |
| DuckLake 1.0 | Lakehouse format + SQL catalog | Object-storage datasets needing DB semantics and versioning | Open source spec; extension in DuckDB | Production-ready since 2026-04 | Younger ecosystem than Iceberg/Delta; catalog choice matters |
| Cloud warehouse (Snowflake/BigQuery/Redshift) | Managed MPP platform | Multi-team governance, concurrency, scale-out | Commercial; consumption pricing | Very high | Cost model and lock-in; heavier local iteration loop |
| MotherDuck-style hosted DuckDB | Managed single-engine service | Small teams wanting shared DuckDB | Commercial | Medium-High | Concentration risk; feature parity with local engine |
| Graph store (Neo4j, RDF triplestore) | Relationship-first storage | Traversal, provenance, ontology queries | Mixed OSS/commercial | High | Modelling cost and skill scarcity; weak fit for wide tabular aggregation |

### 5.3 Notebooks and analysis surfaces

| Surface | Interaction model | Reproducibility controls | Collaboration | Best fit | Limitation |
| --- | --- | --- | --- | --- | --- |
| Jupyter | Cell execution, any kernel | Kernel/env pinning needed; execution order visible but not enforced | Weak native review; relies on git | Exploration, ML, arbitrary Python | Hidden state, environment drift |
| Observable / Plot | Reactive cells, JS-first, notebook publishing | Cell graph is explicit | Strong sharing/forking | Explanatory visual narrative, interactive charts | JS-centric; limited ingestion/governance |
| dbt-style project + BI | Declarative models + dashboards | Tests, version control, environments | Strong code review | Governed recurring metrics | Not exploratory; model-first rigidity |
| Agent-driven notebook/script | Prompt + code generation | Trace-dependent; needs schema validation | Human review gates | Bulk transformation/repair at scale | Probabilistic edits; provenance must be engineered |

### 5.4 BI and visualization products

| Product | Positioning | Deployment / openness | Agent surface | Governance depth | Limitation |
| --- | --- | --- | --- | --- | --- |
| Metabase (v63, 2026-07-21) | Easy self-serve BI + embedded analytics | OSS core + commercial; single-service install; LTS releases (~14 months) + 60-day minimum support | MCP server with authorization audit logs (DCR off by default); Metabot LLM providers | Permissions, 2FA, audit logs, semantic layer features | Advanced governance/viz depth behind higher tiers |
| Apache Superset (6.1.0, 2026-06-11) | Open-source BI platform, extensibility-first | Apache 2.0; heavier multi-process deployment; managed via Preset | MCP service exposed to AI assistants; Extensions framework with stable APIs | Needs deliberate setup for semantic consistency and tenanting | Operational effort; feature timing differs between ASF release and Preset |
| Observable | Code-first, notebook-published visual narrative | Commercial hosted + open components (Plot) | No standard MCP surface identified in this pass | Not a governance layer | Not designed for ingestion/storage/BI administration |
| Notebook + chart library (ad hoc) | Total flexibility | Fully open | Depends on the agent tooling built around it | None by default | Every control (versioning, review, sharing, access) must be built |

### 5.5 Extraction approaches

| Approach | Mechanism | Inputs it handles well | Failure mode | Evidence quality |
| --- | --- | --- | --- | --- |
| Deterministic parsing (regex, templates, delimiters) | Rules over stable text structure | Consistent exports, logs, fixed-layout forms | Silent breakage when the format drifts | High precision, narrow recall `[I]` |
| Layout-aware document parsing (PDF/HTML → structured) | Layout models + table reconstruction | Tables, multi-column PDFs, scans with OCR | Table flattening, header/unit loss | Vendor-documented; benchmark results conflicting `[S]` |
| LLM structured output against a schema | Constrained generation validated by JSON Schema | Prose, mixed formats, semantic fields | Hallucinated fills that still validate; schema drift across model versions | Strong on flexibility; accuracy is task- and model-specific `[F]`/`[S]` |
| Research-assistant extraction (literature tools) | Search + assisted field extraction with quotes | Study-level data extraction in reviews | Value accuracy ≈86% but quote-level support far less stable between runs (Elicit feasibility study, S15) | Peer-reviewed primary evidence `[F]` |
| Vision/browser agents | Perceive rendered pages, act on UI | Dynamic sites, gated content, visual-only data | Nondeterminism, cost, anti-bot and legal exposure | Vendor and practitioner signals `[S]` |

### 5.6 Agent runtimes and coordination frameworks

| Framework | Coordination primitive | Durability / state | Interop | Best fit | Limitation |
| --- | --- | --- | --- | --- | --- |
| LangGraph v1 | Explicit graph of state, nodes, edges | Durable execution, checkpointing, streaming, HITL as first-class primitives | MCP connections | Production agent loops needing state and human gates | Graph modelling effort; ecosystem churn |
| Microsoft Agent Framework 1.0 | Agents + orchestration builders (.NET/Python) | Sessions, checkpointing, workflows; LTS commitment | A2A and MCP | Enterprises on Azure needing multi-runtime interop | New surface; migration from AutoGen/Semantic Kernel |
| CrewAI | Roles, goals, tasks (org-chart metaphor) | Team-run oriented | Tool ecosystem | Fast prototyping of sequential collaborations | Token cost; weaker durability/state control |
| OpenAI Agents SDK | Agents with tools, handoffs, guardrails, tracing | Managed by runtime/session patterns | Provider-centric tooling | Teams inside the OpenAI ecosystem | Provider coupling |
| Plain orchestration (Airflow-class) | Tasks, dependencies, schedules | Mature retries/backfills | No native LLM observability | Deterministic pipelines around agent steps | Not designed for probabilistic step semantics |

### 5.7 Provenance, evidence, and quality standards

| Standard / mechanism | Granularity | Coverage | Maturity | Gap it leaves |
| --- | --- | --- | --- | --- |
| W3C PROV (PROV-DM/O) | Entity, Activity, Agent + derivations | Any artifact/claim lineage, domain-neutral | W3C Recommendation (stable) | Not a storage or query product; adoption must be engineered |
| Nanopublications (+ PROV-K style extension) | Single atomic claim with assertion/provenance/publication graphs | Claim-level support and conflict, immutable identifier | Spec/guidelines; niche tooling | Ecosystem size; RDF fluency required |
| OpenLineage | Dataset/Job/Run events | Pipeline-level lineage in data platforms | Mature spec, broad integrator support | Says nothing about claim truth or document spans |
| dbt tests + docs + lineage | Model-level assertions and DAG | Transformation correctness | Mature in dbt projects | Only covers what is modeled; nothing about sources collected outside the warehouse |
| PRISMA 2020 | Review-level reporting (27 items + flow diagram) | Evidence selection and reporting transparency | Stable, widely required in health sciences | Not a quality-appraisal tool; not enforced in most data workflows |
| Peer-review replication of extraction (S15-type studies) | Field/quote-level accuracy across reruns | Detects instability in tool output *and* its citations | Emerging | Rare in commercial tool evaluations; some published comparisons retracted (S16) |

---

## 6. Research gaps and next investigations

### 6.1 Unresolved questions

1. **Where does the "analyst" boundary settle once agents author dashboards and queries?** Positions in §2.2 assume humans perform stage 7–9 work. If BI MCP servers (Metabase 63, Superset 6.1) become the normal access path, the observable output changes but the accountability question does not `[I]`.
2. **Can claim-level provenance survive contact with mainstream tooling?** PROV and nanopublications are claim-grade; BI lineage and dbt tests are artifact-grade. No verified product joins the two at claim granularity `[I]`.
3. **What are realistic per-stage error budgets?** Only extraction has peer-reviewed accuracy evidence in this pass (S15). Research selection, entity resolution, visualization honesty, and interpretation are unmeasured here `[I]`.
4. **How much of "research-to-data" is actually a retrieval problem?** If most extraction failure traces to source selection rather than parsing, the atlas's centre of gravity shifts earlier in the pipeline `[I]`.
5. **Which entity type does the AI/agent workflow specialist produce?** Candidate answers: agent graph, eval suite, guardrail policy, tool catalog — the evidence in this pass supports "agent graph + evaluation", but title-level samples are thin `[S]`.

### 6.2 Weakly supported claims in this note

| Claim | Why weak | What would strengthen it |
| --- | --- | --- |
| Role boundaries in §2.2 | Posting samples from prior notes are small and title-driven | Systematic posting-sample study with coded skill requirements (n≥200 per title) |
| Employer/sector mapping in §2.5 | No first-party hiring data collected in this pass | Direct review of live postings across the named employers |
| Performance magnitudes implied by pandas 3.0 / Polars 2.0 | Vendor-reported expectations (≈5×) and prior-note benchmarks | Independent, version-pinned benchmarks on documented hardware |
| "Agent error is multiplicative" | Mechanism is documented; multiplication factor is not | Stage-isolated ablations measuring error after injecting upstream faults |
| BI governance limits | Vendor/comparator sources and inference | Hands-on evaluation of permissioning, semantic layers, and audit coverage |
| Research-assistant usefulness | One peer-reviewed study for one tool (S15) plus a retracted comparison (S16) | Replicated multi-tool studies with pre-registered protocols |

### 6.3 Conflicting evidence and source-quality warnings

- **Extraction-tool benchmarks conflict.** Vendor benchmark pages and independent comparisons disagree on parser accuracy and on which tool wins; the disagreement is consistent with different test corpora rather than a single wrong claim `[S]`. Treat all parser accuracy claims as corpus-specific `[R]`.
- **A published AI-tools comparison in this space was retracted** (S16). Any comparative claim about research assistants should be checked for retraction and for replication before use `[R]`.
- **Notebooks: reproducibility claims conflict.** Notebook advocacy cites narrative reproducibility; practitioner analyses emphasise hidden state and execution-order hazards. Both are compatible: the format permits reproducibility without enforcing it `[I]`.
- **BI ease-of-use claims conflict** between vendor pages and third-party reviews, mainly because the criteria differ (time-to-first-chart vs governance at scale) `[S]`.

### 6.4 Missing categories (not covered, deliberately or by omission)

- **Domain-specific regimes** (clinical, financial/regulatory, geospatial, legal e-discovery) — each imposes different evidence rules and validation `[I]`.
- **Non-English and multilingual extraction**, plus transliteration and locale normalisation `[I]`.
- **Data licensing and rights management** as a first-class entity (rights holder, licence, permitted use), distinct from provenance `[I]`.
- **Cost accounting** per stage (tokens, compute, human review hours), which the atlas does not model `[I]`.
- **Security/privacy** for extracted personal data (redaction, retention, purpose limitation) `[I]`.
- **Personal/individual practice** (independent researchers and freelancers) as distinct from organisational roles `[I]`.

### 6.5 Next most valuable searches and interviews

| Priority | Action | Why it is valuable |
| --- | --- | --- |
| 1 | Fetch the Cochrane *Evidence Synthesis and Methods* comparison of Elicit vs human reviewers in RCTs and log its quantitative findings | Second independent primary source on extraction accuracy; currently cited only as a title |
| 2 | Code 200+ live postings across the ten positions in §2.2 into a skill matrix | Replaces title semantics with capability evidence; directly testable |
| 3 | Run a controlled extraction trial on this vault's own corpus (PDFs/pages → schema) with two tools and two models, measuring field accuracy *and* quote stability | Produces first-party evidence for the exact failure mode S15 found |
| 4 | Prototype the §8 relational core in `src/` + DuckDB and load the §4 rows as seed data | Validates whether the entity/relationship model actually answers atlas questions |
| 5 | Interview 3 data engineers, 3 research analysts, 3 knowledge engineers about their last failed pipeline | Surfaces stage-11/12 failures that documentation never records |
| 6 | Evaluate two BI MCP servers end-to-end (schema exposure, auth, audit, agent error handling) | The newest, least-documented boundary in the atlas |

---

## 7. Sources

**Access date for every web source below: 2026-09-27.** Sources marked *(carried)* were used in earlier vault notes and are cited for continuity; they were **not** re-fetched in this pass and should be re-verified before reuse as `[F]`.

### 7.1 Primary sources (fetched and read in this pass unless marked *carried*)

| ID | Source (title, publisher/author, date) | URL | Supports |
| --- | --- | --- | --- |
| S1 | "Why DuckDB", DuckDB Foundation (site footer © 2026) | https://duckdb.org/why_duckdb | DuckDB = relational embedded OLAP DBMS; no external dependencies; single amalgamation build; ACID/MVCC; single-file + lakehouse formats (incl. DuckLake) to petabyte scale; DuckDB-Wasm; **Quack protocol** for remote access; Morsel parallelism; 41.7k GitHub stars; DuckDB Foundation (Amsterdam, NL) |
| S2 | "DuckLabs to Join AWS, Projects to Remain Open Source", Mark Raasveldt & Hannes Mühleisen, 2026-08-26 (update 2026-08-31) | https://www.ducklabs.com/news/2026/08/26/ducklabs-to-join-aws | DuckLabs = >30-person Amsterdam steward company; joined AWS effective 2026-09-01; MIT licence and DuckDB Foundation stewardship retained; >1M downloads/day; planned technical advisory board and third-party signed extensions; CWI (Boncz) and Tübingen (Grust) statements |
| S3 | "DuckLake v1.0: The Lakehouse Format Built on SQL Reaches Production-Readiness", DuckDB team, 2026-04-13 | https://ducklake.select/2026/04/13/ducklake-10/ | DuckLake = lakehouse format whose metadata lives in a SQL catalog (SQLite/PostgreSQL/DuckDB); production-ready spec with backward-compatibility guarantee; shipped in DuckDB v1.5.2; inlining, sorted tables, bucket partitioning, deletion vectors, Iceberg compatibility; clients for DataFusion, Spark, Trino, pandas; top-10 core extension by downloads |
| S4 | "pandas 3.0 released!", pandas project / NumFOCUS, 2026 | https://pandas.pydata.org/community/blog/pandas-3.0.html | Release of pandas 3.0.0; **`str` dtype default** replacing object (pyarrow-backed if installed, not required); **Copy-on-Write default and only mode**; chained assignment and `SettingWithCopyWarning` removed; microsecond datetime default; `pd.col` syntax |
| S5 | "What's new in 3.0.0 (January 21, 2026)", pandas 3.0.6 documentation | https://pandas.pydata.org/docs/whatsnew/v3.0.0.html | Release date 2026-01-21 (latest patch 3.0.6, 2026-09-17); offset-alias enforcement (M→ME etc.); `DataFrame Interchange Protocol` deprecation; removed IO string/byte inputs; full breaking-change inventory |
| S6 | "Pre-release of Polars 2.0", Ritchie Vink, 2026-09-02 | https://pola.rs/posts/announcing-polars-2/ | Polars 2.0 RC; **streaming engine default** for `LazyFrame.collect` with ~5× expected aggregate speedup; row order no longer guaranteed for join/group_by/unpivot unless `maintain_order`; engine affinity settings; strictness changes (lossless `is_in`, concat height errors, cast removals); typed `AttributeRemovedError`/`ArgumentRemovedError`; **agents validate structure via `collect_schema()`**; roadmap (out-of-core streaming, IO plugins, S3 reader, cost-based planner, mmap removal) |
| S7 | "The 2026-07-28 Specification", David Soria Parra & Den Delimarsky, Model Context Protocol (LF Projects), 2026-07-28 | https://blog.modelcontextprotocol.io/posts/2026-07-28/ | MCP **stateless core**; retirement of `initialize`/`Mcp-Session-Id`; `server/discover`; `Mcp-Method`/`Mcp-Name` header routing; cacheable list results with deterministic order; Multi Round-Trip Requests for sampling/elicitation; authorization hardening (RFC 9207 issuer validation, DCR→CIMD); extensions framework (Tasks, MCP Apps, EMA); 12-month deprecation policy; Tier-1 SDKs TS/Python/Go/C#; ~0.5B monthly downloads |
| S8 | "Microsoft Agent Framework Version 1.0", Shawn Henry, Microsoft DevBlogs, 2026-04-03 | https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/ | MAF 1.0 GA for .NET and Python; production-ready with LTS commitment; unifies Semantic Kernel + AutoGen; multi-provider models; cross-runtime interop via **A2A and MCP**; orchestration builders; introduced Oct 2025, RC Feb 2026 |
| S9 | "What's new in LangGraph v1", LangChain documentation | https://docs.langchain.com/oss/python/releases/langgraph-v1 | LangGraph v1 = stability-focused release; graph primitives unchanged; durable execution, checkpointing, persistence, streaming, human-in-the-loop first-class; LangChain v1 `create_agent` built on LangGraph; `create_react_agent` deprecated |
| S10 | dbt documentation: "What is dbt?", "Models", "Add data tests to your DAG", dbt Labs | https://docs.getdbt.com/docs/introduction · https://docs.getdbt.com/docs/build/models · https://docs.getdbt.com/docs/build/data-tests | dbt projects, modular SQL/Python models, DAG, data tests with failing-row semantics, deployment and documentation; the "T" of ELT |
| S11 | "Metabase 63", The Metabase Team, 2026-07-21 | https://www.metabase.com/releases/metabase-63 | Metabase v63: treemaps, 2FA, PDF attachments in dashboard subscriptions, more Metabot LLM providers, one-step sharing, custom visualizations (from v62), **MCP server with authorization audit logs** (DCR off by default), sample DB moved to SQLite, LTS policy (60-day minimum support; twice-yearly LTS ~14 months) |
| S12 | "Apache Superset 6.1 Release", Evan Rusackas (Preset), 2026-06-11; ASF artifacts | https://preset.io/blog/apache-superset-6-1-release/ · https://downloads.apache.org/superset/6.1.0 | Superset 6.1.0: Extensions framework with stable APIs in `@apache-superset/core`, Global Task Framework, **MCP service** for AI assistants, chart/SQL Lab/embedded improvements; 136 contributors; Superset 7.0 in progress — *Preset-authored, vendor-affiliated* |

| S13 | W3C PROV: PROV-DM and PROV-O (2013 Recommendations) *(carried — standard, not re-fetched)* | https://www.w3.org/TR/prov-dm/ · https://www.w3.org/TR/prov-o/ | Entity / Activity / Agent provenance model and its OWL encoding; domain-neutral lineage vocabulary used in §2.7 and §5.7 |
| S14 | PRISMA 2020 statement (Page et al., BMJ 2021;372:n71); PRISMA listing, EQUATOR Network *(carried)* | https://www.bmj.com/content/372/bmj.n71 · https://www.equator-network.org/reporting-guidelines/prisma/ | PRISMA 2020 = 27-item checklist + flow diagram; PRISMA-P for protocols; explicitly not a quality-appraisal instrument |
| S15 | "Using Elicit AI research assistant for data extraction in systematic reviews: A feasibility study across environmental and life sciences", *Research Synthesis Methods* (Cambridge University Press), open access | https://www.cambridge.org/core/journals/research-synthesis-methods/article/using-elicit-ai-research-assistant-for-data-extraction-in-systematic-reviews-a-feasibility-study-across-environmental-and-life-sciences/C97DAEC70C3173A260F0B12E729E7250 | Value accuracy ≈86.6% (TEST) and 85.6% (RETEST) across 67 variables / 7 reviews, no significant difference; high-accuracy mode 82.1%; ≈77% exact re-extraction match; **supporting quotes matched in only 200/448 cases (TEST vs RETEST)** and 51/463 (TEST vs high-accuracy); reasoning narratives matched 158 vs 377; missing quotes in 88 extractions; mismatches dominated by interpretation errors. Preprint and a public testing repository accompany the study. Establishes that *values* can be stable while *cited support* is not |
| S16 | "Retraction: Assessing the Effectiveness of AI Tools (Elicit, SciSpace, and Consensus) in Literature Review and Research", *Canadian Journal of Information and Library Science* (retraction record; existence and identifier confirmed via search, notice page not opened in this pass) | https://ojs.lib.uwo.ca/index.php/cjils/article/view/24694 | A published comparison of AI research tools in this cluster was retracted — evidence that comparative claims about research assistants are unstable and require retraction/replication checks |
| S17 | U.S. Bureau of Labor Statistics, *Occupational Outlook Handbook* (Data Scientists); O*NET OnLine *(carried)* | https://www.bls.gov/ooh/math/data-scientists.htm · https://www.onetonline.org/ | Occupational framing of data collection/categorisation/analysis; task-skill-knowledge taxonomy used for role comparison (occupational categories, not employer title semantics) |

### 7.2 Standards and product documentation *(carried from prior vault notes)*

| ID | Source | URL | Supports |
| --- | --- | --- | --- |
| S18 | Unstructured documentation; LlamaIndex / LlamaParse / LlamaExtract documentation | https://docs.unstructured.io/ · https://docs.llamaindex.ai/ | Schema-constrained document extraction, layout/table handling, per-item citations and confidence; basis of §2.4 and §5.5 *(carried)* |
| S19 | Playwright documentation | https://playwright.dev/ | Browser automation capabilities and assertions used as an extraction substrate *(carried)* |
| S20 | OpenLineage object model; Apache Airflow core concepts | https://openlineage.io/docs/spec/object-model/ · https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html | Dataset/Job/Run lineage vocabulary and scheduled DAG orchestration *(carried)* |
| S21 | OpenAI Agents SDK docs (agents, tracing); CrewAI documentation | https://openai.github.io/openai-agents-python/agents/ · https://openai.github.io/openai-agents-python/tracing/ · https://docs.crewai.com/ | Agent tools, handoffs, guardrails, structured outputs, tracing; role/task agent teams *(carried)* |
| S22 | **Internal vault notes** (synthesis sources, not external evidence): [[ANT GP H]], [[C]], [[DPS]], [[FAI]], [[Q]], [[OP MS 1.3F]], [[DC L5.6]], [[CP L6]], [[G0]]–[[G3]], [[Citations/Citation]], [[Citations/Report]] | — | Consolidated role boundaries, workflow archetypes, agent taxonomy, prior benchmark magnitudes; `[S]`-class when used as evidence, and superseded by S1–S17 wherever they conflict |
| S23 | Nanopublication guidelines (nanopub.net working draft) and the nanopublication/PROV-K structure recorded in [[G1]]–[[G3]] | https://nanopub.net/guidelines/working_draft/ | Atomic claim packaging with assertion/provenance/publication-info graphs, immutable Trusty URIs, multi-source support/conflict extension |
| S24 | W3C RDF / SPARQL 1.1 / OWL 2 / SHACL specifications | https://www.w3.org/TR/sparql11-query/ · https://www.w3.org/TR/owl2-overview/ · https://www.w3.org/TR/shacl/ | Graph data model, query language, ontology and constraint languages used for representation choices |
| S25 | Warehouse documentation: BigQuery ELT guidance, Snowflake key concepts, Databricks medallion architecture (as recorded in [[CP L6]]) | https://docs.cloud.google.com/bigquery/docs/load-transform-export-intro · https://docs.snowflake.com/en/user-guide/intro-key-concepts · https://docs.databricks.com/aws/en/lakehouse/medallion | ETL vs ELT definitions, storage/compute separation, bronze/silver/gold layering, governance primitives *(carried)* |
| S26 | Neo4j documentation | https://neo4j.com/docs/ | Property-graph database capabilities behind the knowledge-engineer role *(carried)* |
| S27 | Jupyter documentation; Observable notebooks and Plot documentation | https://docs.jupyter.org/ · https://observablehq.com/documentation/notebooks · https://observablehq.com/plot/ | Notebook execution models, reactive notebooks, grammar-of-graphics visualization *(carried; marimo referenced only as a reported signal)* |

### 7.3 Source-quality notes

- **Vendor documentation** (S10–S12, S18, S20, S21, S25, S26) is primary for *capabilities and intended behaviour*, and weak for comparative performance, cost, and adoption `[R]`.
- **S12 is authored by Preset**, a commercial Superset vendor: the product facts match first-party ASF artifacts, but the framing is commercial `[S]`.
- **S15 is the strongest single evidence item in this pass** for extraction behaviour: peer-reviewed, quantitative, and reporting a *negative* stability result whose like no vendor would publish `[F]`.
- **S16 is a negative signal about the literature itself**, not about any specific product `[F]`.
- **Prior secondary sources** (comparison blogs, "best tool" roundups, funding trackers) remain catalogued in [[Citations/Citation]] and [[Citations/Report]] and are deliberately excluded from this note's primary set `[R]`.

---

## 8. Modeling handoff

### 8.1 Canonical name register (do not create duplicate nodes)

| Canonical name | Type | Aliases seen in vault/notes (map to canonical) | Note |
| --- | --- | --- | --- |
| DuckDB | Software | duckdb, DuckDB binary, DuckDB engine | Engine/binary. Do **not** use for the company or a hosted service |
| DuckDB (technology) | Technology | in-process OLAP, embedded OLAP | Use only when discussing the class, not the product |
| DuckDB Foundation | Company (nonprofit) | DuckDB foundation (NL) | Steward of DuckDB/DuckLake/Quack |
| DuckLabs | Company | DuckDB Labs, DuckDB Labs B.V. | Joined AWS 2026-09-01; retain as its own node with a valid_to date |
| AWS | Company | Amazon Web Services | Employer of the DuckLabs team from 2026-09-01 |
| DuckLake | Technology (format) / Software (extension) | ducklake, DuckLake format, DuckLake spec | Split: format (Technology/Standard) vs `ducklake` extension (Software) |
| MotherDuck | Company / Product | motherduck.com | Company node + hosted product node |
| pandas | Software | pandas 3.0, pandas2 | Version in the artifact/claim, not in the node name |
| Polars | Software | polars, Polars 1.x/2.x | Version in the claim/artifact |
| dbt | Software | dbt Core, dbt Cloud, dbt Labs | Company = dbt Labs; software = dbt (Core/Cloud) |
| Semantic layer | Technology/Methodology | semantic models, MetricFlow, metrics layer | Keep "metric definition" as a separate entity type |
| Metabase | Software (product) | Metabase Inc. | Company = Metabase, Inc. |
| Superset | Software (product) | Apache Superset, superset | Project = ASF; managed vendor = Preset |
| LangGraph | Software | LangGraph v1, LangChain | LangChain = company/software family; LangGraph = runtime |
| Microsoft Agent Framework | Software | MAF, Agent Framework, MS Agent Framework | Predecessors: AutoGen, Semantic Kernel (separate nodes, `superseded_by`) |
| MCP | Technology (protocol) | Model Context Protocol | Governance node: MCP / LF Projects, LLC |
| A2A | Technology (protocol) | agent-to-agent | Interop surface referenced by MAF |
| PROV | Technology/Standard | PROV-DM, PROV-O, PROV-N | One standard node with three serialisations |
| PRISMA 2020 | Methodology/Standard | PRISMA, PRISMA-P | PRISMA-P is a distinct artefact (protocol checklist) |
| Research/scout agent | Agent | research agent, deep-research agent | Task-scoped node, per §2.9 |
| AI/agent workflow specialist | Market Position | AI automation specialist, agent engineer | Emergent; keep aliases attached, not merged |
| Claim | Entity type | assertion, finding, statement | One type; do not conflate with "metric" |

### 8.2 Claim record contract

Every claim in this note should be loadable as: `claim_id, text, status ∈ {documented_fact, reported_signal, inference, recommendation}, confidence ∈ {high, medium, low}, entity_ids[], source_ids[], evidence_locator, valid_from, valid_until, falsifier, supersedes_claim_id, created_at`. Populating `valid_until` and `falsifier` is what makes the atlas falsifiable rather than merely descriptive `[R]`.

### 8.3 Proposed core tables (DuckDB-compatible sketch)

```sql
CREATE TABLE source        (source_id VARCHAR PRIMARY KEY, category VARCHAR, title VARCHAR,
                            publisher VARCHAR, url VARCHAR, published_at DATE,
                            accessed_at DATE, notes VARCHAR);
CREATE TABLE evidence_span (evidence_id VARCHAR PRIMARY KEY, source_id VARCHAR, locator VARCHAR,
                            quote VARCHAR, captured_at TIMESTAMP);
CREATE TABLE entity        (entity_id VARCHAR PRIMARY KEY, entity_type VARCHAR, canonical_name VARCHAR,
                            definition VARCHAR, valid_from DATE, valid_to DATE);
CREATE TABLE entity_alias  (alias VARCHAR PRIMARY KEY, entity_id VARCHAR, alias_type VARCHAR);
CREATE TABLE relation      (subject_id VARCHAR, predicate VARCHAR, object_id VARCHAR,
                            claim_id VARCHAR, PRIMARY KEY (subject_id, predicate, object_id, claim_id));
CREATE TABLE claim         (claim_id VARCHAR PRIMARY KEY, text VARCHAR, status VARCHAR, confidence VARCHAR,
                            workflow_stage VARCHAR, valid_from DATE, valid_until DATE,
                            falsifier VARCHAR, supersedes_claim_id VARCHAR);
CREATE TABLE claim_evidence(claim_id VARCHAR, evidence_id VARCHAR, relation VARCHAR); -- supports|conflicts|contextualizes
CREATE TABLE workflow_step (step_id VARCHAR PRIMARY KEY, workflow_id VARCHAR, ordinal INT,
                            name VARCHAR, inputs VARCHAR, outputs VARCHAR, quality_gate VARCHAR);
CREATE TABLE agent         (agent_id VARCHAR PRIMARY KEY, name VARCHAR, task VARCHAR, tools VARCHAR,
                            state_contract VARCHAR, verification VARCHAR, failure_modes VARCHAR);
CREATE TABLE activity      (activity_id VARCHAR PRIMARY KEY, kind VARCHAR, agent_id VARCHAR,
                            started_at TIMESTAMP, ended_at TIMESTAMP, status VARCHAR);
CREATE TABLE artifact      (artifact_id VARCHAR PRIMARY KEY, artifact_type VARCHAR, uri VARCHAR,
                            schema_version VARCHAR, checksum VARCHAR, produced_by_activity_id VARCHAR);
CREATE TABLE quality_check (check_id VARCHAR PRIMARY KEY, artifact_id VARCHAR, rule VARCHAR,
                            result VARCHAR, checked_by VARCHAR, checked_at TIMESTAMP);
CREATE TABLE metric        (metric_id VARCHAR PRIMARY KEY, name VARCHAR, definition VARCHAR,
                            owner_position VARCHAR, definition_version VARCHAR);
CREATE TABLE evaluation    (evaluation_id VARCHAR PRIMARY KEY, subject_id VARCHAR, dataset VARCHAR,
                            graders VARCHAR, thresholds VARCHAR, run_at TIMESTAMP);
CREATE TABLE time_sensitive(claim_id VARCHAR PRIMARY KEY, expires_at DATE, recheck_trigger VARCHAR);
```

Projections: DuckDB/SQL for analysis, notebooks for exploration, BI for communication, RDF/PROV or property graph for traversal and claim-level provenance `[R]`.

### 8.4 Time-sensitivity register (claims most likely to expire)

| Claim (section) | Verified value as of 2026-09-27 | Likely expiry | Re-check trigger |
| --- | --- | --- | --- |
| DuckLabs → AWS ownership and foundation stewardship (§1.3, §2.5) | Joined AWS 2026-09-01; MIT retained; DuckDB Foundation stewards | 6–12 months | Any DuckDB governance/licence announcement, extension-signing policy change, or foundation board news |
| DuckDB remote access via Quack protocol and lakehouse scaling (§2.3, §2.4) | Documented on duckdb.org | 6 months | New DuckDB major release notes |
| DuckLake 1.0 status and DuckDB v1.5.2 baseline (§1.4, §5.2) | v1.0 production-ready 2026-04-13; extension in DuckDB v1.5.2 | 6 months | DuckLake 1.1/2.0 or DuckDB release calendar update |
| pandas 3.0 semantics (§1.5, §2.4) | 3.0.0 on 2026-01-21; 3.0.6 on 2026-09-17 | 6 months | pandas 3.1 / 4.0 release notes |
| Polars 2.0 defaults (§1.5, §2.4) | First RC 2026-09-02; final release expected weeks later | **Very short (weeks)** | Polars 2.0 final release + migration guide |
| MCP specification revision and features (§1.7, §2.3) | 2026-07-28 revision; 12-month deprecation policy | 6 months | Next MCP release (est. ~6 months cadence) or SEP changes |
| Microsoft Agent Framework version/status (§2.4, §5.6) | 1.0 GA 2026-04-03 for .NET+Python | 6–12 months | MAF point releases; AutoGen/SK deprecation notices |
| LangGraph v1 API status (§2.4, §5.6) | v1 with `create_react_agent` deprecated | 6–12 months | LangChain/LangGraph v2 announcements |
| Metabase / Superset release facts (§5.4) | Metabase 63 (2026-07-21); Superset 6.1.0 (2026-06-11) | 3–6 months | Next BI releases; MCP server scope and auth changes |
| Extraction accuracy figures (S15) | Value accuracy ≈86%; quote stability ≈45% | Stable (study is fixed) but generalisation-limited | New replicated studies on other tools/domains |
| Role titles and hiring signals (§2.2, §2.5) | Reported signal only | 6 months | New posting samples or labour-market data |
| Benchmark/performance magnitudes inherited from prior notes | Vendor- and hardware-specific | 3 months | Independent version-pinned benchmarks |

### 8.5 Modeling recommendations

1. **Model the evidence → structured-data boundary explicitly** with `evidence_span` rows; do not let "source" double as "record" `[R]`.
2. **Make claim the join point** for provenance, supersession, and confidence; attach relations to claims, not only to entities `[R]`.
3. **Keep the five-way distinction** Technology / Software / Product / Company / Standard in `entity_type` `[R]`.
4. **Treat positions as capability bundles**, storing `requires Skill` and `produces Artifact` edges rather than relying on titles `[R]`.
5. **Record versions on artifacts and claims**, never in node names `[R]`.
6. **Store `valid_until` and `falsifier` on every volatile claim** `[R]`.
7. **Measure per stage, not per pipeline**: evaluations belong to steps and agents, with traces attached to activities `[R]`.

---

## 9. Verification, provenance of this note, and change log

### 9.1 Verification performed

- All eleven prior `research/raw` notes plus the two `Citations/` audits were inventoried for headings, entity rows, comparison tables, and source lists; conflicts between them were recorded in §6.3 rather than silently resolved.
- Twelve external pages were fetched and read in this pass (S1–S12 and S15); S13, S14 and S17 are stable standards/occupational sources carried from prior notes; S16's retraction record was confirmed through search results rather than by opening the notice page. Each source is quoted or paraphrased only within what the page supports.
- Every version-sensitive claim was re-checked against first-party pages (DuckDB, DuckLabs, DuckLake, pandas blog + release notes, Polars blog, MCP spec blog, Microsoft DevBlogs, LangChain docs, dbt docs, Metabase releases, Preset/ASF).
- Two claims that could not be verified in this pass were **not** asserted: parser-benchmark superiority and the findings of the Cochrane Elicit-vs-human comparison (listed as a next investigation instead).
- Vault conventions were followed: YAML frontmatter with `modified`, `[F]/[S]/[I]/[R]` claim labels, per-lens confidence, wiki-links to existing notes, and a table-first presentation.

### 9.2 Known limitations of this note

- No first-party measurement was performed (no benchmark runs, no posting sample coding, no interviews) — this is a document-research result, not an empirical study `[I]`.
- Extraction-related numbers come from a single peer-reviewed study of one tool (S15); no generalisation to other tools is claimed.
- Company, product, and role material is date-stamped but inherently volatile; §8.4 defines when to re-check.
- The relationship predicate register (§4.5) is a recommendation, not a standard; it was designed to be mappable onto W3C PROV and onto a property graph without renaming `[R]`.

### 9.3 Change log

| Date | Change |
| --- | --- |
| 2026-09-27 | `Research.Results.md` created. Consolidated the eleven prior Atlas passes into a single results brief; added §4.5 predicate register, §6.3 conflicting-evidence register, §8 modeling handoff (name register, claim contract, DDL sketch, time-sensitivity register); verified S1–S17 and recorded two newly material facts (DuckLabs → AWS; BI MCP servers) plus one peer-reviewed extraction-stability finding and one retraction |

*Generated as a research result, not as advice. Where this note conflicts with a later primary source, the source wins; update the claim, add a `supersedes` edge, and record the change here.*

