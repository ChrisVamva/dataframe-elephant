---
modified: 2026-09-27T15:08:56+03:00
---
# Research-to-Data Capability Atlas

### An evidence-grounded map of the research → evidence → extraction → structured data → analysis → visualization → new-research loop

_Compiled September 27, 2026. Sourced primarily from vendor documentation, comparison guides, and industry surveys published between late 2025 and September 2026. Time-sensitive claims (pricing, version numbers, market share) are marked and should be re-verified before use in data modeling of record._

---

## 1. Executive synthesis

- The workflow described in the prompt is real but not monolithic: it is at minimum three separable sub-stacks — a **document/web extraction layer** (turning unstructured sources into text/JSON), a **structured-data layer** (DuckDB/pandas/Polars/warehouses), and an **agent-orchestration layer** (LangChain, LangGraph, CrewAI, etc.) — that different vendors, roles, and products specialize in. Treating them as one undifferentiated "AI research stack" collapses real boundaries.
- **DuckDB, Polars, and pandas are not substitutes; they are complements with a settled division of labor** as of mid-2026: pandas for ecosystem compatibility and small/notebook work, Polars for transform-heavy Python pipelines, DuckDB for SQL-shaped analytics over local/columnar files — and current practice increasingly chains DuckDB (ingest/aggregate) into Polars or pandas (last-mile) over Arrow with zero-copy handoff _(reported signal, multiple independent sources)_.
- **Orchestration frameworks are converging on the graph/asset model.** LangGraph, Dagster's asset model, and Airflow 3's new asset-aware scheduling all reflect a shift from "chain of steps" to "declared state with dependencies," which is the same conceptual move happening independently in agent orchestration and in data-pipeline orchestration _(inference, drawn from parallel patterns across two otherwise separate ecosystems)_.
- **The document-extraction market has stratified by document difficulty**, not just by brand: legacy cloud OCR (AWS Textract, Azure Document Intelligence, Google Document AI) for well-integrated, moderate-complexity documents; RAG-native parsers (LlamaParse, Unstructured) for retrieval pipelines; and a newer "agentic/grounded extraction" tier (Reducto, Nutrient, LandingAI ADE) for high-complexity, schema-shaped, audit-grade extraction with confidence scores and citations _(documented pattern across five independent vendor-comparison sources)_.
- **Knowledge graphs and vector databases are not competing technologies but different layers of the same retrieval stack.** Vector search finds semantically similar chunks; knowledge graphs add explicit relationships, provenance, and (for RDF-based systems) formal reasoning. Industry reporting connects the current push toward knowledge-graph-backed retrieval ("GraphRAG") to accuracy gains over pure vector retrieval, though the specific improvement figures come from a single vendor (Graphwise) and should be treated as a vendor claim, not an independent benchmark.
- **Market-position labels ("data analyst," "research analyst," "research engineer," "knowledge engineer," "information architect") do not map cleanly onto workflow stages.** Data analyst and data scientist definitions are converging in marketing content but remain distinct in practice: analysts interpret existing/historical data and communicate to the business; scientists build predictive/ML systems. Research engineer is a distinct, smaller, more engineering-heavy role historically concentrated at large labs, implementing what research scientists design. Knowledge engineer and information architect are older, ontology/taxonomy-focused titles now being pulled back into currency by knowledge-graph and AI-context work.
- **Agent orchestration frameworks are in the middle of a consolidation/re-labeling cycle.** Microsoft AutoGen entered maintenance mode in favor of "Microsoft Agent Framework 1.0" (which merges AutoGen's agent abstractions with Semantic Kernel's enterprise features). LangGraph is reported to have overtaken CrewAI in enterprise adoption during early 2026. This means any entity model built today should version-tag agent-framework claims rather than treat them as stable facts.
- **The orchestration and provenance layers are less mature than the extraction and analysis layers.** OpenLineage is emerging as a shared lineage standard across orchestrators (Airflow, Dagster both emit or support it), but lineage/provenance tooling is still fragmented and mostly bolted onto pipeline orchestrators rather than treated as a first-class layer of its own.
- **Deep-research agent products (Perplexity, ChatGPT Deep Research, Claude, Elicit, Consensus) split along a hard line between general web synthesis and peer-reviewed literature review.** Elicit and Consensus specialize in structured extraction from academic corpora (138M–250M+ papers, reported by the vendors); Perplexity and ChatGPT Deep Research specialize in fast, broad, cited web synthesis. This is a genuine capability boundary, not just brand positioning.
- **Open questions worth flagging for the next investigation pass:** (1) how MCP (Model Context Protocol) is reshaping the boundary between "agent framework" and "data/tool integration layer" — it appears repeatedly across both agent-framework and knowledge-graph sources as connective tissue; (2) whether "agentic extraction" (Reducto-style) is a durable category or a temporary label that folds back into either OCR platforms or agent frameworks; (3) actual (not vendor-reported) accuracy deltas between GraphRAG and vector-only RAG.

---

## 2. Lens findings

### 2.1 Skills

**Definition and scope.** The skill set spans two historically separate traditions: (a) library/information-science skills — research synthesis, information extraction, ontology design, provenance — and (b) data/software-engineering skills — SQL, DuckDB, pandas/Polars, pipeline orchestration, agent orchestration. The research-to-data workflow requires both, which is part of why no single job title covers it end-to-end.

**Core capabilities.**

- _Research synthesis_ — reading, comparing, and reconciling multiple sources into a coherent claim set with attached confidence.
- _Information extraction_ — pulling structured fields (entities, relationships, facts) out of unstructured text, PDFs, web pages, or images.
- _Data modeling / ontology design_ — defining the entities, attributes, and relationships that a domain will be represented by, at two very different levels of formality (a loose star-schema/table design vs. a formal RDF/OWL ontology with inference rules).
- _Normalization_ — reconciling inconsistent representations of the same entity or unit across sources (deduplication, entity resolution, unit/format standardization).
- _SQL / DuckDB / pandas / Polars_ — the practical query-and-transform layer; current guidance treats these as complementary rather than competing skills, with SQL (via DuckDB) as the layer of choice when data is file-resident and query-shaped, and DataFrame libraries (Polars, pandas) as the layer of choice for expression-heavy, row-wise, or ML-adjacent transforms.
- _Visualization_ — encoding structured/aggregated data into charts, dashboards, or narrative graphics for interpretation.
- _Provenance_ — recording where each claim or data point came from, with enough metadata (source, date, confidence, extraction method) to support later verification or falsification.
- _Agent orchestration_ — designing and operating multi-step, multi-tool LLM-driven workflows, including state management, tool calling, and failure handling.

**Position in workflow:** skills span every stage; they are the "how" that sits underneath every other lens.

**Evidence confidence:** high for the skill definitions themselves (well-documented in tool docs and comparison guides); medium for how these skills bundle into job titles, which is contested and shifting (see §2.2).

---

### 2.2 Market positions

**Definition and scope.** Distinct professional titles that combine different subsets of the skills above, aimed at different organizational outputs. Titles are not standardized across companies, so the same title can mean different things at different organizations — this is itself a documented pattern in career-guidance sources, not just an assumption.

