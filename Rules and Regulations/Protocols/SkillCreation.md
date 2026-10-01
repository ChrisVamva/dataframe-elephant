# Skill Creation Protocol

**Version:** 1.0
**Purpose:** Define the process for converting protocols in `Rules and Regulations/Protocols/` into actionable skills in `skills/`.

---

## 1. Overview

This protocol describes how to transform a protocol — a formal definition of *what* to do and *why* — into a skill — an actionable workflow that an agent can execute.

### 1.1 Context

| Artifact | Location | Purpose |
|----------|----------|---------|
| **Protocol** | `Rules and Regulations/Protocols/` | Formal definition of a process, including principles, steps, quality criteria, and constraints |
| **Skill** | `skills/` | Agent-executable workflow distilled from one or more protocols, with clear triggers, steps, and verification |

### 1.2 The Relationship in One Sentence

> A **protocol** is the authority — it defines the rules, constraints, and quality gates.
> A **skill** is the practitioner — it distills the protocol into a workflow an agent can follow.

---

## 2. When to Create a Skill

### 2.1 Criteria for Skill Creation

Create a skill from a protocol when **all** of the following are true:

| Criterion | Question to Ask |
|-----------|-----------------|
| **Repeatable** | Is this process executed more than once? |
| **Agent-executable** | Can an agent follow this without human judgment at every step? |
| **Clear triggers** | Is it obvious when this skill should be used? |
| **Defined outputs** | Does the process produce a concrete, checkable artifact? |
| **Quality gates** | Are there objective criteria for success? |

### 2.2 When NOT to Create a Skill

Do **not** create a skill when:

- The protocol defines organizational conventions (e.g., `OrganisationSpaceRules.md`) — these are reference documents, not workflows
- The protocol is tightly coupled to repo-specific paths and structures that change frequently
- The process requires significant human judgment at every step
- The protocol is a one-time migration or setup task

### 2.3 Many-to-One and One-to-Many Relationships

- **Many protocols → One skill:** A skill may distill multiple related protocols (e.g., `evidence-first-article-writing` combines `Article_Techniques.md` and `ArticleCreation.md`)
- **One protocol → Many skills:** A large protocol may be split into multiple skills by domain or phase

---

## 3. Skill Structure

### 3.1 Required Files

Every skill must have:

```
skills/<skill-name>/
├── SKILL.md              # Main skill definition (required)
└── references/           # Supporting reference files (optional)
    └── protocol-map.md   # Maps skill sections to source protocols (recommended)
```

### 3.2 SKILL.md Format

```markdown
---
name: <skill-name>
description: "<One-sentence description of what the skill does and when to use it.>"
version: 1.0.0
---

# <Skill Title>

<One-paragraph summary: what this skill does and which protocol(s) it distills.>

## When to use this skill

- <Trigger condition 1>
- <Trigger condition 2>
- <Trigger condition 3>

## Prerequisites

- <What must be true before starting>
- <What files/resources must exist>

## The Process

### Step 1: <Step Name>
<Concrete, actionable instruction>

### Step 2: <Step Name>
<Concrete, actionable instruction>

...

## Quality Gates

- [ ] <Objective check 1>
- [ ] <Objective check 2>
- [ ] <Objective check 3>

## Output

<What the skill produces and where it goes>

## References

- <Link to source protocol 1>
- <Link to source protocol 2>
```

### 3.3 protocol-map.md Format

```markdown
# <Skill Name> — References

- <Process/Section>: `Rules and Regulations/Protocols/<file>.md` (<sections>)
- <Process/Section>: `Rules and Regulations/Protocols/<file>.md` (<sections>)
- <External resource>: <path or URL>
- <Worked example>: <path to example output>
```

---

## 4. The Conversion Process

### Phase 1: Analyze the Protocol

**Goal:** Understand the protocol's structure and identify skill-worthy content.

1. **Read the protocol in full**
2. **Identify the core process** — What are the main steps?
3. **Identify the triggers** — When should this process be used?
4. **Identify the quality gates** — How do you know it's done right?
5. **Identify dependencies** — What other protocols, files, or resources are needed?

**Output:** A mental (or written) map of the protocol's skill-relevant content.

---

### Phase 2: Define the Skill Boundary

**Goal:** Determine what the skill covers and what it doesn't.

1. **Define the scope** — What is the single, clear purpose of this skill?
2. **Identify the trigger** — What condition causes an agent to invoke this skill?
3. **Identify the output** — What concrete artifact does the skill produce?
4. **Identify the boundaries** — What is explicitly out of scope?

**Output:** A one-sentence skill definition.

---

### Phase 3: Distill the Process

**Goal:** Convert the protocol's formal steps into actionable agent instructions.

For each step in the protocol:

1. **Make it imperative** — "Extract the source register" not "The source register is extracted"
2. **Make it specific** — Name exact files, functions, and tools
3. **Make it verifiable** — Include a check the agent can perform
4. **Remove ambiguity** — If a step requires judgment, define the decision rule

**Conversion patterns:**

| Protocol Language | Skill Language |
|-------------------|----------------|
| "The process should ensure X" | "Verify X by running Y" |
| "It is recommended to use Z" | "Use Z" |
| "Quality criteria include A, B, C" | "Quality gates: [ ] A [ ] B [ ] C" |
| "The output is placed in directory D" | "Write output to D" |

