# Research-to-Data Capability Atlas — Research Brief

**Date:** 2026-09-27 | **Access date for all web sources:** 2026-09-27
**Scope:** Research → Evidence → Extraction → Structured representation → Normalization → Database → Query → Analysis → Visualization → Interpretation → New research → Agent iteration

> Claim-type legend used below: **[F]** = documented fact (primary source), **[S]** = reported signal (secondary/vendor/press, single-source), **[I]** = inference/synthesis, **[R]** = recommendation. Confidence per lens: High / Medium / Low.

---

### 1. Executive synthesis

1. **The cluster is SQL-centric + Python-centric, not either/or.** DuckDB (in-process OLAP SQL), pandas/Polars (DataFrames), dbt (in-warehouse T) and BI (Metabase/Superset/Observable) are complementary, joined by Arrow zero-copy **[F]**. Confusing "knows SQL" with "does data modeling" is the most common category error.
2. **DuckDB ≠ MotherDuck ≠ DuckLake.** DuckDB = MIT-licensed embedded analytical DBMS (C++, no dependencies, OLAP) **[F]**; DuckDB Labs/DuckLabs = stewards **[S]**; MotherDuck = serverless cloud warehouse built on DuckDB with per-user "Ducklings"/hypertenancy **[F]**; DuckLake = lakehouse table format using SQL catalog, not files **[S]**. Vendor pages blur these; keep separate.
3. **pandas vs Polars vs DuckDB is a workflow-position choice, not a ranking.** Independent benchmarks agree: Polars streaming and DuckDB lead by ~1 order of magnitude over pandas/Dask/PySpark on 10–100 GB PDS-H; pandas OOMs or is ~94× slower at scale **[F]**. pandas wins on ecosystem (<1M rows, scikit-learn, viz libs); Polars on large ETL/lazy+parallel Rust; DuckDB on SQL-native, direct Parquet/S3, larger-than-memory **[I, Medium-High]**.
4. **ELT has displaced ETL as default in cloud analytics; dbt owns the "T".** dbt Docs define models as `SELECT` (.sql/.py) executed inside the warehouse, with DAG, tests, docs, version control **[F]**. Ingestion (Fivetran/Airbyte/dlt) → Load raw → dbt Transform is now the reference architecture **[F]**.
5. **Roles are not interchangeable.** Data analyst/BI (descriptive, dashboards, stakeholder translation) vs research analyst (external/market evidence, reports/briefings, often SPSS/surveys) vs data/research engineer (pipelines, infra) vs knowledge engineer/information architect (ontologies, RDF/OWL/SPARQL, graphs, semantic layer) **[F/S]**. Hiring signals: SQL+BI vs Python+stats vs RDF/Neptune/Neosemantics vs cloud orchestration. "AI/agent workflow specialist" and "automation specialist" are emergent, weakly standardized titles **[I, Low]**.
6. **Provenance has a stable standard (W3C PROV) that almost nobody in BI implements natively.** PROV-DM/PROV-O/PROV-N (Entities, Activities, Agents, 2013 REC) is the interoperable lineage vocabulary **[F]**. BI lineage (dbt Catalog column lineage, Marpit lineage) is proprietary and coarser. This is the biggest governance gap.
7. **Research rigor has a stable standard (PRISMA 2020) that agent pipelines ignore.** PRISMA 2020 = 27-item checklist + flow diagram for systematic reviews; PRISMA-P for protocols; not a quality-appraisal tool **[F]**. Most LLM extraction tools (Unstructured Extract, LlamaExtract) provide schema + citations/confidence but no PRISMA-equivalent gate **[I]**.
8. **Extraction is now schema-first LLM + regex hybrid.** Unstructured documents LLM (contextual, typed JSON via OpenAI Structured Outputs) vs Regex (stable patterns, no model) **[F]**; LlamaParse/LlamaExtract = layout-aware, table-preserving, page-cited PDF→Markdown/JSON **[F]**. Failure mode is silent schema drift + hallucinated fill, not parse crash.
9. **Agent frameworks converged on different primitives; AutoGen is in maintenance.** LangGraph = explicit typed state-graphs + durable memory + HITL + LangSmith observability **[F]**; CrewAI = roles/goals/tasks org-chart, fast start, higher token cost **[S]**; AutoGen → maintenance Oct 2025, successor Microsoft Agent Framework 1.0 GA Apr 2026 **[S]**; Swarm deprecated for OpenAI Agents SDK **[S]**. For research-to-data, LangGraph suits production/stateful loops; CrewAI suits sequential prototyping **[I, Medium]**.
10. **Agent failure is multiplicative, not additive.** Microsoft AIRT taxonomy v2.0 (Apr 2026) + DeepHalluBench/PING (2026): hallucinated path/claim becomes next-step input; propagation + cognitive bias (anchor, homogeneity), context overflow, reasoning loops, memory poisoning, loss of provenance **[F/S]**. Verification must be per-stage with citations, tests, human gates — end-to-end scoring hides it **[I/R]**.

---

### 2. Lens findings

#### 2.1 Skills

**Definition and scope:** Portable human/agent capacities applied across stages. The brief tracks 11: research synthesis, information extraction, data modeling, ontology design, normalization, SQL, DuckDB, pandas, visualization, provenance, agent orchestration.

**Core capabilities / position / relationships:**

