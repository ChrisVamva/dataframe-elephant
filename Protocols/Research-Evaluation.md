# Research Evaluation Protocol

## Status

This protocol is mandatory for every person, agent, or process that evaluates research in this project. A research item is not ready for `research/processed/` until it passes the required gates below.

## 1. Purpose

Evaluate research for whether it is:

- **Traceable:** every material claim can be followed to supporting evidence.
- **Accurate:** the source supports the claim as written, without overstatement.
- **Well-scoped:** definitions, boundaries, time period, and population are explicit.
- **Useful:** the result answers the research question and can support later modeling or analysis.
- **Reproducible:** another evaluator can repeat the search, interpretation, and decision.
- **Uncertainty-aware:** facts, signals, inferences, and recommendations are not conflated.

This protocol evaluates research quality, not whether the evaluator agrees with the conclusion.

## 2. Non-negotiable rules

Every evaluation must:

1. State the research question, scope, and intended use.
2. Separate observations from interpretation and recommendations.
3. Preserve provenance at claim level whenever practical.
4. Identify source type, author or publisher, title, URL, publication date when available, and access date.
5. Prefer primary sources. Use independent sources for important claims, especially claims about companies, products, markets, roles, and current capabilities.
6. Record the date-sensitive nature of claims. Do not present current or changing information as timeless.
7. Record uncertainty, conflicting evidence, missing evidence, and likely source bias.
8. Use stable names and explicit relationships between entities. Do not merge distinct concepts because they share a label.
9. State what evidence would change or falsify the conclusion.
10. Reject unsupported specificity. A precise claim requires precise evidence.

## 3. Required evaluation record

Each evaluated research item must contain the following fields, in Markdown or an equivalent structured format:

| Field | Required content |
| --- | --- |
| Research question | The question being answered, including the decision or model it supports |
| Scope | Included and excluded entities, workflow stages, geography, population, and time period |
| Evaluation date | Date the item was evaluated |
| Evaluator | Person, agent, or process identifier |
| Claims | One claim per row or clearly separable statement |
| Claim type | `documented fact`, `reported signal`, `inference`, or `recommendation` |
| Evidence | Source(s) supporting or contradicting each material claim |
| Confidence | `high`, `medium`, or `low`, with a reason |
| Limitations | Missing data, uncertainty, source bias, conflicts, and freshness concerns |
| Falsifier | Evidence or observation that would change the claim or conclusion |
| Decision | `accept`, `accept with limitations`, `revise`, or `reject` |

## 4. Evaluation gates

Evaluate in order. A failure at an earlier gate must be resolved before later quality can compensate for it.

### Gate A: Question and scope

Pass only if the item defines what is being investigated and what is outside scope.

Check:

- Is the question specific enough to investigate?
- Are key terms defined rather than assumed?
- Is the relevant time period stated?
- Are comparisons using the same unit, population, or workflow stage?
- Is the intended output clear: description, comparison, model input, decision support, or recommendation?

Fail when the item answers a broader or different question than the one posed.

### Gate B: Source quality and coverage

Classify every source as **primary**, **secondary**, or **internal synthesis**.

Preferred evidence, in order:

1. Standards, specifications, peer-reviewed research, official documentation, official datasets, and first-party records.
2. First-party technical or product material, engineering posts, official job postings, and direct organizational statements.
3. Reputable secondary analysis that identifies its evidence and methods.
4. Unverified summaries, aggregators, rankings, commentary, or search snippets, used only as leads or explicitly low-confidence context.

Check:

- Does each source directly support the claim?
- Are important claims supported by more than one independent source when feasible?
- Is the source authoritative for this particular claim?
- Is the evidence current enough for a time-sensitive claim?
- Does the source have a commercial, institutional, or selection bias?

Do not count multiple pages that repeat the same originating claim as independent confirmation.

### Gate C: Claim and citation alignment

Break the item into atomic claims. For each material claim, record:

| Claim | Type | Supporting evidence | Contradicting evidence | Confidence | Reason |
| --- | --- | --- | --- | --- | --- |

Pass only when the wording does not exceed what the evidence establishes.

- A **documented fact** is directly stated or directly observable in a reliable source.
- A **reported signal** is an observed report or indication that is not sufficient to establish a general fact.
- An **inference** is the evaluator's reasoned conclusion from cited evidence.
- A **recommendation** is a proposed action or judgment, not a source-established fact.

Use qualifiers such as `the source reports`, `in this sample`, `as of [date]`, or `the evidence suggests` when generalization is not justified.

### Gate D: Method and reasoning

Pass only if the path from question to conclusion is inspectable.

Record, as applicable:

