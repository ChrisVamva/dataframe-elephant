---
modified: 2026-09-27T14:48:34+03:00
---
# Research-to-Data Capability Atlas — Structured Research Brief

**Date:** 2026-09-27
**Status:** Initial evidence-grounded synthesis; several lenses remain weakly supported by primary sources.

---

## 1. Executive synthesis

- The research-to-data workflow is not a single pipeline but a **layered capability stack** in which research practices, data engineering, analytical tooling, and agent orchestration overlap and constrain one another. The workflow stages (Research → Evidence → Extraction → Structured representation → Normalization → Database → Query → Analysis → Visualization → Interpretation → New research → Agent iteration) describe an **iterative loop**, not a linear sequence; interpretation and new research frequently feed back into earlier stages.
- **Provenance is a cross-cutting requirement**, not a late-stage add-on. Recent work on evidence-grounded extraction pipelines (e.g., SciGraph-LLM, auditable neuro-symbolic knowledge construction) treats sentence-level or span-level provenance as a first-class output, binding every extracted claim to verbatim source text. This changes the design of extraction, storage, and query layers.
- **DuckDB has emerged as a focal technology** for the “local analytical database” layer, bridging pandas/Polars DataFrames and SQL workflows. Its in-process, columnar, vectorized architecture makes it suitable for embedded analytics, ETL, and notebook-based analysis without server management. Benchmark evidence shows DuckDB and Polars substantially outperform pandas on large structured data, though the three tools occupy different ergonomic and architectural positions.
- **Market positions are not interchangeable.** “Research engineer,” “data analyst,” “knowledge engineer,” and “information architect” describe distinct bundles of skills, outputs, and workflow positions. Job postings show research engineers heavily involved in data acquisition, scraping, and feature extraction pipelines, while knowledge engineers focus on ontology design, semantic modeling, and knowledge graph construction. Data analysts emphasize SQL, Python/R, visualization, and reporting. Information architects own conceptual/logical/physical data models and governance standards.
- **The agent layer is maturing rapidly but remains heterogeneous.** Orchestration frameworks such as LangGraph (graph-based, stateful multi-agent applications) and CrewAI (role-playing collaborative agents) are prominent for research-oriented workflows. Agent infrastructure is becoming commoditized, with cloud providers offering managed agent runtimes and databases becoming “active participants” in agentic workflows via protocols like MCP. However, coordination, verification, and failure handling remain unresolved challenges.
- **Methodologies from data warehousing (ETL/ELT, dimensional modeling, Data Vault, medallion architecture) are being adapted for research data**, but systematic review evidence shows automation struggles with weakly structured sources, schema evolution, and fragmented metadata. Research-specific methodologies (evidence-grounded extraction, provenance-aware pipelines, claim-evidence representations) are emerging but not yet standardized.
- **The software layer spans four distinct modes of work**: DataFrame-first (pandas, Polars), SQL-first embedded analytics (DuckDB), notebook environments (Jupyter, Hex), and code-led publishing/BI (Evidence, Observable, Lightdash, Metabase, Superset). These are not mutually exclusive; integration surfaces (e.g., DuckDB querying pandas/Polars DataFrames, dbt transforming data in warehouses) are important differentiators.
- **Companies and products in this space separate into employers, vendors, open-source foundations, and research organizations.** The hiring market reflects the capability cluster (research engineers, data analysts, knowledge engineers), while the vendor market includes data extraction tools, BI platforms, agent infrastructure providers, and research data platforms. Conflating these categories obscures the actual structure of the ecosystem.
- **Key open questions** include: (a) how to reliably verify agent-produced extractions and analyses; (b) how to standardize provenance across heterogeneous artifact classes (chats, PDFs, code, datasets); (c) how research-specific ontologies should relate to enterprise data models; and (d) whether the emerging agent infrastructure layer will consolidate or remain fragmented.

---

## 2. Lens findings

### 2.1 Skills

**Definition and scope:** The skills lens covers the human capabilities required to move from research inputs to structured, queryable, analyzable outputs. It includes research synthesis, information extraction, data modeling, ontology design, normalization, SQL, DuckDB, pandas, visualization, provenance, and agent orchestration.

**Core capabilities and entities:**
- **Research synthesis**: Identifying, evaluating, and integrating findings from multiple sources.
- **Information extraction**: Transforming unstructured content (PDFs, web pages, text) into structured representations.
- **Data modeling**: Designing schemas, tables, relationships, and constraints suitable for analytical querying.
- **Ontology design**: Defining entity types, relation predicates, and constraints for knowledge representation.
- **Normalization**: Type casting, string normalization, unit harmonization, entity canonicalization.
- **SQL**: Querying, joining, aggregating, window functions, CTEs.
- **DuckDB**: Embedded analytical SQL engine usage; in-process analytics.
- **pandas / Polars**: DataFrame manipulation; pandas for prototyping and rich ecosystem, Polars for high-performance columnar processing with lazy execution.
- **Visualization**: Charting, dashboards, interactive data apps.
- **Provenance**: Tracking source, transformations, and evidence chains.
- **Agent orchestration**: Designing, coordinating, and verifying multi-agent workflows.

**Position in workflow:** Skills span every stage. Research synthesis and information extraction are concentrated at the front; data modeling and normalization at the middle; SQL/query and analysis in the core; visualization and provenance throughout; agent orchestration as an increasingly cross-cutting capability.

**Relationships to other lenses:** Skills are `used_in` Workflows; Workflows `uses` Technologies; Technologies are `implemented_by` Software. Skills also map to Market Positions (e.g., SQL → Data Analyst, ontology design → Knowledge Engineer).

**Representative examples:** Job postings for research engineers explicitly list web scraping, data acquisition, information extraction, and feature extraction pipelines. Knowledge engineer postings list ontology design, OWL/RDF, knowledge graph construction, and semantic modeling.

