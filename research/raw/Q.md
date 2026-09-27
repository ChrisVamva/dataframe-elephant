---
modified: 2026-09-27T15:18:08+03:00
---
# Research-to-Data Capability Atlas

## 1. Executive Synthesis

*   **Agentic Extraction Supersedes Fragile Scraping**: The research-to-data workflow is transitioning from hardcoded DOM selectors to vision-language model (VLM) driven browser automation. Tools like Skyvern demonstrate that LLMs paired with computer vision can adapt to dynamic web structures, yielding higher reliability in market research extraction without custom scripting [[1], [10]].
*   **Role Specialization is Fragmenting**: "Knowledge Engineer" and "AI Agent Workflow Specialist" are emerging as distinct, high-leverage roles. The former focuses on ontology design and semantic grounding, while the latter orchestrates multi-agent tool-calling and state management, bridging the gap between traditional data engineering and applied AI [[43], [51]].
*   **Local Analytical Engines are Reshaping Data Prep**: DuckDB and Polars have functionally displaced Pandas for intermediate-to-large scale local data processing. DuckDB excels in SQL-first, on-disk analytics, while Polars dominates lazy-evaluated DataFrame transformations, though Pandas remains the interoperability standard for final-mile analysis [[11], [18]].
*   **Provenance is a First-Class Requirement**: Regulatory and operational demands (e.g., EU AI Act, FDA real-world evidence guidelines) mandate per-fact provenance. Systems are shifting from "best-effort" extraction to auditable pipelines using frameworks like PROV-AGENT and the Model Context Protocol (MCP) [[21], [25]].
*   **Ontology is the Kernel of Agent Coherence**: Ontology design is no longer purely academic; it is the necessary scaffolding for high-throughput, schema-based LLM extraction. Without explicit ontological boundaries, agentic workflows degrade into hallucinated or unalignable outputs [[33], [35]].
*   **Workflow Decomposition is Mandatory**: Monolithic "do-it-all" agent prompts are failing at scale. Successful architectures decompose workflows into specialized agents (extraction, cleaning, analytical, orchestration) with explicit handoffs, state verification, and fallback mechanisms [[19], [58]].

---

## 2. Lens Findings

### 2.1 Skills
*   **Definition & Scope**: The cognitive and technical capabilities required to transform unstructured inquiry into structured, queryable knowledge. Includes research synthesis, information extraction, data modeling, ontology design, normalization, SQL, DuckDB, pandas, visualization, provenance tracking, and agent orchestration.
*   **Workflow Position**: Cross-cutting; applied at every stage from initial research design to final visualization.
*   **Relationships**: `used_in` → Workflow; `required_by` → Market Position.
*   **Trade-offs & Failure Modes**: Over-indexing on advanced orchestration skills without foundational data modeling leads to fragile, unmaintainable agent pipelines. 
*   **Evidence Confidence**: High (documented fact across multiple 2025–2026 job descriptions and technical benchmarks) [[11], [43]].

### 2.2 Market Positions
*   **Definition & Scope**: Distinct professional roles with non-overlapping primary responsibilities. 
    *   *Knowledge Engineer*: Designs semantic frameworks and ontologies to ground AI reasoning [[44]].
    *   *AI Agent Workflow Specialist*: Architects multi-agent systems, tool-calling sequences, and state management [[51]].
    *   *Data/BI Analyst*: Queries existing structured data to build dashboards and derive business insights; minimal involvement in raw extraction or ontology design [[29]].
*   **Workflow Position**: Knowledge Engineers govern *Structured Representation*; Workflow Specialists govern *Agent Iteration*; Analysts govern *Analysis* and *Visualization*.
*   **Relationships**: `performs` → Workflow Stage; `requires` → Skills.
*   **Trade-offs & Failure Modes**: Conflating "Data Analyst" with "AI Agent Workflow Specialist" results in under-resourced automation projects, as the latter requires software engineering and systems thinking beyond traditional BI tooling.
*   **Evidence Confidence**: High (reported signal from 2025–2026 hiring trends) [[42], [51]].

