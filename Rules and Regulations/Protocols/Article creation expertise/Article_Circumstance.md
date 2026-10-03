# Article Circumstance Protocol

## Status
Advisory companion to `ArticleCreation.md` (mandatory) and `Article_Techniques.md` (craft). Read-only against `notebooks/`; article outputs are derivative, not controlling.

---

## 1. Purpose
`ArticleCreation.md` governs **what the evidence allows**. `Article_Techniques.md` governs **how the prose carries it**. This protocol governs **who the prose speaks to and how it sounds** — the circumstances of reading: a person with a smart home, a problem, or a purchase decision, not a reviewer auditing a corpus.

Scientific rigour belongs in evidence collection and evaluation. The language must feel like a knowledgeable friend explaining what's happening in your house, not a lab report describing a system under test.

---

## 2. The Reader's Circumstance

| Dimension | Reality |
|---|---|
| **Who** | A homeowner, renter, or buyer. Maybe technical, maybe not. They have — or want — smart lights, locks, thermostats, sensors. |
| **Why they're reading** | Something broke. Or they're about to spend money and want to avoid regret. Or they heard "Matter fixes everything" and want to know if that's true. |
| **What they know** | They know their devices by brand and function ("my Eve sensor," "my Yale lock"), not by protocol spec. They know "it works" or "it doesn't." |
| **What they need** | A clear picture of what can go wrong, what the evidence actually says, and what to do about it — without having to decode jargon. |
| **Emotional state** | Curious, maybe frustrated, maybe wary. Not looking for academic hedging. Looking for trustworthy guidance. |
## 3. Voice & Tone Rules

### Do
- **Write to one person.** Use "you," "your," "we." Contractions are mandatory (it's, you'll, don't, won't, that's).
- **Lead with a scene.** A hallway going dark. A lock that won't open. A sensor that vanishes at 2 AM. The reader lives there.
- **Explain the term the first time you use it.** "Thread border router (the little box that connects your Thread devices to your home network)" — then just "border router" after.
- **Frame every technical claim in human stakes.** Not "control latency increases" — "your switch stops talking to your bulb." Not "cloud dependency" — "the company can turn off your features."
- **Use concrete specifics.** Brand names, model names, prices, timeframes ("about a minute," "five years of updates," "$40 for an Echo Pop").
- **Present caveats as practical guidance.** "The evidence is one test on one switch-light pair" beats "M006 is medium confidence, reported signal."
- **Show the uncertainty, don't just flag it.** "We only have one measurement, and it's from a lab-style test" is honest and readable.
- **End with a decision.** What should the reader do? What should they ask before buying? What drill should they run?

### Don't
- No "the corpus records," "the cluster indicates," "the provenance panel shows." The corpus is your source, not your subject.
- No "Death 1," "Death 2," "Death 3" as section headers. Use words a person would say: "When the border router dies," "When the internet goes out," "When the vendor pulls the plug."
- No passive voice where active works. "The SRP Server becomes unavailable" → "the SRP Server (the traffic cop for your Thread devices) goes offline."
- No academic hedging piles. One clear caveat per claim, in the sentence, then move on.
- No "interpretation / synthesis" labels. The whole article is synthesis grounded in evidence. Just make the boundary clear: "Here's what the evidence says. Here's what I'd do with it."
- No claim IDs in the main prose. They belong in the provenance panel and hover text, not in the reader's sentence flow.
## 4. Structure for Human Reading

1. **The Hook (1–3 paragraphs).** A scene. A problem. A question. The reader sees themselves.
2. **The Nut Graf (1 paragraph).** "Here's what's really going on, why it matters to you, and what this article will help you decide."
3. **The Body — three sections, each:**
   - A concrete scenario (what it looks like in your house)
   - What the evidence says (plain language, inline caveats)
   - A simple table or bullet list (what works, what fails, what's unknown)
   - The practical takeaway for this failure mode
4. **The "One Number" Box.** The key measurement (`M006`), what it means, what it doesn't mean — in a callout, not a table.
5. **The Gaps (honest, practical).** What we don't know, why it matters to you, what to watch for.
6. **The Checklist / Closing Ask.** Three disaster drills. The certification checklist to demand. A final line that echoes the opening.

---

## 5. Evidence Discipline in Prose (the invisible scaffold)

| Evidence Rule | Prose Translation |
|---|---|
| Every claim has an id | Provenance panel (appendix) carries IDs; main text carries the claim's meaning |
| Every metric has unit, scope, class, confidence | First mention: "about one minute (one test, one switch-light pair, medium confidence)" |
| "Not recorded" ≠ zero | "We have no evidence either way" or "The corpus doesn't say" |
| Reported signal ≠ documented fact | "The test lab reported…" or "The manufacturer claims…" or "One test showed…" |
| Inference labelled | "The analysts infer…" or "This is an educated guess, not a measurement" |
| Recommendation labelled | "The researchers recommend…" (not "we should") |
| Falsifier status | "No test has disproven this yet" (for falsifier-absent claims) |
| Linkage rule | Never say "claim X is linked to metric Y" — say "the number comes from the same source section" or "the number is from a different test" |

---

## 6. Pre-Publication Voice Check

Read the draft aloud. If any sentence sounds like a paper abstract, rewrite it. Check each paragraph:

- [ ] Does it use "you" or "we" at least once?
- [ ] Are contractions present?
- [ ] Is there a concrete image or brand or time or price?
- [ ] Is the caveat in the sentence, not the footnote?
- [ ] Does it tell the reader what this means for their house / wallet / safety?
- [ ] Would a smart non-technical friend understand it without re-reading?

If any check fails, the draft isn't ready.

---

## 7. Sources

- Tone models: Consumer Reports Innovation Blog (Higginbotham), Local Smart Home Guide, Courtney Rosenthal personal essay, Android Police buying guides, Wirecutter starter guides.
- Governing: `ArticleCreation.md` §§4–7 (evidence rules), `Article_Techniques.md` §2 (7-step process), `schemas/stage2.sql` (no claim→metric FK).