**Trade-offs and failure modes:** Breadth vs. depth: “full-stack” research-to-data roles risk shallow expertise. Over-reliance on pandas for large datasets can cause memory pressure; DuckDB/Polars are more suitable for out-of-core or parallel workloads. Provenance skills are often underdeveloped relative to extraction and analysis skills.

**Evidence confidence:** Medium. Job postings are reported signals; tool documentation is high-confidence for capabilities but not for skill distributions.

---

### 2.2 Market positions

**Definition and scope:** Distinct occupational roles that perform or govern research-to-data work.

**Core entities:**
- **Data analyst**: SQL, Python/R, visualization, reporting, dashboards. Outputs: analyses, reports, dashboards. Hiring signals: SQL proficiency, BI tools (Tableau, Looker, Power BI), statistical analysis.
- **Research analyst**: Domain research, synthesis, evidence evaluation; often less tool-heavy than data analysts.
- **Knowledge engineer**: Ontology design, knowledge graph construction, semantic modeling, OWL/RDF, working with domain experts. Outputs: ontologies, knowledge graphs, semantic models.
- **Data/BI analyst**: Overlaps with data analyst but more BI-platform-centric (Looker, Power BI, Metabase).
- **Research engineer**: Data acquisition, scraping, extraction pipelines, feature engineering, software engineering for research. Outputs: datasets, extraction pipelines, tools.
- **Automation specialist**: Workflow automation, n8n/Zapier/Make, AI agent integration. Outputs: automated workflows, integrations.
- **AI/agent workflow specialist**: Multi-agent workflow design, MCP integration, tool invocation patterns, orchestration. Outputs: agent workflows, integrations.
- **Information architect**: Conceptual/logical/physical data models, data governance, taxonomy, semantic structures. Outputs: enterprise data models, data domain maps.

**Position in workflow:** These roles map unevenly to workflow stages. Research engineers concentrate on research→extraction→structured representation; knowledge engineers on structured representation→normalization→database (semantic layer); data analysts on query→analysis→visualization; information architects on data modeling and governance across multiple stages; automation/agent specialists on orchestration across the loop.

**Relationships:** Market positions `appear_in` Workflows; they `perform` or `govern` Workflow Steps. They also relate to Skills (require), Technologies (use), and Products (operate).

**Trade-offs and failure modes:** Label inflation: “research engineer” can mean anything from hardware-adjacent data collection to software-heavy extraction pipeline development. “Knowledge engineer” in enterprise settings often means ontology work for AI reasoning, not research data extraction. Role boundaries blur in small teams.

**Evidence confidence:** Medium. Job postings are reported signals; definitions are synthesized from multiple postings.

---

### 2.3 Technology

**Definition and scope:** Technical substrates and languages enabling research-to-data workflows.

**Core technologies:**
- **Python**: Dominant language for data analysis, extraction, and orchestration.
- **SQL**: Query language for relational and analytical databases.
- **DuckDB**: In-process analytical database; columnar storage, vectorized execution, ACID guarantees, rich SQL dialect, multiple client libraries (Python, R, Java, Node.js, Rust, Go, WebAssembly). Extensible architecture with custom functions and loadable extensions.
- **pandas**: Mature DataFrame library; rich ecosystem; eager execution; in-memory by default.
- **Polars**: Rust-based columnar DataFrame library; multithreaded, lazy API, streaming execution, Apache Arrow memory representation.
- **Notebooks**: Jupyter, Hex, Observable; interactive, iterative analysis environment.
- **APIs and scraping**: HTTP clients, browser automation (Selenium, Playwright, Camoufox), structured extraction from web pages.
- **LLMs**: Used for information extraction, schema-enforced extraction, entity canonicalization, relation extraction, and agent reasoning.
- **Embeddings and vector databases**: Semantic search, RAG, knowledge retrieval; e.g., Qdrant, Pinecone, Azure Cosmos DB vector search.
- **Graph technologies**: Neo4j, RDF/OWL, knowledge graphs for interconnected research data.
- **Data formats**: CSV, Parquet, JSON, Arrow; DuckDB supports querying directly from files.
- **Databases**: DuckDB (embedded), SQLite, PostgreSQL, cloud warehouses (Snowflake, BigQuery).

**Position in workflow:** Technologies span all stages. Python and SQL are pervasive. DuckDB/pandas/Polars are concentrated in query and analysis. LLMs/embeddings are increasingly used in extraction and agent stages. Graph technologies are used in structured representation and knowledge storage.

**Relationships:** Technologies `implemented_by` Software; Workflows `uses` Technologies.

**Trade-offs and failure modes:** DuckDB vs. pandas vs. Polars trade-offs are documented: pandas for prototyping and ecosystem breadth; Polars for high-performance in-memory/lazy processing; DuckDB for SQL-first analytics with out-of-core capability. LLM-based extraction requires strict grounding to avoid hallucination; evidence-grounded pipelines with schema enforcement and textual fidelity constraints improve reliability.

**Evidence confidence:** High for tool capabilities (official documentation, benchmark studies); medium for LLM extraction reliability (emerging literature).

---

### 2.4 Software

**Definition and scope:** Concrete software tools and frameworks implementing the technologies.

**Core software:**
- **DuckDB**: Embedded OLAP database. Official documentation describes in-process architecture, parser/planner/optimizer/execution engine, columnar storage, vectorized execution. System architecture page details core components and query flow.
- **pandas**: DataFrame library. Mature API; wide adoption.
- **Polars**: DataFrame library with lazy API. Lazy execution defers computation until `collect()`, enabling query optimization and parallelization.
- **Jupyter**: Notebook environment for iterative analysis. Typical workflow: add data, create notebook, load and analyze, share results.
- **dbt**: Transformation layer in ELT; runs SQL transformations within the data warehouse. “dbt sits between your raw data and your analytics layer”.
- **Metabase**: Self-serve BI tool; simpler for non-technical users; direct DuckDB connection; weak metric control at scale.
- **Superset**: Self-hosted dashboards; more flexible for complex reporting; higher setup/maintenance.
- **Observable**: Code-led publishing; browser-based interactive data apps; JavaScript-centric; DuckDB-Wasm integration.
- **Orchestration and agent frameworks**: LangGraph (graph-based stateful multi-agent applications), CrewAI (role-playing collaborative agents), AutoGen (conversable agents), MetaGPT (role-based autonomous workforce simulation).
- **Extraction tools**: Camoufox Research (browser automation, table extraction, monitoring), Bright Data MCP, Stagehand (natural language browser automation).
- **Evidence**: Open-source framework for building data products with SQL and Markdown; BI as code; agent-ready.
- **Lightdash**: BI tool fully integrated with dbt; metrics defined in version-controlled YAML; semantic layer.
- **MotherDuck**: Cloud data warehouse powered by DuckDB; serverless, MCP server, AI functions, agent-native ingest.

