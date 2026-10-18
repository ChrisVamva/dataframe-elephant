# Source Register

_Every factual claim in folders 01–05 references an entry here (`[S##]`). Superseded sources get marked, never deleted._

**Reliability scale:**
- **P** — primary: (a) first-party **governing documents** (terms of service, user agreements, community standards, official policy pages) — graded P for *document-content* claims, because "the document says X" is directly checkable against the fetched text; (b) regulators and legal instruments; (c) peer-reviewed papers and preprints.
- **T** — reputable secondary: major news, established trade press, data-driven think tank.
- **C** — company/self-published **claims about the world** (marketing copy, platform-run research, vendor benchmark/adoption claims): the primary source for the company's *own statement*, but not independent evidence of the underlying fact.
- **I** — internal: this repository and the associated Obsidian vault records.

**Notes on grading (deviation from Wave 7, approved by method):** Wave 7 graded all vendor documentation **C** because its claims were about *product capability* (vendor self-claim until reproduced). This wave's core claims are different in kind — "Fiverr's Community Standards state X", "Upwork's Terms §3.2 say Y" — and the governing document *is* the definitive evidence of its own text. Where the same document makes claims about the world (e.g. Upwork's research figures), those specific claims are still graded **C** and tagged `[reported signal]`. Access date for all fetched pages: **2026-10-16** unless another date is given. Blocked/unretrievable sources are recorded with their failure mode rather than omitted.

## A. Platform governing documents — the audit set (fetched 2026-10-16)

| ID | Rel. | Source | URL | Document date | Used for |
|----|------|--------|-----|---------------|----------|
| S01 | P | Upwork Terms of Service (User Agreement, Terms of Use, all addenda on one page) | https://www.upwork.com/legal | fetched 2026-10-16 (Any Hire Terms v1.6 eff. 2025-11-21) | §2.4 User Content and AI Tools (training licence); §3.2 conditional AI clause; "honest about who's doing the work" rule; AI-category nav |
| S02 | P | Upwork AI Agent Playground Participation Terms (Beta), v1.2 | https://www.upwork.com/legal (section "AI Agent Playground Participation Terms") | eff. 2025-07-29 | AI Agents submit deliverables to client job posts; feedback is sole payment; no-human-edit requirement |
| S03 | P | Fiverr — Our Community Standards (incl. section "AI-generated content") | https://help.fiverr.com/hc/en-us/articles/37333125829649-Our-Community-Standards | fetched 2026-10-16 | The fullest platform AI-work clause: allows generative AI, conditions, prohibitions, enforcement |
| S04 | P | Fiverr Help — "Using AI on Fiverr: Guidelines for freelancers and clients" | https://help.fiverr.com/hc/en-us/articles/34998793899665-Using-AI-on-Fiverr-Guidelines-for-freelancers-and-clients | fetched 2026-10-16 | "permits the use of AI across all service categories"; "AI use is encouraged"; client opt-out; dispute factors; enforcement ladder |
| S05 | P | Fiverr Help — "AI services guidelines" | https://help.fiverr.com/hc/en-us/articles/17240598194321-AI-services-guidelines | fetched 2026-10-16 | Category-level rules (voice synthesis, avatars): rights clearance, deletion-after-delivery |
| S06 | P — **Blocked** | Fiverr's Terms of Service (body) | https://www.fiverr.com/legal-portal/legal-terms/terms-of-service | attempts 2026-10-16 | Body is client-rendered; direct fetch serves page shell only; Wayback captures (2023-10-23, 2024-12-06, 2026-01-08) contain shell + catalogue JSON, not the ToS prose. Recorded as Blocked; Fiverr coverage rests on S03–S05 |
| S07 | P | Toptal Website Terms & Conditions | https://www.toptal.com/tos | fetched 2026-10-16 | No AI-work provisions in site T&Cs; limitation: talent-side agreement not public |
| S08 | P | Contra Terms of Service | https://www.contra.com/terms | fetched 2026-10-16 | "Using AI-generated content" + "AI generated content limitations" (responsibility/accuracy/human review); Indy AI provisions |
| S09 | P | Freelancer.com User Agreement | https://www.freelancer.com/about/terms | last modified 2025-06-05; fetched 2026-10-16 | Full text scanned: no AI/generative-AI provisions |
| S10 | P | PeoplePerHour Terms & Conditions | https://www.peopleperhour.com/static/terms | fetched 2026-10-16 | §3.5.1 ML proposal categorisation (platform's own AI); no worker AI-work clause |
| S11 | P | Malt Community Terms and Conditions | https://www.malt.com/legal | in force 2026-04-16; fetched 2026-10-16 | §5.4 AI-based features (training on user data); §12.8 AI accuracy disclaimer; no worker AI-work clause; site trending-skill nav (AI/AI Agent/RAG) |
| S12 | P | freelancermap Terms and Conditions | https://www.freelancermap.com/term-and-conditions.html | "Conditions State December 2018"; fetched 2026-10-16 | No AI provisions; document predates the generative-AI era |
| S13 | P | Arc Terms of Service | https://arc.dev/terms | last modified 2026-08-31; fetched 2026-10-16 | Full text scanned: no AI-work provisions |
| S14 | P | Codementor Terms of Service | https://www.codementor.io/terms | last modified 2026-08-31; fetched 2026-10-16 | No AI-work provisions in ToS; AI tutor/expert service taxonomy in site nav |
| S15 | P | Braintrust Terms of Service | https://www.usebraintrust.com/terms | last updated 2025-02-06; fetched 2026-10-16 | Prohibited-conduct list has no AI item; no worker AI-work clause |
| S16 | P | Braintrust Talent Terms | https://www.usebraintrust.com/talent-terms | fetched 2026-10-16 | Additional terms on talent accounts: no AI-work clause |
| S17 | P | Braintrust Network Standards + Code of Conduct | https://www.usebraintrust.com/network-standards ; https://www.usebraintrust.com/code-of-conduct | fetched 2026-10-16 | Conduct rules: no AI-work clause |
| S18 | P | Braintrust Responsible AI Policy (operator: Freelance Labs Inc.) | https://www.usebraintrust.com/air-artificial-intelligence-policy | last updated 2026-05-01; fetched 2026-10-16 | Platform-side AI governance only (AIR recruiting): human oversight, NYC LL144 bias audit, EU AI Act readiness targeted 2026-08-01 |
| S19 | P | Botpool Terms of Service | https://botpool.ai/term-service | fetched 2026-10-16 | Short terms (15 sections): no AI-work clause |
| S20 | C | Botpool FAQs | https://botpool.ai/faqs | fetched 2026-10-16 | AI-native marketplace positioning; vetted listing; escrow; self-description only |

