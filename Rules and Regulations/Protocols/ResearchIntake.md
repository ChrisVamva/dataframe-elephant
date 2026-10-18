---
status: accepted
scope: All research entry points (Stage 1 waves, brainstorm-to-wave promotion, Stage 2 follow-up research, article-idea research)
created: 2026-10-12
accepted: 2026-10-12
maintainer: workspace maintainer (personal name not recorded)
---

# Research Intake Protocol

## Status

This protocol is mandatory for every person, agent, or process that begins research in this project. No web search, source fetch, source-register seeding, skeleton creation, or research-agent dispatch may begin until the intake gates below pass.

## 1. Purpose

Research quality is bounded by how well the question is fixed before evidence is gathered. This protocol turns the previously implicit step — the bare "user confirms" that the Fusion Energy working pattern carried and later waves dropped — into a recorded, repeatable intake.

It exists to:

- Fix the subject, scope, boundary, and intended output before any search begins.
- Produce the scope fields that downstream stages already consume: `RE:Gate A` in `Research-Evaluation.md`, Step 1 of `TransitionStage2.md`, and Step 1 of `ArticleCreation.md`.
- Let a researcher start from a strong default set when the requester has no prepared brief, without guessing silently.

This protocol defines *how a subject is fixed*. It does not duplicate the evaluation gates in `Rules and Regulations/Protocols/Research-Evaluation.md` or the question-scoping rules in `Rules and Regulations/Protocols/FollowUpResearch.md`; it feeds them.

## 2. When the intake applies

Run the intake when a subject is selected, and complete it **before** any of the following:

- creating the subject's skeleton, README, or source register;
- any web search, source fetch, or research-agent dispatch;
- promoting a bottom-up follow-up question into a research pass;
- beginning article-idea research.

Re-run the intake, and add a new dated record, whenever the scope changes materially mid-survey — a tier, geography, or time period added or removed. Supersede the earlier record; never edit it to match the new scope (`OrganisationSpaceRules.md` §5).

**Cost of a late intake (worked precedent).** The AI Agent Memory wave (`research/raw/Stage 1/Wave 7/`) was first scoped to coding agents, began its survey, then widened to AI agents generally; the widening reordered its findings and required a second research pass. An intake at subject-selection time would have surfaced the breadth question before any search.

## 3. The intake questionnaire

Run **one round of at most four questions** through the interactive question tool, so the requester chooses from concrete options instead of writing a brief. Every question carries a recommended default and a "use your default" option. When a default is taken, record it as an explicit assumption — never as if the requester had stated it.

Derive each default from the strongest available source, in this order: the source brainstorm or ratings item; the closest established convention in an existing wave; the narrowest defensible reading of the request.

**Round 1 — subject and scope (always):**

| # | Question | Default derivation |
|---|----------|--------------------|
| 1 | Subject and the one-sentence research question | headline of the source brainstorm or ratings item |
| 2 | In scope — entities, product tiers, or populations included | the tiers or cases named in the source item |
| 3 | Out of scope — what is explicitly excluded | adjacent concepts named in the source item |
| 4 | Boundary — geography, time period, and unit of comparison | inferred from the source item; stated as an assumption |

**Round 2 — evidence and output (only when Round 1 leaves a material gap):**

| # | Question | Default derivation |
|---|----------|--------------------|
| 5 | Intended output — article, database, decision aid, or brief | the destination the subject was promoted for |
| 6 | Minimum acceptable evidence class, and which source tiers count | the preferred-evidence order in `Rules and Regulations/Protocols/Research-Evaluation.md` §4 |
| 7 | Comparators — alternatives, competitors, or counterexamples to cover | the comparison set in the source item |
| 8 | Stop criteria — what makes the survey complete | saturation of the declared questions |

A vague answer (for example, a category label such as "the AI market") is re-asked **once** with concrete options. A category label is not a scope. If it stays vague, propose a bounded scope, flag it as an assumption, and require confirmation.

## 4. Required answers and the fields they must produce

The intake record must state, at minimum:

- Research question, and the decision or artifact it supports.
- In-scope entities, tiers, or populations.
- Out-of-scope items (the exclusions).
- Boundary: geography, time period, unit of comparison.
- Intended output.
- Minimum evidence class and target source tiers.
- Origin provenance: the brainstorm, ratings, or request that selected the subject, with its date.
- Assumptions: every default taken in place of an explicit answer.

These are exactly the fields `RE:Gate A` requires, the scope and intended use `TransitionStage2.md` Step 1 records, and the exclusions `ArticleCreation.md` Step 1 needs. Nothing outside this list is asked for.

## 5. Intake gates

Evaluate in order; a failure earlier blocks later progress.