**Position in workflow:** Software maps to specific stages: extraction tools → extraction; DuckDB/dbt → normalization/storage; Jupyter/Hex → analysis; Metabase/Superset/Observable/Evidence/Lightdash → visualization/BI; agent frameworks → orchestration across stages.

**Relationships:** Software `produced_by` Company; Software `implements` Technology; Workflows `uses` Software.

**Trade-offs and failure modes:** Metabase is easier for self-serve but weaker for governed metrics; Superset is more flexible but harder to maintain; Lightdash depends on a mature dbt project; Observable is code-first but less suitable for non-technical users. Agent frameworks vary in maturity, control model, and suitability for research workflows.

**Evidence confidence:** High for official documentation; medium for comparative assessments (vendor or third-party benchmarks).

---

### 2.5 Companies

**Definition and scope:** Organizations hiring for, selling, or building around research-to-data capabilities.

**Core entities and categories:**
- **Employers**: Organizations hiring research engineers, data analysts, knowledge engineers, information architects. Examples from job postings include McChrystal Group (research engineer, data acquisition), Accenture (knowledge engineer, ontologies), Northern Trust (information architect, data modeling), Equifax (data analyst, SQL/Python).
- **Vendors**: DuckDB Labs (DuckDB), MotherDuck (cloud DuckDB), dbt Labs (dbt), Metabase, Preset (managed Superset), Observable, Evidence, Lightdash, Hex.
- **Open-source foundations**: Apache Superset, DuckDB (MIT license), Polars (MIT), dbt Core (Apache 2.0).
- **Consultancies**: Accenture, Xebia (ontology/knowledge graph engineering for life sciences).
- **Research organizations**: CAS (Intelligence Hub for scientific R&D data), FAIRDOM (FAIR data management platform), Leibniz Data Manager.

**Position in workflow:** Companies participate at different points: employers provide labor; vendors provide tooling; foundations sustain open-source infrastructure; consultancies provide expertise; research organizations generate domain-specific platforms.

**Relationships:** Companies `produce` Software/Products; Companies `hire_for` Market Positions.

**Trade-offs and failure modes:** Vendor positioning should not be treated as universal fact. Market reports on data extraction software list many players (IBM, UiPath, Talend, Fivetran, etc.) but these categories are broad and include legacy ETL vendors. The agent infrastructure space is highly volatile, with new entrants and acquisitions.

**Evidence confidence:** Medium. Job postings and vendor pages are primary for existence and positioning; market reports are secondary.

---

### 2.6 Products

**Definition and scope:** Specific products addressing research-to-data user problems.

**Core products and user problems:**
- **MotherDuck**: Cloud DuckDB warehouse. User problem: team access to DuckDB without local infrastructure. Differentiator: serverless, MCP server, AI functions, agent-native ingest.
- **Hex**: Collaborative data notebook with Notebook Agent. User problem: iterative analysis with SQL/Python and app-building. Differentiator: agent embedded in notebook experience; SQL + Python interchangeably.
- **Evidence**: BI as code. User problem: version-controlled, code-driven reporting. Differentiator: SQL + Markdown; open-source core; Evidence Agent.
- **Lightdash**: dbt-integrated BI. User problem: governed metrics from dbt models. Differentiator: metrics defined in dbt YAML; semantic layer; no separate modeling.
- **Metabase**: Self-serve BI. User problem: easy dashboards for business users. Differentiator: simplicity, direct database connection.
- **Superset**: Self-hosted BI. User problem: flexible, free BI for technical teams. Differentiator: wide visualization options; DevOps requirement.
- **Observable**: Interactive data apps. User problem: browser-based, shareable data stories. Differentiator: reactive notebooks, JavaScript, DuckDB-Wasm.
- **Open Research Knowledge Graph (ORKG)**: Platform for FAIR scientific knowledge. User problem: shifting scholarly communication from documents to data. Differentiator: research comparisons, thematic reviews.
- **CAS Intelligence Hub**: Harmonized R&D knowledge environment. User problem: fragmented scientific R&D data. Differentiator: AI-supported knowledge environment.
- **Sharpr**: AI-powered knowledge management for research and competitive intelligence. User problem: syndicating content from different sources. Differentiator: automatic processing and organization of research content.

**Position in workflow:** Products map to stages: extraction (Camoufox, Bright Data), storage/query (MotherDuck, DuckDB), analysis (Hex, Jupyter), visualization/BI (Metabase, Superset, Observable, Evidence, Lightdash), knowledge systems (ORKG, CAS Intelligence Hub).

**Relationships:** Products `implemented_by` Software; Products `produced_by` Company; Products `supports` Workflow Stage.

**Trade-offs and failure modes:** BI tools trade governance for ease of use; notebook tools trade sharing for control; code-led BI trades drag-and-drop simplicity for version control and reproducibility. Knowledge systems risk becoming stale without active curation.

**Evidence confidence:** Medium to high for product pages (primary), low for comparative claims without independent testing.

---

### 2.7 Methodologies

**Definition and scope:** Structured approaches governing how research becomes data.

