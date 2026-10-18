# Findings

_Date-stamped findings by research question. Every finding cites `[S##]` from `./Sources.md`. Claim types follow the Research-Evaluation protocol: `[documented fact]` / `[reported signal]` / `[inference]`. Audit pass of 2026-10-16._

## RQ1 — Ban, allow, or silence (the 12-platform audit)

- `[documented fact]` **No platform in the set bans AI-assisted work.** Full fetched texts of all public governing documents scanned 2026-10-16 contain zero prohibitions on freelancer AI use as such `[S01, S03–S05, S07–S19]`.
- `[documented fact]` **Exactly one platform explicitly allows it, with conditions:** Fiverr's Community Standards: "Fiverr embraces new technology and allows the use of generative artificial intelligence (AI) tools to create content," subject to a quality floor ("not a substitute for the freelancer's own skill, effort and judgment"; no "generic, unmodified, or reused AI-generated output"), rights clearance, a harms list, and sanctions up to permanent suspension; the Help Center adds "Fiverr permits the use of AI across all service categories… AI use is encouraged" `[S03, S04, S05]`.
- `[documented fact]` **Upwork's rule is conditional and client-triggered:** using generative AI "to substantially bolster your job proposals or work product" is misconduct only "if such use is restricted by your client or violates any third-party's rights" `[S01]`.
- `[documented fact]` **Contra regulates AI content, not AI labour:** user responsibility for non-infringement plus an accuracy/human-review disclaimer for AI-generated content; no delivery-work clause `[S08]`.
- `[documented fact]` **Three platforms regulate only their own AI:** PPH's ML proposal-ranking `[S10]`; Malt's training-data clause (§5.4) and AI accuracy disclaimer (§12.8) `[S11]`; Braintrust's Responsible AI Policy scoped to its AIR recruiting product `[S18]` — while its worker-facing documents (Site Terms, Talent Terms, Network Standards, Code of Conduct) contain no AI-work item `[S15–S17]`.
- `[documented fact]` **Six platforms are silent in public documents:** Toptal (site T&Cs; talent agreement not public) `[S07]`, Freelancer.com (User Agreement, mod. 2025-06-05) `[S09]`, freelancermap (Terms state Dec 2018) `[S12]`, Arc (mod. 2026-08-31) `[S13]`, Codementor (mod. 2026-08-31) `[S14]`, Botpool `[S19]`.
- `[documented fact]` **Counterintuitive niche finding:** Botpool — an AI-only marketplace whose entire catalogue is AI services — has no AI-work clause `[S19, S20]`. AI-native positioning did not produce AI-work governance.
- `[documented fact]` **Upwork runs parallel rules for AI as participant vs. method:** the AI Agent Playground terms give AI agents a first-class pathway to submit unedited deliverables to job posts (feedback = sole payment, v1.2 eff. 2025-07-29) `[S02]`, while the human's AI-assisted proposal remains governed only by the client-restriction trigger `[S01]`.
- `[inference]` The headline decomposes cleanly: **nobody bans; one allows; the rest default to generic-misconduct absorption** (misrepresentation, IP, fake-review clauses reach fraudulent AI use but not ordinary undisclosed AI-assisted delivery) `[S01, S15, S19]`.

## RQ2 — Where the rules live (enforceability/discoverability)

- `[documented fact]` Fiverr's AI rules span **Community Standards** (governing text) and **Help Center guidance** (operational detail: client opt-out timing, dispute factors, sanction ladder); the ToS body was not retrievable (client-rendered; archive captures are shells) and is recorded **Blocked** `[S03, S04, S06]`.
- `[documented fact]` Upwork's only worker-AI text sits inside the binding Terms (§3.2), but as a sub-bullet of the misrepresentation clause — findable only by reading the fraud section `[S01]`.
- `[documented fact]` All other audited platforms put AI content in taxonomy/nav surfaces only `[S30]`.
- `[inference]` The operational rule-set for the one platform that has one is distributed across at least three documents with unverified incorporation `[S03, S04, S06]`, while six platforms offer no answer at any layer — **discoverability, not just existence, is the failure mode**.

## RQ3 — The positioning gap

