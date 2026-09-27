---
title: Research-to-Data Capability Atlas
aliases:
  - Research-to-Data Atlas
  - Research-to-Data Capability Cluster
created: 2026-09-27
modified: 2026-09-27
status: evidence-grounded synthesis
parent: "[[Research-to-Data]]"
---

# Research-to-Data Capability Atlas

## 1. Executive synthesis

- The cluster is best modeled as a **socio-technical pipeline**, not a single profession or product: research produces evidence; extraction turns evidence into records; modeling and normalization make records comparable; databases make them queryable; analysis and visualization support interpretation; interpretation creates new research questions.
- The most important boundary is between **evidence** and **structured data**. A citation or source is not yet a normalized fact. A useful record needs a claim, source span, extraction method, schema, uncertainty, and provenance.
- **Research synthesis**, **information extraction**, **data modeling**, and **analysis** are distinct capabilities with different quality tests. They can be performed by one person, but they should remain separate entities in the atlas.
- **Pandas, Polars, and DuckDB overlap but are not interchangeable**: pandas is an in-memory Python DataFrame API; Polars is a DataFrame/query engine with a lazy optimizer; DuckDB is an analytical SQL database engine that can query files and tables.
- **ETL/ELT and lineage/provenance solve different problems**. ETL/ELT describes movement and transformation; lineage records what produced what; provenance can also represent agents, activities, sources, responsibility, and claim-level support.
- BI tools optimize for reusable metrics, dashboards, sharing, and decision support. Research notebooks optimize for exploration and narrative. Neither alone provides a complete evidence system.
- Agent systems are most useful as bounded operators with typed inputs/outputs and verification gates. Open-ended “research agents” are not a substitute for source selection, schema design, validation, or human interpretation.
- Role titles are weak ontology keys. Hiring signals are more stable when modeled as capabilities and outputs: SQL + metric definitions + dashboards differs from source criticism + synthesis, even when employers use “analyst” for both.
- A minimum viable atlas record should include: stable name, definition, workflow stage, inputs, outputs, tools, related entities, relationship type, source, evidence class, confidence, time sensitivity, and falsifier.
- Open questions include benchmark-quality evaluation for multi-source extraction, agent error propagation across pipeline stages, how claim-level provenance should join relational and graph stores, and which capabilities employers actually bundle under emerging AI-workflow titles.

## Boundary model

**Workflow boundary:** research → evidence → extraction → structured representation → normalization → database → query → analysis → visualization → interpretation → new research → agent iteration.

**Entity boundary:** Skill, Market Position, Technology, Software, Company, Product, Methodology, Workflow, Agent, Source, Claim, Dataset, Schema, and Metric are distinct. A product may implement a technology; a company may produce a product; a workflow may use both; a claim is supported by sources.

**Evidence classes:**

- `documented fact`: directly stated in primary documentation or a standard.
- `reported signal`: observed in job descriptions, vendor positioning, or market material; useful but biased or time-sensitive.
- `inference`: reasoned synthesis across sources.
- `recommendation`: proposed design choice for this atlas.

## 2. Lens findings

### 2.1 Skills

**Definition and scope.** A skill is a repeatable human or machine capability, not a tool name. The cluster contains research synthesis, source criticism, information extraction, schema/data modeling, ontology design, normalization, SQL, Python/DataFrames, visualization, provenance, and orchestration.

**Workflow position.** Synthesis governs research and interpretation; extraction governs evidence → records; modeling and normalization govern records → database; SQL/DataFrame skills govern query and analysis; visualization governs analysis → communication; provenance and orchestration govern the whole loop.

**Relationships.** `Skill used_in Workflow`; `Skill performed_by Market Position`; `Skill implemented_by Software or Technology`; `Skill evaluated_by Quality Gate`.

**Representative distinctions.** Research synthesis evaluates and combines sources. Information extraction identifies spans/entities/relations. Data modeling chooses entities, keys, grain, and constraints. Ontology design formalizes concepts and relations for interoperability. Normalization reduces duplication and update anomalies; it is not the same as cleaning. Provenance preserves lineage and justification; it is not the same as a bibliography.

**Trade-offs/failure modes.** Broad generalists move quickly but may hide quality debt. Highly formal schemas improve reuse but slow exploration. LLM extraction improves coverage but can hallucinate, collapse uncertainty, or lose source spans. SQL is auditable and composable; notebook-only work can be hard to reproduce.