**Core methodologies:**
- **Research protocols**: Systematic review, PRISMA, evidence synthesis frameworks.
- **ETL/ELT**: Extract, Transform, Load vs. Extract, Load, Transform. ELT transformation occurs within the target warehouse (dbt is built for the “T” in ELT).
- **Data modeling**: Entity-relationship models, dimensional modeling (star schema, snowflake schema), Data Vault, medallion architecture (Bronze/Silver/Gold). Systematic review evidence shows automation is partial; weakly structured sources and schema evolution remain hard.
- **Information extraction**: Schema-constrained extraction, evidence-grounded pipelines, entity canonicalization, relation extraction. SciGraph-LLM uses GPT-5 with schema-enforced prompts, overlapping windows, and strict textual fidelity constraints.
- **Evidence and provenance systems**: W3C PROV distinguishes entities, activities, agents, and relations. Provenance is evidence about artifacts, not proof of claims. Artifact classes have distinct epistemic boundaries (chat export → workflow/draft intent; DOI record → citable identity; proof packet → exact statement checked).
- **Analytical workflows**: Exploratory data analysis (EDA), statistical testing, visualization-first analysis.

**Position in workflow:** Methodologies `govern` Workflow Steps. ETL/ELT governs extraction→storage; data modeling governs structured representation→database; information extraction governs evidence→structured representation; provenance systems govern cross-cutting traceability.

**Relationships:** Methodologies `govern` Workflows; Methodologies `uses` Technologies; Methodologies `implemented_by` Software.

**Trade-offs and failure modes:** ETL vs. ELT: ETL transforms before loading (more control, slower), ELT transforms after loading (more flexible, requires warehouse compute). Data Vault vs. dimensional: Data Vault is more auditable and extensible; dimensional is simpler for BI. Evidence-grounded extraction improves reliability but struggles with non-contiguous evidence and implicit reasoning.

**Evidence confidence:** High for established methodologies (ETL/ELT, dimensional modeling); medium for research-specific methodologies (emerging literature).

---

### 2.8 Workflows

**Definition and scope:** The end-to-end research-to-data loop: research → evidence → extraction → structured representation → normalization → database → query → analysis → visualization → interpretation → new research → agent iteration.

**Stage-by-stage description:**

| Stage | Inputs | Activities | Outputs | Quality checks | Likely tools | Agent roles |
|---|---|---|---|---|---|---|
| Research | Questions, domain knowledge | Literature search, source identification, scoping | Source corpus, research questions | Relevance, coverage | Search engines, APIs, academic databases | Research agent (search, retrieval) |
| Evidence | Source corpus | Source evaluation, evidence selection, span identification | Evidence units, annotated spans | Fidelity, provenance | Annotation tools, LLM grounding | Evidence agent (span extraction, citation) |
| Extraction | Evidence units, unstructured text | Schema-constrained extraction, entity recognition, relation extraction | Structured claims, entities, relations | Schema compliance, evidence precision | LLMs, extraction frameworks, regex | Extraction agent (schema-enforced extraction) |
| Structured representation | Extracted claims/entities | Entity canonicalization, type assignment, relation formalization | Knowledge graph, relational schema, JSON records | Consistency, canonicalization | Ontology tools, KG frameworks, Pydantic | Structuring agent (canonicalization, validation) |
| Normalization | Structured records | Type casting, unit harmonization, string normalization, deduplication | Normalized tables, harmonized datasets | Type correctness, uniqueness, constraints | pandas, Polars, DuckDB, dbt | Data-cleaning agent (normalization, dedup) |
| Database | Normalized data | Schema creation, loading, indexing | Queryable database (DuckDB, PostgreSQL, warehouse) | ACID, referential integrity | DuckDB, PostgreSQL, dbt, MotherDuck | Loading agent (schema migration, ingestion) |
| Query | Database, questions | SQL query writing, optimization, execution | Result sets, intermediate tables | Query correctness, performance | DuckDB, SQL, dbt | Query agent (SQL generation, optimization) |
| Analysis | Query results, datasets | Statistical analysis, aggregation, modeling | Findings, metrics, statistical summaries | Method validity, robustness | pandas, Polars, statsmodels, scikit-learn | Analytical agent (statistical testing, anomaly detection) |
| Visualization | Analysis results | Charting, dashboarding, interactive app building | Charts, dashboards, data apps | Readability, accuracy, accessibility | Metabase, Superset, Observable, Evidence, Hex | Visualization agent (chart recommendation, layout) |
| Interpretation | Visualizations, findings | Contextualization, causal reasoning, narrative | Insights, conclusions, recommendations | Logical coherence, alternative explanations | Human judgment, LLM assistance | Interpretation agent (summarization, hypothesis generation) |
| New research | Insights, gaps | Question reformulation, new source search | New research questions | Novelty, feasibility | Search tools, research agents | Research agent (question refinement) |
| Agent iteration | Feedback, verification results | Error analysis, workflow refinement, agent tuning | Improved workflow, updated agents | Reliability, efficiency | Orchestration frameworks, evaluation harnesses | Coordinating agent (orchestration, verification) |

**Quality gates:** Source validation at evidence stage; schema conformance at extraction; constraint checking at normalization; query validation before analysis; statistical assumption checks at analysis; provenance binding at every stage.

**Feedback loops:** Interpretation → New research; agent iteration → all stages; analysis → extraction (need for different data); visualization → analysis (need for different metrics).

**Evidence confidence:** Medium. Stage decomposition is synthesized from multiple sources; specific quality gates and agent roles are inferences unless otherwise cited.

---

### 2.9 Agents

**Definition and scope:** Software agents that perform or coordinate research-to-data tasks.