## B. Comparator rulebooks — what an explicit rule looks like

| ID | Rel. | Source | URL | Document date | Used for |
|----|------|--------|-----|---------------|----------|
| S21 | P | Steamworks Content Survey, §3 "Generative Artificial Intelligence Content" | https://partner.steamgames.com/doc/gettingstarted/contentsurvey | fetched 2026-10-16 | Mandatory disclosure of pre-generated and live-generated AI content; prerelease review of AI output; guardrail declaration for live generation |
| S22 | P | Etsy Seller Handbook — "What is Etsy's stance on AI creations?" | https://www.etsy.com/seller-handbook/article/1275449912004 | fetched 2026-10-16 | "Sellers must disclose within their listing description if an item is created with the use of AI" |
| S23 | P | Google Play — "Understanding Google Play's AI-Generated Content policy" | https://support.google.com/googleplay/android-developer/answer/14094294 | fetched 2026-10-16 | Developer responsibility for generative-AI app outputs; deceptive-content prohibitions |
| S24 | P | FTC — Trade Regulation Rule on the Use of Consumer Reviews and Testimonials (16 CFR Part 465) | https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials | published 2024-08-22; fetched 2026-10-16 | "AI-generated reviews are covered by the final rule"; regulator names generative AI as a fake-review scaling risk |
| S25 | P | EU AI Act, Article 50 (transparency obligations for providers and deployers) | https://artificialintelligenceact.eu/article/50/ (reproduction; controlling text: Regulation (EU) 2024/1689, EUR-Lex) | fetched 2026-10-16 | Machine-readable marking of AI-generated/manipulated content; deepfake disclosure duty |