- `[documented fact]` All 12 platforms market AI work in categories, trending skills, or AI-branded products `[S30]`; 1/12 publishes a worker-AI clause `[S03, S04]`.
- `[documented fact]` Upwork brands itself "the world's human and AI-powered work marketplace" `[S26]`; Braintrust sells "AI Gig Work" `[S15]`; Fiverr's served data includes an "AI Services" tree with "AI Agents", "Generative Engine Optimization" etc. `[S30]`.
- `[reported signal]` Upwork's FFWI 2026 (C: company research, n=2,400 U.S. workers + platform data): AI-work freelancers earn +34%/hr; gen-AI creative contract starts +90% YoY with −13% per-contract earnings; skilled-freelancer share 28%→38% `[S26]`.
- `[documented fact]` Independent peer-reviewed demand evidence (JEBO 2025): substitutable skills −20–50% post-ChatGPT; ML programming +24%; AI-chatbot development ≈×3; novice demand down `[S28]`.
- `[inference]` No platform discloses the AI-assisted share of delivered work — the number most relevant to buyers exists nowhere publicly (absence across audit set, 2026-10-16).

## RQ4 — Outside context: what explicit rules look like elsewhere

- `[documented fact]` **Disclosure tradition is mature outside labour marketplaces:** Steam requires declaring pre-generated and live-generated AI content with guardrails, and reviews AI output "the same way we evaluate all non-AI content" while excluding mere "efficiency gains" `[S21]`; Etsy: "Sellers must disclose within their listing description if an item is created with the use of AI" `[S22]`; Google Play makes developers responsible for generative-app outputs `[S23]`.
- `[documented fact]` **Regulators already cover AI output provenance:** the FTC review rule (16 CFR 465, 2024-08-22) states "AI-generated reviews are covered by the final rule" `[S24]`; EU AI Act Art. 50 requires machine-readable marking of synthetic content and deepfake disclosure `[S25]`.
- `[documented fact]` **Enforcement opacity is universal in the set:** no platform publishes AI-related enforcement statistics, case records, or appeal outcomes (absence observed across all fetched documents, 2026-10-16) — even Fiverr, which states the ladder `[S04]`.
- `[documented fact]` A 2026 preprint documents that freelance knowledge workers lack organizational training infrastructure and self-direct upskilling with gen-AI tools `[S29]` (preprint: not peer-reviewed).
- `[inference]` The comparator pattern — **allow + declare + own the output + harms list** — is exactly the Fiverr cluster `[S03, S04]` and exactly what the six silent platforms lack; the drafting problem is solved elsewhere, unapplied here.

## RQ5 — Clause design (deliverable)

- `[inference]` Nine elements (E1–E9) with precedents for each are specified in `../05_Clause_Design/ClauseDesign.md`, plus a model clause v0 and a per-platform gap map. Core design choices: default-on permission (E1), artifact-not-toolchain scope borrowed from Steam (E2) `[S21]`, preference-triggered bounded disclosure (E3/E4) following Fiverr's opt-out timing `[S04]` and Etsy's operable disclosure field `[S22]`, honesty-about-who-does-the-work extended to agents (E8) anchored in Upwork's honesty clause `[S01]` and AI Agent Playground reality `[S02]`, and a published enforcement ladder + clause version history (E9).
- `[inference]` Placement recommendation: binding layer (Terms or expressly incorporated Community Standards), not help-center articles — direct response to RQ2's discoverability finding `[S04, S06]`.

## Method limits (carry into any article)

- **Snapshot, not a trend:** all documents fetched **2026-10-16** from a EU (GR) IP, English versions; terms change and localized versions differ `[S01–S19]`.
- **Absence claims are search-scoped:** keyword scan (list in `../01_Background/Concepts.md` §5) + manual review over the *named public document*; they do not cover in-app/private agreements (Toptal talent contract `[S07]`), unindexed pages, or platform practice. Per Gate E: absence of evidence is asserted only to the depth of this design.
- **Blocked sources:** Fiverr ToS body `[S06]` (client-rendered; Wayback captures 2023/2024/2026 contain page shell + catalogue JSON only); Etsy legal page (403, official Seller Handbook used) `[S22]`; ScienceDirect full text (403; abstract via OpenAlex) `[S28]`; Semantic Scholar rate-limited; DuckDuckGo rate-limited late in the session (discovery incomplete for: Upwork help-center AI articles — none located beyond ToS).
- **Tooling note (transparency, Gate D):** the session's native web-search tool was unavailable; discovery used the DuckDuckGo HTML endpoint, and all evidence came from direct HTTP fetches or scholarly metadata APIs (Crossref/OpenAlex). A non-LLM script did the HTML→text conversion and keyword scanning; every hit was manually reviewed by the agent.
- **No enforcement data exists publicly** — sanction ladders are stated powers, not observed actions `[S04]`.
- **Company research is C:** Upwork FFWI/Research figures are self-reported `[S26, S27]`; FRE probe counts are internal single-day observations `[S31]`.
- **Regulator citations:** EU AI Act text via reproduction site (EUR-Lex verification queued) `[S25]`; FTC via Federal Register official document `[S24]`.