- *Research synthesis* (PRISMA, eligibility criteria, risk-of-bias, certainty) → governs Research + Interpretation **[F]**. `governed_by` Methodology; `appears_in` Research Analyst, Research Engineer.
- *Information extraction* (schema design, LLM vs regex choice, table/layout handling) → governs Extraction **[F]**. `uses` Technology LLM/embeddings; `implemented_by` Unstructured, LlamaExtract.
- *Data modeling* (facts/dimensions, dbt models, DAG) → governs Normalization/Storage **[F]**. `uses` SQL/Python; `governs` Workflow.
- *Ontology design* (RDF/OWL/SHACL/SPARQL, competency questions, METHONTOLOGY/TOVE/ENTERPRISE) → governs Structured representation for graphs **[F]**. Distinct from relational modeling; over-scoping is classic failure **[F]**.
- *Normalization* (renaming, casting, joining, enriching; dbt tests) → Extraction→Storage **[F]**.
- *SQL* (Postgres-dialect, DuckDB friendly SQL) → Query/Analysis **[F]**. Stable fact.
- *DuckDB skill* (in-process OLAP, Parquet/S3/Arrow, threads/memory settings) → Storage/Query **[F]**. Not same as generic SQL.
- *pandas skill* (DataFrame, NumPy→Arrow 2.0, viz integration) → Analysis/exploration <1M rows **[F]**.
- *Visualization* (grammar-of-graphics Plot, BI dashboards, Inputs interactivity) → Visualization **[F]**.
- *Provenance* (PROV Entities/Activities/Agents, lineage, citations) → cross-cutting quality gate **[F]**.
- *Agent orchestration* (graphs, state, memory, HITL, streaming, evals) → Iteration/governance **[F/S]**.

**Trade-offs / failure modes:** Synthesis without protocol → cherry-picking; extraction without schema tests → silent drift; modeling without tests → metric drift; viz without semantics → misleading precision; orchestration without checkpointing → domino hallucinations.

**Confidence:** High for SQL/modeling/PROV/PRISMA/DuckDB/pandas definitions; Medium for DuckDB-tuning and orchestration depth (fast-moving); Low for stable "agent orchestration" skill ladder (no standard).

#### 2.2 Market positions

**Definition:** Employer labels for bundles of responsibilities/outputs. Do NOT treat as synonyms **[R]**.

| Role | Responsibility / Output | Distinct skill/tool signal | Workflow locus |
|---|---|---|---|
| Data Analyst | Descriptive analytics, KPIs, dashboards, ad-hoc stakeholder Q&A | SQL, Excel, BI (Tableau/PowerBI/Metabase), storytelling | Query→Viz→Interpretation |
| Data/BI Analyst | Same as above + semantic measures, governance, embedded analytics | + dbt Semantic Layer, metric defs, RLS | Storage→Viz |
| Research Analyst | External intelligence: market/sector reports, briefings, forecasts; own patch | Surveys, SPSS, Excel, domain expertise; Python/R emerging | Research→Evidence→Interpretation |
| Knowledge Engineer | Computable domain models: ontologies, KGs, semantic layer, RAG grounding | RDF/SPARQL/OWL/SHACL, Neptune/Neo4j/Stardog, Bedrock/SageMaker | Representation→Normalization |
| Information Architect | Metadata/taxonomy/navigation structure across systems | Taxonomy, schema, content modeling | Representation (broader than KG) |
| Research Engineer | Productionize research: pipelines, evals, model/tooling | Python, ML infra, experimentation | Research→Iteration |
| Data Engineer (adjacent, needed for boundary) | Pipelines, warehouse/lake, APIs, quality/scale | Airflow, Fivetran, cloud DW | Extraction→Storage |
| Automation Specialist | Rule/script automation of ops workflows | RPA, scripting, integrations | Workflows (generic) |
| AI/Agent Workflow Specialist | LLM agent design, tool/MCP wiring, evals, HITL | LangGraph/CrewAI/MAF, MCP/A2A, LangSmith/OTel | Agent iteration |

Evidence: TechTarget/Indeed/nCube/ChartIO agree engineer builds infra, analyst translates to decisions, scientist predicts **[F]**; H2KInfosys + Guardian + Indeed + Investopedia agree research analyst = external/unstructured + reports vs data analyst = internal/structured + dashboards **[S, convergent]**; Accenture postings define knowledge engineer as ontology/KG/semantic + Neptune/Glue/Bedrock **[F, first-party postings]**; ontology texts define knowledge engineering as logic+ontology for computable models **[F]**.

**Trade-offs:** Title inflation; "data analyst" postings ranging from Excel to ML; "knowledge engineer" now rebranded for RAG without logic background → weak ontologies; automation vs agent roles lack hiring taxonomy.

**Confidence:** High for analyst/engineer/knowledge-engineer boundaries; Medium for research-analyst salary/skill mix (sparse, UK n=2 in ITJobsWatch); Low for automation/AI-workflow specialist (emergent, vendor-driven).

#### 2.3 Technology

**Definition:** Durable technical substrates, distinct from products that package them.

- Python, SQL (stable, universal) **[F]**; Notebooks (Jupyter reactive narrative + code) **[F]**; APIs/scraping/browser automation (ingest unstructured web) **[I]**; LLMs/embeddings (semantic extraction/retrieval) **[F]**; Graph tech (property graph Cypher + RDF/SPARQL/OWL, vector+HNSW hybrid in Neo4j) **[F]**; Data formats (CSV/Parquet/JSON/Markdown/Arrow IPC) **[F]**; Databases (OLAP DuckDB, graph Neo4j/Neptune, warehouse Snowflake/BigQuery/Redshift/MotherDuck) **[F]**.
- Position: Python/pandas/Polars = Analysis; SQL/DuckDB = Storage/Query; APIs/scraping = Research/Extraction; LLMs/embeddings = Extraction/Retrieval; graphs = Representation/Query; formats/DBs = cross-cutting.
- Relationships: `implemented_by` Software; `uses` in Workflow; `supports` Agent tools.

Trade-offs: Scraping fragility/legal; embeddings lose exactness/provenance; graphs cost modeling overhead; Parquet+Arrow win for analytics vs CSV/JSON verbosity.

Confidence: High except scraping/browser-automation legality/robustness (Medium, jurisdiction-dependent).

#### 2.4 Software

**Definition:** Installable/open-source or hosted executables. Keep Technology (e.g., DuckDB engine concept) separate from Software distribution (DuckDB binary/extension) and Company (DuckDB Labs) and Product (MotherDuck warehouse).

