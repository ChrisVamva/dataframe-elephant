# Nobody Bans AI-Assisted Work — Yet Nobody Allows It Either

**Wave:** 8 (`research/raw/Stage 1/Wave 8/`)
**Origin:** FRE freelance-platform scans (`Artifacts/Article Ideas/9/FREideas.md`, idea 3.1 "Nobody Bans AI-Assisted Work — Yet Nobody Allows It Either"), selected as the first article idea to pursue (2026-10-15) and promoted to a Stage 1 research subject by the user on 2026-10-15.
**Protocol context:** `Rules and Regulations/Protocols/Research-Evaluation.md` (claim types, gates, confidence); `Article creation expertise/ArticleCreation.md` evidence discipline adapted to an external policy-audit subject (no internal DB dependencies).

## Research Question

When freelancers use AI tools to do their work, what do the platforms they work through actually say about it — do they ban it, allow it, condition it, or say nothing — and what would a well-written platform rule look like given what regulators, other marketplaces, and the platforms themselves already do elsewhere?

## Research Questions (decomposed)

- **RQ1 — Ban, allow, or silence (the audit):** Across the12 platforms in the FRE scan set (Upwork, Fiverr, Toptal, Contra, Freelancer.com, PeoplePerHour, Malt, Freelancermap, Arc.dev, Codementor, Braintrust, Botpool): does any governing document (Terms of Service, user agreement, community standards, help-center policy) regulate the *freelancer's use of AI to perform contracted work*? Where is such a rule located, what does it say verbatim, and where is the absence?
- **RQ2 — Where the rules live:** If platforms do regulate AI-assisted work, is the rule in the binding Terms — or scattered across help-center articles, community standards, and category guidelines? Which document is enforceable, and what does the split mean for a freelancer trying to find out what's allowed?
- **RQ3 — The positioning gap:** How aggressively do the same platforms *market* AI work (AI categories, AI-branded products, "AI-powered" positioning, research reports) relative to how explicitly they regulate it?
- **RQ4 — The outside context:** What do external rulebooks already do that platforms don't — regulators (FTC review rule, EU AI Act Art. 50), other marketplaces (Steam, Etsy, Google Play) — and what does the empirical evidence say about how much AI-assisted freelance work is actually happening?
- **RQ5 — Clause design (the deliverable):** What elements would a well-written, enforceable freelancer-facing AI-work clause contain, given the existing precedents (Fiverr's is currently the fullest), the generic misconduct clauses platforms fall back on, and the disclosure models used elsewhere?

## Method Sketch

- **Primary-document audit.** Every platform's governing documents were fetched directly (HTTP GET, browser headers, 2026-10-16), converted to text, and machine-scanned with a fixed keyword list (`artificial intelligence`, `generative AI`, `AI-generated`, `AI tools`, `AI-assisted`, `AI-powered`, `LLM`, `machine learning`, `chatbot`, `\bAI\b`, plus German `Künstliche Intelligenz`/`KI` for the German platform), followed by manual context review of every hit. Hits were classified as: **worker-AI clause** (regulates the freelancer's AI use), **platform-own-AI clause** (platform's use of AI), **taxonomy/nav** (AI as a category or marketing label), or **noise**.
- **Absence is a claim with a stated search design.** "No AI-work clause found" means: full fetched text of the named document, scanned 2026-10-16 with the keyword list above plus manual review, contains no such provision. Falsifiers are stated in `06_Evidence/Findings.md`.
- **Claim-type tags** follow `Research-Evaluation.md`: `[documented fact]`, `[reported signal]`, `[inference]`.
- **Reliability grading** (adapted from Wave 7 — see `06_Evidence/Sources.md` for the rationale): official terms/policies are **P** for *document-content* claims ("the document says X" is directly checkable); platform marketing and platform-run research are **C**; internal FRE artifacts are **I**.
- Every factual claim in folders 01–05 cites an `S##` entry in `06_Evidence/Sources.md`.

## Folder Skeleton

| Folder | Purpose | Status |
|--------|---------|--------|
| `00_Index/` | Status tracker + Synthesis (RQ answers, falsifiers) | Done |
| `01_Background/` | Concepts: what "AI-assisted work" means, where platform rules live, the five stances, why the question matters | Done |
| `02_Platform_Policy_Audit/` | The core audit: 12 platforms × clause inventory with verbatim quotes | Done |
| `03_Demand_and_Positioning/` | The positioning gap: AI categories, AI-branded products, research reports vs. rule coverage | Done |
| `04_Adjacent_Rules_and_Enforcement/` | What explicit rules look like elsewhere: Fiverr itself, Steam, Etsy, Google Play, FTC, EU AI Act; enforcement levers | Done |
| `05_Clause_Design/` | The deliverable: elements of a well-written freelancer-facing AI-work clause + model draft | Done |
| `06_Evidence/` | `Sources.md` (S01–S31) + `Findings.md` (RQ1–RQ5, method limits) | Done |
| `99_Archive/` | Superseded material (never deleted) | Empty |

## Scope and Boundary (settled for Wave 8, 2026-10-15/16)

- **Included:** the 12 platforms from the FRE scan set; their public governing documents (Terms, user agreements, community standards, help-center AI policies, category guidelines); comparator rulebooks (Steam, Etsy, Google Play, FTC, EU AI Act); market-positioning evidence and peer-reviewed/platform research on AI-assisted freelance work.
- **The unit of analysis is the *worker-facing AI rule*, not AI features.** A platform's AI product (Upwork's AI Agent Playground, Contra's Indy AI, Braintrust AIR, Malt's training-data clauses) is in scope only where it reveals what the platform thinks about AI in the labor exchange.
- **Excluded:** employment law and collective-bargaining AI clauses (WGA/SAG-AFTRA) except as possible follow-ups; platform *buyer*-side AI rules unless they bind sellers too; app-store rules beyond the comparator set; enforcement case files (no public dispute log exists — see Findings, method limits); Fiverr's ToS *body* (not retrievable — see below).
- **Known access limits (recorded, not worked around):** Fiverr's ToS body is client-rendered and served only to full browser sessions; archived captures contain only the page shell → recorded as **Blocked**, and Fiverr's *policy* coverage rests on its Help Center and Community Standards documents, which are themselves official policy `[S03–S05]`. No login walls were crossed anywhere; documents behind accounts (e.g. Toptal talent agreement) were not inspected.

## Conventions

- Reliability scale: **P** primary (first-party terms/policies for document-content claims; regulators; peer-reviewed), **C** company/self-published (marketing, platform research), **T** reputable secondary, **I** internal repository/vault records.
- Every factual claim in folders 01–05 references an `S##` register entry; quotes are verbatim from the fetched document with fetch date.
- Date-stamp all findings; the audit is a **snapshot of2026-10-16** — terms change, and `00_Index/Index.md` carries the re-check triggers.

## Working Pattern (established in Fusion Energy/Waves 3–7; reused here)

1. Create skeleton → 2. fetch/scan primary documents in parallel → 3. fill notes citing the `S##` register → 4. Synthesis + Findings → 5. Stage 2 promotion when the survey stabilizes.