**Core agent types:**
- **Research agents**: Search, retrieve, and synthesize literature or web content. Tools: search APIs, browser automation, LLMs. State: query history, source corpus. Failure modes: source bias, hallucinated citations, coverage gaps.
- **Extraction agents**: Extract structured claims and entities from unstructured text. Tools: LLMs with schema-enforced prompts, regex, NLP libraries. State: source text, schema definition, extracted records. Failure modes: schema violations, hallucinated entities, missed evidence spans.
- **Coding agents**: Write and execute code for data cleaning, analysis, and visualization. Tools: Python interpreter, SQL engine, libraries. State: code history, execution results. Failure modes: incorrect code, resource exhaustion, silent errors.
- **Data-cleaning agents**: Normalize, deduplicate, type-cast, and validate data. Tools: pandas/Polars, DuckDB, validation frameworks. State: data profiles, cleaning rules. Failure modes: over-cleaning, lost information, inconsistent rules.
- **Analytical agents**: Perform statistical tests, aggregations, and modeling. Tools: pandas, Polars, scikit-learn, statsmodels. State: dataset, analysis plan. Failure modes: p-hacking, assumption violations, misinterpretation.
- **Coordinating/orchestration agents**: Plan and dispatch tasks to worker agents; handle handoffs, verification, and iteration. Frameworks: LangGraph (graph-based state), CrewAI (role-based teams), AutoGen (conversable agents), MetaGPT (role-based workforce). Failure modes: coordination deadlock, task misrouting, verification gaps.

**Position in workflow:** Agents can be assigned to every stage, with coordinating agents overseeing the loop. Handoffs occur between extraction → structuring, structuring → normalization, query → analysis, analysis → visualization.

**Relationships:** Agents `perform` Workflow Steps; Agents `use` Tools/Technologies; Agents `implemented_by` Software/Frameworks.

**Trade-offs and failure modes:** Multi-agent systems face strategic coordination and collaborative reasoning challenges; temporal sequencing of actions matters; partial observability and limited communication are common. Verification remains a critical gap: agent-produced extractions and analyses require human oversight or automated checks against provenance.

**Evidence confidence:** Medium. Framework documentation is primary; failure mode analysis is emerging literature and inference.

---

## 3. Workflow map (consolidated)

The workflow is best understood as a **cyclic graph with feedback edges**, not a linear pipeline. The following stage-by-stage map integrates the lens findings.

**Stage 1: Research**
- **Inputs:** Research questions, domain context, existing knowledge.
- **Activities:** Source discovery, scoping, question refinement.
- **Outputs:** Annotated source corpus, research plan.
- **Quality checks:** Source relevance, coverage, recency.
- **Tools:** Search engines, academic databases, APIs, browser automation.
- **Agent roles:** Research agent (retrieval, ranking, summarization).

**Stage 2: Evidence**
- **Inputs:** Source corpus.
- **Activities:** Source evaluation, evidence identification, span extraction.
- **Outputs:** Evidence units (paragraph-level or span-level), provenance records.
- **Quality checks:** Textual fidelity, provenance completeness.
- **Tools:** Annotation tools, LLM grounding, evidence-unit frameworks.
- **Agent roles:** Evidence agent (span extraction, citation binding).

**Stage 3: Extraction**
- **Inputs:** Evidence units, unstructured text.
- **Activities:** Schema-constrained extraction, NER, relation extraction.
- **Outputs:** Structured claims, entities, relations, all linked to evidence spans.
- **Quality checks:** Schema conformance, evidence precision, claim F1.
- **Tools:** LLMs with schema-enforced prompts, extraction frameworks.
- **Agent roles:** Extraction agent (schema-enforced extraction, canonicalization).

**Stage 4: Structured representation**
- **Inputs:** Extracted claims/entities.
- **Activities:** Entity canonicalization, type assignment, relation formalization, ontology mapping.
- **Outputs:** Knowledge graph, relational schema, JSON records.
- **Quality checks:** Consistency, canonicalization, ontology compliance.
- **Tools:** Ontology tools (OWL/RDF), KG frameworks, Pydantic.
- **Agent roles:** Structuring agent (canonicalization, validation).

**Stage 5: Normalization**
- **Inputs:** Structured records.
- **Activities:** Type casting, unit harmonization, string normalization, deduplication.
- **Outputs:** Normalized tables, harmonized datasets.
- **Quality checks:** Type correctness, uniqueness, constraint validation.
- **Tools:** pandas, Polars, DuckDB, dbt.
- **Agent roles:** Data-cleaning agent (normalization, dedup, validation).

**Stage 6: Database**
- **Inputs:** Normalized data.
- **Activities:** Schema creation, loading, indexing, storage.
- **Outputs:** Queryable database (DuckDB, PostgreSQL, cloud warehouse).
- **Quality checks:** ACID compliance, referential integrity, query performance.
- **Tools:** DuckDB, PostgreSQL, MotherDuck, dbt.
- **Agent roles:** Loading agent (schema migration, ingestion, indexing).

**Stage 7: Query**
- **Inputs:** Database, questions.
- **Activities:** SQL query writing, optimization, execution.
- **Outputs:** Result sets, intermediate tables, views.
- **Quality checks:** Query correctness, performance, result validation.
- **Tools:** DuckDB, SQL, dbt.
- **Agent roles:** Query agent (SQL generation, optimization, validation).

**Stage 8: Analysis**
- **Inputs:** Query results, datasets.
- **Activities:** Statistical analysis, aggregation, modeling, hypothesis testing.
- **Outputs:** Findings, metrics, statistical summaries.
- **Quality checks:** Method validity, robustness, assumption checking.
- **Tools:** pandas, Polars, statsmodels, scikit-learn.
- **Agent roles:** Analytical agent (statistical testing, anomaly detection).

**Stage 9: Visualization**
- **Inputs:** Analysis results.
- **Activities:** Charting, dashboarding, interactive app building.
- **Outputs:** Charts, dashboards, data apps.
- **Quality checks:** Readability, accuracy, accessibility.
- **Tools:** Metabase, Superset, Observable, Evidence, Hex.
- **Agent roles:** Visualization agent (chart recommendation, layout).

