# Concepts — What "AI-Assisted Work" Is, and Where Platforms Put the Rules

_Date: 2026-10-16. Every claim cites `[S##]` from `../06_Evidence/Sources.md`. Claim types: `[documented fact]` / `[reported signal]` / `[inference]`._

## 1. The unit of analysis: the worker-facing AI rule

**AI-assisted work** here means: a freelancer uses generative or analytical AI tools (writing assistants, image generators, code assistants, data-analysis tooling, agents) *in performing a contracted deliverable* — not the platform's own use of AI, and not the client's internal use.

Four distinct rule-types must not be merged (they share the word "AI" and answer different questions):

| Rule type | Question it answers | Example in this audit |
|---|---|---|
| **Worker-AI clause** | May the freelancer use AI to do the work? | Fiverr's Community Standards "AI-generated content" `[S03]`; Upwork ToS §3.2 `[S01]` |
| **Platform-own-AI clause** | How may the platform use AI/data? | Upwork §2.4 training licence `[S01]`; Malt §§5.4/12.8 `[S11]`; Braintrust AIR policy `[S18]` |
| **Taxonomy/marketing** | Is AI work being *sold*? | Fiverr AI category tree; Upwork "AI & Automation" nav `[S30]` |
| **External-content rule** | What about AI content *in the product*? | Steam content survey `[S21]`; Etsy listing disclosure `[S22]` |

`[inference]` The FRE scans' original observation — "no freelancer AI-work policy found on any scanned platform" `[S31]` — was ambiguous across these four types. The audit resolves it: the question is about row 1, and row 1 is where the gap is.

## 2. Where platform rules actually live — a four-layer stack

`[documented fact]` The audit finds platform governance distributed across four layers, not one:

1. **Binding Terms / user agreement** — the enforceable contract (Upwork `[S01]`, Freelancer.com `[S09]`, Toptal `[S07]`, Contra `[S08]`, Braintrust `[S15, S16]`, …).
2. **Community standards / conduct codes** — supplementary behavioural rules, often referenced by the Terms (Fiverr's Community Standards, which *hosts* its AI clause `[S03]`; Braintrust's Code of Conduct/Network Standards `[S17]`).
3. **Help-center policy articles** — guidance pages with the operational detail (Fiverr's "Using AI on Fiverr" `[S04]` and category "AI services guidelines" `[S05]`).
4. **Category/UX surfaces** — taxonomy and prompts where rules meet practice (AI category trees `[S30]`).

`[documented fact]` Fiverr's AI rules span layers 2–3 but **not** the ToS body retrieved in this audit (Blocked, `[S06]`); Fiverr's help article points readers to "Fiverr's Community Standards on AI-generated Content" as the governing text `[S04]`.

`[inference]` Layer determines enforceability and discoverability: a freelancer auditing risk must read at least three documents to learn what Fiverr allows, while a Toptal or Freelancer.com user gets no answer from any layer. **RQ2's answer is built into the audit design.**

## 3. The five stances (coding scheme)

`[inference]` Classifying what each platform's documents *do* about worker AI use yields five stances; the audit (`02_Platform_Policy_Audit/`) codes each platform into exactly one:

1. **Ban** — AI-assisted delivery prohibited as such. *No platform in the set is coded here.*
2. **Explicit allow + conditions** — AI use permitted, with quality/conduct conditions and sometimes an enforcement ladder. (Fiverr `[S03, S04]`.)
3. **Conditional / indirect** — AI use only addressed through a general clause whose trigger is someone else's restriction or a harm (Upwork: prohibited *if the client restricted it* or third-party rights violated `[S01]`; Contra: AI-content responsibility and accuracy disclaimer `[S08]`).
4. **Platform-own-AI only** — the documents regulate the platform's AI, silence on the worker's AI (Malt `[S11]`, Braintrust `[S18]`, PPH's ML proposal categorisation `[S10]`).
5. **Silent** — no AI-work provision found in any public governing document (Toptal `[S07]`, Freelancer.com `[S09]`, freelancermap `[S12]`, Arc `[S13]`, Codementor `[S14]`, Botpool `[S19]`; Braintrust's talent-facing docs `[S16, S17]`).

`[inference]` The title claim decomposes precisely: **nobody bans** (stance 1 is empty) and **explicit allowance is nearly absent** (stance 2 has one member; everything else lives in 3–5).

## 4. Why the question matters (stakes)

- `[documented fact]` AI work is already a large, platform-marketed share of the marketplace: Fiverr serves a top-level "AI Services" category tree with subcategories including AI Agents, AI Content, Data Model Training and Generative Engine Optimization; Upwork's nav leads with "AI & Automation"; Malt's homepage trends "n8n, AI, AI Agent, Zapier, RAG"; Braintrust sells an "AI Gig Work" product `[S30]`.
- `[reported signal]` Upwork's own research reports freelancers doing AI work on its marketplace earn 34% more per hour than those not incorporating AI, while gen-AI creative-production contract starts grew 90% year-over-year with per-contract earnings down 13% `[S26]` (company-run research: platform data + survey of 2,400 U.S. workers, Mar–Apr 2026).
- `[documented fact]` Independent peer-reviewed evidence shows post-ChatGPT demand on "a leading online freelancing platform" fell 20–50% for substitutable skills (writing/translation) while ML programming rose 24% and AI-chatbot development nearly tripled `[S28]` — AI-assisted work is not a niche, it is a restructuring of the demand mix.
- `[documented fact]` Where workers and platforms *did* negotiate explicit AI terms elsewhere, the terms turn on disclosure, consent, and quality floors — the exact elements absent from the silent platforms `[S21–S25]`.
- `[inference]` In the absence of a worker-AI clause, the operative rule becomes **generic misconduct law**: whatever the platform already bans (misrepresentation, IP infringement, fake reviews) absorbs AI disputes case-by-case, with the burden on the complaining party to prove a non-AI-shaped harm. That default favors platforms (discretion) and leaves both sides guessing ex ante — the gap this research designs against (`05_Clause_Design/`).

## 5. Audit method (reproducibility)

- Fetch date for all documents: **2026-10-16**; HTTP GET with browser headers; HTML→text; fixed keyword list: `artificial intelligence`, `generative ai`, `ai-generated`, `ai generated`, `ai tools`, `ai-assisted`, `ai content`, `ai-powered`, `LLM`, `machine learning`, `chatbot`, `\bAI\b`, plus `künstliche intelligenz`/`KI` for the German platform.
- Every hit was reviewed in context and classified into the four rule-types of §1; navigation/taxonomy hits are discarded as noise but *recorded* for RQ3 (`03_Demand_and_Positioning/`).
- **Absence claims carry the search design** (per `Research-Evaluation.md` Gate E: absence of evidence ≠ evidence of absence unless the design supports it): full fetched text of a *named, dated document* + the keyword list + manual review. Absence is scoped to that document and date, never to the platform's private practices or in-app agreements.
- Known blocks: Fiverr ToS body (client-rendered; archives hold only shells) `[S06]`; Toptal talent agreement (in-app); no login walls crossed.
