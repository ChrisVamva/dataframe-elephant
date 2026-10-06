# Evaluation of Software Ideas Protocol

**Version:** 1.0
**Purpose:** Define the principles, criteria, and process for evaluating and rating waves of product ideas in `Artifacts/software product ideas/Step 1/`.

---

## 1. Overview

This protocol describes how to systematically evaluate and rate product ideas generated in Step 1 (waves of suggestions). The evaluation produces a structured assessment that informs which ideas advance to Step 2 (building orientation).

### 1.1 Context

| Step | Location | Purpose |
|------|----------|---------|
| **Step 1** | `Artifacts/software product ideas/Step 1/Wave N/` | Waves of product suggestions derived from research principles |
| **Evaluation** | `Artifacts/software product ideas/Step 1/Wave N/` | Structured evaluation and rating of each wave's ideas |
| **Step 2** | `Artifacts/software product ideas/Step 2/` | Specific product building orientation for selected ideas |

### 1.2 The Evaluation in One Sentence

> Step 1 asks: *"What could we build?"*
> Evaluation asks: *"Which of these should we build?"*
> Step 2 asks: *"How would we actually build it?"*

---

## 2. Prerequisites

Before starting an evaluation:

- [ ] Step 1 output exists (e.g., `Step 1/Wave 1/NovelProductSuggestions1.md`)
- [ ] Step 1 contains at least 5 product suggestions (enough to compare)
- [ ] Each Step 1 suggestion has: Name, Principle, Concept, Why it's novel, Languages
- [ ] You have read the full Step 1 document
- [ ] You have access to competitive landscape information (web search, existing products)

---

## 3. Evaluation Criteria

Each product is scored on five criteria, rated 1-5 (5 = best):

### 3.1 Technical Feasibility (Weight: 25%)

**Question:** Can this be built with current technology?

| Score | Meaning |
|-------|---------|
| 5 | Uses proven, mainstream technology. Integration patterns are well-understood. |
| 4 | Uses mostly proven technology. Some integration challenges but solvable. |
| 3 | Uses a mix of proven and emerging technology. Significant integration challenges. |
| 2 | Uses emerging or niche technology. Major technical risks. |
| 1 | Uses speculative or research-stage technology. May not be buildable yet. |

**Considerations:**
- Are the required languages/frameworks mature and well-supported?
- Are the integration points between components well-understood?
- Are there existing libraries or tools that solve the hard parts?
- What is the estimated complexity (simple / moderate / complex / research-level)?

---

### 3.2 Market Potential (Weight: 25%)

**Question:** Is there a real, painful problem? How large is the addressable market?

| Score | Meaning |
|-------|---------|
| 5 | Large, growing market with a clear, painful problem. Strong willingness to pay. |
| 4 | Significant market with a real problem. Some willingness to pay. |
| 3 | Moderate market. Problem exists but may not be urgent. |
| 2 | Niche market. Problem is real but limited audience. |
| 1 | Unclear market. Problem may not exist or may not be painful enough. |

**Considerations:**
- How many people/teams/companies have this problem?
- How painful is the problem (annoyance / inconvenience / blocker)?
- Are they actively seeking solutions?
- What is the competitive landscape (crowded / fragmented / greenfield)?
- Is there a clear path to monetization?

---

### 3.3 Differentiation (Weight: 20%)

**Question:** How clearly does this differ from existing solutions? Is the gap meaningful?

| Score | Meaning |
|-------|---------|
| 5 | Completely novel. No direct competitors. Creates a new category. |
| 4 | Significant differentiation. Clear improvement over existing solutions. |
| 3 | Some differentiation. Better in some ways, similar in others. |
| 2 | Minor differentiation. Incremental improvement over existing solutions. |
| 1 | No meaningful differentiation. "Me-too" product. |

**Considerations:**
- What existing products address this problem?
- What do they do well? What do they miss?
- Is the product's unique value proposition clear and compelling?
- Would users switch from existing solutions? Why?
- Is the differentiation sustainable (hard to copy) or temporary?