**Stage 10: Interpretation**
- **Inputs:** Visualizations, findings.
- **Activities:** Contextualization, causal reasoning, narrative construction.
- **Outputs:** Insights, conclusions, recommendations.
- **Quality checks:** Logical coherence, alternative explanations, provenance back-references.
- **Tools:** Human judgment, LLM assistance.
- **Agent roles:** Interpretation agent (summarization, hypothesis generation).

**Stage 11: New research**
- **Inputs:** Insights, gaps.
- **Activities:** Question reformulation, new source search, hypothesis generation.
- **Outputs:** New research questions, updated research plan.
- **Quality checks:** Novelty, feasibility, alignment with evidence.
- **Tools:** Search tools, research agents.
- **Agent roles:** Research agent (question refinement, gap detection).

**Stage 12: Agent iteration**
- **Inputs:** Feedback, verification results, error logs.
- **Activities:** Error analysis, workflow refinement, agent tuning, prompt revision.
- **Outputs:** Improved workflow, updated agents, refined prompts.
- **Quality checks:** Reliability, efficiency, verification coverage.
- **Tools:** Orchestration frameworks, evaluation harnesses.
- **Agent roles:** Coordinating agent (orchestration, verification, iteration).

---

## 4. Entity and relationship candidates

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
|---|---|---|---|---|---|---|---|
| Skill | Research synthesis | Identifying and integrating findings from multiple sources | Research, Evidence | Workflow, Market Position | used_in, required_by | Job postings, methodological literature | Medium |
| Skill | Information extraction | Transforming unstructured content into structured representations | Extraction | Technology, Software, Agent | uses, performed_by | SciGraph-LLM, job postings | High |
| Skill | Data modeling | Designing schemas, tables, relationships, constraints | Structured representation, Normalization | Technology, Methodology | used_in, implemented_by | Information architect job postings, DW literature | High |
| Skill | Ontology design | Defining entity types, relation predicates, constraints | Structured representation | Methodology, Software | governs, implemented_by | Knowledge engineer job postings | High |
| Skill | Normalization | Type casting, unit harmonization, deduplication | Normalization | Technology, Software | performed_by, uses | ETL/ELT literature | High |
| Skill | SQL | Query language for relational/analytical databases | Query | Technology, Software | used_in, implemented_by | DuckDB docs, data analyst postings | High |
| Skill | DuckDB | Embedded analytical database usage | Database, Query | Technology, Software | implemented_by | DuckDB docs | High |
| Skill | pandas | DataFrame manipulation for prototyping | Analysis | Technology, Software | implemented_by | pandas docs, benchmark studies | High |
| Skill | Provenance | Tracking source, transformations, evidence chains | Cross-cutting | Methodology, Workflow | governs, required_by | W3C PROV, provenance literature | High |
| Skill | Agent orchestration | Designing and coordinating multi-agent workflows | Agent iteration | Agent, Software | performed_by, implemented_by | LangGraph/CrewAI literature | Medium |
| Market Position | Data analyst | SQL, Python/R, visualization, reporting | Query, Analysis, Visualization | Skill, Workflow | performs, requires | Job postings | Medium |
| Market Position | Knowledge engineer | Ontology design, semantic modeling, KG construction | Structured representation | Skill, Methodology | performs, requires | Job postings | High |
| Market Position | Research engineer | Data acquisition, scraping, extraction pipelines | Research, Extraction | Skill, Workflow | performs, requires | Job postings | Medium |
| Market Position | Information architect | Conceptual/logical/physical data models, governance | Structured representation, Database | Skill, Methodology | governs, requires | Job postings | High |
| Technology | DuckDB | In-process OLAP database | Database, Query | Software, Skill | implemented_by | Official docs | High |
| Technology | Polars | Rust-based columnar DataFrame library | Analysis | Software, Skill | implemented_by | Official docs | High |
| Technology | LLMs | Large language models for extraction and reasoning | Extraction, Analysis, Agent | Software, Agent | used_by, implemented_by | SciGraph-LLM, agent literature | High |
| Technology | Embeddings | Dense vector representations for semantic search | Query, Analysis | Software (vector DB) | used_by | Vector DB literature | Medium |
| Technology | Graph databases | Storage for interconnected entities and relations | Structured representation, Database | Software (Neo4j) | implemented_by | Neo4j research use cases | Medium |
| Software | dbt | Transformation layer in ELT | Normalization, Database | Technology, Company | implements, produced_by | dbt docs | High |
| Software | LangGraph | Graph-based multi-agent orchestration framework | Agent iteration | Technology, Agent | implements | ACL literature | Medium |
| Software | CrewAI | Role-playing collaborative agent framework | Agent iteration | Technology, Agent | implements | ACL literature | Medium |
| Software | Metabase | Self-serve BI tool | Visualization | Company, Product | produced_by | Querio comparison | Medium |
| Software | Superset | Self-hosted BI platform | Visualization | Company, Product | produced_by | Querio comparison | Medium |
| Software | Observable | Browser-based interactive data apps | Visualization | Company, Product | produced_by | Querio comparison | Medium |
| Software | Evidence | BI as code framework | Visualization | Company, Product | produced_by | Evidence docs | Medium |
| Software | Lightdash | dbt-integrated BI tool | Visualization | Company, Product | produced_by | Lightdash docs | Medium |
| Product | MotherDuck | Cloud DuckDB warehouse | Database, Query | Company, Software | produced_by, implements | MotherDuck docs | High |
| Product | Hex | Collaborative data notebook | Analysis | Company, Software | produced_by | Hex docs | Medium |
| Product | ORKG | Open Research Knowledge Graph | Structured representation | Organization, Methodology | produced_by, implements | EOSC page | Medium |
| Methodology | ETL/ELT | Extract-transform-load patterns | Extraction → Database | Technology, Software | governs, implemented_by | DW literature, dbt docs | High |
| Methodology | Data Vault | Auditable data warehouse modeling | Structured representation | Technology | governs | Systematic review | High |
| Methodology | Evidence-grounded extraction | Schema-constrained extraction with provenance | Extraction | Technology, Agent | governs, implemented_by | SciGraph-LLM | Medium |
| Workflow | Research-to-data loop | End-to-end iterative workflow | All stages | All lenses | uses, produces | Synthesized | Medium |
| Agent | Research agent | Search, retrieve, synthesize sources | Research | Technology, Software | performs, uses | Agent literature | Medium |
| Agent | Extraction agent | Extract structured claims from text | Extraction | Technology, Software | performs, uses | SciGraph-LLM, agent literature | Medium |
| Agent | Coding agent | Write and execute data code | Analysis, Visualization | Technology | performs, uses | Agent literature | Medium |
| Agent | Coordinating agent | Plan and dispatch tasks to agents | Agent iteration | Software, Workflow | performs, implemented_by | LangGraph/CrewAI literature | Medium |
| Company | DuckDB Labs | Maintains DuckDB | — | Software | produces | DuckDB docs | High |
| Company | dbt Labs | Maintains dbt | — | Software | produces | dbt docs | High |
| Company | MotherDuck | Cloud DuckDB warehouse | — | Product | produces | MotherDuck docs | High |