## C. Market signals and empirical context

| ID | Rel. | Source | URL | Document date | Used for |
|----|------|--------|-----|---------------|----------|
| S26 | C | Upwork — press release, "Future Workforce Index 2026" | https://www.upwork.com/press/releases/upworks-future-workforce-index-2026-how-ai-is-redefining-the-value-of-work-as-skilled-freelancing-accelerates | 2026-07-14; fetched 2026-10-16 | Self-described as "the world's human and AI-powered work marketplace"; AI-earnings figures (survey of 2,400 U.S. workers, Mar–Apr 2026 + platform data); "AI Orchestrator" framing |
| S27 | C | Upwork Research — "How Generative AI Adds Value to the Future of Work" | https://www.upwork.com/research/generative-ai-work-value | fetched 2026-10-16 | Upwork's research-program framing of gen-AI value creation |
| S28 | P | Teutloff, Einsiedler, Kässi, Braesemann, Mishkin, del Rio-Chanona — "Winners and losers of generative AI: Early Evidence of Shifts in Freelancer Demand", *Journal of Economic Behavior & Organization* | https://doi.org/10.1016/j.jebo.2024.106845 (metadata/abstract via Crossref + OpenAlex, 2026-10-16) | 2025 | Demand shifts on "a leading online freelancing platform": substitutable skills (writing/translation) −20–50% vs counterfactual; ML programming +24%; AI-chatbot development ≈ triples; novice demand declines |
| S29 | P (preprint) | Imteyaz, Lopez, Rajpal, Shin, Savage — "Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers" | https://arxiv.org/abs/2604.27231 | submitted 2026-04-29; fetched 2026-10-16 | Freelancers lack organizational training infrastructure; gen-AI tools as self-directed upskilling (peer context; not peer-reviewed) |
| S30 | P | First-party site-structure observations from the audit fetches (Fiverr served page data incl. AI category tree — AI Services, AI Agents, AI Content, AI Artists, Generative Engine Optimization; Malt trending skills n8n/AI/AI Agent/RAG; Codementor AI tutor & expert categories; Braintrust "AI Gig Work" product; Upwork "AI & Automation" category nav) | pages as per S01, S03, S11, S14, S15 | observed 2026-10-16 | RQ3 positioning gap; site taxonomy, not demand volume |

## D. Internal records

| ID | Rel. | Source | Location | Date | Used for |
|----|------|--------|----------|------|----------|
| S31 | I | FRE daily reports + summary reports (demand probes, platform facts, evidence labels) | `Documents\Obsidian Vaults\TODO\Legacy folder\Legacy Cron Jobs\FRE\Daily\2026-10-07…10.md` and `…\FRE\reports\2026-10-07…10-hermes-FRE.md` | 2026-10-07…10 | Dated demand probes (Upwork automation 1,912; Fiverr dashboards 8,100+/AI integrations 10,000+; Freelancer.com python 188); the 12-platform scan set; evidence-label discipline (`Observed/Reported/Contradicted/Blocked`) |

## Verification queue

- **S06 (Fiverr ToS body):** re-attempt when a rendered client or an official copy is available; until then all "Fiverr ToS" phrasing in notes must say *Community Standards/Help Center* instead.
- **S07 (Toptal):** the talent-side agreement (signed in-app) was not inspected; if obtained, re-run the AI scan.
- **S12 (freelancermap):** document state is December 2018; check for a newer revision page (a `Last updated` may exist elsewhere).
- **S22 (Etsy):** official legal-page copy (`etsy.com/legal/…`) returned 403; the Seller Handbook article is the official statement — verify equivalence if the article moves.
- **S28:** full text paywalled at ScienceDirect (403 on fetch); abstract via OpenAlex. Pull the full paper via institutional access before quoting anything beyond the abstract.
- **S25:** confirm article wording against EUR-Lex official text (Reg. (EU) 2024/1689) before publication-grade citation.
- **S31:** probes are single-day observations; re-run before any demand figure appears in an article.