|Position|Primary focus|Typical outputs|Distinguishing note|
|---|---|---|---|
|**Data analyst**|Understanding and interpreting existing/historical data; connecting data to business questions|Reports, dashboards, ad-hoc analyses|Descriptive/diagnostic more than predictive; the role most exposed to AI-driven task automation for routine SQL/reporting work, per multiple 2026 labor-market sources|
|**Data scientist**|Statistical modeling, prediction, experimentation|Predictive models, forecasts, experiment results, recommendation systems|Distinguished from analyst by asking "what will happen" rather than "what happened"|
|**Data engineer**|Building and operating the pipelines/infrastructure that move and store data|Data pipelines, warehouses, ETL/ELT jobs|Infrastructure-facing; a prerequisite for the analyst/scientist roles to have usable data|
|**Data architect**|Designing the blueprint for how data systems fit together|Data models, warehouse/lake designs, governance frameworks|Broader and more design-oriented than data engineer; overlaps with information architect on the modeling side|
|**Research analyst**|Synthesizing external research (market, competitive, academic) into structured findings|Research briefs, comparative analyses|Distinct from data analyst in that source material is often unstructured/external rather than an internal warehouse|
|**Research engineer**|Implementing and optimizing the algorithms research scientists design|Optimized ML implementations, computational platforms|Historically concentrated at large tech companies and specialized AI labs; is "to research scientist" what "data engineer is to data scientist," per a widely used analogy in career-guidance writing|
|**Knowledge engineer**|Designing and maintaining ontologies, taxonomies, and knowledge representations|Ontologies, RDF/OWL schemas, semantic layers|An older discipline (predates the current AI wave) now being pulled back into demand by knowledge-graph and GraphRAG work; vendor material explicitly targets this title (e.g., Ontotext is positioned for "knowledge engineers")|
|**Information architect**|Organizing information structures for usability/findability|Site/taxonomy structures, content models|Historically a UX/library-science-adjacent title; its boundary with "systems analyst" or "data architect" has been debated for at least two decades (a 2006 mailing-list thread on exactly this question still surfaces in search results, suggesting the boundary problem is long-standing rather than new)|
|**Automation / AI-agent workflow specialist**|Designing and operating agentic and no-code automation (n8n, Zapier, agent frameworks)|Automated workflows, agent pipelines|An emergent title without a settled definition yet; overlaps heavily with both data engineer and agent-orchestration skills|

**Evidence confidence:** high for data analyst/scientist/engineer distinctions (well-documented, converging descriptions across many sources); medium for research engineer, knowledge engineer, and information architect (fewer, less standardized sources; title usage varies by company).

**Labor-market signal (reported, time-sensitive):** By late 2025, more than 1 in 25 job postings referenced AI, and nearly 45% of data/analytics postings contained AI-related terms, per Indeed Hiring Lab data cited in a 2026 career-advice source. The same source reports entry-level data-analyst roles as saturated while senior, AI-augmented analysts who can design experiments and orchestrate AI tools are in stronger demand — a bifurcation pattern, not a uniform decline. U.S. Bureau of Labor Statistics projections cited across multiple sources put data-analyst-category growth around 23% through 2032, well above average — though these projections predate the most recent wave of AI-driven task automation and should be treated as directional rather than current.

---

### 2.3 Technology

**Definition and scope.** The underlying technical building blocks — languages, protocols, and data formats — that the software layer (§2.4) is built on.

- **Python** — the dominant language across the whole workflow; every major library and agent framework surveyed (pandas, Polars, LangChain, CrewAI, LlamaIndex) is Python-first, with some (Polars, DuckDB) implemented in Rust/C++ for performance and exposed via Python bindings.
- **SQL** — the query language for DuckDB and for most warehouses; treated as a durable, portable skill that both DataFrame libraries and orchestration tools are increasingly built to interoperate with rather than replace.
- **DuckDB** — an embedded, in-process, columnar OLAP SQL engine; positioned as "SQLite for analytics." Runs without a server, queries Parquet/CSV/JSON files directly, and spills to disk when data exceeds memory.
- **pandas** — an eager, single-threaded, NumPy/Arrow-backed DataFrame library; the ecosystem default with the largest number of compatible downstream libraries, but memory-bound and prone to out-of-memory failure on large datasets.
- **APIs / scraping / browser automation** — the acquisition layer for external evidence; tools here range from simple HTTP scraping (Firecrawl, Apify, Bright Data) to full browser automation for JavaScript-heavy or authenticated sources.
- **LLMs** — used both as extraction engines (turning unstructured text into structured fields) and as orchestration "brains" inside agent frameworks.
- **Embeddings** — numerical vector representations of text/image/audio used for semantic similarity search; the foundation of both RAG pipelines and vector databases.
- **Graph technologies** — property graphs (Neo4j-style, queried with Cypher/openCypher) and RDF/OWL graphs (Stardog/Ontotext-style, queried with SPARQL); these are architecturally distinct, not just branding differences — property graphs prioritize traversal performance, RDF graphs prioritize standards-based semantic reasoning.
- **Data formats** — Parquet and Arrow are the two formats repeatedly cited as enabling "zero-copy" handoff between DuckDB, Polars, and pandas; CSV/JSON remain common ingestion formats despite being less efficient.
- **Databases** — spans embedded analytical engines (DuckDB), traditional warehouses (Snowflake, Databricks, referenced but not deep-dived in this pass), graph databases (Neo4j, Amazon Neptune, TigerGraph), RDF triple stores (Stardog, Ontotext GraphDB), and vector databases (Pinecone, Weaviate, Qdrant, Milvus, pgvector).

**Evidence confidence:** high — this lens is the most consistently and specifically documented across sources.

---

### 2.4 Software

**Definition and scope.** Named, installable/purchasable implementations of the technology layer.

**Local analytical engines (pandas / Polars / DuckDB).** As of mid-2026 releases (DuckDB 1.5.4, June 17 2026; Polars 1.42.1, June 30 2026, per one engineering-lead source), the settled practitioner guidance is: use DuckDB when the team thinks in SQL and data lives in files; use Polars when the pipeline is a long chain of Python joins/group-bys/expressions; use pandas when the dataset is small, the team already knows pandas, or downstream libraries expect a pandas DataFrame. Multiple independent sources converge on this same three-way split, which raises confidence that it reflects genuine practitioner consensus rather than one vendor's framing.

**Transformation and orchestration (dbt, Airflow, Dagster, Prefect, Mage, Temporal, Flyte).**

- **dbt** — SQL-based data _transformation_ (not orchestration); positioned against Metabase not as a competitor but as a different layer (dbt transforms in-warehouse, Metabase visualizes).
- **Airflow** — the incumbent, task-based orchestrator with the largest ecosystem and hiring pool; Airflow 3 (2025) added asset-aware scheduling, narrowing its historical gap with Dagster's asset model.
- **Dagster** — asset-based orchestration (declares _what data exists_, not just _what task ran_), with first-class lineage, testing, and dbt integration; favored for greenfield, dbt-centric analytics teams.
- **Prefect** — Python-native, decorator-based flows with less orchestration boilerplate than Airflow; favored for simplicity and fast iteration by smaller/solo teams.
- **Mage** — notebook-centric orchestration, positioned as a third philosophy alongside Airflow's task-centrism and Dagster's asset-centrism.
- **Temporal / Flyte** — targeted less at batch ETL and more at long-running, fault-tolerant, or GPU-heavy/agentic workloads; Temporal in particular is positioned for workflows that must survive crashes rather than nightly batch jobs.

**BI / visualization (Metabase, Apache Superset, Redash, Lightdash, Observable, Evidence, Grafana).** Reported 2026 market data (a Dresner Advisory Services survey cited in two independent blog sources) puts open-source BI usage at 41% of organizations in production, up from 28% in 2022 — treat this figure as a reported signal from a single underlying survey, since it is cited (not independently re-derived) by both secondary sources. Within open-source BI:

- **Metabase** — easiest to self-host, aimed at non-technical business users; open-core (AGPL community edition, paid Pro/Enterprise for sandboxing, advanced caching, audit logs).
- **Apache Superset** — the more powerful, technical option; fully Apache 2.0 with no open-core gating, used at Airbnb, Dropbox, and (variously reported) Twitter/Lyft; requires more operational overhead (Python app + metadata DB + Redis + Celery workers).
- **Redash** — in maintenance mode since its acquisition by Databricks; multiple sources describe it as a legacy option rather than an active recommendation.
- **Lightdash** — positioned as the default BI layer specifically for dbt-native teams, i.e., BI tightly coupled to the transformation layer rather than a general-purpose tool.
- **Observable / Evidence** — code-first, git-versioned approaches aimed at developer-led dashboards rather than business-user self-service.

