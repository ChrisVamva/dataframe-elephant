<!-- prompts/lib/deliverable_brief.md — the standard research-brief deliverable
     shape. Task definition, not a protocol rule. -->

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
