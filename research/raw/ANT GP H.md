# Research-to-Data Capability Atlas: Structured Brief

## 1. Executive synthesis

- **Agent Orchestration is Maturing**: Frameworks like LangGraph and CrewAI are providing the necessary state management and role-based coordination to move from single-prompt interactions to complex, multi-agent workflows (e.g., specialized extracting, cleaning, and analyzing agents).
- **The Shift from ETL to ELT in Modern Data**: Driven by cloud compute capabilities, data workflows are shifting from ETL (transform before loading) to ELT (load raw, transform in place), giving research engineers and data analysts more access to raw source data.
- **Role Differentiation**: Market positions like Knowledge Engineer (focusing on structuring human expertise), Data Analyst (focusing on business insights), and Research Engineer (focusing on R&D and prototypes) represent distinct skill sets despite overlapping tools (like Python and SQL).
- **Tooling Convergence via Arrow**: The distinction between DuckDB (SQL-centric, out-of-core), Polars (Rust-based, programmatic), and Pandas is bridged by Apache Arrow, allowing zero-copy data passing and modular pipelines where each tool handles what it does best.
- **Provenance is Critical**: As workflows become more distributed across extraction tools, LLMs, and databases, maintaining data provenance (tracking origin and authenticity) is crucial for trust, auditability, and reproducibility in new research.

## 2. Lens findings

### Skills & Market Positions
- **Definition and scope**: The specific capabilities and roles involved in the research-to-data pipeline.
- **Core capabilities**: Knowledge representation (OWL, RDF), statistical analysis, Python, SQL, data visualization.
- **Position in workflow**: Throughout the pipeline, dictating who performs extraction (Knowledge/Research Engineers) versus analysis and interpretation (Data Analysts).
- **Representative examples**: Knowledge Engineer, Data Analyst, Research Engineer.
- **Trade-offs and failure modes**: Misalignment of roles (e.g., treating a data analyst as a knowledge engineer) leads to poor system design or failure to capture tacit knowledge.
- **Evidence confidence**: High.

### Technology & Software
- **Definition and scope**: The computational tools and libraries used to implement the pipeline.
- **Core capabilities**: In-memory data processing, SQL-based transformation, multi-threading, orchestration.
- **Representative examples**: Pandas, Polars, DuckDB, dbt, LangGraph, CrewAI.
- **Relationships to other lenses**: Software implements Technology and is used by Market Positions to execute Workflows.
- **Trade-offs**: Polars offers performance and multithreading but has a steeper learning curve; DuckDB is excellent for SQL-heavy workflows; Pandas is standard but struggles with out-of-core data.
- **Evidence confidence**: High.

### Methodologies & Workflows
- **Definition and scope**: The structural approaches to moving and transforming data (e.g., ETL vs ELT) and preserving its history (Provenance).
- **Core capabilities**: Data extraction, transformation, loading, and tracking lineage/provenance.
- **Representative examples**: ELT, ETL, Data Lineage Tracking.
- **Relationships**: Methodologies govern Workflows; Workflows use Technologies.
- **Evidence confidence**: High.

### Agents
- **Definition and scope**: Autonomous or semi-autonomous software entities that execute specific steps in the workflow.
- **Core capabilities**: State management, role-based execution, tool usage, human-in-the-loop validation.
- **Representative examples**: Extraction agents, Analytical agents, LangGraph-based state machines, CrewAI role-players.
- **Trade-offs and failure modes**: Hallucination in extraction, loss of context between handoffs, lack of observability.
- **Evidence confidence**: Medium-High (rapidly evolving field).

## 3. Workflow map