### 2.3 Technology
*   **Definition & Scope**: The foundational protocols, languages, and computational paradigms. Includes Python, SQL, DuckDB, pandas, notebooks, APIs, scraping, browser automation, LLMs, embeddings, graph technologies, and data formats (Parquet, JSONL).
*   **Workflow Position**: The substrate upon which all software and agents are built.
*   **Relationships**: `implemented_by` → Software; `used_by` → Agents.
*   **Trade-offs & Failure Modes**: Relying solely on LLM APIs for extraction without deterministic fallbacks (e.g., regex or schema validation) introduces non-deterministic failure modes and cost volatility.
*   **Evidence Confidence**: High (documented fact) [[13], [39]].

### 2.4 Software
*   **Definition & Scope**: The executable applications and libraries. Includes DuckDB, pandas, Polars, Jupyter, dbt, Metabase, Superset, Observable, and specialized extraction tools like Skyvern (which uses LLMs and computer vision to automate browser tasks without predefined scripts) [[9], [10]].
*   **Workflow Position**: Maps directly to workflow stages (e.g., Skyvern for *Extraction*, dbt for *Normalization*, DuckDB for *Database/Query*, Metabase for *Visualization*).
*   **Relationships**: `produced_by` → Company; `supports` → Workflow.
*   **Trade-offs & Failure Modes**: Tool sprawl. Using Polars for simple tasks introduces unnecessary complexity, while using Pandas for >10GB datasets causes out-of-memory crashes [[12]].
*   **Evidence Confidence**: High (documented fact, benchmarked) [[11], [16]].

### 2.5 Companies
*   **Definition & Scope**: Entities hiring for, selling, or building around these capabilities. Includes open-source foundations (DuckDB Foundation), vendors (dbt Labs, Skyvern), consultancies (Accenture), and research organizations (Hill Research) [[37], [43]].
*   **Workflow Position**: Provide the tools, infrastructure, or labor that `produces` Software or `employs` Market Positions.
*   **Relationships**: `produces` → Product; `employs` → Market Position.
*   **Trade-offs & Failure Modes**: Vendor lock-in with proprietary "end-to-end" AI research platforms that obscure data provenance and prevent local export.
*   **Evidence Confidence**: Medium (reported signal, subject to market volatility) [[42], [46]].

### 2.6 Products
*   **Definition & Scope**: Specific solutions addressing user problems. 
    *   *Skyvern*: Browser automation for form-heavy, no-code market research extraction [[5]].
    *   *dbt*: Transformation workflow for normalization and testing.
    *   *Observable*: Interactive, notebook-based environments supporting agent-assisted data exploration.
*   **Workflow Position**: Occupy specific nodes in the workflow (e.g., Skyvern at *Extraction*, dbt at *Normalization*).
*   **Relationships**: `solves` → User Problem; `used_in` → Workflow.
*   **Trade-offs & Failure Modes**: Products marketing "fully autonomous research" often fail at edge cases, requiring human-in-the-loop verification gates.
*   **Evidence Confidence**: High (documented fact from product documentation) [[5], [10]].

### 2.7 Methodologies
*   **Definition & Scope**: Formalized procedures and frameworks. Includes ETL/ELT, ontology-as-a-kernel, schema-based LLM extraction, append-only data models, and hybrid GraphRAG (Retrieval-Augmented Generation) [[33], [41]].
*   **Workflow Position**: `governs` → Workflow. Dictates how stages are connected and validated.
*   **Relationships**: `enforces` → Quality Checks; `requires` → Skills.
*   **Trade-offs & Failure Modes**: Strict ontology-as-a-kernel methodologies slow initial prototyping but prevent catastrophic schema drift in production.
*   **Evidence Confidence**: Medium (inference from recent academic and industry publications) [[33], [41]].

### 2.8 Workflows
*   **Definition & Scope**: The ordered sequence of operations: Research → Evidence → Extraction → Structured representation → Normalization → Database → Query → Analysis → Visualization → Interpretation → New research → Agent iteration.
*   **Workflow Position**: The central spine of the atlas.
*   **Relationships**: `composed_of` → Stages; `uses` → Technology.
*   **Trade-offs & Failure Modes**: Linear workflows fail in dynamic research environments; iterative, cyclical workflows with feedback loops are required for agent correction.
*   **Evidence Confidence**: High (documented fact, synthesized from data engineering and AI agent literature) [[19], [39]].