| Gate | Pass condition |
|------|----------------|
| `RI:Gate A` — Scope declared | Question specific enough to investigate; in-scope and out-of-scope stated; geography, time period, and unit of comparison stated. |
| `RI:Gate B` — Intended output named | The artifact or decision the research supports is stated (article, database, decision aid, or brief). |
| `RI:Gate C` — Evidence bar set | Minimum evidence class and target source tiers named; comparator set stated, or explicitly declared empty. |
| `RI:Gate D` — Provenance and defaults disclosed | Subject origin recorded with a date; every default taken is flagged as an assumption. |

Gate identifiers are qualified as `RI:` to avoid collision with `RE:` (Research-Evaluation) and `FU:` (FollowUpResearch), as required by `MaintainingProsperity.md` R2. Note a current limitation: the prompt linter (`src/prompt_core.py`, rule R2) recognises only the `RE:` and `FU:` qualifiers, so prompt templates cite this protocol **by path** — not by `RI:` gate ID — and reference `RE:Gate A` for the downstream scope gate.

## 6. Non-negotiable rules

1. No search, fetch, register seeding, skeleton creation, or agent dispatch before `RI:Gate A`–`RI:Gate D` pass.
2. Ask through the interactive question tool, not a wall of prose.
3. Every question carries a recommended default; a default is recorded as an assumption, never as the requester's answer.
4. A vague answer is re-asked once with concrete options; a label is not a scope.
5. Restate the agreed scope in one paragraph and obtain confirmation before the first search.
6. Re-run the intake on any material scope change; supersede, never overwrite, the earlier record.
7. This protocol is authoritative for the question set. `src/prompt_templates/templates/research_intake.md` is the downstream mirror (R9) that renders it as a form; update the protocol first and the mirror second (R1, R9).
8. Cite, do not duplicate, `RE:Gate A`, `FU:Gate A`, and Step 1 of `TransitionStage2.md`.

## 7. Record template

Create `<Wave folder>/00_Index/Intake.md` for the subject. Use this shape:

```markdown
# Research Intake — [subject] (Wave N)

- Date: YYYY-MM-DD
- Interviewer: [agent or person]
- Subject origin: [brainstorm / ratings file, date, rank]

## Answers
| # | Question | Answer | Source of answer |
|---|----------|--------|------------------|
| 1 | Subject and research question | | user / default |
| 2 | In scope | | user / default |
| 3 | Out of scope | | user / default |
| 4 | Boundary (geography, time, unit) | | user / default |
| 5 | Intended output | | user / default |
| 6 | Minimum evidence class / source tiers | | user / default |
| 7 | Comparators | | user / default |
| 8 | Stop criteria | | user / default |

## Declared scope
- Research question:
- In scope:
- Out of scope:
- Boundary (geography, time period, unit of comparison):
- Intended output:
- Minimum evidence class and source tiers:
- Comparators:
- Stop criteria:

## Gate results
| Gate | Result | Note |
|------|--------|------|
| RI:Gate A | pass / fail | |
| RI:Gate B | pass / fail | |
| RI:Gate C | pass / fail | |
| RI:Gate D | pass / fail | |

## Assumptions and open questions
- [every default taken, and anything left unresolved]
```

Record a dated row in the wave's `00_Index/Index.md`, for example: `Research intake completed (RI:Gate A–D pass); scope recorded in 00_Index/Intake.md`.

## 8. Exit criteria and update triggers

The intake is complete when `RI:Gate A`–`RI:Gate D` pass, the record exists, the wave index has a dated row, and the requester has confirmed the restated scope. Search may then begin.

Update triggers:

- A material scope change (tier, geography, or time period added or removed).
- A contested or ambiguous answer later contradicted by the evidence.
- Selection of a different subject after the intake was taken.
- A change to the downstream scope gates (`RE:Gate A`, `TransitionStage2.md` Step 1, `ArticleCreation.md` Step 1) that changes which fields the intake must capture.

## 9. Related documents

- `Rules and Regulations/Protocols/Research-Evaluation.md` — `RE:Gate A` (question and scope) is the downstream consumer of this intake.
- `Rules and Regulations/Protocols/FollowUpResearch.md` — `FU:Gate A` scope requirements for follow-up questions.
- `Rules and Regulations/Protocols/TransitionStage2.md` — Step 1 records the subject's scope and intended use.
- `Rules and Regulations/Protocols/FreeBrainstorming.md` — external-projection rules for the upstream brainstorm that selects the subject.
- `Rules and Regulations/Protocols/OrganisationSpaceRules.md` — document status/lifecycle and single-copy rules.
- `src/prompt_templates/templates/research_intake.md` — the mirror form (rule R9).