**Evidence confidence:** High for the distinctions as synthesis; high for provenance vocabulary from W3C PROV-O; medium for market packaging.

### 2.2 Market positions

| Position | Primary question/output | Typical signals | Boundary |
|---|---|---|---|
| Data analyst | What happened and what should a decision-maker notice? | SQL, metrics, dashboards, stakeholder communication | Usually consumes governed data rather than designing research evidence systems |
| Research analyst | What does the evidence say about a defined question? | source evaluation, literature/market research, synthesis, reports | May not build durable data products |
| Knowledge engineer | How should domain concepts, facts, rules, and provenance be represented? | ontology, taxonomy, graph/semantic modeling, retrieval | More formal representation than ordinary reporting |
| BI/data analyst | How can repeatable business questions be answered and shared? | semantic metrics, dashboards, warehouse SQL, access controls | Optimizes operational decision support |
| Research engineer | How can a research method become a reliable computational system? | Python, APIs, experiment design, data pipelines, evaluation | Bridges research intent and production implementation |
| Automation specialist | Which repeatable process can be made deterministic? | APIs, browser automation, scripting, scheduling, error handling | Automation may move data without providing interpretation |
| AI/agent workflow specialist | Which bounded tasks can agents perform with tools and controls? | tool calling, schemas, evals, tracing, guardrails, orchestration | Emerging title; scope varies widely |
| Information architect | How should information be organized for findability and use? | taxonomy, metadata, navigation, content models | Focuses information structure and retrieval experience |

BLS describes operations research analysts as using mathematics and logic for organizational decisions, while its data-science profile emphasizes collecting, categorizing, and analyzing data. These are useful labor-market anchors, not complete definitions of every employer title. Hiring signals in the table are a synthesis from role patterns and should be validated against actual postings.

**Evidence confidence:** Medium. Stable conceptual differences; title boundaries are reported signals and time-sensitive.

### 2.3 Technology

- **Python:** general-purpose language for collection, transformation, analysis, APIs, automation, and agent glue code.
- **SQL:** declarative language for relational querying, joins, aggregation, constraints, and increasingly transformation/testing workflows.
- **DuckDB:** embedded analytical SQL database; strong for local files, columnar formats, and reproducible analytical queries.
- **pandas:** Python library centered on labeled Series/DataFrame structures and flexible data manipulation.
- **Polars:** DataFrame library with a Rust core and a lazy query graph enabling optimization and streaming patterns.
- **Notebooks:** interactive computational documents combining code, narrative, equations, and visual outputs; excellent for exploration, weaker as the sole production control plane.
- **APIs/scraping/browser automation:** acquisition mechanisms with different legality, stability, rate-limit, and provenance properties. An API is usually more stable than scraping; browser automation handles rendered interaction but is brittle and expensive.
- **LLMs/embeddings:** probabilistic language and similarity capabilities. They assist extraction, classification, retrieval, and synthesis but require schema validation and evidence checks.
- **Graphs/ontologies:** useful when relationships, identity, semantics, and provenance are first-class; relational models are often simpler for tabular facts and aggregates.
- **Formats:** CSV/JSON are accessible interchange formats; Parquet/Arrow improve typed, columnar interchange; JSON Schema validates structural constraints but does not prove truth.
- **Databases:** relational, document, graph, vector, and lakehouse systems optimize different access patterns. Storage choice should follow query and provenance requirements, not fashion.

**Evidence confidence:** High for documented tool capabilities; medium for comparative recommendations.

### 2.4 Software

