---
name: software-idea-evaluation
description: "Evaluates and rates waves of product ideas from Step 1 using 5 weighted criteria (Technical Feasibility, Market Potential, Differentiation, Team Fit, Excitement). Use when asked to evaluate product ideas, rank suggestions, or decide which products should advance to Step 2. Produces a structured evaluation document with scores, tiers, and recommendations."
version: 1.0.0
---

# Software Idea Evaluation

Evaluates and rates waves of product ideas from Step 1, producing a structured assessment that informs which ideas advance to Step 2. Distilled from `Rules and Regulations/Protocols/Software Experties/Evaluation_of_SoftwareIDEAS.md`.

## When to use this skill

- Evaluating product ideas from a Step 1 wave
- Ranking product suggestions to decide which should advance to Step 2
- Asked to "evaluate these ideas" or "rate these products"
- Comparing multiple product ideas objectively

## Prerequisites

- Step 1 output exists (e.g., `Step 1/Wave 1/NovelProductSuggestions1.md`)
- Step 1 contains at least 5 product suggestions (enough to compare)
- Each Step 1 suggestion has: Name, Principle, Concept, Why it's novel, Languages
- You have read the full Step 1 document
- You have access to competitive landscape information (web search, existing products)

## The Evaluation Criteria

Each product is scored on five criteria, rated 1-5 (5 = best):

| Criterion | Weight | Question |
|-----------|--------|----------|
| **Technical Feasibility** | 25% | Can this be built with current technology? |
| **Market Potential** | 25% | Is there a real, painful problem? How large is the market? |
| **Differentiation** | 20% | How clearly does this differ from existing solutions? |
| **Team Fit** | 15% | Does it align with typical team skills and resources? |
| **Excitement** | 15% | Is this a product engineers would be motivated to build? |

**Overall Score Formula:**
```
Overall = (Feasibility × 0.25 + Market × 0.25 + Differentiation × 0.20 + Team Fit × 0.15 + Excitement × 0.15) × 2
```

## The Process

### Step 1: Preparation

1. Read the full Step 1 document — understand all product suggestions
2. Research the competitive landscape — for each product, identify existing solutions
3. Gather any additional context — market data, user research, technical constraints

### Step 2: Individual Evaluation

For each product suggestion:

1. **Score each criterion** (1-5) with written justification
2. **Calculate the weighted overall score** (scaled to 1-10)
3. **Write a verdict** — 2-3 sentences summarizing the assessment
4. **Identify key risks** — what could make this product fail?

### Step 3: Comparative Ranking

1. **Rank all products** by overall score
2. **Group into tiers:**
   - **Tier 1 (7.0+):** Strong candidates for Step 2
   - **Tier 2 (6.0-6.9):** Promising but needs refinement
   - **Tier 3 (5.0-5.9):** Good ideas, limited market or differentiation
   - **Tier 4 (<5.0):** Weak candidates, likely not worth pursuing

### Step 4: Synthesis

1. **Identify key insights** — what patterns emerge across the evaluations?
2. **Note common strengths** — what do the top products have in common?
3. **Note common weaknesses** — what do the bottom products have in common?
4. **Make recommendations** — which products should advance to Step 2?

### Step 5: Writing the Evaluation Document

Produce a structured evaluation document with:
- Evaluation methodology
- Individual evaluations (scores + verdicts for each product)
- Summary rankings table
- Tiered recommendations
- Key insights
- Recommended next steps

## Quality Gates

- [ ] Consistent — all products scored using the same criteria and scale
- [ ] Justified — every score has a written rationale
- [ ] Comparative — products are ranked relative to each other
- [ ] Honest — weaknesses and risks are acknowledged
- [ ] Actionable — clear recommendations for next steps
- [ ] Structured — follows the defined output format
- [ ] Complete — every product in Step 1 is evaluated

## Output

A markdown file (e.g., `NovelIdeasEvaluation1.md`) written to the Step 1 output directory.

## Principles for Fair Evaluation

- **Be objective, not emotional** — score based on evidence, not personal preference
- **Consider the full picture** — a product with one very high and one very low score is riskier than consistent medium scores
- **Acknowledge uncertainty** — if you don't know enough, say so
- **Think like an investor** — would you fund this? What's the path to revenue?
- **Think like an engineer** — would you want to build this? What's the maintenance burden?
- **Think like a user** — would you use this? What's the "aha moment"?

## Common Pitfalls to Avoid

- Scoring everything the same — force yourself to differentiate
- Ignoring the competitive landscape — always research existing solutions first
- Overweighting excitement — excitement is only 15%
- Underestimating integration complexity — cross-language integration is always harder than it looks
- Confusing novelty with value — a product can be novel but not valuable
- Sunk cost bias — don't score higher just because you spent time on it
- Confirmation bias — don't score higher because you want it to succeed

## References

- Process: `Rules and Regulations/Protocols/Software Experties/Evaluation_of_SoftwareIDEAS.md` (§§3-8: criteria, process, quality criteria, principles)
- Worked example: `Artifacts/software product ideas/Wave 1/Stage 1/Step 1/NovelIdeasEvaluation1.md`
- Step 1 to Step 2: `Rules and Regulations/Protocols/Software Experties/FromStep1toStep2.md`
- Skill creation: `Rules and Regulations/Protocols/SkillCreation.md`