- **DuckDB:** in-process OLAP, zero-dependency, Arrow/Pandas/Polars zero-copy, Parquet/S3/spatial extensions, single-file ACID **[F]**. Position: Storage/Query.
- **pandas 2.x:** DataFrame, NumPy→Arrow backend, widest viz/ML integration, single-threaded, OOM >memory **[F]**.
- **Polars:** Rust, lazy optimizer + parallel/streaming, 11.4× pandas on 10M-row agg in one test; PDS-H SF10 total 3.89s streaming vs 365s pandas **[S, benchmark-specific]**.
- **Jupyter:** interactive exploration, narrative + code **[F]**.
- **dbt Core/Cloud:** T in ELT, SQL/Python models, DAG, tests/docs, CI/CD **[F]**.
- **Metabase:** OSS BI, no-code question builder, 1-container, built-in Metabot NLQ + semantic glossary; weaker advanced viz/SQL vs Superset **[S, vendor + G2]**.
- **Superset:** OSS BI ex-Airbnb, 30+ viz incl. geo/D3, advanced SQL Lab, needs 5-process stack + tech ops; MCP server but no native chat (Preset paid) **[S]**.
- **Observable (+Plot):** reactive JS notebooks, Plot grammar-of-graphics, Inputs interactivity, import/fork/version history; Python via pyobsplot/Arrow **[F]**.
- **Orchestration/agent frameworks:** LangGraph (graph+state+HITL+memory+streaming), CrewAI (roles/tasks), Microsoft Agent Framework (successor to AutoGen+Semantic Kernel, YAML+checkpoint+MCP/A2A), Temporal (durable generic workflows, no native LLM observability) **[F/S]**.
- **Extraction:** Unstructured (partition→Extract LLM/Regex→DocumentData JSON), LlamaParse/LlamaExtract (layout-aware, tables, citations/confidence, bulk API), UnstructuredReader for LlamaIndex **[F]**.

Trade-offs/failures: pandas silent memory blowup; Polars expression-API learning curve; DuckDB single-node limits vs distributed; Metabase governance limits in free tier; Superset admin load; Observable JS-centric; agent frameworks token/latency overhead.

Confidence: High for DuckDB/dbt/Observable/Unstructured/Llama docs; Medium for benchmark magnitudes (hardware/version-sensitive) and BI ease claims (biased sources).

#### 2.5 Companies

Separate: **Employers** (hire roles), **Vendors** (sell products), **OSS foundations/communities** (steward code/standards), **Consultancies**, **Research orgs**.

- Vendors: MotherDuck (serverless DuckDB, $100M total, Series B $52.5M Felicis 2023) **[S]**; DuckDB Labs (engine stewards, co-founder of MotherDuck effort) **[S]**; dbt Labs (dbt Cloud, acquired SDF, Copilot) **[F]**; Metabase Inc., Preset (managed Superset), Observable Inc., Neo4j Inc., Unstructured Inc., LlamaIndex Inc. **[S/F]**.
- OSS/Standards: DuckDB OSS (MIT), Apache Superset (ASF), W3C PROV WG (closed, stable REC), PRISMA Group/EQUATOR, Polars OSS, Jupyter Project **[F]**.
- Consultancies/employers: Accenture (knowledge-engineer hiring at scale on AWS/GCP) **[F]**; asset managers/banks/insurers/hedges (research analysts) **[F]**; Gartner/Forrester/Wood Mackenzie (sector analysts) **[S]**.
- Research orgs: Zhejiang/HKU (DeepHalluBench), Microsoft AIRT/Security, CWI (DuckDB origins: Raasveldt/Mühleisen papers SIGMOD19/CIDR20) **[F/S]**.

Trade-off: Vendor BI comparisons (Metabase vs Superset) are positioning, not facts **[R: discount]**; Tracxn funding/employee counts are stale proxies.

Confidence: High for role-employer mapping; Medium for funding/headcount (time-sensitive).

#### 2.6 Products

Define by user problem + workflow position + differentiator, not feature list:

- Research/data platforms: MotherDuck (serverless DuckDB for teams/agents, dual execution laptop+cloud, DuckLake managed) — problem: fast cheap analytics without infra **[S]**.
- Extraction: Unstructured Extract (schema-first JSON in-pipeline), LlamaExtract/LlamaParse (accurate bulk PDF→JSON/Markdown with traceability) **[F]**.
- BI: Metabase (self-serve for mixed-skill teams, 5-min dashboard) vs Superset/Preset (SQL-heavy control, richer viz, heavier ops) vs Observable (exploratory viz prototyping → data apps) **[S/F]**.
- Knowledge: Neo4j Graph + vector index + GraphRAG retrievers (Vector/Hybrid/Cypher) — problem: factual grounding + semantic recall **[F]**.
- Agent infra: LangGraph Platform (+LangSmith evals/observability, Deep Agents token optimization), CrewAI Cloud (visual builder, VPC/FedRAMP), Microsoft Agent Framework (.NET+Python, OTel) **[S]**.

Confidence: Medium (docs strong, differentiation claims vendor-biased).

#### 2.7 Methodologies

- Research protocols: PRISMA 2020 (27 items + flow; PRISMA-P 17 items for protocols; extensions for scoping/network/IPD) **[F]**. `governs` Research→Interpretation.
- ETL/ELT: ETL = transform-before-load (external engine); ELT = load-raw-then-transform-in-warehouse; hybrid common; ELT preferred on cloud for scale/democratization **[F, dbt Labs]**.
- Data modeling: dbt models/DAG/tests/docs/CI; dimensional modeling implicit **[F]**.
- Information extraction: LLM (inferred, typed, nested) vs Regex (pattern-matched strings); pilot both on sample before standardizing **[F, Unstructured]**.
- Evidence/provenance: W3C PROV (Entity/Activity/Agent + derivation/revision/roles) + serializations (PROV-O/N/XML) **[F]**; operational lineage (dbt Catalog column lineage, Llama citations) is partial implementation **[I]**.
- Analytical workflows: style guides, docs, prod monitoring, incremental/state-aware orchestration, defer/rerun-from-failure **[F, dbt best-practice]**.