| Software | Core job | Strength | Limitation / boundary |
|---|---|---|---|
| DuckDB | local/in-process analytical SQL | SQL over files and tables; portable | not a general multi-user warehouse control plane |
| pandas | Python tabular manipulation | ecosystem and exploratory flexibility | memory/performance and implicit state can become limits |
| Polars | fast DataFrame/query execution | lazy optimization, parallelism, Arrow-friendly | smaller ecosystem and different semantics from pandas |
| Jupyter | exploration and computational narrative | rapid iteration and explanation | execution order, environment, and hidden state need controls |
| dbt | SQL/Python transformations in a project | modular models, tests, docs, lineage | depends on an execution backend; not a source-research tool |
| Metabase | questions, models, dashboards, sharing | accessible BI and inspectable questions | semantic correctness still depends on modeled data |
| Superset | open-source BI exploration and dashboards | broad visualization/database connectivity | governance and semantic consistency require setup |
| Observable | reactive notebook/data visualization | interactive browser-based visual narratives | less suited to full ingestion/storage governance |
| Airflow | scheduled DAG orchestration | explicit tasks, dependencies, scheduling | orchestration is not data quality or business semantics |
| Playwright | browser automation | multi-browser interaction and assertions | selectors, authentication, and site changes create brittleness |
| OpenLineage | lineage event standard/platform | dataset/job/run model | lineage metadata does not itself verify values |
| Agent SDKs/frameworks | tool-using, stateful coordination | handoffs, guardrails, tracing, structured outputs | probabilistic behavior and framework churn |

**Evidence confidence:** High for official feature descriptions; medium for limitations because they are comparative synthesis.

### 2.5 Companies

The company lens should distinguish **employers**, **vendors**, **open-source foundations/projects**, **consultancies**, and **research organizations**.

- **Open-source projects/foundations:** DuckDB project, pandas project, Polars project, Apache Arrow, Jupyter, Apache Airflow, OpenLineage. They define or maintain reusable technology and standards; they are not interchangeable commercial vendors.
- **Vendors/product companies:** dbt Labs (analytics transformation workflow), Metabase (BI), Preset/Superset ecosystem (BI), MotherDuck (managed/cloud-adjacent DuckDB positioning), and model/platform providers that expose LLM or agent infrastructure. Vendor pages document positioning, not neutral performance.
- **Employers:** any organization with research, analytics, data platform, knowledge management, or automation teams may hire into this cluster. The same employer may use different titles for similar work.
- **Consultancies/integrators:** package data modeling, BI implementation, research operations, or automation as client services; their outputs are often systems plus operating procedures rather than a single product.
- **Research organizations:** universities, public laboratories, standards bodies, and applied research groups often advance provenance, ontology, evaluation, and domain-specific extraction.

**Evidence confidence:** Medium. Categories are stable; individual company strategy, hiring, and product scope are time-sensitive.

### 2.6 Products

A product is a user-facing or deployable solution to a workflow problem. Record its **user**, **input**, **output**, **workflow position**, **integration surface**, **differentiator**, and **failure mode**.

- Research platforms: discovery, source collection, annotation, synthesis, and citation management. They reduce search/reading friction but may not create normalized datasets.
- Extraction tools: convert PDFs, webpages, or documents into structured fields. Their key differentiator is coverage/accuracy plus source-span traceability and schema control.
- Data transformation products: implement repeatable SQL/Python models, tests, documentation, and lineage. They govern transformation rather than primary research judgment.
- BI products: expose modeled data as questions, metrics, dashboards, alerts, and reports. They optimize access and communication rather than source criticism.
- Knowledge systems: organize documents, entities, concepts, and relations for retrieval and reasoning. Their risk is semantic drift and weak fact provenance.
- Agent infrastructure: supplies tools, state, handoffs, guardrails, tracing, and evaluation. It coordinates work but does not automatically make outputs correct.

**Evidence confidence:** Medium; official product descriptions are strong for intended use, weak for universal superiority claims.

### 2.7 Methodologies

- **Research protocol:** explicit question, scope, search strategy, inclusion/exclusion criteria, source evaluation, extraction plan, synthesis, and update policy.
- **Information extraction:** identify fields, entities, relations, claims, quantities, and evidence spans from unstructured sources; preserve offsets and source identifiers.
- **Data modeling:** define entities, relationships, grain, keys, constraints, types, and semantic definitions before scaling ingestion.
- **Normalization:** de-duplicate and structure data to reduce anomalies; also includes entity resolution, units, dates, controlled vocabularies, and null semantics.
- **ETL/ELT:** move and transform data. ETL transforms before loading; ELT loads raw data before transforming in the target engine. Modern analytics commonly favors ELT when the target engine is capable.
- **Evidence/provenance:** link claims and derived records to source artifacts, extraction activities, agents, timestamps, transformations, and confidence. W3C PROV models entities, activities, and agents; OpenLineage specializes in dataset/job/run lineage.
- **Analytical workflow:** question → operational definition → data selection → query/model → validation → analysis → visualization → interpretation → decision or new question.