### 2.9 Agents
*   **Definition & Scope**: Autonomous or semi-autonomous software entities performing specific workflow steps. Includes research agents (hypothesis generation), extraction agents (parsing), data-cleaning agents (normalization), analytical agents (SQL generation), and orchestration agents (routing and state management).
*   **Workflow Position**: `performs` → Workflow Stage.
*   **Relationships**: `uses` → Technology; `managed_by` → AI Agent Workflow Specialist.
*   **Trade-offs & Failure Modes**: Orchestration agents introduce latency and complicate debugging. Failure modes include infinite loops, tool-calling hallucinations, and state corruption.
*   **Evidence Confidence**: Medium (reported signal, rapidly evolving) [[19], [22]].

---

## 3. Workflow Map

| Stage | Inputs | Activities | Outputs | Quality Checks | Likely Tools | Suitable Agent Roles |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Research** | Research question, domain constraints | Define scope, identify sources, design extraction schema | Research protocol, target URLs, ontology draft | Peer review, scope feasibility check | Perplexity, Consensus, Jupyter | Research Agent (scoping) |
| **Evidence** | Target URLs, documents, APIs | Retrieve raw content, handle authentication, manage rate limits | Raw HTML, PDFs, JSON payloads | HTTP status validation, completeness check | Skyvern, Firecrawl, Playwright | Extraction Agent (fetching) |
| **Extraction** | Raw content, extraction schema | Parse unstructured data into structured fields using LLMs or selectors | Semi-structured JSON, tabular data | Schema validation, confidence scoring | Skyvern, LlamaIndex, LangChain | Extraction Agent (parsing) |
| **Structured Rep.**| Semi-structured data | Map extracted fields to canonical ontology, resolve entities | Ontology-grounded records | Entity resolution checks, duplicate detection | Graph databases, Python scripts | Data-Cleaning Agent |
| **Normalization** | Ontology-grounded records | Standardize formats (dates, currencies), handle nulls, apply business logic | Clean, typed tabular data | dbt tests, Great Expectations assertions | dbt, Polars, DuckDB | Data-Cleaning Agent |
| **Database** | Clean, typed data | Ingest into analytical store, index for query performance | Queryable tables, materialized views | Row count validation, checksum verification | DuckDB, MotherDuck, PostgreSQL | Coding Agent (pipeline setup) |
| **Query** | Analytical store, user question | Translate natural language or analytical intent into executable queries | Result sets, intermediate DataFrames | SQL syntax validation, execution time limits | DuckDB, pandas, SQLMesh | Analytical Agent (Text-to-SQL) |
| **Analysis** | Result sets | Statistical testing, trend identification, cohort comparison | Analytical insights, metrics | Statistical significance checks, outlier detection | pandas, Polars, SciPy | Analytical Agent |
| **Visualization** | Analytical insights | Map data to visual encodings (charts, graphs) | Dashboards, static plots | Visual clarity, axis labeling, accessibility | Metabase, Superset, Observable | Analytical Agent (plotting) |
| **Interpretation**| Dashboards, plots | Contextualize findings, identify limitations, formulate conclusions | Research report, executive summary | Fact-checking against source provenance | Jupyter, Word, Notion | Research Agent (synthesis) |
| **New Research** | Research report, gaps | Identify missing data, formulate follow-up questions | Updated research protocol | Relevance to original objective | N/A | Human researcher, Research Agent |
| **Agent Iteration**| Execution logs, error traces | Refine prompts, update schemas, adjust tool parameters | Updated agent configurations | Regression testing on historical data | LangSmith, Arize Phoenix | Orchestration Agent |

---

## 4. Entity and Relationship Candidates

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Skill | Ontology Design | The practice of defining formal representations of concepts and relationships within a domain. | Structured representation | Knowledge Engineer, Agent | `required_by`, `governs` | Documented fact [[33]] | High |
| Market Position | AI Agent Workflow Specialist | Professional focused on designing, developing, and optimizing agentic workflows and multi-agent orchestration. | Agent iteration | Orchestration Agent, Software | `performs`, `manages` | Reported signal [[51]] | High |
| Technology | Computer Vision (in automation) | Use of VLMs to interpret visual DOM structures for robust web interaction without hardcoded selectors. | Extraction | Skyvern, Browser Automation | `implemented_by`, `enables` | Documented fact [[2], [9]] | High |
| Software | Skyvern | AI-driven browser automation platform using LLMs and computer vision for reliable web workflows. | Extraction | Market Research, Python | `used_in`, `produced_by` (Skyvern Inc.) | Documented fact [[1], [10]] | High |
| Software | DuckDB | In-process analytical OLAP database optimized for fast SQL queries on local or remote data files. | Database, Query | Polars, pandas | `alternative_to`, `integrates_with` | Documented fact [[11], [14]] | High |
| Methodology | Schema-based LLM Extraction | Using strict JSON schemas or Pydantic models to constrain LLM outputs during information extraction. | Extraction | Ontology Design, Extraction Agent | `governs`, `improves` | Documented fact [[27], [39]] | High |
| Agent | Orchestration Agent | An agent responsible for routing tasks, managing state, and handling handoffs between specialized agents. | Agent iteration | AI Agent Workflow Specialist, Tool API | `coordinates`, `manages_state` | Inference [[19], [22]] | Medium |
| Skill | Provenance Tracking | The capability to log and trace the origin, transformation, and reasoning steps of every data point. | Cross-cutting | Regulatory Compliance, Database | `ensures`, `required_by` | Documented fact [[21], [25]] | High |

