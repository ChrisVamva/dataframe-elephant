# Research Prompt: Research-to-Data Capability Atlas

## Role

You are a research agent contributing to an evidence-grounded atlas of the research-to-data capability cluster. Investigate how research becomes structured, queryable, analyzable, visualizable knowledge, and how people, software, companies, products, methodologies, workflows, and agents participate in that process.

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

## Source and evidence rules

- Prefer primary sources: official documentation, technical papers, standards, company engineering posts, product documentation, job postings, and first-party product pages.
- Use multiple independent sources for important claims, especially market, company, product, and role claims.
- Record the source URL, title, publisher or author, publication date when available, and access date.
- Quote or paraphrase only what the source supports. Do not turn vendor positioning into a universal fact.
- Mark each finding as `documented fact`, `reported signal`, `inference`, or `recommendation`.
- Note uncertainty, conflicting evidence, missing data, and likely source bias.
- Prefer current evidence, but preserve historical context when it explains a transition.

## Deliverable

Return a structured research brief in Markdown with these sections:

### 1. Executive synthesis

Summarize the most important patterns, boundaries, and open questions in 5-10 bullets.

### 2. Lens findings

For each applicable lens, provide:

- Definition and scope
- Core capabilities or entities
- Position in the research-to-data workflow
- Relationships to the other lenses
- Representative examples
- Trade-offs and failure modes
- Evidence confidence: high, medium, or low

### 3. Workflow map

Describe the workflow stage by stage. For every stage, include inputs, activities, outputs, quality checks, likely tools, and suitable agent roles.

### 4. Entity and relationship candidates

Use a table with these columns:

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use one row per candidate entity or relationship. Do not merge distinct entities merely to reduce row count.

### 5. Comparison tables

Where useful, compare roles, technologies, software, products, methodologies, companies, or agents using explicit criteria such as purpose, users, inputs, outputs, integration surface, maturity, cost, openness, and limitations.

### 6. Research gaps and next investigations

List unresolved questions, weakly supported claims, missing categories, and the next most valuable searches or interviews.

### 7. Sources

List every source with its URL and the claims or sections it supports.

## Quality bar

Be precise, skeptical, and useful for later data modeling. Separate observation from interpretation. Preserve provenance at claim level where possible. Use stable names, avoid duplicate concepts, and make relationships explicit. A concise, well-supported result is better than a broad list of unverified examples.