**Evidence confidence:** High for formal standards and documented methods; medium for the recommended combined protocol.

### 2.8 Workflows

The workflow is a feedback system, not a one-way conveyor belt. Every output should be able to point backward to inputs and forward to decisions or new research. See the detailed map below.

**Evidence confidence:** High as a reference architecture; implementation choices are recommendations.

### 2.9 Agents

| Agent role | Task | Required state/tools | Verification | Main failure mode |
|---|---|---|---|---|
| Research agent | search, compare, and collect candidate sources | browser/search, source ledger, query plan | source relevance, date, independence | shallow or circular sourcing |
| Extraction agent | map passages/documents to a schema | parser/OCR, LLM, JSON Schema, offsets | field-level source span and type checks | hallucinated or truncated fields |
| Cleaning agent | standardize units, dates, names, categories | mapping tables, deterministic code, entity resolver | before/after counts, exception queue | silent coercion and over-merging |
| Coding agent | write queries, transformations, tests, visualizations | repository, runtime, sample data, test runner | tests, explain plan, diff review | code that runs but encodes wrong grain |
| Analytical agent | calculate, compare, model, and explain patterns | database/notebook, metric definitions | independent recomputation, uncertainty checks | causal overclaim or denominator error |
| Visualization agent | choose chart and encode result | chart library, accessibility rules, metric metadata | label/source/scale review | misleading scale or decoration |
| Orchestrator | sequence agents and route exceptions | state machine/DAG, traces, retries, approvals | handoff contracts and audit log | compounding upstream errors |

Agents should be modeled as performers of bounded workflow steps: `Agent performs WorkflowStep`, `Agent uses Tool`, `Agent produces Artifact`, `Agent is verified_by QualityGate`.

## 3. Workflow map

| Stage | Inputs | Activities | Outputs | Quality checks | Likely tools | Suitable agent role |
|---|---|---|---|---|---|---|
| Research | question, scope, prior notes | search, source selection, protocol | source set, research log | relevance, coverage, independence | browser, APIs, citation manager | research agent |
| Evidence | source artifacts | identify passages, figures, tables, claims | evidence spans, source metadata | exact location, access date, version | PDF/web readers, OCR | research/extraction agent |
| Extraction | evidence spans, schema | classify, parse, extract fields/relations | raw records with provenance | schema validity, no unsupported fields | Python, LLM, JSON Schema | extraction agent |
| Structured representation | raw records | assign entity/claim types and relations | typed objects/JSON/rows/graph triples | required fields, stable IDs | JSON Schema, RDF/SQL | extraction/modeling agent |
| Normalization | typed records | units, dates, names, categories, identity resolution | canonical records + exceptions | duplicate rate, referential integrity | pandas/Polars/DuckDB, mapping tables | cleaning agent |
| Database | canonical records, raw archive | load, index, partition, snapshot | queryable tables/graph/files | counts, constraints, lineage | DuckDB, PostgreSQL, lakehouse | coding/data engineer agent |
| Query | schema, question, metric definitions | filter, join, aggregate, window, search | result set and query artifact | grain, nulls, denominator, reproducibility | SQL, DuckDB, dbt | coding/analytical agent |
| Analysis | result set, assumptions | describe, compare, model, test sensitivity | findings, uncertainty, derived tables | independent check, alternatives, confounding | pandas/Polars, notebooks | analytical agent |
| Visualization | findings, metadata | select chart, encode, annotate, publish | chart/dashboard/report | truthful scale, accessibility, provenance | Jupyter, Metabase, Superset, Observable | visualization agent |
| Interpretation | evidence, analysis, context | explain limits, implications, decisions | claim set, recommendation, open questions | claim-evidence fit, uncertainty | report/wiki/meeting | analyst/researcher + human review |
| New research | gaps, anomalies, failed checks | refine question and search protocol | next research plan | explicit falsifier and stopping rule | research tools | research agent |
| Agent iteration | traces, evaluations, corrections | update prompts, tools, schemas, gates | improved workflow version | regression set, error taxonomy | orchestrator, eval harness | orchestrator + human owner |

### Quality gates