- Search terms, databases, sites, or datasets consulted.
- Inclusion and exclusion criteria.
- Extraction or transcription method.
- Transformations, normalization, calculations, and assumptions.
- Comparison criteria and weighting.
- How conflicting evidence was handled.
- Whether an agent or automated tool was used, including its role and human checks.

An unrecorded transformation or unexamined assumption is a reproducibility defect.

### Gate E: Completeness and counterevidence

Pass only after actively looking for evidence that could weaken the conclusion.

Check:

- Are relevant alternatives, exceptions, and boundary cases included?
- Are negative results and unavailable evidence recorded?
- Were contradictory sources investigated rather than silently omitted?
- Are categories mutually understandable and non-duplicative?
- Are workflow dependencies, failure modes, and trade-offs described?

The evaluator must not treat absence of evidence as evidence of absence unless the search design supports that conclusion.

### Gate F: Usefulness and data readiness

Pass only if a later researcher or data modeler can use the result without reconstructing the investigation from scratch.

Check:

- Are entities named consistently?
- Are relationships explicit, such as `uses`, `implemented_by`, `produced_by`, `governs`, `performs`, or `supports`?
- Are duplicate concepts distinguished?
- Are dates, versions, units, and jurisdictions retained?
- Can claims and sources be represented as separate records?
- Are open questions and next investigations listed?

## 5. Confidence rubric

Confidence describes support for a claim, not the importance of the claim.

| Level | Required conditions |
| --- | --- |
| High | Direct, relevant primary evidence; strong claim-source alignment; corroboration when the claim is material; no unresolved contradiction that changes the conclusion |
| Medium | Relevant evidence exists, but coverage, independence, recency, generalizability, or source quality is limited; limitations are explicit |
| Low | Indirect, sparse, conflicting, outdated, or mostly secondary evidence; the claim is retained only as a lead, signal, or clearly labeled inference |

Confidence must be assigned per material claim. A high-confidence source does not automatically make every conclusion drawn from it high confidence.

## 6. Decision rules

- **Accept:** all mandatory gates pass; material claims have adequate evidence and explicit confidence.
- **Accept with limitations:** the item is useful despite documented gaps; no unsupported claim is presented as established fact.
- **Revise:** the question is useful, but claims, citations, scope, method, or structure require correction or additional investigation.
- **Reject:** the item is materially untraceable, answer-misaligned, plagiarized, irreparably biased for its intended use, or unsupported after reasonable investigation.

Any failed mandatory gate requires `revise` or `reject`. The evaluator must name the failed gate and the smallest corrective action.

## 7. Minimum review procedure

For every item, the evaluator must:

1. Read the question, scope, conclusion, and source list before judging individual claims.
2. Extract the material claims and label each claim type.
3. Open or verify each source used for a material claim.
4. Check whether the source actually supports the wording and whether important context was omitted.
5. Search for at least one credible alternative, limitation, or counterexample.
6. Assign claim-level confidence and record the reason.
7. Confirm that entities, relationships, dates, and provenance are usable for later analysis.
8. Record the decision, failed or passed gates, limitations, and next action.

## 8. Standard evaluation template

```markdown
# Evaluation: [research item]

## Scope
- Research question:
- Intended use:
- Included:
- Excluded:
- Time period and evaluation date:
- Evaluator:

## Gate results
| Gate | Result | Evidence or defect |
| --- | --- | --- |
| A. Question and scope | pass / fail | |
| B. Source quality and coverage | pass / fail | |
| C. Claim and citation alignment | pass / fail | |
| D. Method and reasoning | pass / fail | |
| E. Completeness and counterevidence | pass / fail | |
| F. Usefulness and data readiness | pass / fail | |

## Claim review
| Claim | Type | Sources | Counterevidence | Confidence | Reason |
| --- | --- | --- | --- | --- | --- |

## Limitations and open questions
-

## Decision
- Outcome: accept / accept with limitations / revise / reject
- Failed gates:
- Required next action:
- Falsifier or update trigger:
```

## 9. Update triggers

Re-evaluate an accepted item when any of the following occurs:

- A source is withdrawn, materially corrected, or becomes inaccessible.
- A product, company, role, technology, standard, or workflow changes materially.
- New credible evidence contradicts a material claim.
- The research is reused for a different population, geography, decision, or time period.
- The schema, entity definitions, or workflow changes in a way that affects interpretation.

When updating, preserve the previous evaluation date, decision, and evidence trail. Do not silently overwrite history.

## 10. Final quality principle

The standard is not that research is certain. The standard is that a reasonable evaluator can see what is claimed, why it is claimed, how well it is supported, what remains uncertain, and what would change the result.