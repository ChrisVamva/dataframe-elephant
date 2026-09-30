---
name: evidence-first-article-writing
description: "Drafts compelling evidence-first articles from the smarthome corpus. Use when writing, revising, or reviewing any article derived from notebooks/2 (or notebooks/1) and data/smarthome.duckdb: applies the 7-step process (story sentence, lede, nut graf, sectioned body, inline uncertainty, kicker, gate review) and the 10-point pre-publication checklist from Rules and Regulations/Protocols/Article_Techniques.md, under the evidence discipline of ArticleCreation.md."
version: 1.0.0
---

# Evidence-First Article Writing

Companion skill to `Rules and Regulations/Protocols/Article_Techniques.md` (craft: how the prose carries evidence) under `Rules and Regulations/Protocols/ArticleCreation.md` (authority: what the evidence allows). Read both files in full before drafting — the protocol excerpts below are an aide-memoire, not a substitute.

## When to use this skill

- Drafting a new article from a `notebooks/1` or `notebooks/2` claim cluster (see `Artifacts/Article Ideas/2/ArticleIdeas2.md` for commissioned ideas, `Ratings/Best5.md` for priority order).
- Revising a draft in `Artifacts/Article Ideas/2/First Draft/`.
- Reviewing someone else's draft against the gates.

## The 7-step process (from Article_Techniques.md §2)

1. **Story sentence.** Write "This is a story about …" until it names an action with movement and can carry a claim id. No id → no mandate → back to ArticleCreation Step 1.
2. **Lede (1–4 paragraphs, nut graf within ~150 words).** Pick one type: anecdotal/scene, startling figure (value + unit + scope), descriptive (the visual as hook), stakes-first. Never: direct address, epigraph/quote, unanswerable question. Never invent a scene no claim supports.
3. **Nut graf = transition + summary lede.** Must state the claim cluster in plain words, the scale (cluster vs corpus size), and the reader's promised decision. Test: delete the lede — the nut graf alone still states the story.
4. **Body as sections, not a funnel.** One section per failure class / claim group / figure; each opens with a mini-nut. Alternate scene → data → implication; never three data blocks without a human consequence. Evidence inline (claim ids in the sentence; metric value + unit + scope + class/confidence; linkage rule per join).
5. **Uncertainty in the sentence, not the appendix.** "Not recorded" for absences (never zero/never/does-not-exist unless a claim states it). Reported signal vs documented fact verbatim. Conflicts side by side with the reason. Falsifier status at first mention; `L030`-flagged claims named.
6. **Kicker, not summary.** Return to the opening image with changed understanding, deliver the corpus recommendation, or state the reader's decision. Pre-write the last line before drafting the body. No new claims in the final paragraph.
7. **Gate review.** ArticleCreation §7 (AC:Scope … AC:Maintenance) + the 10-point checklist (Techniques §4). A non-drafter reviewer answers the five §7 questions; any "I can't tell" returns the draft.

## Structural shapes (pick one per article)

- **Three-act / hourglass** (default for consumer pieces) · **Martini glass** (actionable finding first) · **Number-led** (one verified figure as spine; retire when a second competes) · **Audit / trust piece** (gap counts as plot).

## Mandatory verification (every draft)

- Every `C###`/`M###` id exists in `data/smarthome.duckdb` (read-only): re-check with `viz.fetch_claims` / `viz.metrics_by_id` before delivery; any id that stops verifying returns the idea to draft.
- Freshness: `scripts/build_visualization_notebooks.py --check` and `src/tests/test_viz_notebooks.py` gate pass.
- Output follows the Required Document Outline (ArticleCreation §9): Document Control → Claim Summary → Provenance Panel → Evidence and Metrics → Visualization/Reference → Uncertainty/Gaps/Limitations → Interpretation/Synthesis (labelled) → Sources and Reproducibility.