1. **Source gate:** source is identifiable, relevant, accessible, and not merely duplicated.
2. **Evidence gate:** every important field/claim has a source span or explicit “inference” label.
3. **Schema gate:** records validate against the schema and preserve unknowns rather than inventing values.
4. **Normalization gate:** units, dates, identities, and controlled vocabulary transformations are logged.
5. **Query gate:** grain, joins, denominators, and null handling are explicit.
6. **Interpretation gate:** conclusions distinguish correlation, description, causal claim, and recommendation.
7. **Iteration gate:** corrections become test cases or protocol changes rather than disappearing in chat history.

## 4. Entity and relationship candidates

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
|---|---|---|---|---|---|---|---|
| Skill | Research synthesis | Combine evaluated sources into a bounded answer | Research/Interpretation | Source, Claim, Market Position | used_in; produces | Inference from research protocol | Medium |
| Skill | Information extraction | Convert source content into fields, entities, relations, or claims | Evidence/Extraction | Source, Schema, Agent | transforms; constrained_by | JSON Schema; inference | High |
| Skill | Data modeling | Define entities, grain, keys, relations, constraints | Structured representation/Database | Schema, Database, Workflow | governs; implemented_by | Inference | High |
| Skill | Provenance capture | Preserve source, activity, agent, time, and derivation links | All stages | Source, Claim, Agent, Artifact | supports; traces | W3C PROV-O | High |
| Market Position | Data analyst | Decision-facing analysis and communication | Query/Analysis/Visualization | Skill, Software, Product | appears_in; performs | BLS + synthesis | Medium |
| Market Position | Research analyst | Evidence-centered question answering and synthesis | Research/Interpretation | Source, Claim, Skill | performs | BLS-adjacent synthesis | Medium |
| Market Position | Knowledge engineer | Formal domain representation and reasoning support | Modeling/Database | Ontology, Graph, Claim | designs; governs | Inference | Medium |
| Technology | SQL | Declarative language for relational data operations | Database/Query | DuckDB, dbt, Database | implemented_by; uses | DuckDB docs | High |
| Technology | Columnar interchange | Typed column-oriented memory/file interchange | Structured/Database | Arrow, pandas, Polars, DuckDB | enables_interoperability | Apache Arrow | High |
| Technology | Browser automation | Programmatic interaction with rendered web pages | Research/Extraction | Playwright, Agent | implemented_by; used_in | Playwright docs | High |
| Technology | Embeddings | Vector representations used for similarity/retrieval | Research/Query | LLM, Vector store, Product | supports | General technical definition; medium | Medium |
| Software | DuckDB | Embedded analytical SQL database system | Database/Query/Analysis | SQL, Arrow, Workflow | implements; used_in | DuckDB docs | High |
| Software | pandas | Python DataFrame/data analysis library | Normalization/Analysis | Python, Jupyter | implements; used_in | pandas docs | High |
| Software | Polars | Rust-based DataFrame/query library with lazy execution | Normalization/Analysis | Arrow, Python | implements; used_in | Polars docs | High |
| Software | dbt | Transformation project framework with models/tests/docs/lineage | Normalization/Database | SQL, Warehouse, OpenLineage | governs; implements | dbt docs | High |
| Software | Jupyter | Interactive computational document environment | Analysis/Visualization | Python, Notebook, Agent | hosts; produces | Jupyter docs | High |
| Software | Airflow | DAG workflow orchestration platform | Agent iteration/Operations | Task, Workflow, Agent | orchestrates | Airflow docs | High |
| Software | OpenLineage | Open lineage collection model/platform | Database/Iteration | Dataset, Job, Run | records | OpenLineage docs | High |
| Methodology | ETL | Transform before loading into target | Extraction/Database | Workflow, Software | governs | Standard industry distinction; medium | Medium |
| Methodology | ELT | Load raw data then transform in target engine | Extraction/Database | DuckDB, dbt, Database | governs | dbt positioning + synthesis | Medium |
| Methodology | Normalization | Reduce redundancy and standardize semantics | Structured/Database | Schema, Record, Entity | governs | Data-modeling synthesis | High |
| Methodology | Evidence ledger | Claim/source/span/status register | Evidence/Interpretation | Claim, Source | governs; supports | Recommendation | Medium |
| Workflow | Research-to-data loop | Feedback loop from question to structured analysis and new research | All | all entities | contains; iterates | User-provided architecture | High |
| Agent | Extraction agent | Bounded agent producing schema-valid records from evidence | Extraction | Source, Schema, Artifact | performs; produces | Agent SDK + synthesis | Medium |
| Agent | Orchestrator | Coordinates steps, state, tools, retries, and approvals | All | Workflow, Agent, Quality Gate | orchestrates; routes | Airflow/OpenAI SDK | High |
| Product | BI dashboard | Shareable interactive view of modeled metrics | Visualization | Metabase, Superset, Metric | visualizes; communicates | Metabase docs | High |
| Product | Knowledge system | Searchable/relational representation of concepts and claims | Database/Query | Ontology, Graph, Source | stores; supports | Synthesis | Medium |
| Company type | Open-source foundation/project | Maintains reusable software or standard | Technology/Software | Company, Software | produces; maintains | Project docs | High |
| Source | Primary documentation | First-party specification or product documentation | All | Claim | supports | Source rules | High |
| Claim | Derived finding | A statement produced from records or analysis | Interpretation | Source, Dataset, Methodology | supported_by; derived_from | W3C PROV-O conceptually | High |