Failures: No protocol → irreproducible review; ETL stored-proc spaghetti → untraceable lineage (dbt's stated migration motive); PROV without tooling → shelfware.

Confidence: High for PRISMA/PROV/ELT definitions; Medium for "best practice" universality.

#### 2.8 Workflows

See §3 for stage map. Summary: loop is not linear; quality gates (protocol, schema test, dbt test, human review, viz sanity, re-registration) and feedback (interpretation → new research; eval → agent revision) define maturity. `governed_by` Methodology; `uses` Technology; `performs` Agent.

Confidence: Medium (synthesis across sources, no single primary source covers full loop).

#### 2.9 Agents

**Definitions (task + tools/state + handoff + verification + failure):**

- *Research agent:* plans sub-queries, searches/browses/APIs, ranks evidence. Tools: search, browser, retrievers. State: plan + chunk memory. Handoff: cited evidence bundle → extraction. Verify: claim→source entailment (NLI/LLM judge). Fail: intent drift, restriction neglect, noise prioritization (PING Intent/Noise) **[S, DeepHalluBench]**.
- *Extraction agent:* applies schema (LLM/Regex), normalizes values. Tools: Unstructured/LlamaExtract, code exec. State: schema version + raw refs. Handoff: typed JSON + page coords → cleaning. Verify: schema validation + spot audit. Fail: hallucinated fill, table scramble **[F/S]**.
- *Coding/data-cleaning agent:* dedupes, casts, joins, writes DuckDB/Parquet, dbt models/tests. Tools: Python/SQL/DuckDB/Polars, git. Verify: dbt tests, uniqueness/not-null/relational. Fail: silent coercion, metric drift **[F]**.
- *Analytical agent:* queries, stats/models, answers. Tools: SQL, notebooks, vector/graph retrieval. Verify: reproduce query + effect sizes. Fail: p-hacking, temporal anchor bias **[S]**.
- *Coordinating/orchestration agent:* routes, branches, checkpoints, HITL interrupts, streams, persists memory. Tools: LangGraph/MAF/CrewAI, MCP/A2A, OTel/LangSmith. Verify: trace + evals + annotation queue. Fail: loops, context overflow (20M-token failure vs 1.2k with pointers per AWS/IBM report **[S]**), memory poisoning, HITL bypass **[F, AIRT]**.

Confidence: Medium (convergent but largely 2025–2026 preprints/vendor eng posts, time-sensitive).

---

### 3. Workflow map

| Stage | Inputs | Activities | Outputs | Quality checks / Gates | Likely tools | Suitable agent roles |
|---|---|---|---|---|---|---|
| 1. Research | Question, prior lit, protocol draft | Formulate PICOS/eligibility, register protocol, plan searches | Protocol (PRISMA-P), query plan | Protocol exists? Registered? Amendments logged? | PRISMA checklists, search APIs, notebooks | Research + Coordinator |
| 2. Evidence | Candidates from search/scrape/API | Screen (title/abstract/full-text), appraise bias, select | Included set + PRISMA flow counts, exclusion log | Dual screening? Risk-of-bias? Inter-rater? | Browser automation, Zotero-like stores, LLM rankers | Research |
| 3. Extraction | Included docs, JSON schema / guidance | Partition/layout parse, LLM or Regex extract, normalize values | Typed JSON (DocumentData) + page citations + confidence | Schema valid? Sample audit pass? Nesting ≤10? | Unstructured Extract, LlamaExtract/Parse | Extraction |
| 4. Structured representation | Extracted JSON, ontology/model | Map to relational (facts/dims) or graph (RDF/OWL/SHACL) | Tables / KG nodes-edges + mapping spec | Competency Qs answered? No over-scope? SHACL pass? | Python, Neo4j/n10s, Neptune | Extraction→Cleaning |
| 5. Normalization | Raw tables | Rename/cast/join/enrich, model in warehouse | dbt models + DAG + docs | dbt tests (unique/not-null/relational)? CI green? | dbt, SQL/Python, DuckDB/Polars | Cleaning/Coding |
| 6. Database | Modeled sets | Load/store, index (incl. vector HNSW dims+cosine), version | DuckDB/MotherDuck/DuckLake/Iceberg + catalog | ACID? Index dims match model? Lineage recorded (PROV)? | DuckDB, MotherDuck, Neo4j vector index | Cleaning + Coordinator |
| 7. Query | Question + catalog | Write/parametrize SQL/Cypher/vector search | Result sets + SQL text | SQL reviewed? Traceable (FixIt/Metabot trace)? | DuckDB SQL, Cypher 25 SEARCH, SQL Labs | Analytical |
| 8. Analysis | Result sets | Aggregate, stats/ML, hybrid retrieval traversal | Tables, estimates, model artifacts | Reproducible notebook? Effect + uncertainty? | pandas/Polars/Jupyter, GraphRAG retrievers | Analytical |
| 9. Visualization | Analysis outputs | Choose marks/scales, build dashboards/notebooks, add Inputs | Charts, dashboards, Observable notebooks | Visual sanity (axis, denoms)? Accessible? No-code vs SQL fit? | Plot, Metabase, Superset, pyobsplot | Analytical (+Human) |
| 10. Interpretation | Viz + prior evidence | Contextualize, GRADE certainty, discuss limits/implications | Report/briefing + certainty + limits | PRISMA 23a-d (interpretation/limits/implications)? Provenance attached? | Docs, Glossary/semantic layer | Research + Human approver |
| 11. New research | Gaps/limits | Reformulate Q, update living review | New protocol / backlog | Registered update? | Same as 1 | Research + Coordinator |
| 12. Agent iteration | Traces, evals, feedback | Replay, patch prompts/code/schema, re-eval, checkpoint | Improved agents + eval report | Per-step traces? LLM-judge + human annotation? Token/latency within budget? | LangGraph+LangSmith / MAF+OTel / CrewAI | Coordinator |

Feedback loops: 10→1 (evidence update), 12→all (agent revision), 5→3 (schema fix on test failure), 9→7 (viz exposes query error). Gates are load-bearing; skipping yields domino hallucination **[I/R]**.

---

### 4. Entity and relationship candidates

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
|---|---|---|---|---|---|---|---|
| Skill | Research synthesis | Systematic collation/appraisal/synthesis per PRISMA | Research, Interpretation | PRISMA 2020, Research Analyst | governed_by, appears_in | bmj.com PRISMA 2020; equator-network | High |
| Skill | Information extraction | Schema-guided conversion of unstructured→typed data | Extraction | Unstructured Extract, LlamaExtract | implemented_by | docs.unstructured.io; developers.llamaindex.ai | High |
| Skill | Data modeling | Designing facts/dims/DAG for analytics | Normalization, Storage | dbt models | governs, uses | docs.getdbt.com/models | High |
| Skill | Ontology design | Formal shared conceptualization (OWL/RDF/SHACL) | Representation | Knowledge Engineer, Neo4j | performs, uses | Southampton ontology eng.; Accenture postings | High |
| Skill | Normalization | Cleaning/casting/joining/enriching raw extracts | Normalization | dbt Transform | produced_by | getdbt.com ELT pages | High |
| Skill | SQL | Declarative relational query language | Query, Analysis | DuckDB, dbt, Metabase | uses | duckdb.org/why_duckdb; dbt docs | High |
| Skill | DuckDB operation | In-process OLAP tuning (threads, memory, Parquet/S3) | Storage, Query | DuckDB, MotherDuck | implemented_by | duckdb.org; motherduck.com | High |
| Skill | pandas | DataFrame manipulation/exploration | Analysis | pandas software | implemented_by | motherduck.com/blog comparison | High |
| Skill | Visualization | Grammar-of-graphics + dashboard design | Visualization | Plot, Metabase, Superset | implemented_by | observablehq.com/plot; metabase.com | High |
| Skill | Provenance | Recording entities/activities/agents lineage (PROV) | Cross-cutting | W3C PROV, dbt lineage | governs | w3.org/TR/prov-dm, prov-o | High |
| Skill | Agent orchestration | Stateful graph/HITL/memory/eval design | Iteration | LangGraph, MAF, CrewAI | implemented_by | langchain.com/langgraph; n-ix.com 2026 | Medium |
| Market Position | Data Analyst | Translates internal structured data to decisions via reports/dashboards | Query→Interpretation | SQL, BI tools | uses, appears_in | TechTarget; Indeed UK; nCube | High |
| Market Position | Data/BI Analyst | Above + semantic/governance focus | Storage→Viz | dbt Semantic, Metabase | uses | Metabase semantic-layer pages | Medium |
| Market Position | Research Analyst | External intelligence → reports/briefings on sector | Research→Interpretation | SPSS, surveys, Excel | performs | Guardian; Investopedia; Indeed hire | Medium |
| Market Position | Knowledge Engineer | Builds ontologies/KGs/semantic+RAG layers | Representation | RDF/SPARQL/Neptune | performs | Accenture postings (4x) | High |
| Market Position | Information Architect | Cross-system taxonomy/metadata/navigation | Representation | Ontology design | supports | Southampton types; inference | Medium |
| Market Position | Research Engineer | Productionizes research methods/systems | Research→Iteration | Python, evals | performs | Inference from DS/Research Scientist splits | Low |
| Market Position | Automation Specialist | Scripts/rules automation of ops tasks | Workflows | APIs, RPA | performs | Generic; no primary source found | Low |
| Market Position | AI/Agent Workflow Specialist | Designs/evals LLM agent workflows | Iteration | LangGraph, MCP | performs | LangChain/CrewAI vendor + N-IX | Low |
| Technology | Python | General language for analysis/pipelines | Analysis, Extraction | pandas, Polars, Jupyter | implemented_by | MotherDuck/PDS-H benchmarks | High |
| Technology | SQL | Query language for relational/OLAP | Query | DuckDB, dbt | implemented_by | DuckDB docs; dbt docs | High |
| Technology | DuckDB engine | Embedded columnar vectorized OLAP | Storage, Query | DuckDB SW, MotherDuck | implemented_by | SIGMOD19; CIDR20; duckdb.org | High |
| Technology | pandas library concept | Eager DataFrame (NumPy→Arrow) | Analysis | pandas SW | implemented_by | MotherDuck blog; Polars benchmarks | High |
| Technology | Notebooks | Narrative+code reactive docs | Analysis, Viz | Jupyter, Observable | implemented_by | observablehq.com/notebooks | High |
| Technology | APIs / Scraping / Browser automation | Programmatic/web evidence ingest | Research, Extraction | Extraction tools | supports | Llama/Unstructured ingestion docs | Medium |
| Technology | LLMs | Contextual inference/extraction/generation | Extraction, Analysis | Unstructured LLM, LlamaExtract | uses | docs.unstructured.io | High |
| Technology | Embeddings + Vector search | Numeric semantics + HNSW ANN (cosine/euclid.) | Retrieval, Query | Neo4j vector index | implemented_by | neo4j.com vector docs | High |
| Technology | Graph technologies | Property/RDF graphs, Cypher/SPARQL/OWL | Representation, Query | Neo4j, Neptune | implemented_by | neo4j.com; n10s guides | High |
| Technology | Data formats (Parquet/Arrow/CSV/JSON) | Storage/exchange encodings | Cross-cutting | DuckDB, Polars | supports | DuckDB/Arrow docs | High |
| Technology | Databases (warehouse/lakehouse/graph) | Persistent queryable stores | Storage | MotherDuck, Neo4j | implemented_by | motherduck.com; neo4j.com | High |
| Software | DuckDB | OSS embedded OLAP DBMS binary + extensions | Storage, Query | DuckDB Labs (steward) | produced_by | duckdb.org | High |
| Software | pandas | OSS DataFrame lib | Analysis | Python | implemented_by | MotherDuck sizing (312M w/ pyarrow) | High |
| Software | Polars | Rust DataFrame, lazy/streaming | Normalization, Analysis | Python/Rust | implemented_by | pola.rs PDS-H; johal.in test | Medium |
| Software | Jupyter | OSS notebook runtime | Analysis | Python | supports | Standard; Observable contrast | High |
| Software | dbt | SQL/Python transformation + tests/docs | Normalization | dbt Labs | produced_by | docs.getdbt.com | High |
| Software | Metabase | OSS BI + Cloud/Pro, Metabot, glossary | Viz | Metabase Inc. | produced_by | metabase.com LP + alternatives | Medium |
| Software | Apache Superset / Preset | OSS BI + managed cloud | Viz | ASF / Preset | produced_by | metabase.com vs; preset context | Medium |
| Software | Observable + Plot | Reactive notebooks + OSS viz lib | Viz | Observable Inc. | produced_by | observablehq.com; github plot | High |
| Software | LangGraph (+LangSmith) | Graph orchestration + observability | Iteration | LangChain Inc. | produced_by | langchain.com | High |
| Software | CrewAI | Role/task multi-agent framework + cloud | Iteration | CrewAI Inc. | produced_by | crewai docs via meta-intel/n-ix | Medium |
| Software | Microsoft Agent Framework | AutoGen+SK successor, YAML/graph/MCP/A2A | Iteration | Microsoft | produced_by | langchain.com 2026-06; n-ix 2026-09 | Medium |
| Software | Unstructured Extract | LLM/Regex schema extractor + pipelines | Extraction | Unstructured Inc. | produced_by | docs.unstructured.io | High |
| Software | LlamaExtract/LlamaParse | Layout-aware PDF→JSON/Markdown + bulk API | Extraction | LlamaIndex Inc. | produced_by | developers.llamaindex.ai; llamaindex.ai | High |
| Company | DuckDB Labs | Stewards DuckDB engine | Storage | DuckDB | produced_by | motherduck.com/company; duckdb.org | Medium |
| Company | MotherDuck | Serverless DuckDB warehouse (Ducklings, DuckLake) | Storage, Query | DuckDB, DuckLake | produced_by | motherduck.com; TechCrunch 2023 | Medium |
| Company | dbt Labs | Sells dbt Cloud, stewards dbt Core | Normalization | dbt | produced_by | getdbt.com; docs.getdbt.com | High |
| Company | Metabase Inc. / Preset / Observable / Neo4j | BI/graph/notebook vendors | Viz, Representation | Respective SW | produced_by | Respective .com + Tracxn | Medium |
| Company | Accenture (consultancy/employer) | Hires knowledge engineers at scale | Representation | Knowledge Engineer | appears_in | accenture.com postings | High |
| Product | MotherDuck warehouse | Serverless analytics for humans+agents | Storage→Analysis | DuckDB, dbt, Hex | uses | motherduck.com/product | Medium |
| Product | DuckLake format | SQL-catalog lakehouse (alt. Iceberg/Delta) | Storage | MotherDuck, DuckDB | uses | motherduck.com/ducklake + blog | Medium |
| Product | Metabase BI | Self-serve Q&A/dashboards/embedding | Viz | SQL DWs | supports | metabase.com | Medium |
| Product | Superset/Preset BI | Advanced SQL/viz/governed embeds | Viz | SQL DWs | supports | metabase.com vs; preset context | Medium |
| Product | Neo4j GraphRAG stack | Vector+graph hybrid retrieval + grounding | Representation→Query | Embeddings, Cypher | uses | neo4j.com genai docs | High |
| Methodology | PRISMA 2020 (+P) | Reporting guideline, 27 items + flow | Research, Interpretation | Research synthesis | governs | bmj.com n71/n160; equator | High |
| Methodology | ETL/ELT (+dbt-T) | Ingest-transform-load orderings | Extraction→Storage | dbt, Fivetran/Airbyte | governs | docs.getdbt.com/terms/elt | High |
| Methodology | LLM-vs-Regex extraction | Contextual-typed vs pattern-matched choice | Extraction | Unstructured | governs | docs.unstructured.io concepts | High |
| Methodology | W3C PROV | Entity/Activity/Agent provenance model | Cross-cutting | Provenance skill | governs | w3.org PROV-DM/O/Primer | High |
| Workflow | Full R→E→N→S→Q→A→V→I→New→Iter loop | End-to-end with gates + feedback | All | All lenses | uses, appears_in | Synthesis (no single source) | Medium |
| Agent | Research agent | Plans/searches/ranks cited evidence | Research, Evidence | Search/browser tools | performs | DeepHalluBench PING | Medium |
| Agent | Extraction agent | Schema-fills typed evidence | Extraction | Unstructured/Llama | performs | Unstructured/Llama docs + PING Grounding | Medium |
| Agent | Coding / Data-cleaning agent | Transforms/tests/loads | Normalization, Storage | dbt/DuckDB | performs | dbt best-practice; benchmarks | Medium |
| Agent | Analytical agent | Queries/models/answers | Query, Analysis | SQL/Python/graph | performs | PDS-H + GraphRAG docs | Medium |
| Agent | Coordinating agent | Graphs/state/HITL/memory/evals | Iteration | LangGraph/MAF | performs | LangGraph docs; AIRT v2 | Medium |

---

### 5. Comparison tables

#### 5.1 Roles (purpose / users / inputs / outputs / hiring signal)

| Role | Purpose | Serves | Inputs | Outputs | Hiring signal (distinguisher) |
|---|---|---|---|---|---|
| Data / BI Analyst | Answer business Qs descriptively | Ops/mgmt | Clean tables, metric defs | Dashboards, KPIs, narratives | SQL + BI + storytelling; no pipeline ownership |
| Research Analyst | Advise on external market/sector | Clients/mgmt | Surveys, filings, reports, interviews | Dense reports, spreadsheets, briefings | Domain patch + SPSS/Excel + precision writing |
| Knowledge Engineer | Make domain computable for AI | AI/data teams | Expert + unstructured knowledge | Ontologies, KGs, semantic/RAG layers | RDF/SPARQL/OWL/SHACL + Neptune/Neo4j |
| Research Engineer | Turn research into working systems | Product/research | Papers, prototypes, data | Pipelines, evals, models | ML + SWE + experimentation |
| Automation / Agent Specialist | Automate/orchestrate workflows/agents | Ops + eng | APIs, docs, tools | Bots, crews/graphs, evals | RPA/integrations vs LangGraph/MCP/A2A (emergent) |

#### 5.2 Core tech/software (purpose / interface / scale / openness / limit)

| Tool | Purpose | Interface | Best scale | Openness/cost | Key limit |
|---|---|---|---|---|---|
| DuckDB | Embedded OLAP query | SQL + Arrow/Parquet/S3 | GB–low TB single-node, >memory | MIT, tiny (~57M) | Not distributed; needs MotherDuck/scale-out for concurrency |
| pandas | Exploratory DataFrames | Python methods | <1M rows, ML/viz eco | OSS, heavy (~312M w/ pyarrow) | Single-thread, OOM, no optimizer |
| Polars | Fast ETL/frames | Expr + lazy + SQL | 10M–100GB streaming | OSS, light (~150M) | API learning curve; cache-bound in-memory at 100GB |
| dbt | In-warehouse T + tests/docs | SQL/Python + YAML + git | Any warehouse size | OSS Core + paid Cloud | Not EL; needs loader + warehouse |
| Metabase | Self-serve BI | No-code + SQL + Metabot | SMB–mid, mixed skills | OSS + Cloud/Pro | Lighter SQL/viz breadth; governance paywalled |
| Superset | Power-user BI | SQL Lab + rich viz | Data-mature, analyst-led | ASF OSS + Preset paid | 5-process ops, analyst-dependent |
| Observable/Plot | Exploratory viz → apps | JS/SQL/Markdown + Inputs | Prototyping–apps | OSS Plot + paid Teams | JS-centric; Python only via bridge |
| Neo4j (+vector) | Factual + semantic retrieval | Cypher 25 SEARCH + HNSW | KG + embedding scale | Community/Enterprise/Aura | Modeling + dim/config overhead |

#### 5.3 Methodologies

| Method | Governs | Input→Output | Strength | Limit |
|---|---|---|---|---|
| PRISMA 2020 | Research→Interpretation | Q + studies → transparent review + flow | Reproducibility, bias discipline | Reporting only, not quality appraisal |
| ELT (+dbt) | Extraction→Storage | Raw DW → tested modeled marts | Speed, democratization, lineage | Storage cost, needs warehouse power |
| ETL | Same | Sources → cleaned DW | Governance pre-load, legacy fit | Bottleneck, hidden logic in procs |
| LLM extraction | Extraction | Docs + schema → typed JSON | Handles context/nesting/tables | Hallucinated fill, cost/latency |
| Regex extraction | Extraction | Text + patterns → string arrays | Cheap, exact for IDs/dates | Brittle to template drift |
| W3C PROV | Cross-cutting | Runs → Entity/Activity/Agent graph | Interoperable trust | Rarely implemented in BI; overhead |

#### 5.4 Agent frameworks / agents

| Framework/Agent | Primitive | State/memory/HITL | Observability | Maturity/failure note |
|---|---|---|---|---|
| LangGraph | Directed state-graph | Built-in short/long memory + `interrupt()` + streaming | LangSmith traces/evals/queues | GA 1.0 Oct 2025; prod choice, steeper curve |
| CrewAI | Roles+tasks crew | Checkpoint (Qdrant Edge) | Cloud evals | Fast start; higher tokens (5.2k vs 2.8k in one test **[S]**) |
| Microsoft Agent Framework | Graph workflows + YAML | Checkpointing | OTel native | GA Apr 2026; AutoGen in maintenance **[S]** |
| Temporal | Durable generic workflows | DIY signals, 2MB cap | 3rd-party | Not agent-native (no LLM evals/memory) |
| Research/Extraction/Cleaning/Analytical/Coordinator | Task agents above | Pointer pattern for large data; explicit SUCCESS/FAILED | Claim→source + dbt tests + annotation | Loops, overflow, propagation, poisoning without gates |

---

### 6. Research gaps and next investigations

1. **Missing primary evidence:** Salary/leveling for knowledge engineer vs information architect vs agent specialist (only Accenture postings + sparse ITJobsWatch n=2 captured). Next: scrape 50 postings per title on LinkedIn/Indeed + O*NET/ESCO mapping.
2. **Weakly supported:** Token/latency/quality deltas across frameworks (single 2026 test: 4.2s/2.8k/9.1 LangGraph vs 8.7s/5.2k/8.5 CrewAI). Needs replication on fixed commit + hardware + PDS-H-like agent bench. Falsifier: independent rerun with reversed ranking.
3. **No head-to-head:** Unstructured vs LlamaExtract accuracy/cost on same PDFs (ExtractBench claims exist but not reviewed). Next: run ExtractBench + manual audit with citations.
4. **Provenance in practice:** Does any BI (Metabase/Superset/Observable) emit PROV-O? Docs suggest no. Next: inspect MCP servers + export formats + dbt artifact `manifest.json` → PROV mapping spike.
5. **DuckLake vs Iceberg/Delta:** Only MotherDuck/DuckDB sources. Needs independent TPC-style metadata-ops bench + multi-engine interop test.
6. **Living reviews + agents:** PRISMA living-review guidance vs agent iteration loops unmapped. Next: interview systematic-review teams using LLM screening.
7. **Scraping/browser legality & robustness:** Not covered with primary legal/engineering sources. Next: TOS case review + Playwright vs managed-browser eval.
8. **Falsification rules:** If DuckDB adds distributed execution, or dbt deprecates Core, or W3C supersedes PROV, or MAF adoption collapses, §§2–4 rows must be revised. Time-sensitive claims (versions, funding, GA dates) expire fastest.

---

### 7. Sources

* DuckDB homepage + Why DuckDB + SIGMOD19/CIDR20 papers — `https://duckdb.org/`, `http://duckdb.org/why_duckdb`, `https://duckdb.org/library/duckdb`, `https://duckdb.org/library/embedded-analytics/` — Supports: DuckDB = embedded OLAP, no deps, in-process, Arrow/Parquet. **[F]**
* MotherDuck homepage/company/data-teams/DuckLake + PR + TechCrunch — `https://motherduck.com/`, `https://www.motherduck.com/company`, `http://motherduck.com/product/data-teams`, `https://motherduck.com/product/ducklake/`, `https://techcrunch.com/2023/09/20/...` — Supports: serverless DuckDB, Ducklings/hypertenancy, DuckLake SQL-catalog, $52.5M Series B / $100M total, 2022 founding. **[F for product defs; S for pricing/performance/funding]**
* MotherDuck DuckDB vs pandas vs Polars + Johal benchmark + Polars PDS-H + prrao87 study — `https://motherduck.com/blog/duckdb-versus-pandas-versus-polars`, `https://motherduck.com/videos/...`, `https://johal.in/...`, `https://pola.rs/posts/benchmarks`, `https://github.com/prrao87/duckdb-study` — Supports: complementarity via Arrow, sizing (57/150/312M), 33M-row OOM for pandas, 11.4×/9.7× deltas, PDS-H 3.89s vs 365s. **[F for architecture; S for magnitudes]**
* dbt Labs ELT/ETL/model/best-practice docs — `https://docs.getdbt.com/terms/elt`, `https://docs.getdbt.com/docs/build/models`, `https://www.getdbt.com/product/elt-migration`, `https://www.getdbt.com/blog/etl-pipeline-best-practices`, `https://courses.getdbt.com/blog/etl-tools-data-pipeline-architecture` — Supports: ELT def, dbt = T, models/DAG/tests/docs/CI, ingestion+dbt architecture. **[F]**
* TechTarget / Indeed UK / nCube / ChartIO / Research.com / StrataScratch role explainers — `https://www.techtarget.com/...`, `https://uk.indeed.com/...`, `https://ncube.com/...`, `https://chartio.com/...`, `https://research.com/advice/...` — Supports: engineer vs analyst vs scientist boundaries. **[F as consensus secondary]**
* Research-analyst definers — `https://www.theguardian.com/careers/...`, `http://investopedia.com/terms/r/research-analyst.asp`, `https://www.indeed.com/hire/job-description/research-analyst`, `https://www.h2kinfosys.com/blog/research-analyst-vs-data-analyst`, `https://www.itjobswatch.co.uk/jobs/uk/research%20analyst.do` — Supports: external/unstructured + reports vs internal/structured + dashboards; salary sparsity note. **[S]**
* Knowledge-engineer definers — `https://www.accenture.com/us-en/careers/jobdetails?id=ATCI-5698567...` (+3 variants), `https://edshare.soton.ac.uk/5056/1/6_-_Ontology_Engineering.pdf`, `https://www.sciencedirect.com/topics/.../knowledge-engineer` — Supports: ontology/KG/semantic/RDF/SPARQL/OWL/SHACL + Neptune, METHONTOLOGY/TOVE pitfalls. **[F postings + academic]**
* W3C PROV family — `https://www.w3.org/TR/prov-dm`, `https://www.w3.org/TR/prov-primer/`, `https://www.w3.org/ns/prov`, `http://w3.org/TR/prov-overview`, `https://msi.dublincore.org/standards/prov` — Supports: Entity/Activity/Agent, PROV-O/N/XML, 2013 RECs, domain-neutral lineage. **[F]**
* PRISMA family — `https://www.bmj.com/content/339/bmj.b2535`, `https://www.bmj.com/content/372/bmj.n71`, `https://www.bmj.com/content/372/bmj.n160`, `https://resources.equator-network.org/reporting-guidelines/prisma`, `https://pmc.ncbi.nlm.nih.gov/articles/PMC4320440` — Supports: 27-item + flow, PRISMA-P 17-item, 2020 update, not a quality tool. **[F]**
* BI comparators — `https://www.metabase.com/lp/metabase-vs-superset`, `https://www.metabase.com/blog/metabase-alternatives`, `https://www.appaca.ai/compare/superset-vs-metabase`, `https://querio.ai/articles/...`, `https://valiotti.com/...`, `https://blog.elest.io/...` — Supports: Metabase ease/1-container/no-code/Metabot vs Superset SQL/viz breadth/ops load; both OSS; Preset paid. **[S, vendor-biased — triangulated with G2/Appaca/Querio]**
* Observable + Plot — `https://observablehq.com/documentation/notebooks`, `https://observablehq.com/plot/getting-started`, `https://github.com/observablehq/plot/blob/main/README.md`, `https://github.com/juba/pyobsplot` — Supports: reactive notebooks, Plot grammar, Inputs, imports/history, pyobsplot Arrow bridge. **[F]**
* Neo4j vector/graph/GraphRAG — `https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/`, `https://neo4j.com/developer/genai-ecosystem/vector-search`, `https://neo4j.com/docs/genai/tutorials/current/embeddings-vector-indexes/`, `http://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_rag.html`, `https://neo4j.com/press-releases/neo4j-vector-search` — Supports: HNSW vector index dims/cosine, Cypher 25 SEARCH, hybrid/Text2Cypher retrievers. **[F]**
* Extraction products — `https://docs.unstructured.io/api-reference/workflow/nodes/enhancement/extract-llm.md`, `https://docs.unstructured.io/concepts/structured-data-extractor/...`, `https://unstructured.io/blog/introducing-extract`, `https://developers.llamaindex.ai/llamaparse/extract`, `https://www.llamaindex.ai/services/...` — Supports: LLM vs Regex, OpenAI Structured Outputs ≤10 depth, layout/tables/citations/confidence, bulk API. **[F]**
* Agent frameworks — `https://www.langchain.com/langgraph`, `https://www.langchain.com/resources/langchain-vs-autogen`, `https://www.langchain.com/resources/langgraph-vs-temporal`, `http://n-ix.com/langgraph-vs-crewai-vs-autogen`, `https://www.meta-intelligence.tech/en/insight-ai-agent-frameworks`, `https://app.ailog.fr/en/blog/guides/agent-frameworks-comparison-2026`, `https://developer.ibm.com/articles/...` — Supports: graph vs roles vs conversations, memory/HITL/streaming/evals, AutoGen maintenance + MAF 1.0 GA, token/latency anecdotes. **[F for LangGraph primitives; S for comparisons/dates — cross-checked N-IX + LangChain]**
* Agent failures — `https://arxiv.org/abs/2601.22984` (+v1/v2 HTML/PDF, DeepHalluBench PING/PIES), `https://cdn-dynmedia-1.microsoft.com/.../Taxonomy-of-Failure-Modes...v2-0.pdf`, `https://www.microsoft.com/en-us/security/blog/2025/04/24/...`, `https://builder.aws.com/content/.../why-ai-agents-fail...` — Supports: propagation/bias/noise/grounding, multiplicative hallucinations, memory poisoning, context-pointer fix, HITL bypass. **[S preprints + F vendor taxonomy; time-sensitive]**