**Agent/orchestration frameworks** — see §2.9 (Agents), which covers this in depth since the lens overlaps almost entirely with the Agents lens.

**Knowledge graph software** — see §2.6/2.9 overlap notes; core players are Neo4j (property graph, Cypher, largest ecosystem, no native RDF/OWL — added via the neosemantics/n10s plugin), Amazon Neptune (managed, supports Gremlin/SPARQL/openCypher against the same data), Stardog (RDF/SPARQL with OWL reasoning and virtual-graph federation), Ontotext GraphDB (RDF-centric, positioned for "knowledge engineers," strong inference), and TigerGraph.

**Document/web extraction software** — see §2.6 (Products) for the fuller comparison; core players are Unstructured, LlamaParse/LlamaExtract, Reducto, Docling (open-source), Mistral OCR, Firecrawl, Apify, Bright Data, and the three hyperscaler OCR APIs (AWS Textract, Azure Document Intelligence, Google Document AI).

**Evidence confidence:** high for the DuckDB/Polars/pandas and orchestrator comparisons (many independent, converging sources); medium for BI market-share figures (traced back to one survey cited secondhand).

---

### 2.5 Companies

**Definition and scope.** Organizations that build, sell, or hire around research-to-data capabilities. Not deeply investigated in this pass beyond what surfaced incidentally in product/software research; flagged here as a gap for the next investigation (see §6).

**Observed from this pass (incidental, not exhaustive):**

- _Open-source foundations / stewards_: Apache Software Foundation (Superset, Airflow); this governance model is repeatedly cited as a trust signal in BI/orchestrator comparisons (no open-core paywall).
- _Vendor-led open-core companies_: Metabase Inc. (Metabase), dbt Labs (dbt), Astronomer (managed Airflow/"Astro"), Dagster Labs / Elementl (Dagster), Prefect (Prefect).
- _Knowledge-graph vendors_: Neo4j Inc. (recently reported, per a five-day-old Hacker News/Register item surfaced in search results, to have acquired GraphAware — reported as a move toward an intelligence-analysis product positioned against Palantir Gotham; this is a recent, single-sourced claim and should be verified directly before treating as fact), Stardog, Ontotext/Graphwise, TigerGraph, Palantir (Foundry).
- _Document-extraction vendors_: Reducto, Unstructured, LlamaIndex (LlamaParse/LlamaExtract), Nutrient, Mistral (OCR), the three hyperscalers (AWS, Microsoft/Azure, Google).
- _Deep-research / literature-review vendors_: Elicit, Consensus, Perplexity, OpenAI (ChatGPT Deep Research), Anthropic (Claude), Google (Gemini + NotebookLM), Scite, ResearchRabbit.
- _Vector database vendors_: Pinecone, Weaviate, Qdrant, Zilliz (Milvus), Chroma, Turbopuffer, plus PostgreSQL's pgvector extension as an incumbent-infrastructure alternative to a dedicated vector database.

**Evidence confidence:** low-to-medium — this lens was assembled from product research rather than dedicated company-level investigation (hiring signals, funding, org structure). Flagged as the weakest-covered lens in this pass.

---

### 2.6 Products

**Definition and scope.** Named, purchasable/usable systems that occupy a specific position in the workflow.

**Document/web extraction tier (feeds "Extraction" and "Evidence" stages):**

|Product|Best for|Differentiator|
|---|---|---|
|Reducto|Complex documents, production RAG, audit-grade extraction|Multi-pass, agentic extraction with citations, confidence scores, private/air-gapped deployment|
|LlamaParse / LlamaExtract|LlamaIndex-centered RAG stacks|Converts documents to clean markdown for embedding; LlamaExtract maps documents to a caller-defined JSON schema|
|Unstructured|Connector-rich enterprise ingestion pipelines|Partitioning/chunking focus; open-source library plus managed platform|
|Docling|Local control / open-source / self-hosted workflows|No managed-service dependency|
|Mistral OCR|Multilingual OCR|Cost-transparent, structure-preserving output|
|Nutrient Data Extraction API|Schema-shaped results needing per-field confidence and bounding-box grounding|Positioned as not relying on vision-language models for its extraction mode, for repeatability|
|Amazon Textract / Azure Document Intelligence / Google Document AI|Teams already committed to that cloud|Deepest integration with the rest of that cloud's data stack|
|Firecrawl / Apify / Bright Data|Web (not document) extraction at scale|LLM-ready web content, proxy networks, reusable scraper marketplaces|
|Diffbot|Knowledge-graph-oriented web extraction|Entity understanding layered onto web scraping|

**Knowledge/graph products (feed "Structured representation," "Normalization," "Database," and reasoning-heavy "Analysis"):**

|Product|Modeling approach|Primary use case|
|---|---|---|
|Neo4j|Property graph, Cypher/openCypher|Developer-led graph projects; largest tooling ecosystem; recently expanding into an "agentic brain"/enterprise-knowledge-layer positioning for AI agents|
|Amazon Neptune|Property graph, managed|AWS-committed teams; uniquely answers Gremlin, SPARQL, and openCypher against the same data|
|Stardog|RDF/SPARQL, OWL reasoning|Standards-driven semantic modeling; virtual-graph federation over relational sources without an ETL step|
|Ontotext GraphDB / Graphwise|RDF, real-time inference|Reasoning-heavy RDF work; vendor-reported accuracy gains for GraphRAG over pure vector retrieval|
|TigerGraph|Property graph|High-scale graph analytics|
|Palantir Foundry|Proprietary ontology|Regulated, operational enterprise workflows|

**Deep-research / literature products (feed "Research" and "New research" stages):**

|Product|Corpus / index|Distinguishing behavior|
|---|---|---|
|Perplexity (Pro)|Real-time web index|Fast, cited, general-purpose web synthesis; a large number of "deep research" runs per day on its paid tier|
|ChatGPT Deep Research|Web + curated sources|Longer, deeper multi-step reports; browses on the order of dozens to 100 sources per query, per one comparison source|
|Claude|Uploaded documents + reasoning|Positioned by comparison sources as strongest at synthesis/reasoning over messy or conflicting sources, rather than breadth of web coverage|
|Elicit|Semantic Scholar + academic databases (~138M+ papers, vendor-reported)|Structures papers into a comparable table (methods, sample size, results) rather than prose — a genuinely distinct output shape from the other tools in this table|
|Consensus|200M–250M+ peer-reviewed papers (vendor-reported)|"Consensus meter" answering yes/no or degree-of-agreement questions against the literature|
|Gemini + NotebookLM|User's own documents (grounded)|Best fit for teams already in Google Workspace who want answers grounded in their own corpus|
|Scite|Citation graph|Classifies citations as supporting vs. contrasting a claim, rather than just counting them|
|ResearchRabbit|Citation graph|Visual paper discovery via citation-network maps|

**Vector database products (feed "Database" and semantic "Query"):** Pinecone (fully managed, zero-ops), Weaviate (hybrid vector+keyword search), Milvus/Zilliz (enterprise scale, billions of vectors), Qdrant (Rust-based performance, strong filtered search, reported as steadily gaining share against Pinecone on cost/features), Chroma (developer-friendly prototyping), pgvector (Postgres extension — repeatedly described across sources as the "boring winner" for teams already on Postgres and under roughly tens of millions of vectors), Turbopuffer (object-storage-backed, cheaper at large corpus size at some latency cost).

