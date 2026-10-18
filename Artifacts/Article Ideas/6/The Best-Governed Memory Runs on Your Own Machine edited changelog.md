# Article Edit — Changelog

**Status:** Edited draft (one pass completed; not publication-approved, not externally reviewed)
**Date:** 2026-10-13
**Recipe:** Rs11 (`status: draft`; executed per direct operator instruction)
**Editor skill:** `/skill:orange-tomato-article-editor`
**Craft reference:** `Rules and Regulations/Protocols/Article creation expertise/EditingProcess.md` (three-stage revision framework applied)

---

## Source / Output

| File | Role | Path | Word count (original) | Word count (edited) |
|---|---|---|---|---|
| Source article | Draft (Rs10 output; not edited) | `Artifacts/Article Ideas/6/The Best-Governed Memory Runs on Your Own Machine.md` | 2,727 | — |
| Edited copy | Edited version (this changelog's companion) | `Artifacts/Article Ideas/6/The Best-Governed Memory Runs on Your Own Machine Edited.md` | — | 2,741 |
| This changelog | Sidecar record | `Artifacts/Article Ideas/6/The Best-Governed Memory Runs on Your Own Machine edited changelog.md` | — | — |

**Pitch / idea mapped:** 4.1 "The Best-Governed Memory Runs on Your Own Machine" (`CAMidea.md`), rated #2 of 19 in `CAMidearatings.md` (2026-10-13). Note: Rs10 default slot is pitch 1.3; this edit follows pitch 4.1 per the operator's direct instruction, not the recipe default. The original source file (`CAMidea.md`) remains unchanged; no ratings or source files were edited.

**New text percentage:** ~0.5% of edited body (14 additional words; one tightened transition sentence in section 4; the grammar correction `a 81.3%` → `an 81.3%` is a correction, not an addition). All `[NEW]` bridging/gloss additions kept well under the ~5% ceiling.

---

## Stage 1 — Big Picture Read (Structure & Purpose)

**Read-through without edits completed.** No structural problems found.

- **Purpose:** The edited copy preserves the commissioned pitch (4.1) — the governance inversion (local-first agents are the best-governed). The thesis, the cloud/local-first contrast, and the practical checklist at the end remain intact.
- **Structure:** Hourglass shape confirmed intact: scene (the `MEMORY.md` file) → data (Hermes + OpenClaw details) → implication (what it means) → counterpoint (security) → practical (checklist) → kicker (return to the file image). No sections missing, no redundant sections, no sections out of sequence.
- **Lead / nut graf:** Lede is descriptive (not invented anecdote); nut graf lands within the acceptable range (~160 words including the dek standfirst, which is acceptable given the dek's role as a transition). The nut graf states the claim cluster (memory governance), the scale (local vs cloud tiers), and the reader's promised decision (the three questions to ask any agent).
- **Kicker:** Returns to the opening file image ("The file is still on your disk...") and delivers a decision framework — no summary, no new claims, no bare quote. Complies with `Article_Structure.md` kicker rules.
- **Body sections:** Each of six body sections has a mini-nut opener; transitions are explicit (contrast bridge "The cloud default is the opposite"; progression bridge "The enterprise tier already has the primitives"; counterpoint bridge "None of this makes self-hosting..."; practical bridge "How to read any agent's memory from now on"). No abrupt shifts found.

**High-level revision priorities identified (Stage 1 list):**
1. Tighten one transition sentence in section 4 for stronger rhythm (applied in Stage 2).
2. Confirm the box callout's claim is the sharpest one-line summary from the vendors' own documentation (verified — unchanged).
3. Confirm the gaps section frames every open item as practical guidance rather than academic hedging (verified — unchanged).
4. Confirm the appendix's source-map table is complete and that every claim in the body resolves to it (verified — unchanged; no claim was silently dropped or altered).

No major structural revisions required. The draft's architecture already satisfies the `Article_Structure.md` checklist (§4 pre-publication check) and `ThisIsForPeopleToRead.md` requirements.

---

## Stage 2 — Reverse-Outline, Flow, Transitions, Paragraph Organization

**Reverse outline (paragraph-level summaries):**
1. Dek: the inversion stated concisely.
2. P1: the concrete file scene (`MEMORY.md`).
3. P2: Hermes' control mechanism.
4. P3: the inversion observation (local-first vs big-user-base).
5. Nut: the survey's question and thesis.
6. Section 1 mini-nut: "What the local agents actually keep."
7. P4–P8: Hermes specifics (files, approval, tags, write refusal, no hidden DB).
8. P9–P12: OpenClaw specifics (files, workflow, incognito, opt-in, SQLite, flush).
9. P13: direction of both agents (memory belongs to machine owner).
10. Section 2 mini-nut: "The cloud default is the opposite."
11. P14–P16: Copilot details (hidden folder, audit gap, Purview gap, admin gap, default-on).
12. P17–P19: ChatGPT, Claude, Gemini details (soft delete, no delete, turn-on required).
13. P20: the non-sinister framing.
14. Box: the two-sentence contrast (Copilot / Hermes).
15. Section 3 mini-nut: "The enterprise tier already has the primitives."
16. P21: enterprise primitives (Azure, Vertex, Bedrock).
17. P22: the ranking inference (local > enterprise > consumer).
18. Section 4 mini-nut: "The catch: your machine is also your attack surface."
19. P23: the tightened transition sentence (consolidated from previous "magic answer" phrasing).
20. P24: poisoning survey (AgentPoison, MINJA, MemoryGraft, MemCollusion — all paper-reported, flagged).
21. P25: MemCollusion numbers on OpenClaw (81.3% / 75.0%, paper-reported, unreplicated).
22. P26: OpenClaw security paper framing; Hermes "not a hard boundary."
23. P27: the two-honest-caveats structure (lab-only evidence; approval defaults off as default, not dead end).
24. Section 5 mini-nut: "What we don't know."
25. P28–P32: the five bullet caveats (C-only evidence; no independent benchmark for Hermes; 2026 preprints unreplicated; no real-world incident rate; unresolved GDPR-derived-erasure mechanism).
26. Section 6 mini-nut: "How to read any agent's memory from now on."
27. P33: practical checklist (three questions: where it lives, who can change it, what "forget" means) — concrete, actionable.
28. P34: self-hosted checklist (open file, turn on approval, use incognito).
29. P35: cloud checklist (assume memory on, soft delete, no audit log; move important conversations).
30. Kicker (P36): return to file image + decision framework ("If it can't [show you], you now know where to look for one that can").

**Changes made (Stage 2):**
- Section 4 transition consolidated from two adjacent transition sentences ("None of this makes self-hosting a magic answer, and the same corpus that supports the inversion immediately complicates it") to a sharper two-part sentence ("Self-hosting is not safe by default. The same agents with the best controls are also named targets of the newest poisoning research, and the same survey that supports the inversion documents the threat." — [NEW]).
- No paragraph reorder; no section reorder; no content moved between sections. The consolidation improves rhythm without changing meaning.

---

## Stage 3 — Clarity, Voice, Accessibility, Mechanics, Consistency

**Voice:** Contracts, active voice, concrete specifics, direct address ("you", "your") used consistently; no jargon without in-context explanation (e.g., "border router" not used — not needed for this pitch; "approval queue", "incognito thread", "consolidation", "derived memory" explained naturally). The tone is direct but not harsh; the "What we don't know" section presents limits as practical guidance, not as hedging piles.

**Mechanics:**
- No claim IDs (`C###`/`S##`/`M###`) in the reader-facing body — verified (programmatically confirmed: zero matches for `S\d{2}` or `[CM]\d{3}`).
- No database/notebook/local-file paths in body — verified (programmatically confirmed: zero `research/` or `.duckdb` matches in body).
- No invented scenes, quotes, personal anecdotes, or fabricated product behaviour — the opening describes a concrete file object documented in `S88`/`S82` (descriptive lede, permitted by `Article_Circumstance.md`); no "at 2 AM in a dark hallway" fiction.
- Source attributions preserved: vendor documentation claims are presented as vendor claims (e.g., "According to Microsoft's own documentation...", "Hermes' documentation describes...", "Hermes' own security pages are candid..."). The tier-ranking sentence is explicitly labeled "our reading of the documentation" rather than presented as vendor fact.
- Evidence-class labels preserved implicitly: the body never upgrades a vendor claim to verified truth; the "What we don't know" section explicitly flags C-only backing; security numbers are described as "lab results from very recent papers", "not measurements of attacks happening in the wild", "too new to call replicated"; GDPR mechanism flagged as "unresolved".
- The [NEW] transition sentence in section 4 does not change any claim; it only consolidates two adjacent transition sentences into one sharper pair for readability (under ~5% of total body, as required).

**Read-aloud check (simulated):** The lead reads smoothly; the box breaks the flow at the right moment (after Copilot/ChatGPT/Claude paragraph, before the enterprise section); the checklist at the end is scannable; transitions between sections are explicit and varied (contrast bridge, progression bridge, counterpoint bridge, practical bridge); no sentence is self-referential; no paragraph exceeds ~5 sentences; the kicker echoes the opening without restating it.

**Line-level fixes applied (Stage 3):**
- Section 4 opening: tightened transition (see Stage 2) — [NEW].
- No additional [NEW] text; no claim changes; no new factual claims added; no claims removed, upgraded, or downgraded; the internal source map (appendix) was preserved intact in the edited file.
- The grammar correction (`a 81.3%` → `an 81.3%`) from the original file was preserved in the edited copy (verified: `an 81.3%` present, no `a 81.3%` in edited file).

---

## Unresolved Concerns — Not Silently Corrected

These concerns existed in the original and were preserved unchanged in the edited copy; they are documented here rather than hidden.

1. **Product-documentation bias (C-class only):** Every product capability claim (Hermes' approval flow, OpenClaw's incognito, Copilot's mailbox storage, Azure/Vertex controls) is drawn from the vendors' own documentation. No independent product test confirmed any of these behaviours as of the snapshot date. The edited copy keeps the attribution intact and does not upgrade any C claim to verified truth.
2. **No independent benchmark for Hermes memory:** The survey notes Hermes' only public memory evaluation is its own Hermes Bench "Memory" category (`S86`). The edited copy preserves this caveat in "What we don't know"; it is not resolved.
3. **Security figures unreplicated:** MemCollusion (`S69`), AgentPoison (`S66`), MINJA (`S65`), MemoryGraft (`S67`), OpenClaw security paper (`S94`) — all 2026-dated preprints; no independent replication verified. The body keeps the "lab results" framing; the edited copy preserves it unchanged.
4. **No real-world incident rate:** The survey found no disclosed real-world memory poisoning or cross-tenant leakage incident. The edited copy preserves this absence rather than implying wide-spread live attack.
5. **Self-hosting is not automatically safer:** The inversion is the survey's sharpest finding, but the security evidence itself limits the claim — Hermes' guards are "not a hard boundary" (`S84`), OpenClaw is a named target (`S69`), and the approval mechanism defaults off (`S82`). The edited copy preserves these three limits exactly.
6. **GDPR Art. 17 erasure mechanism unresolved:** The "What we don't know" section states clearly that no mechanism reaching derived memory (summaries, embeddings, graph edges) has been demonstrated; the edited copy does not resolve it.
7. **No external review performed:** This is a single editorial pass (Stage 1 → 3), not a peer review. The changelog does not claim external review.
8. **Recipe slot deviation preserved in record only:** The Rs10 default pitch is 1.3; this edit serves pitch 4.1. The edited file's appendix notes the deviation; the user explicitly commissioned pitch 4.1 and directed the edit directly.

---

## Evidence Integrity Check

- **No substantive claim altered:** The edited file contains no sentence that changes a fact, upgrades an evidence class, removes an attribution, removes a caveat, or introduces a new claim absent from the source map.
- **No claim silently dropped:** All 16 source-map entries from the original's appendix are preserved in the edited file's appendix; all claims referenced in the body resolve to the same source-map entries.
- **No [NEW] claim added:** The only [NEW] text (section 4 opening) is a transition consolidation, not a claim addition; it is listed explicitly above and accounts for <5% of body.
- **Evidence class preserved:** Every material claim remains labelled implicitly through its prose framing (vendor documentation claims presented as vendor documentation; lab preprints described as lab results; inference labelled as inference — see "our reading of the documentation" for the tier ranking; "lab results" / "not independently tested" for security claims).
- **Uncertainty preserved:** All open questions (GDPR derived erasure, independent benchmarks, real-world incident rate, C-class verification) are carried into the edited file unchanged.
- **Source links intact:** Every readable inline link and every appendix source-map entry preserved; no links broken by editing.

---

## External-Review Status

**Not claimed.** This changelog records one editorial pass by the drafting specialist (`orange-tomato-article-editor`), not a peer review, not an independent fact-check, and not publication approval. Per the `EditingProcess.md` protocol (§6 collaboration workflow), an external (non-specialist) reader review and a final polish would follow this pass if commissioned; neither occurred here. The user may request an additional pass or an external review at any time; this changelog is written to support that handoff without ambiguity.

---

## Final Verification

- Original source file (`The Best-Governed Memory Runs on Your Own Machine.md`) remains unchanged (checked: timestamp 2026-10-13 19:01, size 17,015 bytes — unchanged before/after this edit pass).
- Edited file (`The Best-Governed Memory Runs on Your Own Machine Edited.md`) created at new path; valid Markdown; no syntax errors; all headings intact; appendix present and clearly labeled.
- No site route created; nothing written to `C:/Users/user/orange_-tomato/`; the site intake remains a separate gated step per the `cam-article-workflow` rules.
- No claim IDs (`C###`/`S##`/`M###`) in the edited file's reader-facing body; no database paths in body; internal IDs only in the clearly labeled appendix.
- All claims resolved to the source-map table; no claim added, removed, or upgraded.
