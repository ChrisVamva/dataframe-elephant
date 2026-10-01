---
modified: 2026-09-27T13:02:13+03:00
---
### The components to investigate

| Dimension            | What we are looking for                                                                                                                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Skills**           | research synthesis, information extraction, data modeling, ontology design, normalization, SQL, DuckDB, pandas, visualization, provenance, agent orchestration                                                          |
| **Market positions** | data analyst, research analyst, knowledge engineer, data/BI analyst, research engineer, automation specialist, AI/agent workflow specialist, information architect, etc. — without assuming these labels are equivalent |
| **Technology**       | Python, SQL, DuckDB, pandas, notebooks, APIs, scraping, browser automation, LLMs, embeddings, graph technologies, data formats, databases                                                                               |
| **Software**         | DuckDB, pandas, Polars, Jupyter, dbt, Metabase, Superset, Observable, orchestration/agent frameworks, extraction tools, etc.                                                                                            |
| **Companies**        | companies hiring for or building around these capabilities                                                                                                                                                              |
| **Products**         | research/data platforms, extraction tools, BI tools, knowledge systems, agent infrastructure                                                                                                                            |
| **Methodologies**    | research protocols, ETL/ELT, data modeling, information extraction, evidence/provenance systems, analytical workflows                                                                                                   |
| **Workflows**        | research → extraction → normalization → storage → query → analysis → visualization → iteration                                                                                                                          |
| **Agents**           | research agents, extraction agents, coding agents, data-cleaning agents, analytical agents,                                                                                                                             |

Research
   ↓
Evidence
   ↓
Extraction
   ↓
Structured representation
   ↓
Normalization
   ↓
Database
   ↓
Query
   ↓
Analysis
   ↓
Visualization
   ↓
Interpretation
   ↓
New research
   ↓
Agent iteration

                    ┌── Skills
                    ├── Market positions
                    ├── Technologies
                    ├── Software
Research-to-data ───┼── Companies
workflow             ├── Products
                    ├── Methodologies
                    ├── Workflows
                    └── Agents

                    
                    OPP-ATLAS
                       │
                       ▼
          Research-to-Data Capability
                    Cluster
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    Research       Technology      Market
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Workflows
                       │
                       ▼
                  Database
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         Analysis          Visualization
             │                   │
             └─────────┬─────────┘
                       ▼
                   Evidence
                       │
                       ▼
                 New Research


Skill
  └── used_in → Workflow

Workflow
  └── uses → Technology

Technology
  └── implemented_by → Software

Software
  └── produced_by → Company

Workflow
  └── appears_in → Market Position

Methodology
  └── governs → Workflow

Agent
  └── performs → Workflow Step

Source
  └── supports → Claim

Claim
  └── describes → Skill / Technology / Workflow / Company / Product