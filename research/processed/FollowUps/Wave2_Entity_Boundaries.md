# Follow-Up Research Agenda

## Executive Summary

This research agenda was systematically formulated from the Stage 2 extraction layer (`research/raw/Stage 2/`) and the citation intelligence database (`data/citations.duckdb`), governed by `Protocols/FollowUpResearch.md`.

- **Total Research Questions Formulated:** 22
- **P1 (Immediate Priority):** 7
- **P2 (Scheduled Waves):** 15
- **P3 (Backlog / Opportunistic):** 0

---

## Priority Ranking Table

| Question ID | Title | Gap Code | Category | Score | Tier |
| --- | --- | --- | --- | ---: | --- |
| [RQ-001](#rq-001) | Operational Boundary & Architectural Role of DuckDB | `GAP-BND` | Entity Boundary (Software) | 20.0 | **P1** |
| [RQ-016](#rq-016) | Operational Boundary & Architectural Role of MCP | `GAP-BND` | Entity Boundary (Technology (protocol)) | 20.0 | **P1** |
| [RQ-007](#rq-007) | Operational Boundary & Architectural Role of MotherDuck | `GAP-BND` | Entity Boundary (Company / Product) | 16.0 | **P1** |
| [RQ-008](#rq-008) | Operational Boundary & Architectural Role of pandas | `GAP-BND` | Entity Boundary (Software) | 12.0 | **P1** |
| [RQ-009](#rq-009) | Operational Boundary & Architectural Role of Polars | `GAP-BND` | Entity Boundary (Software) | 12.0 | **P1** |
| [RQ-010](#rq-010) | Operational Boundary & Architectural Role of dbt | `GAP-BND` | Entity Boundary (Software) | 12.0 | **P1** |
| [RQ-018](#rq-018) | Operational Boundary & Architectural Role of PROV | `GAP-BND` | Entity Boundary (Technology/Standard) | 12.0 | **P1** |
| [RQ-002](#rq-002) | Operational Boundary & Architectural Role of DuckDB (technology) | `GAP-BND` | Entity Boundary (Technology) | 9.0 | **P2** |
| [RQ-003](#rq-003) | Operational Boundary & Architectural Role of DuckDB Foundation | `GAP-BND` | Entity Boundary (Company (nonprofit)) | 9.0 | **P2** |
| [RQ-004](#rq-004) | Operational Boundary & Architectural Role of DuckLabs | `GAP-BND` | Entity Boundary (Company) | 9.0 | **P2** |
| [RQ-005](#rq-005) | Operational Boundary & Architectural Role of AWS | `GAP-BND` | Entity Boundary (Company) | 9.0 | **P2** |
| [RQ-012](#rq-012) | Operational Boundary & Architectural Role of Metabase | `GAP-BND` | Entity Boundary (Software (product)) | 9.0 | **P2** |
| [RQ-013](#rq-013) | Operational Boundary & Architectural Role of Superset | `GAP-BND` | Entity Boundary (Software (product)) | 9.0 | **P2** |
| [RQ-019](#rq-019) | Operational Boundary & Architectural Role of PRISMA 2020 | `GAP-BND` | Entity Boundary (Methodology/Standard) | 9.0 | **P2** |
| [RQ-020](#rq-020) | Operational Boundary & Architectural Role of Research/scout agent | `GAP-BND` | Entity Boundary (Agent) | 9.0 | **P2** |
| [RQ-021](#rq-021) | Operational Boundary & Architectural Role of AI/agent workflow specialist | `GAP-BND` | Entity Boundary (Market Position) | 9.0 | **P2** |
| [RQ-022](#rq-022) | Operational Boundary & Architectural Role of Claim | `GAP-BND` | Entity Boundary (Entity type) | 9.0 | **P2** |
| [RQ-006](#rq-006) | Operational Boundary & Architectural Role of DuckLake | `GAP-BND` | Entity Boundary (Technology (format) / Software (extension)) | 8.0 | **P2** |
| [RQ-011](#rq-011) | Operational Boundary & Architectural Role of Semantic layer | `GAP-BND` | Entity Boundary (Technology/Methodology) | 8.0 | **P2** |
| [RQ-014](#rq-014) | Operational Boundary & Architectural Role of LangGraph | `GAP-BND` | Entity Boundary (Software) | 8.0 | **P2** |
| [RQ-015](#rq-015) | Operational Boundary & Architectural Role of Microsoft Agent Framework | `GAP-BND` | Entity Boundary (Software) | 8.0 | **P2** |
| [RQ-017](#rq-017) | Operational Boundary & Architectural Role of A2A | `GAP-BND` | Entity Boundary (Technology (protocol)) | 8.0 | **P2** |

---

## Formulated Research Question Dossiers

<a id="rq-001"></a>
### [RQ-001] Operational Boundary & Architectural Role of DuckDB

- **Priority Tier:** **P1** (Priority Score: **20.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software))
- **Trigger Reference:** `Entities.md row E001`
- **Scoring Breakdown:** Workflow Centrality = 5/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of DuckDB, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** DuckDB core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for DuckDB with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for DuckDB
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what DuckDB is not.
- **Falsifier:** Evidence demonstrating that DuckDB natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-016"></a>
### [RQ-016] Operational Boundary & Architectural Role of MCP

- **Priority Tier:** **P1** (Priority Score: **20.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Technology (protocol)))
- **Trigger Reference:** `Entities.md row E016`
- **Scoring Breakdown:** Workflow Centrality = 5/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of MCP, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** MCP core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for MCP with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for MCP
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what MCP is not.
- **Falsifier:** Evidence demonstrating that MCP natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-007"></a>
### [RQ-007] Operational Boundary & Architectural Role of MotherDuck

- **Priority Tier:** **P1** (Priority Score: **16.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Company / Product))
- **Trigger Reference:** `Entities.md row E007`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of MotherDuck, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** MotherDuck core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for MotherDuck with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for MotherDuck
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what MotherDuck is not.
- **Falsifier:** Evidence demonstrating that MotherDuck natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-008"></a>
### [RQ-008] Operational Boundary & Architectural Role of pandas

- **Priority Tier:** **P1** (Priority Score: **12.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software))
- **Trigger Reference:** `Entities.md row E008`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of pandas, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** pandas core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for pandas with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for pandas
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what pandas is not.
- **Falsifier:** Evidence demonstrating that pandas natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-009"></a>
### [RQ-009] Operational Boundary & Architectural Role of Polars

- **Priority Tier:** **P1** (Priority Score: **12.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software))
- **Trigger Reference:** `Entities.md row E009`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Polars, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Polars core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Polars with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Polars
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Polars is not.
- **Falsifier:** Evidence demonstrating that Polars natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-010"></a>
### [RQ-010] Operational Boundary & Architectural Role of dbt

- **Priority Tier:** **P1** (Priority Score: **12.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software))
- **Trigger Reference:** `Entities.md row E010`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of dbt, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** dbt core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for dbt with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for dbt
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what dbt is not.
- **Falsifier:** Evidence demonstrating that dbt natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-018"></a>
### [RQ-018] Operational Boundary & Architectural Role of PROV

- **Priority Tier:** **P1** (Priority Score: **12.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Technology/Standard))
- **Trigger Reference:** `Entities.md row E018`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of PROV, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** PROV core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for PROV with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for PROV
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what PROV is not.
- **Falsifier:** Evidence demonstrating that PROV natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-002"></a>
### [RQ-002] Operational Boundary & Architectural Role of DuckDB (technology)

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Technology))
- **Trigger Reference:** `Entities.md row E002`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of DuckDB (technology), and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** DuckDB (technology) core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for DuckDB (technology) with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for DuckDB (technology)
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what DuckDB (technology) is not.
- **Falsifier:** Evidence demonstrating that DuckDB (technology) natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-003"></a>
### [RQ-003] Operational Boundary & Architectural Role of DuckDB Foundation

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Company (nonprofit)))
- **Trigger Reference:** `Entities.md row E003`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of DuckDB Foundation, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** DuckDB Foundation core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for DuckDB Foundation with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for DuckDB Foundation
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what DuckDB Foundation is not.
- **Falsifier:** Evidence demonstrating that DuckDB Foundation natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-004"></a>
### [RQ-004] Operational Boundary & Architectural Role of DuckLabs

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Company))
- **Trigger Reference:** `Entities.md row E004`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of DuckLabs, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** DuckLabs core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for DuckLabs with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for DuckLabs
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what DuckLabs is not.
- **Falsifier:** Evidence demonstrating that DuckLabs natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-005"></a>
### [RQ-005] Operational Boundary & Architectural Role of AWS

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Company))
- **Trigger Reference:** `Entities.md row E005`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of AWS, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** AWS core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for AWS with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for AWS
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what AWS is not.
- **Falsifier:** Evidence demonstrating that AWS natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-012"></a>
### [RQ-012] Operational Boundary & Architectural Role of Metabase

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software (product)))
- **Trigger Reference:** `Entities.md row E012`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Metabase, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Metabase core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Metabase with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Metabase
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Metabase is not.
- **Falsifier:** Evidence demonstrating that Metabase natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-013"></a>
### [RQ-013] Operational Boundary & Architectural Role of Superset

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software (product)))
- **Trigger Reference:** `Entities.md row E013`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Superset, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Superset core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Superset with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Superset
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Superset is not.
- **Falsifier:** Evidence demonstrating that Superset natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-019"></a>
### [RQ-019] Operational Boundary & Architectural Role of PRISMA 2020

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Methodology/Standard))
- **Trigger Reference:** `Entities.md row E019`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of PRISMA 2020, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** PRISMA 2020 core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for PRISMA 2020 with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for PRISMA 2020
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what PRISMA 2020 is not.
- **Falsifier:** Evidence demonstrating that PRISMA 2020 natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-020"></a>
### [RQ-020] Operational Boundary & Architectural Role of Research/scout agent

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Agent))
- **Trigger Reference:** `Entities.md row E020`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Research/scout agent, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Research/scout agent core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Research/scout agent with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Research/scout agent
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Research/scout agent is not.
- **Falsifier:** Evidence demonstrating that Research/scout agent natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-021"></a>
### [RQ-021] Operational Boundary & Architectural Role of AI/agent workflow specialist

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Market Position))
- **Trigger Reference:** `Entities.md row E021`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of AI/agent workflow specialist, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** AI/agent workflow specialist core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for AI/agent workflow specialist with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for AI/agent workflow specialist
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what AI/agent workflow specialist is not.
- **Falsifier:** Evidence demonstrating that AI/agent workflow specialist natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-022"></a>
### [RQ-022] Operational Boundary & Architectural Role of Claim

