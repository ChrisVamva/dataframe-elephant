---
id: research_brief
version: 2.0
status: active
protocol_refs:
  - Rules and Regulations/Protocols/Research-Evaluation.md
partials:
  - lib/role_research_agent.md
  - lib/evidence_rules.md
  - lib/deliverable_brief.md
  - lib/quality_bar.md
  - lib/verification.md
---

# Research Brief Template: Research-to-Data Capability Atlas

## Role

<!-- include: lib/role_research_agent.md -->

You are contributing to an evidence-grounded atlas of the research-to-data capability cluster. Investigate how research becomes structured, queryable, analyzable, visualizable knowledge, and how people, software, companies, products, methodologies, workflows, and agents participate in that process.

## Research objective

Build a clear, source-backed map of the capabilities and ecosystem surrounding this workflow:

Research -> Evidence -> Extraction -> Structured representation -> Normalization -> Database -> Query -> Analysis -> Visualization -> Interpretation -> New research -> Agent iteration

Do not assume that similar labels describe the same thing. Identify boundaries, overlaps, dependencies, and meaningful differences.

## Lenses to investigate

Cover the following nine lenses. Keep each lens distinct while recording relationships between them.

1. **Skills**: research synthesis, information extraction, data modeling, ontology design, normalization, SQL, DuckDB, pandas, visualization, provenance, and agent orchestration.
2. **Market positions**: data analyst, research analyst, knowledge engineer, data/BI analyst, research engineer, automation specialist, AI/agent workflow specialist, information architect, and adjacent roles. Compare responsibilities, outputs, skills, and hiring signals rather than treating the labels as equivalent.
3. **Technology**: Python, SQL, DuckDB, pandas, notebooks, APIs, scraping, browser automation, LLMs, embeddings, graph technologies, data formats, and databases.
4. **Software**: DuckDB, pandas, Polars, Jupyter, dbt, Metabase, Superset, Observable, orchestration and agent frameworks, extraction tools, and relevant adjacent tools.
5. **Companies**: companies hiring for, selling, or building around these capabilities. Separate employers, vendors, open-source foundations, consultancies, and research organizations where relevant.
6. **Products**: research and data platforms, extraction tools, BI tools, knowledge systems, and agent infrastructure. Describe the user problem, workflow position, and differentiating capability.
7. **Methodologies**: research protocols, ETL/ELT, data modeling, information extraction, evidence and provenance systems, and analytical workflows.
8. **Workflows**: the complete research -> extraction -> normalization -> storage -> query -> analysis -> visualization -> iteration loop. Identify inputs, outputs, decisions, quality gates, and feedback loops.
9. **Agents**: research agents, extraction agents, coding agents, data-cleaning agents, analytical agents, and coordinating/orchestration agents. Define the task each performs, required tools and state, handoffs, verification, and failure modes.

## Questions to answer

- What is the precise definition and boundary of each item?
- Which workflow stage does it support or govern?
- What inputs, outputs, skills, tools, and evidence does it require?
- What entities does it relate to: Skill, Market Position, Technology, Software, Company, Product, Methodology, Workflow, Agent, Source, or Claim?
- What relationships are useful to record, such as `uses`, `implemented_by`, `produced_by`, `appears_in`, `governs`, `performs`, or `supports`?
- What are the major alternatives, trade-offs, maturity levels, and failure modes?
- Which claims are stable facts, which are time-sensitive, and which are your synthesis or recommendation?
- What evidence would change or falsify the conclusion?

## Evidence rules

<!-- include: lib/evidence_rules.md -->

## Deliverable

<!-- include: lib/deliverable_brief.md -->

## Quality bar

<!-- include: lib/quality_bar.md -->

## Self-check

Report results for `RE:Gate A` (question and scope), `RE:Gate B` (source quality
and coverage), `RE:Gate C` (claim and citation alignment), `RE:Gate D` (method and
reasoning), `RE:Gate E` (completeness and counterevidence), and `RE:Gate F`
(usefulness and data readiness) per lens before submitting. The gates are defined
in `Rules and Regulations/Protocols/Research-Evaluation.md` §4 — cite them by qualified ID, never
renumber them.

## Verification

<!-- include: lib/verification.md -->