---

## 5. Comparison tables

### 5.1 DataFrame and analytical engines

| Criterion | pandas | Polars | DuckDB |
|---|---|---|---|
| **Purpose** | General-purpose DataFrame manipulation | High-performance columnar DataFrame processing | Embedded analytical SQL engine |
| **Execution** | Eager, single-threaded by default | Lazy and eager, multithreaded | Vectorized, parallel, cost-based optimizer |
| **Out-of-core** | No (chunking required) | Streaming for some operations | Yes (spilling to disk) |
| **Language** | Python | Rust (Python bindings) | C++ (SQL, Python/R/Java/etc. clients) |
| **Memory representation** | NumPy/Arrow (2.x) | Apache Arrow | Columnar storage format |
| **Best for** | Prototyping, EDA, rich ecosystem | Large in-memory/lazy transformations | SQL-first analytics, local ETL, embedded analytics |
| **Ecosystem** | Very mature | Growing | Rich integrations with pandas/Polars/Arrow |
| **Maturity** | High | Medium-high | High |
| **Source** |  |  |  |

### 5.2 BI and visualization tools

| Criterion | Metabase | Superset | Observable | Evidence | Lightdash |
|---|---|---|---|---|---|
| **Primary mode** | Drag-and-drop self-serve | Self-hosted dashboards | Code-led interactive apps | BI as code | dbt-integrated BI |
| **Target user** | Business users | Technical teams with DevOps | Data journalists, coders | Analytics engineers | dbt-mature teams |
| **Governance** | Weak metric control | Flexible but manual | Code-based | Version-controlled | Strong (dbt semantic layer) |
| **Setup complexity** | Low | High | Low | Low (hosted) | Medium (requires dbt) |
| **DuckDB integration** | Direct connection | Connector | Browser-side (Wasm) | Local/browser engine | Via dbt/warehouse |
| **Best for** | Simple self-serve | Complex custom dashboards | Custom data apps | Version-controlled reporting | Governed metrics |
| **Source** |  |  |  |  |  |

### 5.3 Agent orchestration frameworks

| Criterion | LangGraph | CrewAI | AutoGen | MetaGPT |
|---|---|---|---|---|
| **Paradigm** | Graph-based stateful multi-agent | Role-playing collaborative teams | Conversable multi-agent | Role-based virtual workforce |
| **Control model** | Explicit graph, state-maintaining | Agent roles and goals | Conversational, flexible | Opinionated, role-driven |
| **Best for** | Cyclical iteration and reflection | Collaborative task execution | Research-oriented collaboration | Software development simulation |
| **Maturity** | Medium-high | Medium | Medium-high | Medium |
| **Source** |  |  |  |  |

### 5.4 Market positions

| Criterion | Data Analyst | Knowledge Engineer | Research Engineer | Information Architect |
|---|---|---|---|---|
| **Core output** | Analyses, dashboards, reports | Ontologies, knowledge graphs | Datasets, extraction pipelines | Enterprise data models |
| **Primary skills** | SQL, Python/R, BI tools | Ontology design, OWL/RDF, KG | Web scraping, NLP, software eng. | Data modeling, governance, taxonomy |
| **Workflow focus** | Query → Analysis → Visualization | Structured representation → Database | Research → Extraction | Structured representation → Database |
| **Hiring signal** | SQL proficiency, visualization | Ontology, semantic modeling | Data acquisition, extraction | Conceptual/logical/physical models |
| **Source** |  |  |  |  |

---

## 6. Research gaps and next investigations

**Unresolved questions:**
- How do research-specific evidence/provenance systems (claim-evidence representations, evidence units) integrate with enterprise data governance frameworks (data mesh, Data Vault)?
- What are the actual failure rates and verification costs of LLM-based extraction agents in production research-to-data pipelines? The SciGraph-LLM paper reports 81.3% evidence precision and 59.9% claim F1; more independent evaluations are needed.
- How do agent orchestration frameworks handle long-running, cyclical research workflows where the workflow itself changes based on intermediate findings?
- What is the relationship between “knowledge engineer” and “information architect” in organizations that have both roles? Are they complementary, overlapping, or competing?

**Weakly supported claims:**
- Comparative performance of DuckDB vs. Polars vs. pandas is well-documented for specific benchmarks, but generalizability across diverse research datasets (heterogeneous schemas, messy text) is less clear.
- The claim that agent infrastructure is becoming commoditized is based on a single trade article; more primary evidence (product announcements, pricing models) is needed.
- Market position definitions are synthesized from job postings; actual role boundaries vary by organization and are not standardized.

**Missing categories:**
- **Evaluation and benchmarking**: There is no widely adopted framework for evaluating research-to-data pipelines end-to-end. Metrics for extraction precision, provenance completeness, and analytical validity are fragmented.
- **Human-in-the-loop patterns**: The literature acknowledges the need for human oversight but does not provide detailed interaction patterns or tooling.
- **Cost models**: The cost of LLM-based extraction, agent orchestration, and cloud storage is rarely discussed in comparative terms.