**Evidence confidence:** high for the document-extraction and vector-database comparisons (many independent, converging vendor-neutral sources); medium for the deep-research product comparisons (heavier reliance on vendor-reported corpus sizes and a smaller number of independent evaluators); medium for knowledge-graph products (strong on architecture, weaker on independently verified performance claims).

---

### 2.7 Methodologies

**Definition and scope.** Repeatable procedures that govern how a workflow stage is carried out, independent of which specific tool executes it.

- **ETL vs. ELT** — Extract-Transform-Load (transform before loading, historically necessary when storage/compute was expensive) vs. Extract-Load-Transform (load raw data first, transform inside the warehouse/engine — enabled by cheap columnar storage and engines like DuckDB/Snowflake). The DuckDB/Polars/pandas material above implicitly assumes an ELT-style pattern: land files, then query/transform in place.
- **Data modeling** — defining schemas (star/snowflake schemas for warehouses, or entity-relationship models) that structured data will conform to before or during load.
- **Ontology design** — the more formal, RDF/OWL-flavored sibling of data modeling, used where reasoning/inference over relationships (not just storage and lookup) is required.
- **Information extraction methodology** — ranges from rule-based/regex extraction (older, brittle, but fully auditable) to LLM-based extraction (flexible, handles unstructured layouts, but requires confidence scoring and human review to be trustworthy) to hybrid "agentic extraction" (LLM-driven multi-pass extraction with citation/grounding back to source text, the category Reducto and similar vendors are pushing).
- **Evidence and provenance systems** — methodologies for attaching source, date, extraction method, and confidence to every claim so it can later be traced back and re-verified or falsified; OpenLineage is the closest thing to a shared standard surfaced in this research, though it is scoped to pipeline lineage (which job produced which table) rather than claim-level provenance (which sentence in which source supports which fact).
- **Analytical workflow methodology** — the general pattern of query → aggregate → visualize → interpret, implemented differently depending on whether the team is SQL-first (DuckDB/warehouse) or DataFrame-first (Polars/pandas/notebooks).

