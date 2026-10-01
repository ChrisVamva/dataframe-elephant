# FreeBrainstorming Protocol

## Purpose
Facilitate external, independent brainstorming without self-referential projection or focus on internal project artifacts.

## Core Principles

### 1. External Frame of Reference
- Focus on universal research problems, methodologies, or domains **outside** this project's artifacts, processes, or goals
- Use established external literature, standards, or domains as primary reference points
- Treat this project as a **case study** or **example** only, never as the central inquiry

### 2. Broad Scope & Independence
- Topics must have clear external relevance (scientific, industry, policy, societal impact)
- Avoid "how to improve X" or "what to add to this repo"
- Prioritize questions that exist in the broader field regardless of this project's existence

### 3. No Internal Projection
- Never frame questions as "if only we had X feature" or "if we removed Y"
- Avoid discussing internal decisions, priorities, or technical debt
- When referencing this project, use it only as data, not as analytical focus

### 4. Actionable Independence
- Expected outputs should be applicable **regardless** of this project's current state
- Results should be reusable by other teams or projects
- Deliverables should not require internal project changes to be useful

## Session Structure

### 1. Topic Generation (External Focus)
- **External Triggers:** News articles, policy documents, industry reports, academic publications, standard bodies
- **Cross‑Domain Mapping:** Identify 5+ external domains (health, finance, climate, transportation, education, etc.)
- **Universal Problems:** List 10–20 problems that exist across multiple domains (privacy, bias, interpretability, reproducibility, scalability, ethics)

### 2. Problem Reframing
- **Remove Internal Context:** Describe each problem as if the project didn't exist
- **External Benchmarks:** Reference established frameworks in other fields (e.g., software engineering, biomedical research, public policy)
- **Scope Creep Guard:** Reject "how would this project do it differently" questions

### 3. Solution Exploration (External Validity)
- **Cross‑Reference:** Compare against solutions in other domains, not this project's approach
- **Generalization Tests:** "Would this solution work for a hospital, a bank, and a transportation authority simultaneously?"
- **External Validation:** Use peer‑reviewed literature, industry standards, regulatory requirements

### 4. Deliverable Format

```markdown
# External Research Idea: [Universal Problem]

## External Context
- Domain: [Healthcare/Finance/etc.]
- Established Solutions: [List 3–5 approaches from other fields]
- Gaps Identified: [2–3 missing elements in external approaches]

## Proposed Approach
- Methodology: [Borrowed/adapted from external domain]
- Key Innovations: [Universal innovations, not "new for us"]
- External Validation: [Evidence from other domains]

## Expected Impact
- Cross‑domain applicability
- Reproducible methodology
- Actionable for external stakeholders

## Limitations (External Only)
- Scope deliberately bounded to universal problem
- No internal project dependencies
```

## Governance & Quality

### Quality Gates (External Standards)
- **External Relevance:** Can be understood and applied by organizations outside this project?
- **Reproducibility:** Can a team with no internal knowledge implement the approach?
- **Impact:** Measurable benefits in the external domain, not internal efficiency.
- **Ethics:** No references to internal ethical frameworks unless universally accepted principles.

### Review Process
- **Blind Review:** Evaluators have no access to project internals
- **External Experts:** At least one reviewer from unrelated domain
- **Peer Validation:** Reference to established external literature/frameworks

## Exit Criteria

A brainstorming session is complete when:
- All ideas have at least one external reference point (publication, standard, industry practice)
- No idea requires internal project changes to be implemented
- Each idea can be understood by someone unfamiliar with this project

## Artifacts

### Generated
- FreeBrainstorming Session Notes (external‑only observations)
- Research Idea Templates (external format)
- Cross‑Domain Reference Library (selected external frameworks)
- Independent Implementation Plans (step‑by‑step for external teams)

### Not Generated
- Internal feature requests
- Roadmap items for this project
- Technical debt assessments
- Internal process improvements

## Notes for Facilitators

- When internal references creep in, ask: "Would this make sense if the project never existed?"
- Use "external stakeholder" framing: "How would a public health agency approach this problem?"
- Keep a "projection detector" checklist:
  - Am I describing how **we** would do something?
  - Am I analyzing our **internal** weaknesses?
  - Am I focusing on **our** needs vs. **universal** needs?
  - Should this exist even if **no one** had this project?

---

## Example Session Log (External Focus)

```
[Brainstorming 2026-10-01 14:00]
Topic: "How do complex multi‑stakeholder decision‑making processes work in disaster response?"
Reference: FEMA ICS, WHO emergency response protocols, Air Traffic Control
Problem: Coordinating 50+ agencies with conflicting priorities, resource constraints, time pressure
External Solution: NYC Emergency Management tiered activation system
Gap: No universal model for private‑sector partnership integration
Proposed: Adapt tiered activation to integrate corporate emergency response plans
External Validation: Applied to hospital network, logistics provider, financial services firm simulation
```

---

**Protocol Status:** Active for external research ideation only
**Internal Project Impact:** May generate insights that indirectly inform this project, but deliverable independence is required