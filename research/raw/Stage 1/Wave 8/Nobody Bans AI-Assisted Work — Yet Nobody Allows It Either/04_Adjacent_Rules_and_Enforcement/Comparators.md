# Adjacent Rules and Enforcement — What Explicit AI Rules Look Like Elsewhere

_Date: 2026-10-16. Every claim cites `[S##]`. Claim types: `[documented fact]` / `[reported signal]` / `[inference]`. Supports RQ4; feeds `../05_Clause_Design/`._

## 1. Why comparators matter for this audit

`[inference]` A "nobody bans / nobody allows" finding is only interesting if *someone else has written the rule*. The comparator set shows three distinct drafting traditions already in force — **disclosure**, **responsibility/quality floors**, and **prohibited uses** — applied by regulators and by non-labour marketplaces, while labour marketplaces (except Fiverr) publish none of them.

## 2. The regulator lane

### 2.1 FTC — AI-generated reviews are already regulated `[S24]`

`[documented fact]` The FTC's Trade Regulation Rule on the Use of Consumer Reviews and Testimonials (16 CFR Part 465, published 2024-08-22) states in its preamble: "**AI-generated reviews are covered by the final rule**, which the Commission hopes will deter the use of AI for that illicit purpose," and names "reporting regarding the use of generative artificial intelligence ('AI') tools that make it easier for bad actors to write fake reviews" among its findings `[S24]`.

`[inference]` Relevance to freelance platforms: reviews and ratings are the trust currency of every audited marketplace, and fake-review rules now bind *content provenance* regardless of human or AI authorship — a rule about AI *output* already touches platform ecosystems, while a rule about AI *labour* does not exist.

### 2.2 EU AI Act Article 50 — the transparency template `[S25]`

`[documented fact]` Art. 50(2) requires providers of AI systems generating synthetic content to ensure outputs "are marked in a machine-readable format and detectable as artificially generated or manipulated," with technical solutions that are "effective, interoperable, robust and reliable as far as this is technically feasible"; Art. 50(4) requires **deepfakes** to disclose that content "has been artificially generated or manipulated," with an artistic/creative caveat that narrows the duty to disclosure of existence `[S25]` (reproduction consulted; controlling text Regulation (EU) 2024/1689 on EUR-Lex — re-verify before publication-grade citation).

`[inference]` The EU draughts AI transparency as a **marking/disclosure duty with proportionality**, not a ban — the same shape a platform clause would take (disclose, don't prohibit).

## 3. The marketplace lane (non-labour)

### 3.1 Steam — mandatory disclosure with review `[S21]`

`[documented fact]` Steam's Content Survey, §3 "Generative Artificial Intelligence Content": developers must describe AI use in shipped content, split into "**Pre-Generated**" content (created with AI during development) and "**Live-Generated**" content (created at runtime); live generation additionally requires declaring "what kind of guardrails you're putting on your AI to ensure it's not generating illegal content"; Valve states: "In our prerelease review, we will evaluate the output of AI generated content in your game the same way we evaluate all non-AI content." Efficiency tooling is explicitly *out of scope*: "Efficiency gains through the use of these tools is not the focus of this section" `[S21]`.

`[inference]` Steam's line-drawing is directly portable to freelance work: **regulate the artifact that ships to the buyer, not the toolchain used to make it** — which is also where Fiverr's dispute review lands ("quality of the final delivery" `[S04]`).

### 3.2 Etsy — listing-level disclosure `[S22]`

`[documented fact]` Etsy's official Seller Handbook: "Sellers must disclose within their listing description if an item is created with the use of AI," while allowing AI-assisted creation "based on a seller's original prompt or inputs" — framed as aligning "with our values of supporting artists" `[S22]`.

`[inference]` Etsy proves a **one-field disclosure requirement is operable at marketplace scale** — the simplest mechanism absent from every audited freelance platform except Fiverr's client-communication norm `[S04]`.

### 3.3 Google Play — producer responsibility for outputs `[S23]`

`[documented fact]` Google Play's AI-Generated Content policy: "Developers are responsible for ensuring that their generative AI apps do not generate offensive content, including prohibited content … content that can deceive users or enable dishonest behavior," with declared AI functionality in the Play Console `[S23]`.

`[inference]` Same pattern: allowed + declared + output-responsibility — never a ban on using the technology.

## 4. The platform's-own-AI lane (already inside the audit set)

`[documented fact]` Braintrust's Responsible AI Policy applies governance (human oversight, fairness testing, third-party NYC LL144 bias audit, candidate-notice support, EU AI Act readiness by 2026-08-01) to **its own** recruiting AI `[S18]`; Malt disclaims accuracy of its integrated AI and reserves training rights over user data `[S11]`; PPH deploys ML to rank proposals `[S10]`; Contra's Terms govern Indy AI's data sources, consent, and "as is" disclaimers `[S08]`; Upwork's §2.4 licenses user content to train generative models `[S01]`.

`[inference]` Every platform that is silent on worker AI has been *legally attentive* to its own AI — draft clauses exist in-house; the missing clause is one about the other party's conduct.

## 5. Enforcement levers that already exist (unused for AI-work specifically)

`[documented fact]` Platforms already hold stated sanctions usable against AI misuse *as fraud or quality failure*: Fiverr — order cancellation + full refund + permanent suspension for "misrepresentation of AI usage" `[S04]`; Upwork — misrepresentation provisions + honesty-about-who-does-the-work `[S01]`; Braintrust — removal/permanent ban for conduct violations `[S15, S17]`.

`[documented fact]` **No platform publishes enforcement data** — no counts, case names, or appeal outcomes for AI-related actions were found in any fetched document (2026-10-16).

`[inference]` The enforcement gap compounds the drafting gap: even Fiverr's explicit rules are enforced by opaque post-hoc review, so deterrence rests on unobservable sanctions — a fairness and reproducibility problem worth naming in the article.

## 6. What the comparators imply for clause design (bridge to `../05_Clause_Design/`)

| Element | Precedent | Source |
|---|---|---|
| Disclosure of AI use | Etsy listing disclosure; Steam content survey; EU Art. 50 marking | `[S22, S21, S25]` |
| Artifact-not-toolchain scope | Steam ("efficiency gains … not the focus") | `[S21]` |
| Output responsibility + quality floor | Fiverr; Google Play; FTC (provenance of reviews) | `[S04, S03, S23, S24]` |
| Client/buyer opt-out | Fiverr (honor explicit non-AI requests) | `[S04]` |
| Prohibited uses (harms list) | Fiverr; Google Play; FTC; EU deepfake duty | `[S03, S23, S24, S25]` |
| Rights clearance | Fiverr (all necessary rights); category rules (voice deletion) | `[S03, S05]` |
| Enforcement ladder + stated sanctions | Fiverr (cancel → refund → suspension) | `[S04]` |
| Guardrails for generative runtime | Steam (live-generation guardrail declaration) | `[S21]` |
| Machine-readable marking (aspirational) | EU AI Act Art. 50(2) | `[S25]` |

## 7. Limits

- Comparator set is purposive (illustrative drafting traditions), not exhaustive marketplace coverage `[inference; design choice recorded per Research-Evaluation Gate D]`.
- EU AI Act text consulted via reproduction site; EUR-Lex verification queued `[S25]`.
- Etsy article accessed via Seller Handbook (legal page returned 403) `[S22]`.
- No claim here about legal *applicability* to freelance contracts — comparators are used as drafting precedents, not as governing law `[inference]`.