---

## 5. Comparison Tables

### 5.1 Market Positions: Boundaries and Responsibilities
| Role | Primary Purpose | Core Inputs | Core Outputs | Integration Surface | Maturity in Market |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Data/BI Analyst** | Derive business insights from existing structured data. | SQL databases, BI dashboards, clean datasets. | Reports, dashboards, KPI tracking. | Metabase, Tableau, SQL, Excel. | High (Established) |
| **Knowledge Engineer** | Structure domain knowledge to make it machine-reasonable. | Unstructured domain docs, business logic, ontologies. | Knowledge graphs, schema definitions, embedding strategies. | Graph DBs, LLM APIs, Vector stores. | Medium (Rapidly growing) [[44], [49]] |
| **AI Agent Workflow Specialist** | Architect and maintain multi-step, multi-agent automated systems. | API documentation, workflow requirements, agent logs. | Deployed agent pipelines, orchestration graphs, fallback logic. | LangChain, Skyvern, MCP, Cloud functions. | Low-Medium (Emerging) [[51], [53]] |

### 5.2 Technology/Software: Local Data Processing Stack
| Tool | Primary Paradigm | Best Use Case | Memory/Performance Profile | Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Pandas** | In-memory DataFrame | Final-mile analysis, ecosystem compatibility (ML libs). | High memory usage; crashes on >RAM datasets [[12]]. | Not designed for out-of-core or lazy evaluation. |
| **Polars** | Lazy/Streaming DataFrame | High-speed transformations, ETL preprocessing. | Extremely fast, memory-efficient via Rust backend [[16]]. | Steeper learning curve; smaller ecosystem than Pandas. |
| **DuckDB** | In-process OLAP SQL | Complex aggregations, joining large Parquet/CSV files directly. | Exceptional speed for analytical queries; out-of-core capable [[11]]. | Less suited for complex, row-by-row imperative Python logic. |

### 5.3 Agent Archetypes in Research-to-Data Workflows
| Agent Type | Task Performed | Required Tools/State | Verification Method | Primary Failure Mode |
| :--- | :--- | :--- | :--- | :--- |
| **Extraction Agent** | Parse raw web/DOC content into structured JSON. | Browser context (e.g., Skyvern), JSON schema. | Schema validation, confidence thresholding. | Hallucination on ambiguous text; infinite retry loops. |
| **Data-Cleaning Agent** | Normalize formats, impute missing values, resolve entities. | Pandas/Polars, DuckDB, ontology mapping rules. | Great Expectations tests, row-count checks. | Over-aggressive imputation destroying signal. |
| **Analytical Agent** | Generate SQL or Python code to answer specific queries. | Database schema (via MCP), execution sandbox. | Dry-run SQL, unit tests on sample data. | Hallucinated column names; inefficient Cartesian joins. |
| **Orchestration Agent** | Route tasks, manage retries, aggregate final outputs. | State machine, memory buffer, routing logic. | End-to-end workflow success rate, latency metrics. | State corruption; getting stuck in circular handoffs. |

---

## 6. Research Gaps and Next Investigations