## 5. Comparison tables

### Relational, DataFrame, and graph choices

| Criterion | Relational/SQL | DataFrame | Property graph/RDF |
|---|---|---|---|
| Best for | repeatable joins, constraints, aggregates | exploration and in-process transformations | rich relationships, identity, semantics, provenance |
| Primary unit | table/row/column | Series/DataFrame | node/edge/triple |
| Strength | declarative, auditable, composable | interactive, expressive Python | explicit relationships and ontology alignment |
| Risk | poor modeling creates join/metric errors | hidden state and memory limits | complexity, identity resolution, query learning curve |
| Good fit here | canonical facts and metrics | extraction cleanup and analysis | claims, concepts, source relations, provenance |

### Methodology maturity levels

| Level | Characteristics | Typical controls |
|---|---|---|
| Ad hoc | browser tabs, copied notes, one-off scripts | manual citation and spot checks |
| Repeatable | documented queries/scripts, stable folders, schemas | version control, validation, run log |
| Governed | tested models, lineage, data contracts, source ledger | CI, quality gates, ownership, snapshots |
| Agentic | bounded agents with typed handoffs and evaluation | traces, guardrails, regression set, human approval |
| Adaptive | workflow learns from corrections and new evidence | feedback metrics, drift detection, protocol updates |

### Claim status model

| Status | Meaning | Required evidence |
|---|---|---|
| Documented fact | source directly states it | URL, title, publisher, date/access date |
| Reported signal | market/vendor/job evidence suggests it | multiple independent signals where important |
| Inference | reasoned synthesis | premises and uncertainty stated |
| Recommendation | proposed design choice | rationale, trade-off, falsifier |

## 6. Research gaps and next investigations

- Collect a dated sample of job postings for the named roles and code responsibilities, outputs, and tools separately from titles.
- Benchmark extraction agents on a shared corpus with field-level source spans, abstention, uncertainty, and schema-validity metrics.
- Compare relational claim stores, RDF/PROV-K, and property graphs for multi-source support/conflict and temporal updates.
- Test when DuckDB, Polars, pandas, or a warehouse is the best boundary for datasets that exceed memory or require concurrency.
- Investigate how BI semantic layers preserve claim-level provenance rather than only table/column lineage.
- Build an error taxonomy for the full loop: source bias, missing evidence, extraction hallucination, entity over-merging, join explosion, denominator error, visualization distortion, and causal overclaim.
- Interview practitioners in research operations, analytics engineering, knowledge engineering, and agent workflow design to discover unrepresented hybrid positions.
- Verify legal, ethical, and access constraints for scraping and browser automation in each target domain.
- Falsifier for the central architecture: if a simpler workflow without explicit schemas/provenance produces equal or better independently audited results across representative tasks, the recommended governance overhead is excessive.

## 7. Sources

Access date for all sources below: **2026-09-27**.