| Stage | Inputs | Activities | Outputs | Quality Checks | Tools/Agents |
|---|---|---|---|---|---|
| **Research & Evidence** | Raw text, URLs, documents | Gathering, scraping, observing | Raw data corpus | Source verification | Browser automation, Research Agents |
| **Extraction & Structure** | Raw data corpus | Entity extraction, NLP parsing | JSON, structured tables | Schema validation | Pydantic AI, LLMs, Extraction Agents |
| **Normalization** | Structured tables | Cleaning, standardizing formats | Cleaned datasets | Type checking, anomaly detection | Polars, pandas |
| **Database & Storage** | Cleaned datasets | Loading into warehouse/lake | Accessible tables | Constraints, Provenance tracking | DuckDB, dbt |
| **Query & Analysis** | Accessible tables | SQL joins, statistical modeling | Aggregated results, models | Code review, statistical validation | DuckDB, SQL, Analytical Agents |
| **Visualization & Interpretation** | Aggregated results | Graphing, dashboarding | Charts, BI dashboards | Audience comprehension check | Metabase, BI tools, Data Analysts |
| **New Research & Iteration** | Charts, Insights | Hypothesis generation | New research questions | Peer review | Agent Orchestration, Researchers |

## 4. Entity and relationship candidates

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
|---|---|---|---|---|---|---|---|
| Market Position | Knowledge Engineer | Formalizes human expertise | Extraction / Structure | Ontology | creates | Job descriptions | High |
| Market Position | Data Analyst | Drives insights from data | Analysis / Visualization | BI Tools | uses | Industry roles | High |
| Software | DuckDB | In-process SQL OLAP database | Database / Query | SQL | implemented_by | Docs | High |
| Software | Polars | Fast multithreaded DataFrame library | Normalization | Python/Rust | implemented_by | Docs | High |
| Framework | LangGraph | Stateful multi-agent orchestration | Agent Iteration | Agents | orchestrates | Vendor docs | High |
| Methodology | ELT | Extract, Load, Transform pipeline | Extraction to Storage | dbt | supported_by | Articles | High |
| Concept | Data Provenance | Origin and history of data | Entire workflow | Evidence | tracks | Papers | High |

## 5. Comparison tables

### Tooling Comparison: pandas vs Polars vs DuckDB vs dbt
| Tool | Primary Interface | Best For | Scaling Behavior |
|---|---|---|---|
| **pandas** | Python API | Small data, ML integration | In-memory, single-threaded |
| **Polars** | Python (Expressions) | Complex logic, fast pipelines | High (multithreaded/lazy) |
| **DuckDB** | SQL | Aggregations, out-of-core SQL | High (out-of-core streaming) |
| **dbt** | SQL / Python | Managing SQL models / ELT | Depends on underlying database |

### Agent Frameworks Comparison
| Framework | Core Paradigm | Best For |
|---|---|---|
| **LangGraph** | State Machine (Graphs) | Complex, stateful, human-in-the-loop workflows |
| **CrewAI** | Role-based Teams | Rapid prototyping of multi-agent collaboration |
| **Pydantic AI** | Type-safe Extraction | Strict schema enforcement during data extraction |
| **LlamaIndex** | RAG workflows | Data-heavy document retrieval and synthesis |

## 6. Research gaps and next investigations

- **Gap**: The exact boundaries between 'Extraction Agents' and traditional 'ETL tools' remain blurry.
- **Next Investigation**: Deep dive into how enterprises are combining dbt with agentic frameworks like LangGraph.
- **Gap**: The specific data models and ontologies used by Knowledge Engineers in modern LLM-driven architectures.
- **Next Investigation**: Case studies of ontology design for LLM extraction pipelines.

## 7. Sources

- freelancermap.com, upriverdata.com: Role definitions for Knowledge Engineer, Data Analyst, Research Engineer.
- getdbt.com, medium.com, secoda.co: Methodologies on ETL vs ELT and Data Provenance.
- langchain.com, crewai.com, pydantic.dev: AI Agent orchestration frameworks and their specific use-cases.
- codecentric.de, medium.com: Comparisons of pandas, Polars, DuckDB, and dbt.