**Output:** A step-by-step process section.

---

### Phase 4: Add Triggers and Context

**Goal:** Help the agent know when to use this skill.

1. **Write the description** — One sentence that names the trigger and the outcome
2. **List trigger conditions** — Concrete situations that should invoke this skill
3. **List prerequisites** — What must be true before starting
4. **Add cross-references** — Link to related skills

**Output:** Complete frontmatter and "When to use" section.

---

### Phase 5: Add Quality Gates

**Goal:** Define objective success criteria.

1. **Extract all quality criteria** from the protocol
2. **Convert to checklist items** — Each must be objectively verifiable
3. **Add verification commands** — Where possible, include a command or check
4. **Define failure conditions** — What happens if a gate fails?

**Output:** Quality gates section.

---

### Phase 6: Create Reference Files

**Goal:** Provide traceability back to source protocols.

1. **Create `references/protocol-map.md`** — Map each skill section to its source protocol section
2. **Add external references** — Link to related files, tools, or documentation
3. **Add worked examples** — Point to real outputs if they exist

**Output:** Complete reference files.

---

### Phase 7: Review and Validate

**Goal:** Ensure the skill is complete, accurate, and actionable.

1. **Check completeness** — Does the skill cover all protocol steps?
2. **Check accuracy** — Does the skill faithfully represent the protocol?
3. **Check actionability** — Can an agent follow this without reading the protocol?
4. **Check verifiability** — Are all quality gates objective?
5. **Check consistency** — Does the skill follow the format in Section 3?

**Output:** A validated, ready-to-use skill.

---

## 5. Quality Criteria

A good skill:

- [ ] **Triggered** — Has clear, concrete trigger conditions
- [ ] **Self-contained** — An agent can execute it without reading the protocol first
- [ ] **Specific** — Names exact files, functions, and tools (not "the database" but "data/smarthome.duckdb")
- [ ] **Verifiable** — Has objective quality gates with concrete checks
- [ ] **Traceable** — References source protocols in `references/protocol-map.md`
- [ ] **Consistent** — Follows the format defined in Section 3
- [ ] **Scoped** — Covers one clear purpose; doesn't try to do everything
- [ ] **Current** — Reflects the latest version of the source protocol(s)

---

## 6. Maintenance

### 6.1 When to Update a Skill

Update a skill when:

- The source protocol is revised
- New trigger conditions are discovered
- Quality gates change
- New reference files or examples become available

### 6.2 Versioning

- **Major version (1.0.0 → 2.0.0):** Process fundamentally changes
- **Minor version (1.0.0 → 1.1.0):** New steps or quality gates added
- **Patch version (1.0.0 → 1.0.1):** Clarifications, typo fixes, reference updates

### 6.3 Deprecation

A skill should be deprecated when:

- The source protocol is removed or replaced
- The process is no longer used in the project
- A better skill supersedes it

Deprecated skills should be moved to `skills/_deprecated/` with a note pointing to the replacement.

---

## 7. Example: Converting NovelProductSuggestor to a Skill

### Step 1: Analyze the Protocol

`NovelProductSuggestor.md` contains:
- 5 phases (Reconnaissance, Deep Reading, Synthesis, Product Ideation, Structuring)
- Clear inputs (research folder) and outputs (markdown file)
- Quality criteria (Section 5)
- A worked example (Section 6)

### Step 2: Define the Skill Boundary

**Scope:** Generate novel product suggestions from a research folder.
**Trigger:** When asked to create product ideas from research content.
**Output:** A markdown file with 8-15 product suggestions.

### Step 3: Distill the Process

```markdown
## The Process

### Step 1: Reconnaissance
List the research folder structure. Identify subfolders and files.

### Step 2: Deep Reading
Read cross-cutting documents first, then product logic files, then examples.
Extract: principles, patterns, constraints, strengths, pairings.

### Step 3: Synthesis
Identify recurring themes, complementary pairings, gaps, cross-domain applications.

### Step 4: Product Ideation
Generate 8-15 ideas using: combine principles, apply patterns to new domains,
remove constraints, scale strengths.

### Step 5: Structuring and Writing
Write each idea with: Name, Principle, Concept, Why it's novel, Languages.
Add summary table and common threads.
```

### Step 4: Add Triggers

```markdown
## When to use this skill

- Generating product ideas from a research folder (e.g., research/Programming Languages/)
- Creating a new wave of product suggestions
- Exploring commercial opportunities from research content
```

### Step 5: Add Quality Gates

```markdown
## Quality Gates

- [ ] 8-15 product ideas generated
- [ ] Each idea has: Name, Principle, Concept, Why it's novel, Languages
- [ ] Every idea traces to a specific research principle
- [ ] No idea duplicates an existing product (check DistinctProductExamples)
- [ ] Summary table included
- [ ] Common threads section included
```

---

## 8. Relationship to Other Protocols

| Protocol | Relationship |
|----------|-------------|
| `NovelProductSuggestor.md` | Source protocol for `novel-product-suggestor` skill |
| `Evaluation_of_SoftwareIDEAS.md` | Source protocol for `software-idea-evaluation` skill |
| `FromStep1toStep2.md` | Source protocol for `step1-to-step2-transition` skill |
| `evidence-first-article-writing` (skill) | Existing skill demonstrating the pattern |

---

*Document version: 1.0*
*Last updated: 2026-10-01*