1. W3C, **PROV-O: The PROV Ontology** (2013): https://www.w3.org/TR/prov-o/ — provenance entities, activities, agents, and relations.
2. W3C, **PROV-DM: The PROV Data Model** (2013): https://www.w3.org/TR/prov-dm/ — use and production of entities by activities influenced by agents.
3. W3C, **Data Catalog Vocabulary (DCAT) v3** (2024): https://www.w3.org/TR/vocab-dcat-3/ — interoperable dataset/catalog vocabulary.
4. DuckDB, **Why DuckDB / Documentation**: https://duckdb.org/why_duckdb.html and https://duckdb.org/docs/current/ — analytical SQL engine and file/data connectivity.
5. pandas, **User Guide**: https://pandas.pydata.org/docs/user_guide/index.html — Series/DataFrame concepts and data manipulation.
6. Polars, **User Guide**: https://docs.pola.rs/ — DataFrame library; lazy API and query optimization.
7. Apache Arrow, **Apache Arrow**: https://arrow.apache.org/ — columnar format and multi-language analytical interchange.
8. Jupyter, **Documentation**: https://docs.jupyter.org/ — interactive environment for code, narrative, exploration, and visualization.
9. dbt, **What is dbt?**: https://docs.getdbt.com/docs/introduction — collaborative SQL/Python transformation, testing, documentation, and lineage positioning.
10. Metabase, **Documentation**: https://www.metabase.com/docs/latest/ — questions, models, dashboards, sharing, and embedded analytics workflows.
11. Apache Airflow, **Core concepts / DAGs**: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html — tasks, dependencies, schedules, and workflow DAGs.
12. OpenLineage, **Home and Object Model**: https://openlineage.io/ and https://openlineage.io/docs/spec/object-model/ — open model for datasets, jobs, runs, and lineage events.
13. JSON Schema, **Specification**: https://json-schema.org/specification — structural validation and interoperability for JSON instances.
14. Playwright, **Official documentation**: https://playwright.dev/ — browser automation, multi-browser support, actions, and assertions.
15. OpenAI Agents SDK, **Agents and tracing**: https://openai.github.io/openai-agents-python/agents/ and https://openai.github.io/openai-agents-python/tracing/ — agents with tools, handoffs, guardrails, structured outputs, and traces.
16. NIST, **AI Risk Management Framework: Generative AI Profile** (2024): https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence — risk-management context for generative AI, including content provenance concerns.
17. U.S. Bureau of Labor Statistics, **Operations Research Analysts**: https://www.bls.gov/ooh/math/operations-research-analysts.htm — occupational description for decision-oriented analytical work.
18. U.S. Bureau of Labor Statistics, **Data Scientists**: https://www.bls.gov/ooh/math/data-scientists.htm — data collection, categorization, analysis, and algorithmic work.
19. O*NET OnLine, **Career exploration and job analysis**: https://www.onetonline.org/ — occupational task, skill, and knowledge taxonomy; used as a labor-market classification reference.
20. Existing vault note, **PROV-K Ontology – Detailed Overview**: [[PROV-K Ontology – Detailed Overview]] — local synthesis of multi-source knowledge provenance, support/conflict, trust, and truth values.
21. Existing vault note, **The components to investigate**: [[The components to investigate]] — user-provided scope, lenses, workflow, and initial relationship candidates.

## Modeling recommendation

Use a claim-centric relational core plus optional graph projections:

- `source(source_id, uri, title, publisher, published_at, accessed_at, source_type)`
- `claim(claim_id, text, status, confidence, created_at, supersedes_claim_id)`
- `evidence(evidence_id, source_id, locator, quote_or_span, captured_at)`
- `claim_support(claim_id, evidence_id, relation=supports|conflicts|contextualizes)`
- `entity(entity_id, entity_type, canonical_name, definition, valid_from, valid_to)`
- `relation(subject_id, predicate, object_id, claim_id)`
- `artifact(artifact_id, type, uri, checksum, produced_by_activity_id)`
- `workflow_run(run_id, workflow_id, started_at, ended_at, status)`
- `activity(activity_id, type, agent_id, input_artifact_id, output_artifact_id)`
- `quality_check(check_id, artifact_id, rule, result, reviewer, checked_at)`

This design preserves source-grounded claims while allowing projections into DuckDB/SQL for analysis, notebooks for exploration, BI for communication, and RDF/graph forms for semantic traversal and provenance.

## Notes on uncertainty and source bias

Official documentation is strongest for definitions and intended capabilities, but it is not independent evidence of performance, cost, adoption, or superiority. BLS/O*NET provide occupational categories rather than employer-specific title semantics. Vendor product pages describe positioning. The role taxonomy, maturity model, failure modes, and recommended schema are synthesis/recommendation and should be revised when job-posting samples, user interviews, or benchmark results provide contrary evidence.