---

### 3.4 Team Fit (Weight: 15%)

**Question:** Does it align with typical team skills and available resources?

| Score | Meaning |
|-------|---------|
| 5 | Perfect fit. Uses skills the team already has. Easy to hire for. |
| 4 | Good fit. Mostly aligns with team skills. Some learning required. |
| 3 | Moderate fit. Requires some new skills but learnable. |
| 2 | Poor fit. Requires significant new expertise. Hard to hire for. |
| 1 | Very poor fit. Requires rare or research-level expertise. |

**Considerations:**
- What languages/frameworks does the team already know?
- What is the learning curve for new technologies?
- How easy is it to hire developers with the required skills?
- Does the team have domain expertise in the problem area?
- What is the estimated ramp-up time?

---

### 3.5 Excitement (Weight: 15%)

**Question:** Is this a product engineers would be motivated to build and use?

| Score | Meaning |
|-------|---------|
| 5 | Highly compelling. Engineers would be passionate about building and using this. |
| 4 | Interesting. Engineers would be motivated to work on this. |
| 3 | Moderately interesting. Engineers would work on this but not excitedly. |
| 2 | Uninspiring. Engineers would see this as just another task. |
| 1 | Unappealing. Engineers would not want to work on this. |

**Considerations:**
- Does the product solve a problem engineers care about?
- Is the technical challenge interesting?
- Would engineers use this product themselves?
- Does the product have a compelling vision?
- Would this be a project engineers are proud to show?

---

## 4. Evaluation Process

### Phase 1: Preparation

1. **Read the full Step 1 document** — Understand all product suggestions
2. **Research the competitive landscape** — For each product, identify existing solutions
3. **Gather any additional context** — Market data, user research, technical constraints

### Phase 2: Individual Evaluation

For each product suggestion:

1. **Score each criterion** (1-5) with written justification
2. **Calculate the weighted overall score** (scaled to 1-10)
3. **Write a verdict** — 2-3 sentences summarizing the assessment
4. **Identify key risks** — What could make this product fail?

**Formula:**
```
Overall = (Feasibility × 0.25 + Market × 0.25 + Differentiation × 0.20 + Team Fit × 0.15 + Excitement × 0.15) × 2
```

### Phase 3: Comparative Ranking

1. **Rank all products** by overall score
2. **Group into tiers:**
   - **Tier 1 (7.0+):** Strong candidates for Step 2
   - **Tier 2 (6.0-6.9):** Promising but needs refinement
   - **Tier 3 (5.0-5.9):** Good ideas, limited market or differentiation
   - **Tier 4 (<5.0):** Weak candidates, likely not worth pursuing

### Phase 4: Synthesis

1. **Identify key insights** — What patterns emerge across the evaluations?
2. **Note common strengths** — What do the top products have in common?
3. **Note common weaknesses** — What do the bottom products have in common?
4. **Make recommendations** — Which products should advance to Step 2?

### Phase 5: Writing the Evaluation Document

Produce a structured evaluation document following the template in Section 5.

---

## 5. Output Format

The evaluation document should follow this structure:

```markdown
# Novel Ideas Evaluation N

**Date:** [YYYY-MM-DD]
**Source:** Evaluation of `[Step 1 filename]` ([N] product ideas)
**Evaluator:** [Name/Team]

---

## 1. Evaluation Methodology
[Brief description of criteria and weights]

---

## 2. Individual Evaluations

### 1. [Product Name]

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | X/5 | [Justification] |
| Market Potential | X/5 | [Justification] |
| Differentiation | X/5 | [Justification] |
| Team Fit | X/5 | [Justification] |
| Excitement | X/5 | [Justification] |

**Overall: X.X/10**

**Verdict:** [2-3 sentence summary]

---

[Repeat for each product]

---

## 3. Summary Rankings

| Rank | Product | Overall Score | Feasibility | Market | Differentiation | Team Fit | Excitement |
|------|---------|---------------|-------------|--------|-----------------|----------|------------|
| 1 | [Name] | X.X | X | X | X | X | X |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## 4. Recommendations

### Tier 1: Strong Candidates for Step 2
[Products with rationale]

### Tier 2: Promising but Needs Refinement
[Products with rationale]

### Tier 3: Good Ideas, Limited Market or Differentiation
[Products with rationale]

---

## 5. Key Insights
[Patterns and observations across all evaluations]

---

## 6. Recommended Next Steps
[Specific actions to take]
```

