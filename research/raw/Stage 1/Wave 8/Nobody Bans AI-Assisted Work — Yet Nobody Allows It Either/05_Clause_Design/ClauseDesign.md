# Clause Design — What a Well-Written Freelancer-Facing AI-Work Clause Contains

_Date: 2026-10-16. **Deliverable** of RQ5. Synthesis/proposal — everything here is `[inference]` / `[recommendation]` unless a `[S##]` precede is cited. Not legal advice; a design for platform counsel and a checklist for readers comparing platform terms._

## 1. Design inputs

The clause set below is derived from precedents that already exist in the wild — Fiverr's Community Standards and guidance (the fullest labour-market precedent) `[S03, S04, S05]`, Upwork's conditional clause `[S01]`, Steam/Etsy/Google Play disclosure models `[S21, S22, S23]`, FTC provenance rules `[S24]`, and EU AI Act Art. 50 proportionality `[S25]` — plus the six silence-pattern platforms it must replace `[S07, S09, S12, S13, S14, S19]`. The target document is the **binding layer** (Terms or incorporated Community Standards), because `02_Platform_Policy_Audit/` shows today's operational detail sits in help-center articles `[S04]` whose incorporation status was not verified `[S06]`.

## 2. The nine elements

| # | Element | What it must say | Why (precedent / audit gap) |
|---|---------|------------------|-----------------------------|
| E1 | **Permission (default-on)** | AI tools may be used to perform work, in all categories, as an ordinary professional tool | The default today is silence: 6/12 silent, 0/12 ban `[S07, S09, S12–S14, S19]`; Fiverr alone states permission `[S03, S04]` |
| E2 | **Artifact-scope rule** | Regulation attaches to the delivered artifact and its quality, not to the toolchain; efficiency use is out of scope | Steam's explicit carve-out ("efficiency gains … not the focus") `[S21]`; keeps the clause enforceable and audit-proof `[inference]` |
| E3 | **Disclosure duty (bounded)** | Freelancer discloses AI use on request or per client's stated preference at order start — not a blanket per-delivery tick-box | Etsy's one-field disclosure is operable `[S22]`; Upwork's default (nothing unless client restricted) leaves buyers of short-cycle work unprotected `[S01, S28]`; unbounded disclosure imposes costs Fiverr itself declines ("do not necessarily disclose all the tools") `[S04]` |
| E4 | **Client opt-out, time-boxed** | A client may require non-AI work if stated before or at the start of the order; retroactive objections don't create a breach | Fiverr's rule verbatim ("honor a client's explicit request for non-AI work… before or at the start of an order") `[S04]` |
| E5 | **Quality floor + accountability** | Delivery must be meaningfully refined, original to the order, client-tailored; freelancer owns errors "regardless of the use of AI tools"; no generic/unmodified/reused output | Fiverr `[S03, S04]`; Google Play output-responsibility `[S23]` |
| E6 | **Rights clearance** | Freelancer warrants necessary copyright/trademark/licences for AI-assisted inputs and outputs; special handling for voice/likeness with post-delivery deletion | Fiverr community standards + voice guidelines `[S03, S05]` |
| E7 | **Harms list (closed)** | Prohibited: non-consensual content, deepfakes, impersonation/fake accounts, misinformation, illegal content, fake reviews/credentials | Fiverr `[S03, S04]`; FTC covers AI reviews `[S24]`; EU deepfake duty `[S25]`; Google Play deception rules `[S23]` |
| E8 | **Honesty about who does the work** | Misrepresenting the identity/process of performance (including undeclared delegation to agents or third parties) is misconduct | Upwork's honesty clause already reaches this for humans `[S01]`; Upwork's AI Agent Playground shows agents-as-participants are coming `[S02]` `[inference]` |
| E9 | **Enforcement ladder + change log** | Stated progression (warning → order cancellation/refund → suspension) with published aggregate enforcement counts and a dated version history of the clause | Fiverr states the ladder but no platform publishes enforcement data (absence observed 2026-10-16) `[S04]`; version-staleness is visible in freelancermap's Dec-2018 terms `[S12]` `[inference]` |

## 3. Model clause (draft, v0)