1. **Longitudinal Efficacy of VLM Extraction**: While tools like Skyvern show high initial success rates in avoiding DOM fragility [[5]], there is a lack of longitudinal, peer-reviewed data comparing the total cost of ownership (TCO) and maintenance burden of VLM-based extraction versus traditional selector-based scraping over a 12-month period.
2. **Standardization of Agent Handoffs**: The Model Context Protocol (MCP) is emerging as a standard for tool calling [[21]], but formalized, universally adopted schemas for *agent-to-agent* state handoff (especially for error propagation and rollback) remain fragmented.
3. **Regulatory Provenance at Scale**: Current per-fact provenance systems (e.g., PROV-AGENT) are computationally expensive. Investigating lightweight, cryptographic hashing methods for agent reasoning traces without degrading LLM throughput is a critical open area.
4. **Local vs. Cloud Compute Trade-offs**: As DuckDB and Polars push the boundaries of local machine analytics, a formal decision matrix is needed for mid-tier research operations to determine the exact data volume threshold where migrating to a cloud data warehouse becomes more cost-effective than scaling local hardware.

---

## 7. Sources

| URL | Title | Publisher / Author | Date | Claims Supported |
| :--- | :--- | :--- | :--- | :--- |
| `https://www.skyvern.com/blog/ai-web-agents-complete-guide-to-intelligent-browser-automation-november-2025/` | AI Web Agents: Complete Guide to Intelligent Browser Automation | Skyvern Blog | Nov 2025 | Skyvern uses live browser access and VLMs to avoid hardcoded selectors for market research extraction [[1]]. |
| `https://www.skyvern.com/blog/browserbase-vs-firecrawl-vs-skyvern-which-is-better-for-workflow-automation-december-2025/` | Browserbase vs Firecrawl vs Skyvern (Dec 2025) | Skyvern Blog | Dec 2025 | Skyvern automates browser workflows using LLMs/computer vision instead of predefined scripts [[10]]. |
| `https://www.codecentric.de/en/knowledge-hub/blog/duckdb-vs-dataframe-libraries` | DuckDB vs. Polars vs. Pandas: Benchmark & Comparison | Codecentric | Dec 2025 | DuckDB is strongest for SQL-first, on-disk analytics; Polars for fast DataFrame transformations [[11]]. |
| `https://medium.com/@rameshkannanyt0078/pandas-vs-polars-vs-duckdb-2026-i-processed-1-million-rows-in-fastapi-pandas-crashed-my-ram-c3f908546a2e` | Pandas vs Polars vs DuckDB 2026 | Medium (Ramesh Kannan) | ~Jun 2026 | Empirical benchmark showing DuckDB and Polars significantly outperforming Pandas in speed and memory on 1M+ rows [[12]]. |
| `https://impact.ornl.gov/en/publications/prov-agent-unified-provenance-for-tracking-ai-agent-interactions-/` | Unified Provenance for Tracking AI Agent Interactions | ORNL / R. Souza et al. | 2025 | Introduction of PROV-AGENT, extending W3C PROV and leveraging MCP for data observability in agent workflows [[21]]. |
| `https://www.talby.com/p/fact-level-provenance-in-healthcare` | The 42 capabilities behind an FDA-ready clinical data platform | Talby | Sep 2026 | FDA guidance requires provenance and accuracy at a per-fact level for real-world evidence [[25]]. |
| `https://arxiv.org/html/2608.22974v1` | Toward Effective and Reliable LLM Agents via Dynamic Ontology | arXiv | Aug 2026 | Ontology-as-a-kernel (OaK) framework dynamically constructs task-oriented ontologies to ground LLM agents [[33]]. |
| `https://simplify.jobs/p/8c02f73c-34a0-4064-9b04-f3b94e396158/Knowledge-Engineer` | Knowledge Engineer @ Accenture | Simplify.jobs / Accenture | 2026 | Knowledge Engineers design and structure knowledge frameworks enabling AI systems to reason [[43]]. |
| `https://www.linkedin.com/jobs/view/agentic-ai-workflow-developer-at-secumatic-technologies-llp-4207627654` | Agentic AI Workflow Developer | LinkedIn / Secumatic Technologies | 2026 | Emerging role of AI Agent Workflow Specialist focused on designing and optimizing agentic workflows [[51]]. |
| `https://brightdata.com/blog/ai/best-agent-browsers` | 10 Best Agentic Browsers for AI Automation in 2026 | Bright Data Blog | 2026 | Skyvern uses LLMs and computer vision to automate browser tasks without requiring custom code per website [[9]]. |

*Note: All findings are classified based on the requested taxonomy: `documented fact` (empirical or official documentation), `reported signal` (emerging trends in job markets or vendor claims), or `inference` (logical synthesis of multiple sources). Confidence levels reflect the volume and consistency of primary source corroboration.*