- **Priority Tier:** **P2** (Priority Score: **9.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Entity type))
- **Trigger Reference:** `Entities.md row E022`
- **Scoring Breakdown:** Workflow Centrality = 3/5 | Evidence Severity = 3/5 | Difficulty = 1/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Claim, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Claim core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Claim with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Claim
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Claim is not.
- **Falsifier:** Evidence demonstrating that Claim natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-006"></a>
### [RQ-006] Operational Boundary & Architectural Role of DuckLake

- **Priority Tier:** **P2** (Priority Score: **8.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Technology (format) / Software (extension)))
- **Trigger Reference:** `Entities.md row E006`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 2/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of DuckLake, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** DuckLake core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for DuckLake with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for DuckLake
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what DuckLake is not.
- **Falsifier:** Evidence demonstrating that DuckLake natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-011"></a>
### [RQ-011] Operational Boundary & Architectural Role of Semantic layer

- **Priority Tier:** **P2** (Priority Score: **8.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Technology/Methodology))
- **Trigger Reference:** `Entities.md row E011`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 2/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Semantic layer, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Semantic layer core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Semantic layer with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Semantic layer
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Semantic layer is not.
- **Falsifier:** Evidence demonstrating that Semantic layer natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-014"></a>
### [RQ-014] Operational Boundary & Architectural Role of LangGraph