> **AI-Assisted Work.**
> **(a) Permission.** You may use artificial-intelligence tools to perform Services. Such use is permitted in all categories unless the Client has stated otherwise as provided in paragraph (b), and is out of scope for this Article where it concerns your internal tooling and does not affect the Deliverable.
> **(b) Client preference.** A Client may require AI-free work by stating so before or at the start of the Order. Absent such statement, the Parties proceed under paragraph (a).
> **(c) Disclosure.** On the Client's request, or where the Client's stated preference applies, you will disclose in reasonable detail which AI tools were material to the Deliverable.
> **(d) Standard of delivery.** You remain fully responsible for every Deliverable, including any error or inaccuracy, regardless of AI use. Deliverables must be substantially tailored to the Order; delivery of generic, unmodified or reused AI output is a material breach.
> **(e) Rights.** You warrant that you hold all rights necessary to deliver the Work, including rights to AI-assisted inputs and outputs, and that use of any person's voice, likeness or data is authorised; on completion you will delete client-provided source material used to create derived models.
> **(f) Prohibited uses.** AI tools may not be used to create non-consensual or intimate content, deepfakes, impersonation of any person or account, misinformation, illegal content, or fake reviews/credentials.
> **(g) Undeclared performance.** Misrepresenting who performs the work — including submitting work as your own when performance was materially delegated to another person or autonomous agent contrary to the Client's expectation — is misconduct.
> **(h) Enforcement and transparency.** Breach handling follows the published enforcement ladder; aggregate enforcement statistics and the version history of this Article are published on the legal page.

`[recommendation]` Placement: as a **numbered article of the Terms** (or expressly incorporated Community Standards with an incorporation clause), not a help-center article — the audit's central structural finding is that operational AI rules currently live where enforceability is unverified `[S04, S06]`.

## 4. Gap map: element → platform (as audited 2026-10-16)

| Platform | E1 | E3–E4 | E5 | E6 | E7 | E9 | Note |
|---|---|---|---|---|---|---|---|
| Fiverr | ✅ `[S03, S04]` | ⚠️ E4 ✅ / E3 informal `[S04]` | ✅ `[S03]` | ✅ `[S03, S05]` | ✅ `[S03]` | ⚠️ ladder ✅ / counts ❌ `[S04]` | closest; ToS-incorporation unverified `[S06]` |
| Upwork | ⚠️ client-conditional `[S01]` | ❌ | ⚠️ honesty-absorption `[S01]` | ❌ | ⚠️ third-party-rights only `[S01]` | ❌ | AI-agent pathway exists, AI-method rule doesn't `[S02]` |
| Contra | ⚠️ content-only `[S08]` | ❌ | ⚠️ "human review as appropriate" `[S08]` | ⚠️ IP only `[S08]` | ❌ | ❌ | feature-disclaimer, not labour rule |
| PPH / Malt / Braintrust | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | platform-own-AI clauses only `[S10, S11, S18]` |
| Toptal / Freelancer.com / Freelancermap / Arc / Codementor / Botpool | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | silent in public documents `[S07, S09, S12–S14, S19]` |

✅ published · ⚠️ partial/indirect · ❌ absent

## 5. Trade-offs and objections (recorded per Research-Evaluation Gate E)

- **Disclosure cost vs. buyer protection.** Unbounded disclosure would chill tool use and is arguably unenforceable (Fiverr declines it in practice `[S04]`); E3 therefore keeps disclosure *preference-triggered*. Counter-position: buyers of substitutable short-cycle work `[S28]` arguably deserve default-on disclosure — flagged as an open design fork, not resolved.
- **Over-disclosure as competitive disclosure.** Platforms may resist E3 because revealing AI share could deter buyers — `[inference]` a market-design conflict of interest, since the platform profits from both AI-category supply `[S30]` and buyer trust.
- **Agent era.** E8 is drafted for delegation, not just tooling, because the platform set already contains a contract for autonomous-agent deliverables `[S02]`; as agent-submitted work grows, "who does the work" becomes the central clause.
- **Not legal advice;** jurisdictional enforceability (e.g. EU consumer transparency norms) untested here. EU Art. 50 duties fall on AI *providers/deployers*, not marketplaces `[S25]` — cited as drafting precedent only.

## 6. Falsifier

The design would need revision if: (a) a platform in the audit set publishes a worker-AI clause after 2026-10-16 (re-check triggers in `../00_Index/Index.md`); (b) Fiverr's ToS body, once retrievable, contains a *different* governing AI article than the Community Standards `[S06]`; (c) enforcement statistics, once published anywhere, contradict the ladder-as-stated; or (d) a jurisdiction imposes a blanket AI-use disclosure duty on labour platforms, which would make E3's opt-in trigger unlawful-in-reverse.