**Next most valuable searches or interviews:**
- Primary sources from DuckDB Labs, dbt Labs, MotherDuck, and Hex on their agent integration roadmaps.
- Job postings from research organizations (e.g., Allen Institute, Chan Zuckerberg Initiative, NIH) for research engineer and knowledge engineer roles.
- Technical reports from organizations implementing agent-based research pipelines (e.g., FutureHouse, Elicit, Consensus).
- Interviews with practitioners who have built research-to-data pipelines end-to-end.

---

## 7. Sources

1. **DuckDB System Architecture** — https://mintlify.wiki/duckdb/duckdb/concepts/architecture — Supports: DuckDB in-process architecture, core components (parser, planner, optimizer, execution engine), query flow, columnar storage, vectorized execution.
2. **DuckDB Introduction** — https://mintlify.wiki/duckdb/duckdb/introduction — Supports: DuckDB features (rich SQL dialect, in-process analytics, client libraries, extensibility, use cases).
3. **Codecentric: DuckDB vs. Polars vs. Pandas** — https://www.codecentric.de/en/knowledge-hub/blog/duckdb-vs-dataframe-libraries — Supports: Comparison of pandas, Polars, DuckDB across performance, memory, scalability, ergonomics, interoperability.
4. **Querio: The 9 Best DuckDB-Powered Analytics Tools** — https://querio.ai/articles/best-duckdb-powered-analytics-tools — Supports: Comparison of BI/analytics tools with DuckDB integration (MotherDuck, Hex, Jupyter, Evidence, Superset, Metabase, Lightdash, Observable, Preset).
5. **SciGraph-LLM (ACM)** — https://acm-stag.literatumonline.com/doi/10.1145/3779211.3793169 — Supports: Evidence-grounded extraction pipeline, schema-enforced prompts, provenance-aware knowledge graphs, evidence precision and claim F1 metrics.
6. **Multi-Agent AI Open-Source Ecosystem (ACL)** — https://aclanthology.org/2026.acl-long.971.pdf — Supports: LangGraph, CrewAI, AutoGen, MetaGPT frameworks; challenges in multi-agent coordination and verification.
7. **Provenance, Timestamp Evidence, and Source-Chain Auditability (Zenodo)** — https://zenodo.org/records/21330680 — Supports: Artifact classes and epistemic boundaries; provenance as evidence about artifacts, not proof of claims; W3C PROV.
8. **Systematic Review of Automation in Data Warehouse Design (Springer)** — https://link.springer.com/article/10.1186/s40537-026-01564-9 — Supports: ETL/ELT automation, Data Vault, medallion architecture, limitations with weakly structured sources.
9. **Research Engineer Job Posting (ZipRecruiter)** — https://www.ziprecruiter.com — Supports: Research engineer responsibilities in data acquisition, web scraping, extraction, NLP.
10. **Knowledge Engineer Job Posting (SmartRecruiters)** — https://jobs.smartrecruiters.com — Supports: Knowledge engineer responsibilities in ontology design, knowledge graphs, OWL/RDF, semantic modeling.
11. **Data Analyst Job Posting (Accel Job Board)** — https://jobs.accel.com — Supports: Data analyst requirements in SQL, Python/R, statistical analysis, visualization.
12. **AI Automation Specialist Job Posting (Upwork)** — https://www.upwork.com — Supports: AI automation specialist responsibilities in n8n, OpenClaw, LLMs, workflow automation.
13. **Information Architect Job Posting (ZipRecruiter)** — https://www.ziprecruiter.com — Supports: Information architect responsibilities in conceptual/logical/physical data models, governance, naming standards.
14. **dbt Documentation (dbt Labs)** — https://docs.getdbt.com — Supports: dbt as transformation layer in ELT; runs SQL transformations in warehouse.
15. **Jupyter Documentation (IBM Cloud)** — https://dataplatform.cloud.ibm.com — Supports: Jupyter notebook workflow (add data, create notebook, load/analyze, share).
16. **Camoufox Research (PyPI)** — https://pypi.org — Supports: Browser automation capabilities for research (read JS-heavy pages, extract tables, export structured data).
17. **MotherDuck Product Page** — https://motherduck.com — Supports: Cloud DuckDB warehouse features (serverless, MCP server, AI functions, agent-native ingest).
18. **Hex Product Page** — https://hex.tech — Supports: Collaborative data notebook with Notebook Agent; SQL + Python analysis.
19. **Evidence Documentation** — https://docs.evidence.dev — Supports: BI as code framework; SQL + Markdown; Evidence Core and Studio; agent-ready.
20. **Lightdash Documentation** — https://docs.lightdash.com — Supports: dbt-integrated BI; metrics in version-controlled YAML; semantic layer.
21. **Polars Lazy API Documentation** — https://docs.pola.rs — Supports: Lazy execution model; deferred computation; query optimization.
22. **ORKG (EOSC Association)** — https://eosc.eu — Supports: Open Research Knowledge Graph platform; FAIR scientific knowledge; research comparisons.
23. **CAS Intelligence Hub** — https://www.cas.org — Supports: Harmonized R&D knowledge environment; AI-supported knowledge platform.
24. **Sharpr (Dynata)** — https://www.dynata.com — Supports: AI-powered knowledge management for research and competitive intelligence.
25. **Agent Infrastructure Commoditization (Forkast)** — https://forkast.news — Supports: Managed agent runtimes, MCP standardization, databases as active participants in agentic workflows.
26. **Global Data Extraction Software Market Report** — https://www.marketresearch.com — Supports: Key players in data extraction software market (IBM, UiPath, Talend, Fivetran, etc.).

---

**Document status:** This brief is a synthesis of available evidence at the access date. Claims marked as “reported signal” or “inference” should be verified with primary sources before being treated as stable facts. The entity and relationship candidates are designed for later data modeling; distinct entities should not be merged solely to reduce row count.