**Position in workflow:** methodologies govern (in the sense used by the prompt's relationship vocabulary) the Workflow stages; they are the codified "right way to do it" that sits above individual tool choice.

**Evidence confidence:** medium — ETL/ELT and data modeling are well-established and stable; "agentic extraction" as a named methodology is newer (documented primarily in 2026 vendor-comparison content) and its terminology may not stabilize.

---

### 2.8 Workflows

**Definition and scope.** The end-to-end process the whole atlas is organized around. Stage-by-stage detail is given in §3 (Workflow map) rather than repeated here to avoid duplication.

**Relationship to other lenses:** a workflow _uses_ technologies, is _governed by_ methodologies, is _performed by_ agents and market positions, and _appears in_ job postings and product marketing as the thing being automated or accelerated.

---

### 2.9 Agents

**Definition and scope.** Software (often LLM-driven) that autonomously or semi-autonomously performs one or more workflow stages, typically by calling tools and maintaining some form of state across steps.

**Frameworks, compared on architecture and current status (all claims here are version/time-sensitive; treat as a 2026 snapshot):**

|Framework|Core model|Best-fit use case|Status note|
|---|---|---|---|
|LangChain / LangGraph|Chains/graphs of LLM calls, tool calls, and memory retrievals; LangGraph adds stateful, cyclical, node-and-edge orchestration|Broad orchestration flexibility; LangGraph specifically for agents that must survive restarts, branch conditionally, or roll back|Reported to have surpassed CrewAI in enterprise adoption in early 2026, driven by demand for state persistence and conditional routing|
|CrewAI|Role-based multi-agent coordination|Fast prototyping of structured, role-based agent teams|Lightweight, independent of LangChain|
|Microsoft AutoGen → Microsoft Agent Framework|Conversational, multi-agent-as-conversation model|Human-in-the-loop workflows; enterprise Microsoft/.NET/Azure stacks|AutoGen entered Microsoft-declared maintenance mode October 2, 2025; new work is directed to Agent Framework 1.0, which merges AutoGen's agent abstractions with Semantic Kernel's enterprise features (session state, type safety, middleware, telemetry) plus graph-based multi-agent orchestration|
|LlamaIndex (Workflows)|Data/retrieval-centered agent framework|Agents that must reason across large document collections spanning vector indexes, SQL, and APIs simultaneously|Evolved from a pure data/RAG framework into a fuller agent framework|
|OpenAI Agents SDK / Swarm|Lightweight agent primitives from the model vendor|Teams standardized on OpenAI models wanting minimal-abstraction agent code|Swarm is described in multiple sources as an earlier, simpler predecessor pattern|
|Google ADK|Google's agent development kit|Teams on Google Cloud / Gemini|Newer entrant in 2026 comparison guides|
|Mastra|JS/TS-oriented agent framework|Teams building agent products in a JavaScript/TypeScript stack|Appears in 2026 "best of" comparisons alongside the Python-first frameworks|
|Semantic Kernel|Enterprise, strongly typed, Microsoft/.NET-aligned|Large enterprise teams on the Microsoft stack needing long-term support|Explicitly described as carrying more setup overhead than CrewAI/Mastra — a real cost, not just enterprise polish|
|n8n / Zapier|Low-code/no-code automation platforms rather than developer frameworks|Business-process automation, often the "last mile" connecting agent output to real-world actions (webhooks, SaaS actions)|Function as an automation layer that agent frameworks increasingly integrate with (e.g., via MCP bridges), not a competing agent-reasoning layer|
|Model Context Protocol (MCP)|An open protocol (not a framework) for connecting agents to tools/data|Cross-framework interoperability — appeared as connective tissue across nearly every agent-framework and knowledge-graph source surveyed|Increasingly treated as the interoperability layer that lets an agent built in one framework call tools/servers built for another|

**Types of agents in the workflow (by task, drawing on the prompt's own taxonomy plus what the research surfaced):**

- _Research agents_ — Perplexity, ChatGPT Deep Research, Claude's research mode, Elicit, Consensus (see §2.6). Required tools/state: web or literature search access, source tracking, synthesis memory across sources. Verification: citation checking against the original source. Failure mode: citation drift/hallucinated sources, especially reported to worsen on niche technical topics.
- _Extraction agents_ — the "agentic extraction" tier of document tools (Reducto and comparable products), which use multi-pass LLM extraction with citations back to source text/bounding boxes as their verification mechanism. Failure mode: incomplete extraction on very long, visually irregular, or schema-heavy documents — the dimension one 2026 benchmark (LongExtractionBench, reported as released by micro1 in June 2026) was specifically designed to test.
- _Coding/data-cleaning agents_ — increasingly built inside orchestration frameworks (LangGraph, Dagster/Airflow combined with LLM steps) rather than as a separate named product category in the sources surveyed; this is a gap worth a dedicated follow-up search.
- _Analytical agents_ — agents that write and execute SQL/DataFrame code against DuckDB/Polars/pandas to answer a question; the vector-database and BI product comparisons hint at this pattern (natural-language-to-SQL features appearing across BI tools) but it wasn't independently deep-dived in this pass.
- _Coordinating/orchestration agents_ — the explicit purpose of LangGraph, CrewAI, and Microsoft Agent Framework; these manage handoffs between the other agent types and maintain overall workflow state.

**Evidence confidence:** high for the framework landscape and its current consolidation trend (many independent, converging 2026 sources); medium for the extraction/coding/analytical agent sub-categories (inferred from adjacent product research rather than dedicated agent-taxonomy sources — flagged as a research gap in §6).

---

## 3. Workflow map

|Stage|Inputs|Activities|Outputs|Quality checks|Likely tools|Suitable agent roles|
|---|---|---|---|---|---|---|
|**Research**|A question or topic|Searching web/literature, scoping the question|Candidate source list|Source diversity, primary-vs-secondary check|Perplexity, ChatGPT Deep Research, Elicit, Consensus, Claude|Research agent|
|**Evidence**|Candidate sources|Reading, evaluating credibility, deciding what to keep|Selected source set with credibility notes|Independent-source cross-check for load-bearing claims|Scite, ResearchRabbit, manual review|Research agent, human analyst|
|**Extraction**|Selected sources (PDFs, web pages, papers)|Pulling text/fields/tables out of unstructured or semi-structured sources|Raw structured/semi-structured records|Confidence scores, source grounding/citations, completeness rate on long documents|Reducto, LlamaParse/LlamaExtract, Unstructured, Docling, Mistral OCR, Firecrawl|Extraction agent|
|**Structured representation**|Raw extracted records|Mapping extracted fields to a defined schema or ontology|Schema-conformant records|Schema validation, entity typing consistency|JSON Schema, RDF/OWL ontologies, pandas/Polars DataFrames|Extraction agent, knowledge engineer|
|**Normalization**|Schema-conformant but inconsistent records|Deduplication, entity resolution, unit/format standardization|Canonicalized records|Duplicate rate, entity-resolution precision/recall|dbt, Polars/pandas transforms, entity-resolution tools (e.g., Tamr, per knowledge-graph research)|Data-cleaning agent, data engineer|
|**Database**|Canonicalized records|Loading into a queryable store|Populated database|Load completeness, referential integrity|DuckDB, warehouses (Snowflake/Databricks), Neo4j/Stardog/GraphDB (graph), Pinecone/Weaviate/Qdrant/pgvector (vector)|Data engineer|
|**Query**|Populated database, an analytical question|Writing SQL/Cypher/SPARQL/DataFrame queries|Query result sets|Query correctness against a known-answer test case|DuckDB SQL, Cypher, SPARQL, Polars/pandas expressions|Analytical agent, data/research analyst|
|**Analysis**|Query results|Statistical summarization, comparison, pattern-finding|Findings with supporting numbers|Sanity checks against source data, statistical validity|pandas/Polars/DuckDB, dbt models, notebooks|Data/research analyst, data scientist|
|**Visualization**|Findings|Encoding findings into charts/dashboards|Charts, dashboards, narrative graphics|Does the chart type match the claim being made; is the axis/scale honest|Metabase, Apache Superset, Lightdash, Observable, Evidence|Data/BI analyst|
|**Interpretation**|Visualized findings|Drawing conclusions, flagging uncertainty and disagreement|Interpreted findings with confidence/uncertainty notes|Are claims properly separated from interpretation (documented fact vs. inference)|Human judgment, LLM-assisted synthesis|Research analyst, human reviewer|
|**New research**|Interpreted findings, open questions|Identifying what's still unresolved and what to investigate next|A refined research question|Are the new questions actually answerable with available sources|—|Research agent, human analyst|
|**Agent iteration**|The whole prior cycle's outputs and gaps|Adjusting agent prompts, tool sets, or workflow structure based on what worked/failed|An updated agent/workflow configuration|Regression check against prior known-good runs|LangGraph/CrewAI/Agent Framework configuration, evals (e.g., LangSmith)|Coordinating/orchestration agent, AI-agent-workflow specialist|

---

## 4. Entity and relationship candidates

|Entity|Name|Definition|Workflow stage|Related entities|Relationship type|Evidence|Confidence|
|---|---|---|---|---|---|---|---|
|Technology|DuckDB|Embedded, in-process columnar SQL OLAP engine|Database, Query|Software: DuckDB; Technology: SQL, Parquet|implemented_by|MotherDuck, danilchenko.dev, multiple comparison sources|High|
|Technology|Polars|Rust-backed, multi-threaded, lazy-evaluated DataFrame library|Structured representation, Normalization, Analysis|Technology: Arrow; Software: pandas, DuckDB|uses (Arrow)|Wikipedia, Chat2DB, danilchenko.dev|High|
|Software|pandas|Eager, single-threaded, NumPy/Arrow-backed DataFrame library|Structured representation, Normalization, Analysis|Technology: Python; Software: Polars, DuckDB|implemented_by|Analytics Vidhya, CodeCut, MotherDuck|High|
|Methodology|ETL/ELT|Ordering of extract/transform/load steps|Extraction, Normalization, Database|Software: dbt, Airflow, Dagster|governs|General industry usage; dbt-vs-Metabase comparison|High|
|Software|dbt|SQL-based in-warehouse data transformation tool|Normalization|Software: Metabase, Lightdash; Company: dbt Labs|appears_in (workflow)|toolradar dbt-vs-Metabase comparison|High|
|Software|Apache Airflow|Task-based (with asset-aware scheduling as of v3) pipeline orchestrator|Workflow (orchestration)|Software: OpenLineage, Dagster; Company: Apache Software Foundation, Astronomer|uses (OpenLineage)|Astronomer Airflow-vs-Dagster, datavidhya orchestrator comparisons|High|
|Software|Dagster|Asset-based pipeline orchestrator|Workflow (orchestration)|Software: dbt, OpenLineage; Company: Dagster Labs|governs (Workflow)|Astronomer, datavidhya|High|
|Methodology|OpenLineage|Shared, cross-platform data-lineage emission standard|Provenance (cross-stage)|Software: Airflow, Dagster, Marquez|implemented_by|GitHub OpenLineage project page, Astronomer comparison|Medium|
|Software|Apache Superset|Fully open-source (Apache 2.0), technical/scale-oriented BI platform|Visualization|Company: Apache Software Foundation; Software: Metabase, Redash|governed_by (Apache Software Foundation)|basedash, coefficient.io, elest.io|High|
|Software|Metabase|Open-core, self-serve BI platform for non-technical users|Visualization|Company: Metabase Inc.; Software: Superset, dbt|produced_by (Metabase Inc.)|basedash, thebricks, coefficient.io|High|
|Software|Neo4j|Property-graph database, Cypher/openCypher query language|Database, Structured representation|Technology: graph technologies; Software: neosemantics/n10s plugin (for RDF)|implemented_by|Atlan knowledge-graph-vs-graph-database, futureagi enterprise KG comparison|High|
|Software|Stardog|RDF/SPARQL graph database with OWL reasoning and virtual-graph federation|Database, Analysis (reasoning)|Technology: RDF, OWL, SPARQL|implemented_by|futureagi, Atlan|Medium|
|Software|Ontotext GraphDB / Graphwise|RDF graph database, real-time inference, positioned for GraphRAG|Database, Analysis (reasoning)|Product: GraphRAG use case|supports (GraphRAG)|getgalaxy.io knowledge-graph-platforms report|Medium (vendor-adjacent source)|
|Product|Reducto|Agentic, multi-pass document extraction with citations and confidence scores|Extraction|Product: LlamaParse, Unstructured, Nutrient (alternatives)|performs (Extraction)|nutrient.io alternatives guides, reducto.ai guide, llamaindex.ai alternatives guide|High|
|Product|LlamaParse / LlamaExtract|Document parsing and schema-based extraction tied to the LlamaIndex ecosystem|Extraction, Structured representation|Company: LlamaIndex; Product: Reducto (alternative)|performs (Extraction)|nutrient.io, dev.thedrive.ai|High|
|Product|Unstructured|Connector-rich document partitioning/chunking for RAG ingestion|Extraction|Product: Reducto, LlamaParse (alternatives)|performs (Extraction)|extend.ai review, nutrient.io|High|
|Product|Elicit|Structured, tabular extraction from academic literature (Semantic Scholar-backed)|Research, Evidence, Structured representation|Product: Consensus (comparator); Company: Elicit|performs (Research)|dupple.com, costbench.com, GWU engineering recap|High|
|Product|Consensus|Evidence-synthesis over peer-reviewed papers with a "consensus meter"|Research, Interpretation|Product: Elicit (comparator)|performs (Research)|dupple.com, costbench.com, CB Insights|High|
|Product|Perplexity (Pro)|Fast, cited, real-time web research synthesis|Research|Product: ChatGPT Deep Research, Claude (comparators)|performs (Research)|dupple.com, guptadeepak.com|High|
|Agent framework|LangGraph|Graph-based, stateful multi-agent orchestration within the LangChain ecosystem|Agent iteration, Coordinating|Framework: LangChain, CrewAI (comparators); Protocol: MCP|performs (Workflow orchestration)|langchain.com, pickaxe.co, atlan.com|High|
|Agent framework|CrewAI|Role-based multi-agent coordination framework|Agent iteration, Coordinating|Framework: LangGraph, AutoGen (comparators)|performs (Workflow orchestration)|techaheadcorp.com, langchain.com|High|
|Agent framework|Microsoft Agent Framework|Merger of AutoGen's agent abstractions and Semantic Kernel's enterprise features|Agent iteration, Coordinating|Framework: AutoGen (predecessor), Semantic Kernel|performs (Workflow orchestration)|pickaxe.co, atlan.com|Medium (recent, single-source-cluster claim about the October 2025 maintenance-mode transition)|
|Protocol|Model Context Protocol (MCP)|Open protocol connecting agents to external tools/data/servers|Agent iteration (cross-framework)|Framework: LangChain, CrewAI, n8n (all bridge to it); Software: Neo4j (MCP servers for DB access)|supports (cross-framework interoperability)|github.com/munesoft/agent, go.neo4j.com Neo4j AI keynote, iimoyjv0493b Medium piece|Medium|
|Software|Pinecone|Fully managed, serverless vector database|Database (vector)|Software: Weaviate, Qdrant, Milvus, pgvector (comparators)|implemented_by|reintech.io, groovyweb.co, codeboxr.com|High|
|Software|pgvector|PostgreSQL extension adding vector search to an existing relational database|Database (vector)|Software: Pinecone, Qdrant (comparators); Technology: PostgreSQL|implemented_by|alexcloudstar.com, encore.dev|High|
|Market position|Data analyst|Interprets existing/historical data for business decisions|Analysis, Visualization, Interpretation|Market position: Data scientist, Research analyst|appears_in (Workflow)|thedataschool.co.uk, codefinity.com, careery.pro|High|
|Market position|Data scientist|Builds predictive/statistical models|Analysis|Market position: Data analyst, Data engineer|appears_in (Workflow)|thedataschool.co.uk, interviewkickstart.com|High|
|Market position|Data engineer|Builds and operates data pipelines/infrastructure|Extraction, Normalization, Database|Market position: Data architect, Research engineer (analogy)|appears_in (Workflow)|wscubetech.com, towardsdatascience.com|High|
|Market position|Research engineer|Implements/optimizes algorithms designed by research scientists|Extraction, Analysis (implementation)|Market position: Data engineer (explicit analogy in source)|appears_in (Workflow)|towardsdatascience.com "different roles in the data ecosystem"|Medium|
|Market position|Knowledge engineer|Designs/maintains ontologies and semantic knowledge representations|Structured representation, Normalization|Product: Ontotext GraphDB (explicitly targets this title)|appears_in (Workflow)|energent.ai industry report|Medium|
|Claim|GraphRAG accuracy improvement (60%→90%+)|Vendor-reported accuracy gain from using knowledge graphs vs. vector chunks alone in RAG|Analysis, Query|Source: Graphwise; describes: Knowledge graph, GraphRAG|describes|getgalaxy.io, attributing the figure to Graphwise|Low (single-vendor-sourced statistic, not independently verified)|
|Claim|Open-source BI adoption (41% of orgs, up from 28% in 2022)|Reported share of organizations using open-source BI in production|Visualization|Source: Dresner Advisory Services 2025 survey, cited secondhand|describes|basedash.com, coefficient.io (both citing the same underlying survey)|Medium (consistent secondary citation, but not traced to the primary survey itself)|

_(This table is illustrative rather than exhaustive — a full data-modeling pass would extend it substantially, particularly for the Companies lens, which this research round under-covered; see §6.)_

---

## 5. Comparison tables

### 5.1 Local analytical engines

|Criterion|pandas|Polars|DuckDB|
|---|---|---|---|
|Execution model|Eager, single-threaded|Lazy, multi-threaded, query-optimized|SQL query engine, columnar|
|Best for|Small/medium data, notebooks, ML-library compatibility|Transform-heavy Python pipelines, expression-based logic|SQL-shaped analytics over local files, joins across files|
|Weakness|Out-of-memory on large data|Newer, smaller ecosystem than pandas|Less natural for complex row-wise/window logic than Polars' expression API|
|Interop|Arrow-based handoff to Polars/DuckDB|Arrow-native, zero-copy with DuckDB|Queries Parquet/CSV directly; Arrow handoff to Polars/pandas|

### 5.2 Pipeline orchestrators

|Criterion|Airflow|Dagster|Prefect|Mage|
|---|---|---|---|---|
|Core philosophy|Task-centric (asset-aware as of v3)|Asset-centric|Flow-centric Python|Notebook-centric|
|Ecosystem/hiring pool|Largest|Smaller, growing|Smaller|Smallest of the four|
|Lineage|Plugin-based (OpenLineage)|Built-in, first-class|Limited|Built-in|
|Best fit|Established, large-scale production platforms|Greenfield, dbt-centric analytics teams|Teams prioritizing simplicity/fast iteration|Notebook-first data-science teams|

### 5.3 Document extraction tier

|Criterion|Reducto|LlamaParse|Unstructured|Docling|Hyperscaler OCR (Textract/DI/DocAI)|
|---|---|---|---|---|---|
|Positioning|Agentic, high-fidelity extraction for hard documents|RAG-optimized parsing tied to LlamaIndex|Connector-rich ingestion/chunking|Open-source, self-hosted|Cloud-native, integrated with that cloud's broader stack|
|Output|Structured JSON with citations/confidence|Clean markdown (not structured JSON)|Partitioned/chunked text|Structured, locally processed|Forms/tables/OCR text|
|Deployment|Hosted, private VPC, air-gapped options|Managed/hosted|Open-source library + managed platform|Fully local|Cloud-only|
|Best for|Long, visually irregular, schema-heavy documents|Vector-embedding pipelines in LlamaIndex stacks|Enterprise RAG ingestion at scale|Teams wanting no managed-service dependency|Teams already committed to that cloud|

### 5.4 Deep-research / literature agents

|Criterion|Perplexity|ChatGPT Deep Research|Elicit|Consensus|
|---|---|---|---|---|
|Source base|Real-time web index|Web + curated sources|Semantic Scholar (~138M+ papers)|Peer-reviewed papers (~200–250M+)|
|Output shape|Cited prose synthesis|Long structured report|Comparable table (methods/results/sample size per paper)|"Consensus meter" plus study-level citations|
|Speed|Fast (minutes)|Slower, deeper (reported 15–30 min cycles)|Table-building over selected papers|Fast for yes/no style questions|
|Best for|General, current-events-adjacent research|Longest, most exhaustive reports|Systematic literature review|Quick scientific-consensus checks|

---

## 6. Research gaps and next investigations

- **Companies lens is under-covered.** This pass surfaced companies incidentally through product research. A dedicated pass should separate employers (who hires for these skills), vendors (who sells the tools), open-source foundations/stewards, consultancies, and research organizations, with job-posting-level evidence for hiring signals rather than career-advice-blog framing.
- **The GraphRAG accuracy claim (60%→90%+) is single-vendor-sourced (Graphwise) and should not be treated as an independent benchmark.** A useful next search: find independent (non-vendor) benchmarks comparing knowledge-graph-augmented retrieval to pure vector RAG.
- **The "agentic extraction" category (Reducto and peers) is newly named and its main independent benchmark (LongExtractionBench) is itself vendor-adjacent (reported as released by micro1, cited primarily through Reducto's own guide).** Worth tracing to the primary benchmark publication and checking for independent replication.
- **Coding/data-cleaning agents as a distinct product category were not independently found** — this pass only inferred their existence from adjacent orchestration-framework and BI natural-language-to-SQL material. A dedicated search on "data-cleaning agent," "AI data wrangling agent," and similar terms would fill this gap.
- **Claim-level provenance systems (as opposed to pipeline-level lineage like OpenLineage) were not clearly identified.** It's unclear whether a mature, widely adopted standard exists for tracking "this sentence in this source supports this database field" the way OpenLineage tracks "this job produced this table." Worth a dedicated search on W3C PROV and its actual adoption in AI-research pipelines specifically.
- **The Neo4j/GraphAware acquisition claim (reported as five days old at the time of the search, sourced via a Hacker News/Register aggregation) should be verified against a primary Neo4j or Register source before being treated as a stable fact** — it currently rests on a single indirect citation.
- **Market-position salary/demand figures were mostly U.S.- and Australia/New-Zealand-specific** (from the sources that surfaced); a next pass should widen geographic coverage if the atlas needs to be region-general.
- **Weakly supported claims to re-verify before formal data modeling:** the 41% open-source-BI-adoption figure (traced to one underlying 2025 survey, cited secondhand by two blogs rather than the primary Dresner report); the LangGraph-overtook-CrewAI adoption claim (reported by one 2026 comparison guide without a named underlying dataset); Qdrant's "steadily gaining market share" framing (qualitative, not quantified, in the source it came from).

---

## 7. Sources

_(Each entry lists the URL, publisher/title, and the section(s) of this brief it primarily supports. Access date for all: September 27, 2026.)_

1. https://www.analyticsvidhya.com/blog/2026/05/pandas-vs-polars-vs-duckdb/ — Analytics Vidhya, "Pandas vs Polars vs DuckDB" (May 25, 2026). Supports §2.3, §2.4, §5.1.
2. https://chat2db.ai/resources/blog/duckdb-vs-pandas-vs-polars — Chat2DB, "DuckDB vs Polars vs Pandas: Which to Use in 2026." Supports §2.3, §2.4, §5.1.
3. https://levelup.gitconnected.com/beyond-pandas-polars-or-duckdb-for-faster-local-data-analysis-7953574e6dae — Yang Zhou, Level Up Coding (June 19, 2026). Supports §2.4, §5.1.
4. https://motherduck.com/blog/duckdb-versus-pandas-versus-polars/ — MotherDuck blog (July 7, 2026). Supports §2.3, §2.4.
5. https://en.wikipedia.org/wiki/Polars_(software) — Wikipedia, "Polars (software)." Supports §2.3, §4.
6. https://www.analyticsinsight.net/programming/pandas-vs-polars-vs-duckdb-what-data-scientists-should-use-in-2026 — Analytics Insight (March 22, 2026). Supports §2.4.
7. https://codecut.ai/pandas-vs-polars-vs-duckdb-comparison/ — CodeCut, "pandas vs Polars vs DuckDB" (May 31, 2026). Supports §2.4.
8. https://www.codecentric.de/en/knowledge-hub/blog/duckdb-vs-dataframe-libraries — codecentric, benchmark comparison (December 1, 2025). Supports §2.4, §5.1.
9. https://www.danilchenko.dev/posts/duckdb-vs-polars/ — Maksim Danilchenko, "DuckDB vs Polars in 2026" (July 3, 2026). Supports §2.4, §5.1 (version numbers).
10. https://github.com/munesoft/agent — GitHub, agent-framework bridge project. Supports §2.9, §4 (MCP).
11. https://atlan.com/know/ai-agents-frameworks-compared/ — Atlan, "AI Agent Frameworks Compared" (May 1, 2026). Supports §2.9.
12. https://www.langchain.com/resources/ai-agent-frameworks — LangChain, "The best AI agent frameworks in 2026" (June 9, 2026). Supports §2.9, §4.
13. https://www.turing.com/resources/ai-agent-frameworks — Turing, "A Detailed Comparison of Top 6 AI Agent Frameworks" (February 11, 2026). Supports §2.9.
14. https://github.com/artnitolog/awesome-agent-learning — GitHub, curated agent-framework learning resources. Supports §2.9.
15. https://www.techaheadcorp.com/blog/top-agent-frameworks/ — TechAhead (August 6, 2026). Supports §2.9.
16. https://pickaxe.co/post/top-ai-agent-frameworks — Pickaxe, "Top 15 AI Agent Frameworks in 2026" (May 26, 2026). Supports §2.9, §4 (AutoGen→Agent Framework transition).
17. https://medium.com/@iimoyjv0493b/top-9-ai-agent-frameworks-in-2026-3d95383b8146 — Medium (February 9, 2026). Supports §2.9.
18. https://arsum.com/blog/posts/ai-agent-frameworks/ — Arsum blog (July 1, 2026). Supports §2.9 (critical/skeptical perspective on framework overhead).
19. https://basedash.com/blog/best-open-source-bi-tools-compared-2026 — Basedash, open-source BI comparison. Supports §2.4, §6 (adoption-figure caveat).
20. https://blog.elest.io/apache-superset-vs-metabase-vs-redash-which-open-source-bi-tool-to-self-host-in-2026/ — elest.io. Supports §2.4.
21. https://www.basedash.com/blog/best-bi-tools-for-supabase-2026 — Basedash, Supabase-specific BI comparison. Supports §2.4.
22. https://coefficient.io/open-source-bi-tools — Coefficient, "Open Source BI Tools to Consider in 2026." Supports §2.4, §6.
23. https://www.thebricks.com/resources/metabase-vs-superset — The Bricks (December 6, 2025). Supports §2.4.
24. https://dev.to/gowthampotureddi/apache-superset-metabase-compared-open-source-bi-for-data-teams-52n2 — DEV Community. Supports §2.4.
25. https://www.thebricks.com/resources/metabase-vs-superset-vs-redash — The Bricks (December 6, 2025). Supports §2.4.
26. https://www.definite.app/blog/metabase-alternatives — Definite, "Metabase alternatives." Supports §2.4.
27. https://toolradar.com/compare/dbt-vs-metabase — ToolRadar, "dbt vs Metabase." Supports §2.4, §4.
28. https://thedataschool.co.uk/marcus-rocco/data-analyst-vs-data-scientist-vs-data-engineer-whats-the-difference-2/ — The Data School. Supports §2.2.
29. https://resources.depaul.edu/career-center/career-advising/communities/technology-design/Documents/CareersinDataScience2020_resourceflyer_v4.pdf — DePaul University career resource. Supports §2.2 (data architect).
30. https://towardsdatascience.com/the-different-roles-in-the-data-ecosystem-fc575b8db467/ — Towards Data Science, "The Different Roles in the Data Ecosystem." Supports §2.2, §4 (research engineer).
31. https://www.wscubetech.com/blog/data-analyst-vs-data-engineer/ — WsCube Tech. Supports §2.2.
32. https://asist-archive.ischool.illinois.edu/sigia-l/2006-April/017180.html — SIGIA-L mailing-list archive (2006). Supports §2.2 (information architect boundary problem, historical context).
33. https://en.wikipedia.org/wiki/DuckDB (referenced within document 6). Supports §2.3.
34. https://atlan.com/know/ai-agent/knowledge-graph/knowledge-graph-vs-graph-database.md — Atlan, "Knowledge Graph vs Graph Database" (June 15, 2026). Supports §2.3, §2.6, §4.
35. https://www.energent.ai/use-cases/en/compare/ai-tools-for-knowledge-graph — Energent.ai industry report. Supports §2.2 (knowledge engineer), §2.6.
36. https://www.getgalaxy.io/articles/top-knowledge-graph-platforms-enterprise-data-intelligence-2026 — Galaxy, "Top Knowledge Graph Platforms" (2026). Supports §2.6, §6 (GraphRAG accuracy claim caveat).
37. https://go.neo4j.com/rs/710-RRC-335/images/Neo4j%20AI%20Product%20Keynote%20July%202026.pdf — Neo4j AI product keynote (July 2026). Supports §2.6, §4 (MCP).
38. https://futureagi.com/blog/enterprise-knowledge-graph-platforms-2026/ — FutureAGI, enterprise knowledge-graph platform comparison. Supports §2.6, §4.
39. https://scour.ing/@widget101/interests/Knowledge%20Graphs — Scour.ing news aggregation. Supports §2.5 (Neo4j/GraphAware acquisition — flagged low-confidence, single indirect source).
40. https://www.rajeshkumar.xyz/blog/knowledge-graph-construction-tools/ — Knowledge graph construction tools comparison. Supports §2.6.
41. https://www.nutrient.io/blog/reducto-alternatives/ — Nutrient, "Best Reducto alternatives" (2026). Supports §2.6, §5.3.
42. https://www.nutrient.io/blog/llamaparse-alternatives.md — Nutrient, "Best LlamaParse alternatives" (August 27, 2026). Supports §2.6, §5.3.
43. https://llamaindex.ai/insights/best-alternatives-to-reducto — LlamaIndex, "Best Alternatives to Reducto." Supports §2.6.
44. https://reducto.ai/guides/best-ai-data-extraction-tools-unstructured-documents — Reducto, extraction tools guide. Supports §2.6, §6 (LongExtractionBench).
45. https://www.firecrawl.dev/blog/best-data-extraction-tools — Firecrawl blog (August 10, 2026). Supports §2.3, §2.6.
46. https://www.tooljunction.io/blog/best-document-parsing-apis-2026 — ToolJunction, document parsing API comparison. Supports §2.6, §5.3.
47. https://www.extend.ai/resources/unstructured-review-features-pricing-alternatives — Extend.ai, Unstructured review (March 10, 2026). Supports §2.6.
48. https://dev.thedrive.ai/blog/best-document-extraction-apis-2026 — TheDrive.ai (July 2, 2026). Supports §2.6, §5.3.
49. https://theaiepoch.beehiiv.com/p/6-ai-tools-that-make-deep-research-actually-useful — AI Epoch newsletter. Supports §2.6, §5.4.
50. https://dupple.com/learn/best-ai-research-tools — Dupple, "The Best AI Research Tools in 2026." Supports §2.6, §5.4.
51. https://www.cbinsights.com/company/consensus-1/alternatives-competitors — CB Insights, Consensus competitor listing. Supports §2.5, §2.6.
52. https://guptadeepak.com/tools/top-5-ai-research-tools-2026/ — Deepak Gupta, research-tools comparison (April 11, 2026). Supports §2.6, §5.4.
53. https://engineering.gwu.edu/node/13601 — George Washington University Engineering, session recap on AI for literature review. Supports §2.6.
54. https://libguides.bentley.edu/Artificial_Intelligence_Research/AI_Tools_Research — Bentley University library guide. Supports §2.6.
55. https://aiversehub1.lovable.app/articles/ai-research-assistants — AIverse Hub comparison (June 10, 2026). Supports §2.6.
56. https://www.rfp.wiki/artificial-intelligence/ai-agents-research-automation/elicit/consensus — RFP.wiki, Elicit vs Consensus. Supports §2.6, §5.4.
57. https://www.rfp.wiki/artificial-intelligence/ai-agents-research-automation/consensus/elicit — RFP.wiki, Consensus vs Elicit. Supports §2.6, §5.4.
58. https://costbench.com/compare/consensus-vs-elicit/ — CostBench, pricing comparison. Supports §2.6, §5.4.
59. https://github.com/BKEIT/OpenLineage — GitHub, OpenLineage project. Supports §2.7, §4.
60. https://www.astronomer.io/airflow/astro-vs-dagster/ — Astronomer, "Airflow vs. Dagster." Supports §2.4, §5.2.
61. https://zero2dataengineer.substack.com/p/prefect-vs-airflow-vs-dagster — Zero2DataEngineer Substack. Supports §2.4, §5.2.
62. https://automationatlas.io/answers/best-apache-airflow-alternatives-2026/ — AutomationAtlas, Airflow alternatives (April 2026). Supports §2.4, §5.2.
63. https://datavidhya.com/blog/airflow-vs-dagster-vs-prefect/ — DataVidhya (March 29, 2026). Supports §2.4, §5.2.
64. https://datavidhya.com/learn/de-system-design/technology-deep-dives/orchestrator-comparison — DataVidhya, orchestrator deep dive. Supports §2.4, §5.2.
65. https://agentpedia.codes/blog/ai-ml-orchestration-tools-2026 — Agentpedia, "AI & ML Orchestration in 2026." Supports §2.4.
66. https://interviewkickstart.com/blogs/career-advice/switch-to-data-science — Interview Kickstart, data analyst career analysis. Supports §2.2 (labor-market signal).
67. https://online.edgewood.edu/?p=14356 and https://online.edgewood.edu/blog/is-data-analyst-a-good-career/ and https://online.edgewood.edu/blog/future-of-data-analyst-jobs-with-ai/ and https://online.edgewood.edu/?p=14352 — Edgewood College online-program blog, several 2026 posts on data-analyst career outlook. Supports §2.2.
68. https://intuitionlabs.ai/articles/tags/ai-hiring-data — IntuitionLabs, AI/hiring data tag page. Supports §2.2.
69. https://bootcamp.unf.edu/blog/tech-areas-hiring — UNF Bootcamp, tech hiring areas. Supports §2.2.
70. https://www.learningpeople.com/au/resources/data-analyst-anz-career-market-summary/ — Learning People, ANZ data-analyst market summary. Supports §2.2 (regional salary/demand figures).
71. https://careery.pro/blog/data-analyst-careers/is-data-analyst-a-good-career — Careery.pro (February 17, 2026). Supports §2.2.
72. https://reintech.io/blog/vector-database-comparison-2026-pinecone-weaviate-milvus-qdrant-chroma — Reintech, vector database comparison. Supports §2.3, §2.6.
73. https://minhvo.is-a.dev/blogs/vector-databases-compared-pinecone-weaviate-qdrant-and-milvus — MinhVo blog. Supports §2.3, §2.6 (market size figure).
74. https://encore.dev/articles/best-vector-databases — Encore, vector database comparison. Supports §2.6.
75. https://www.groovyweb.co/blog/top-10-ai-vector-databases-2026 — GroovyWeb, "Top 10 AI Vector Databases in 2026." Supports §2.6.
76. https://codeboxr.com/the-ultimate-guide-to-vector-databases-in-2026/ — CodeBoxr (April 6, 2026). Supports §2.6.
77. https://www.perfectiongeeks.com/blogs/vector-database-comparison-2026 and https://new.perfectiongeeks.com/blogs/vector-database-comparison-2026 — PerfectionGeeks, vector database comparison (duplicate URLs, same content). Supports §2.6.
78. https://alexcloudstar.com/blog/vector-database-comparison-2026/ — Alex Cloudstar, hands-on vector database comparison. Supports §2.6, §5 (pgvector positioning).
79. https://agentpedia.codes/blog/best-vector-databases-ai-agents — Agentpedia, "Best Vector Databases for AI Agents in 2026." Supports §2.6.

---

_End of brief. This document reflects a single research pass; the Companies lens and several flagged claims (§6) warrant a dedicated follow-up before being treated as stable inputs to formal data modeling._