- **Priority Tier:** **P2** (Priority Score: **8.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software))
- **Trigger Reference:** `Entities.md row E014`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 2/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of LangGraph, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** LangGraph core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for LangGraph with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for LangGraph
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what LangGraph is not.
- **Falsifier:** Evidence demonstrating that LangGraph natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-015"></a>
### [RQ-015] Operational Boundary & Architectural Role of Microsoft Agent Framework

- **Priority Tier:** **P2** (Priority Score: **8.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Software))
- **Trigger Reference:** `Entities.md row E015`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 2/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of Microsoft Agent Framework, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** Microsoft Agent Framework core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for Microsoft Agent Framework with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for Microsoft Agent Framework
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what Microsoft Agent Framework is not.
- **Falsifier:** Evidence demonstrating that Microsoft Agent Framework natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---

<a id="rq-017"></a>
### [RQ-017] Operational Boundary & Architectural Role of A2A

- **Priority Tier:** **P2** (Priority Score: **8.0**)
- **Gap Code:** `GAP-BND` (Entity Boundary (Technology (protocol)))
- **Trigger Reference:** `Entities.md row E017`
- **Scoring Breakdown:** Workflow Centrality = 4/5 | Evidence Severity = 4/5 | Difficulty = 2/3

#### 1. Core Research Question
> What is the precise architectural boundary and operational scope of A2A, and what adjacent technologies, roles, or formats does it explicitly NOT encompass?

#### 2. Scope & Boundaries
- **In Scope:** A2A core definition, API surface, execution model, and primary deployment posture.
- **Out of Scope:** Unverified marketing narratives, unreleased roadmap speculation.
- **Intended Downstream Use:** Update Entities.md row for A2A with a verifiable 'Boundary (what it is not)' definition.

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** `Primary documentation, official technical specifications, or author codebases.`
- **Target Sources:**
  - Official documentation for A2A
  - Repository README/specifications

#### 4. Falsification & Resolution Criteria
- **Resolution Condition:** A clear, 1-2 sentence negative boundary stating exactly what A2A is not.
- **Falsifier:** Evidence demonstrating that A2A natively implements functionality previously assumed to be out of scope (e.g. built-in distributed cluster coordination, proprietary storage format).

---
