---
name: step1-to-step2-transition
description: "Transforms a Step 1 product suggestion into a concrete Step 2 product building orientation. Use when asked to expand a product idea into a full technical approach, create a Step 2 document, or develop a product building plan. Applies the 6-phase process: Selection, Deep Analysis, Architecture Design, Development Planning, Risk Assessment, Writing."
version: 1.0.0
---

# Step 1 to Step 2 Transition

Transforms a Step 1 product suggestion into a concrete, actionable Step 2 product building orientation. Distilled from `Rules and Regulations/Protocols/Software Experties/FromStep1toStep2.md`.

## When to use this skill

- Expanding a product idea from Step 1 into a full technical approach
- Creating a Step 2 document for a selected product
- Developing a product building plan with architecture, phases, and risks
- Asked to "develop this product idea" or "create a Step 2 document"

## Prerequisites

- Step 1 output exists (e.g., `Step 1/Wave 1/NovelProductSuggestions1.md`)
- Step 1 contains at least 5 product suggestions (enough to choose from)
- Each Step 1 suggestion has: Name, Principle, Concept, Why it's novel, Languages
- The Step 2 output directory exists (`Artifacts/software product ideas/Step 2/`)
- You have read the full Step 1 document

## The Process

### Step 1: Selection — Choosing One Product

1. **List all Step 1 suggestions** — write down each product name and one-line concept
2. **Score each suggestion** on these criteria (1-5):
   - Technical Feasibility (High weight)
   - Market Potential (High weight)
   - Differentiation (Medium weight)
   - Team Fit (Medium weight)
   - Excitement (Low weight)
3. **Calculate weighted scores** — sum the scores
4. **Select the top candidate** — highest-scoring suggestion becomes the Step 2 focus
5. **Document the decision** — record why this product was chosen over others

### Step 2: Deep Analysis — Understanding the Product

1. **Research the problem space:**
   - Identify the core problem — what specific pain point does this solve?
   - List existing solutions — what products already address this?
   - Find the gap — what do existing solutions miss?
   - Validate the gap — is this gap real and worth filling?

2. **Analyze technical requirements** for each language/technology:
   - What is this language's role in the product?
   - What are the integration points between languages?
   - What are the known constraints of this language?
   - What libraries/frameworks are needed?
   - What is the performance characteristics?

3. **Identify key technical challenges** (top 3-5):
   - Challenge description — what is hard about this?
   - Why it's hard — what makes this non-trivial?
   - Possible approaches — what are the options?
   - Risk level — High, Medium, or Low?

### Step 3: Architecture Design — How It Fits Together

1. **Component breakdown** — decompose into core components:
   ```
   Product Name
   ├── Component 1
   │   ├── Technology: [language/framework]
   │   ├── Responsibility: [what it does]
   │   └── Dependencies: [what it needs]
   └── Component N
       ├── Technology: [language/framework]
       ├── Responsibility: [what it does]
       └── Dependencies: [what it needs]
   ```

2. **Data flow** — describe how data moves:
   - Input — where does data enter?
   - Processing — what transformations happen?
   - Output — where does data leave?
   - Storage — where is data persisted?

3. **Integration points** — for each pair of components:
   - Mechanism (gRPC, HTTP, shared memory, etc.)
   - Data format (Protobuf, JSON, Arrow, etc.)
   - Challenge (serialization overhead, latency, etc.)

### Step 4: Development Planning — How to Build It

1. **Define 3-5 phases**, each with:
   - Clear goal
   - Testable deliverables
   - Builds on previous phase
   - Achievable in 1-3 months

2. **For each phase, specify:**
   - Goal
   - Deliverables (checklist)
   - Tech stack
   - Success criteria
   - Estimated duration

3. **Identify dependencies** between phases

4. **Define success metrics** for each phase:
   - Metric name
   - Target value
   - How to measure

### Step 5: Risk Assessment — What Could Go Wrong

1. **Technical risks** — likelihood, impact, mitigation
2. **Market risks** — likelihood, impact, mitigation
3. **Execution risks** — likelihood, impact, mitigation

### Step 6: Writing the Step 2 Document

Produce a document with this structure:

```markdown
# [Product Name] — [Tagline]

**Step 2: Initial Product Approach**
**Source:** Derived from `Step 1/[filename]` — Product #[N]
**Date:** [YYYY-MM-DD]

## 1. Product Vision
### 1.1 Problem Statement
### 1.2 Solution
### 1.3 Value Proposition

## 2. Technical Architecture
### 2.1 High-Level Architecture
### 2.2 Core Components
### 2.3 Data Flow

## 3. Language Integration Strategy
### 3.1 Why These Languages?
### 3.2 Data Marshaling
### 3.3 Transaction Coordination (if applicable)

## 4. Development Phases
### Phase 1: [Name]
### Phase 2: [Name]
### Phase 3: [Name]
### Phase 4: [Name]

## 5. Technical Challenges & Solutions
### Challenge 1: [Name]
### Challenge 2: [Name]
### Challenge 3: [Name]

## 6. Competitive Landscape

## 7. Success Metrics

## 8. Team & Responsibilities

## 9. Open Questions

## 10. Next Steps
```

## Quality Gates

- [ ] Specific — names exact languages, libraries, and tools
- [ ] Grounded — every technical decision traces back to a Step 1 principle
- [ ] Feasible — the development plan is realistic given current technology
- [ ] Complete — covers all sections from the template
- [ ] Honest — acknowledges risks, unknowns, and open questions
- [ ] Actionable — a reader could start building after reading it
- [ ] Structured — follows the defined document structure
- [ ] Measurable — has concrete success metrics for each phase

## Output

A markdown file (e.g., `EdgeDeploy.md`) written to the Step 2 output directory.

## Tips

- Start with the problem, not the solution — make sure the problem is real
- Use the Step 1 principles as guardrails — if a technical decision contradicts a principle, reconsider
- Draw diagrams — architecture and data flow diagrams save paragraphs of explanation
- Include code examples — even pseudo-code helps readers understand the approach
- Be realistic about timelines — everything takes longer than you think
- Identify the riskiest assumption — test that first
- Write for a new team member — the document should be enough for someone new to start contributing

## References

- Process: `Rules and Regulations/Protocols/Software Experties/FromStep1toStep2.md` (§§3-7: 6-phase process, document structure, quality criteria)
- Worked example: `Artifacts/software product ideas/Wave 1/Stage 1/Step 2/EdgeDeploy.md`
- Evaluation: `Rules and Regulations/Protocols/Software Experties/Evaluation_of_SoftwareIDEAS.md`
- Skill creation: `Rules and Regulations/Protocols/SkillCreation.md`
