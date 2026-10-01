---
name: follow-up-research
description: "Formulates, prioritizes, and dispatches follow-up research questions from Stage 2 extraction gaps and citation database signals. Use when asked to create a research agenda, formulate follow-up questions, or identify gaps in the research pipeline. Applies the gap typology (GAP-BND, GAP-CND, GAP-EPI, GAP-FAL, GAP-OPN, GAP-CON) and the priority scoring algorithm."
version: 1.0.0
---

# Follow-Up Research

Formulates, prioritizes, and dispatches follow-up research questions from Stage 2 extraction gaps and citation database signals. Distilled from `Rules and Regulations/Protocols/FollowUpResearch.md`.

## When to use this skill

- Creating a research agenda from Stage 2 extraction gaps
- Formulating follow-up research questions
- Identifying and prioritizing gaps in the research pipeline
- Asked to "create follow-up questions" or "identify research gaps"
- Running the gap detection and question formulation process

## Prerequisites

- Stage 2 extraction files exist (`research/raw/Stage 2/`)
- Citation database exists (`data/citations.duckdb`)
- You have read access to Stage 2 files and the database
- You have write access to `research/processed/FollowUps/`

## Gap Typology

The formulation engine identifies six distinct classes of research gaps:

| Gap Code | Typology | Trigger Source | Condition |
|----------|----------|----------------|-----------|
| **GAP-BND** | Entity Boundary Gap | `Entities.md` | Boundary column is `[boundary not stated in source]` |
| **GAP-CND** | Metric Condition Gap | `Metrics.md` | Scope/conditions column is `[conditions not stated in source]` |
| **GAP-EPI** | Epistemic Evidence Gap | `Claims.md` & DuckDB | Confidence is `low`, or mapped primary sources = 0 |
| **GAP-FAL** | Falsification Gap | `Claims.md` | Falsifier column is `[falsifier not stated]` |
| **GAP-OPN** | Carried Open Question | `ExtractionLog.md` | Decision type is `open_question` or `omission` |
| **GAP-CON** | Classification Conflict | `ExtractionLog.md` & DuckDB | Decision type is `classification_conflict` or unresolved alias |

## The Process

### Step 1: Automated Gap Scan

Run the formulation tool:
```powershell
.venv\Scripts\python scripts/formulate_research_questions.py `
  --stage2-dir "research/raw/Stage 2" `
  --database "data/citations.duckdb" `
  --output-dir "research/processed/FollowUps"
```

### Step 2: Gap Classification and Scoring

For each identified gap, calculate the **Priority Score**:

```
Score = (Workflow Centrality × Evidence Severity) / Verification Difficulty
```

**Workflow Centrality (1-5):**
- 5 (Critical): Core storage, execution engine, or fundamental data model
- 4 (High): Major workflow stage or primary orchestration framework
- 3 (Medium): Specialized analytical capability or secondary tool
- 2 (Low): Auxiliary utility or exploratory role
- 1 (Peripheral): Contextual or historical notes

**Evidence Severity (1-5):**
- 5 (Severe): Uncorroborated vendor claim or metric without conditions
- 4 (High): Material claim relying exclusively on secondary sources
- 3 (Medium): Low-confidence claim with some supporting evidence
- 2 (Low): Incomplete metadata or minor omitted detail
- 1 (Negligible): Stylistic or formatting ambiguity

**Verification Difficulty (1-3):**
- 1 (Direct/Accessible): Readily available in official specs or public repos
- 2 (Moderate): Requires comparative benchmarking or reviewing multiple sources
- 3 (Complex/Opaque): Requires proprietary access or custom experiments

**Priority Tiers:**
- **P1 (Score >= 12.0):** Immediate priority — must be answered before next major iteration
- **P2 (Score 6.0-11.9):** Secondary priority — scheduled into regular research waves
- **P3 (Score < 6.0):** Informational / backlog — addressed as opportunistic investigations

### Step 3: Question Formulation

For each gap, produce a question dossier:

```markdown
### [RQ-###] [Concise Question Title]

- **Priority:** P1 / P2 / P3 (Score: X.X)
- **Gap Code:** GAP-BND | GAP-CND | GAP-EPI | GAP-FAL | GAP-OPN | GAP-CON
- **Target Entity / Concept:** [Entity or Claim ID]
- **Downstream Impact:** [Affected workflow stage, table, or schema column]

#### 1. Core Research Question
[Precise, specific question statement]

#### 2. Scope & Boundaries
- **In Scope:** [Entities, versions, environments, workflow stages included]
- **Out of Scope:** [Excluded tools, speculative claims, out-of-context uses]
- **Intended Use:** [How the answer will be applied in Stage 2 / citations database]

#### 3. Target Evidence & Sources
- **Minimum Evidence Class:** Primary / Peer-Reviewed / Official Spec
- **Target Sources:** [Specific docs, GitHub repos, benchmark suites to consult]

#### 4. Falsification & Resolution Criteria
- **Resolution:** [What finding establishes the answer]
- **Falsifier:** [What evidence would invalidate the existing claim or boundary]
```

### Step 4: Quality Gates

Before acceptance, verify:
- [ ] **Gate A (Scope):** Every question has explicit In Scope, Out of Scope, and Intended Use
- [ ] **Gate B (Falsifier):** No question has an empty or non-testable falsifier
- [ ] **Gate C (Provenance):** Every question references its originating Stage 2 entity ID, claim ID, or log ID
- [ ] **Gate D (Score Coverage):** Every question has audited workflow centrality, severity, and difficulty scores

### Step 5: Output

Write to `research/processed/FollowUps/`:
1. **`ResearchAgenda.md`** — Master index of all questions, ranked by Priority Score
2. **Thematic Question Packs** — Grouped by gap type

## Non-Negotiable Rules

1. **Every question must be falsifiable** — specify what evidence would confirm, modify, or falsify the target
2. **Every question must define explicit scope** — included entities, excluded concepts, time period, intended use
3. **No untraced questions** — every question must trace to a specific trigger in Stage 2 or the database
4. **Target evidence class must be explicit** — specify minimum acceptable evidence class
5. **Deterministic prioritization** — use the objective scoring formula
6. **Standardized output location** — all output goes to `research/processed/FollowUps/`

## References

- Process: `Rules and Regulations/Protocols/FollowUpResearch.md` (§§1-7: gap typology, scoring algorithm, question formulation, execution procedure)
- Research evaluation: `Rules and Regulations/Protocols/Research-Evaluation.md`
- Skill creation: `Rules and Regulations/Protocols/SkillCreation.md`