---

## 6. Quality Criteria

A good evaluation:

- [ ] **Consistent** — All products scored using the same criteria and scale
- [ ] **Justified** — Every score has a written rationale
- [ ] **Comparative** — Products are ranked relative to each other
- [ ] **Honest** — Weaknesses and risks are acknowledged
- [ ] **Actionable** — Clear recommendations for next steps
- [ ] **Structured** — Follows the defined output format
- [ ] **Complete** — Every product in Step 1 is evaluated

---

## 7. Principles for Fair Evaluation

### 7.1 Be Objective, Not Emotional

- Score based on evidence, not personal preference
- A product you don't like personally may still score high on market potential
- A product you find exciting may still score low on feasibility

### 7.2 Consider the Full Picture

- A product with one very high score and one very low score is riskier than a product with consistent medium scores
- Weight the criteria appropriately — feasibility and market potential matter most
- Don't let excitement override technical reality

### 7.3 Acknowledge Uncertainty

- If you don't know enough about a market, say so
- If a technical approach is unproven, flag it
- Use phrases like "appears to be," "likely," "may require"

### 7.4 Think Like an Investor

- Would you fund this product? Why or why not?
- What is the path to revenue?
- What is the risk-adjusted return?

### 7.5 Think Like an Engineer

- Would you want to build this? Why or why not?
- What is the estimated development time?
- What are the maintenance implications?

### 7.6 Think Like a User

- Would you use this product? Why or why not?
- What is the onboarding experience?
- What is the "aha moment"?

---

## 8. Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| **Scoring everything the same** | Force yourself to differentiate; not every product is a 3/5 |
| **Ignoring the competitive landscape** | Always research existing solutions before scoring differentiation |
| **Overweighting excitement** | Excitement is only 15% — don't let it dominate the score |
| **Underestimating integration complexity** | Cross-language and cross-system integration is always harder than it looks |
| **Confusing novelty with value** | A product can be novel but not valuable; score market potential separately |
| **Sunk cost bias** | Don't score a product higher just because you spent time on it in Step 1 |
| **Confirmation bias** | Don't score a product higher because you want it to succeed |

---

## 9. Relationship to Other Protocols

| Protocol | Relationship |
|----------|-------------|
| `NovelProductSuggestor.md` | Produces Step 1 output; this protocol evaluates it |
| `FromStep1toStep2.md` | Uses evaluation results to select products for Step 2 |
| `TransitionStage2.md` | Similar concept but for research data extraction (Stage 1 → Stage 2 research files) |

---

## 10. Example: Wave 1 Evaluation Summary

**Input:** `Step 1/Wave 1/NovelProductSuggestions1.md` (12 products)

**Top 3 Products:**

| Rank | Product | Score | Key Strength |
|------|---------|-------|--------------|
| 1 | EdgeDeploy | 7.8 | Large growing market, clear differentiation |
| 2 | Convex | 7.2 | Compelling vision, feasible technology |
| 3 | PolyglotDB | 7.0 | Highest market potential, completely novel |

**Key Insights:**
- Products using mainstream languages (Rust, Go, TypeScript, Python) score higher on team fit
- Haskell-based ideas score high on differentiation but low on feasibility and team fit
- Platform products have higher market potential than point solutions
- Developer tools are exciting but hard to monetize

**Recommendation:** Proceed with Step 2 for PolyglotDB (already in progress); evaluate EdgeDeploy as next candidate.

---

*Document version: 1.0*
*Last updated: 2026-10-01*
