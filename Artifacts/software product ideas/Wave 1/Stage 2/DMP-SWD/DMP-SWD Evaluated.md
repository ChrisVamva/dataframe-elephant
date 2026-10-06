# DMP-SWD Evaluation 1

**Date:** 2026-10-05
**Source:** Evaluation of `Wave 1/Stage 2/DMP-SWD/DMP-SWD brainstorming.md` (10 product ideas)
**Evaluator:** @zcode (ZCode agent), for Chris
**Protocol:** `Evaluation_of_SoftwareIDEAS.md` v1.0 — formula-strict scoring
**Decision inputs from Chris (2026-10-05):** prefer the **most defensible build** over the fastest loop; this batch is sufficient (no further ideation rounds); **one-time pricing** currently more attractive than subscription.

---

## 1. Evaluation Methodology

Same five criteria and weights as the Step-1 evaluation (`NovelIdeasEvaluation1.md`), per `Evaluation_of_SoftwareIDEAS.md`:

| Criterion | Weight |
|-----------|--------|
| Technical Feasibility | 25% |
| Market Potential | 25% |
| Differentiation | 20% |
| Team Fit | 15% |
| Excitement | 15% |

**Formula:** `Overall = (Feasibility × 0.25 + Market × 0.25 + Differentiation × 0.20 + Team Fit × 0.15 + Excitement × 0.15) × 2`

**Preparation (Phase 1):** competitive landscape researched via web on 2026-10-05 in four parallel research passes covering all ten ideas. Summary of findings that drove the scores:

- **Etsy analytics is saturated:** eRank ($5.99–29.99/mo), EverBee ($24.99–99/mo), Marmalead, Sale Samurai, Alura, Listadum — 8+ freemium tools, all Etsy-locked, all estimate-grade data, all subscription.
- **Cross-marketplace claim survived with one exception:** no product joins Etsy + Gumroad + Creative Market; **Creative Market has zero third-party analytics**. Exception: **profitable.app** ($29–49/mo, 13 datasets incl. 3.7M Gumroad products, ships an MCP server on its annual plan) already occupies "Gumroad + adjacent indie-revenue intelligence" — it is the incumbent to beat on the Gumroad side.
- **Trend/newsletter lane is open:** no paid cross-marketplace "what to make next" newsletter found; Exploding Topics ($39–249/mo) is the generic ceiling anchor; Etsy's own free trend reports are the floor. Data-pack/API commerce exists (Bright Data, Apify ~$4.50/1k records; Exploding Topics API $1,000–4,000/mo) — raw data is commoditized at scale, trust-labeled data is not.
- **Template-seller tooling:** brand-kit generators exist for end users (Canva Pro ~$15/mo, Figma AI, Looka ~$96/yr), **none seller-side**; batch mockup generation is an existing priced category for POD (Listybox $99/mo, Bulk Mockup ~$15/mo) but not for Canva/Figma digital-template files; no bundle/pricing-ladder advisor for digital sellers exists; no dedicated new-seller onboarding SaaS exists (incumbents serve post-launch analytics; courses charge $197–247 one-time).
- **Creator/freelancer tools:** transcript→ebook/course is crowded (Designrr, Castmagic, Courseau, Coursebox; platforms $19–399/mo) but **none outputs marketplace-native sellable SKUs**; rate benchmarks are commoditized (Bonsai free calculator, Upwork free ranges, Apify/Piloterr sell raw scrape data) while the **scope-creep guard space is verified near-empty**; Figma and VS Code have no native payments — every plugin seller hand-rolls licensing (Lemon Squeezy, Keygen, Gumroad API fill this cheaply); every plugin ecosystem has a free maintained scaffold.
- **Legal friction:** marketplace scraping is a tolerated gray zone (no enforcement cases found; eRank/EverBee/Apify/Bright Data operate openly) — practical risk is data-source breakage, not litigation.

Full source lists per idea are recorded in the research notes; key anchors cited inline below.

---

## 2. Individual Evaluations

### 1. MarketLoom — Cross-Marketplace Intelligence for Digital-Product Sellers

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 4/5 | The data infrastructure already runs daily (Hermes cron, append-only ledger). Dashboard and Postgres are proven. Marketplace scraping fragility is the main integration risk, and it is already managed. |
| Market Potential | 4/5 | Proven willingness to pay: 8+ incumbents charge $6–99/mo to Etsy sellers alone. Our wedge (the Etsy+Gumroad+CM triangle, especially Creative Market with zero competition) is real, and the top-heavy market (2.4% ever sell) makes an edge structural. Capped because the Etsy side is saturated and profitable.app holds the Gumroad side. |
| Differentiation | 3/5 | "Only intelligence layer covering the three actual digital-product marketplaces, with honest evidence labels" is verified unoccupied — but narrower than the brainstorm doc's original claim, because profitable.app covers Gumroad cross-vertical. Differentiation *compounds over time* as the dataset accumulates (the only asset here incumbents can't copy quickly). |
| Team Fit | 4/5 | Python/TypeScript/data-pipeline skills match; we are our own first user (self-serve dogfooding via SWD-8). |
| Excitement | 4/5 | Data product with a genuine moat story; we use it daily for our own decisions. |

**Overall: 7.6/10** — `(4×.25 + 4×.25 + 3×.20 + 4×.15 + 4×.15) × 2 = 7.6`

**Verdict:** The most defensible build in the batch. Its moat is the accumulating, evidence-tiered dataset — the one asset no competitor gets for free — and it directly powers the batch's other ideas (pricing suggestions, trend intel). It is an app-layer bet, so it is slower to first revenue than 4.6/4.7, but its differentiation strengthens with every daily scan.

**Key risks:** profitable.app adds Etsy/Creative Market datasets (they move fast — check quarterly); marketplace scraping ToS moves from tolerated to enforced; Etsy-side saturation makes marketing expensive.

---

### 2. PulseDigest — Rising-Category Early Warning (Newsletter-First)

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 5/5 | A paid newsletter on top of the existing DMP pipeline. No meaningful technical risk. |
| Market Potential | 3/5 | Sellers actively seek "what to make next," and EverBee's paid trend features show some willingness to pay — but the floor is free (Etsy's own trend reports) and the lane being empty may partly mean the niche is small. Unproven willingness to pay at indie scale. |
| Differentiation | 4/5 | Verified open lane: no paid cross-marketplace "what to make" newsletter exists; Exploding Topics is generic, EverBee is Etsy-locked. |
| Team Fit | 5/5 | Writing + the pipeline we already operate. Could ship this week. |
| Excitement | 3/5 | Valuable, but it is content operations, not a build. |

**Overall: 8.0/10** — `(5×.25 + 3×.25 + 4×.20 + 5×.15 + 3×.15) × 2 = 8.0`

**Verdict:** Highest raw score in the batch and the fastest market contact available anywhere in the pipeline. But it fails Chris's stated criterion on its own: a newsletter is content, trivially copied, with no build moat — its defensibility is borrowed entirely from the dataset behind it.

**Key risks:** willingness to pay unproven (may need to launch free and convert); commoditization by any incumbent's content team; alone it teaches shipping but not defensible product-building.

---

### 3. FirstHundred — Operations Companion for New Digital Sellers

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 4/5 | Standard web app plus the data services we already run. Content-heavy rather than technically hard. |
| Market Potential | 3/5 | Large measurable influx (Etsy "digital products" #45→#6) — but pre-revenue customers are notoriously cheap: incumbents absorb demand with free tiers and courses monetize them ($197–247 one-time) instead of SaaS. One-time $30–79 pricing matches both the segment psychology and Chris's pricing preference; willingness to pay remains unproven. |
| Differentiation | 4/5 | Verified open: dedicated onboarding/operations SaaS for the first-100-sales phase was not found; incumbents serve post-launch analytics. A competitive-analysis source independently flags launch-checklist products as low-competition. |
| Team Fit | 4/5 | Web app + content + our pricing data. BundleBaker (4.9) merges in here as the pricing-ladder feature. |
| Excitement | 3/5 | Useful and clear, modestly interesting to build. |

**Overall: 7.2/10** — `(4×.25 + 3×.25 + 4×.20 + 4×.15 + 3×.15) × 2 = 7.2`

**Verdict:** The best fit in the batch for one-time pricing (course-seller economics without being a course) and a genuinely open wedge. The unresolved question is whether sellers pay for software before they have revenue; the $197–247 course market suggests they pay *once*, for hope and structure — which is exactly what a one-time companion is.

**Key risks:** free incumbents (eRank/Alura free tiers) cap pricing power; the empty space may signal no WTP rather than no competition; churn-by-graduation (customers outgrow it by design) requires a constant influx funnel.

---

### 4. Transmute — Content-to-Product Compiler for Creators

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 4/5 | LLM pipeline plus format packaging is proven technology; output quality control (a sellable workbook, not slop) is the hard engineering part. |
| Market Potential | 3/5 | Creator economy is huge but tooling is saturated and the "middle melts" — mid-tier creators and mid-tier tools are most exposed. The $20 ChatGPT Plus + Canva manual workflow is a strong substitute. |
| Differentiation | 3/5 | The generic layer is occupied (Designrr, Castmagic, Courseau); the *combination* — marketplace-native SKU output + data-grounded pricing — survived null searches, but incumbents could bolt on export in a sprint. Novelty holds at combination level only. |
| Team Fit | 4/5 | Python/LLM/TypeScript matches; LLM-output evaluation is a real skill the research skill-set covers. |
| Excitement | 4/5 | Compiling content into products is a genuinely fun compiler-shaped problem. |

**Overall: 7.1/10** — `(4×.25 + 3×.25 + 3×.20 + 4×.15 + 4×.15) × 2 = 7.1`

**Verdict:** A feature-velocity race, not a moat — except for the pricing-recommender piece, which no competitor has and which depends on exactly the dataset we accumulate. As specified it is weaker than MarketLoom because its only defensible component is a subset of MarketLoom's asset.

**Key risks:** funded incumbents add Gumroad/Etsy export; pricing recommendations inherit estimate-grade inputs (~80% accuracy) — "suggest $29 because comparable listings cluster there" is defensible, "this will earn $X" is not; buyers skew free-tool-expectation.

---

### 5. BenchData — The Ledger as a Product (Data Packs + API)

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 5/5 | Zero marginal build — the collection infrastructure runs daily regardless. Packaging CSV/API is trivial. |
| Market Potential | 2/5 | Niche: buyers are other tool-builders and analysts. Raw marketplace data is commoditized (Bright Data, Apify at ~$4.50/1k records); Exploding Topics anchors trend APIs at $1,000+/mo but that is a different scale. A few hundred realistic customers at indie prices. |
| Differentiation | 3/5 | Evidence-tier labeling as a trust feature is unique; the underlying data is not. |
| Team Fit | 5/5 | It is our existing work, packaged. |
| Excitement | 3/5 | Plumbing. |

**Overall: 7.1/10** — `(5×.25 + 2×.25 + 3×.20 + 5×.15 + 3×.15) × 2 = 7.1`

**Verdict:** Excellent as a *complement* and funnel — the cheapest possible second surface on the same dataset (and one-time CSV packs fit Chris's pricing preference perfectly) — but thin as the main product. The high feasibility score with a low market score is the classic "solution looking for a buyer" profile the protocol warns about.

**Key risks:** scraping ToS enforcement; profitable.app's MCP/API surface already serves the agent-builder segment; commoditization from data-broker incumbents.

---

### 6. KitForge — Brand-Kit Production Line for Template Sellers

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 3/5 | Figma/Canva API automation is real but headless rendering, API rate limits, and ToS constraints on automated account use are significant integration work. |
| Market Potential | 3/5 | Template sellers are proven spenders, but the output is a commodity: a buyer can self-serve a brand guideline nearly free (Canva Pro $15/mo, Looka $96/yr, PLR/MRR resell bundles flood Etsy at $2–10). The seller-side demand for *mass production* is assumed, not evidenced. |
| Differentiation | 4/5 | Verified unoccupied: no tool whose users are template sellers mass-producing brand-guideline products to resell. Every existing generator serves a brand owner making one document. |
| Team Fit | 3/5 | Platform-API automation is learnable; visual quality of generated output is a non-trivial craft risk. |
| Excitement | 4/5 | A generative production line is fun to build. |

**Overall: 6.7/10** — `(3×.25 + 3×.25 + 4×.20 + 3×.15 + 4×.15) × 2 = 6.7`

**Verdict:** Open at the tool level, saturated at the output level. Its differentiation claim survives verification, but it sits on Canva/Figma APIs that could ship a competing feature any quarter, and the demand question (do sellers want to *mass*-produce, or do PLR bundles already satisfy them at $5?) is unanswered. Highest-upside/highest-platform-risk build in the batch.

**Key risks:** Canva/Figma ship a native competitor; API terms block automation; PLR price floor compresses the seller's margins below tool affordability.

---

### 7. RatePilot — Rate Benchmarks & Scope Guard for Freelancers

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 3/5 | Benchmarks are easy (scrapers exist off-the-shelf); the scope guard — continuously comparing delivered work against quoted scope — is a heavy integration lift (contracts, email, PM context). |
| Market Potential | 2/5 | Freelancers are a large base, but the benchmark half is commoditized (Bonsai's free 30k-contract calculator, Upwork's free ranges) and the guard's demand evidence is Reddit-anecdote grade. Nobody currently charges standalone for rate data — possibly because nobody would pay. |
| Differentiation | 3/5 | The novelty claim was backwards: benchmarks are the crowded part; the scope guard is the verified near-empty part — and one idea-report marketplace (MicroGaps) is already selling the blueprint, so the wedge is visible to others. |
| Team Fit | 3/5 | Integration-heavy product is a poor match for a small team's bandwidth. |
| Excitement | 3/5 | Moderately interesting. |

**Overall: 5.5/10** — `(3×.25 + 2×.25 + 3×.20 + 3×.15 + 3×.15) × 2 = 5.5`

**Verdict:** The honest dependency note from the brainstorm doc stands — without FRE data this is Bonsai's free calculator with a weaker dataset. The open half (scope guard) is hard to build and unproven to sell; the easy half (benchmarks) is free everywhere. Revisit only if the FRE stream later surfaces concrete WTP signals.

**Key risks:** FRE data quality/legality; incumbents (Bonsai) absorbing the guard feature; empty space = hard, not undiscovered.

---

### 8. BundleBaker — Catalog Bundler & Pricing-Ladder Planner

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 4/5 | Small, standard build on top of our ladder dataset. |
| Market Potential | 2/5 | No demand evidence found at all: no product, no community threads, no app surface (Etsy has no bundle-app ecosystem; Shopify bundle apps are saturated for physical goods and broken for digital). The gap looks like absence of demand, not of competition. |
| Differentiation | 3/5 | Open, but open because nobody wants it as a standalone. |
| Team Fit | 4/5 | Trivial for us. |
| Excitement | 2/5 | A feature, not a product. |

**Overall: 6.0/10** — `(4×.25 + 2×.25 + 3×.20 + 4×.15 + 2×.15) × 2 = 6.0`

**Verdict:** The brainstorm doc's own flag is confirmed by research: a feature in search of a product. Merge into FirstHundred (4.3) as the pricing-ladder module; do not build standalone.

**Key risks:** standalone launch would die of no demand; platform APIs don't support bundle automation for digital downloads anyway.

---

### 9. MockMachine — Listing-Mockup Mass Production for Template Sellers

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 3/5 | Headless rendering of Canva/Figma files is technically awkward and ToS-sensitive; PSD-based batch tools solve a different (POD) pipeline. |
| Market Potential | 3/5 | Real pain (hours per listing), but incumbents are cheap (Bulk Mockup ~$15/mo, Listybox $99/mo) and the seller fallback — Canva mockup template bundles — costs ~$10 forever. |
| Differentiation | 2/5 | Crowded category; the Canva/Figma-digital-file variant is a genuinely open micro-wedge, but Canva Bulk Create erodes it from below. Incremental. |
| Team Fit | 3/5 | Rendering infrastructure is new ground for the team. |
| Excitement | 3/5 | Moderately interesting. |

**Overall: 5.6/10** — `(3×.25 + 3×.25 + 2×.20 + 3×.15 + 3×.15) × 2 = 5.6`

**Verdict:** The doc's ⚠️ warning was correct — this is a feature of a broader seller workflow, viable only folded into something like KitForge or FirstHundred, not standalone.

**Key risks:** Canva API terms; Canva Bulk Create commoditization; incumbents adding the digital-file variant.

---

### 10. PluginForge — Production Line for Marketplace Code Products

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 2/5 | The "one maintained codebase → four marketplaces" premise is structurally broken: Blender (Python/GPL), Figma (TypeScript/React), VS Code (TypeScript), WordPress (PHP) are four divergent codebases. What remains is four separate scaffolds — and free maintained scaffolds already exist in every ecosystem (wp-cli, `yo code`, create-figma-plugin, community Blender templates). |
| Market Potential | 2/5 | Developer-sellers of plugins are a small, fragmented base; licensing/update plumbing is commoditized (Gumroad API, Lemon Squeezy 5%+$0.50, Keygen, EDD); the one unoccupied position (a commercial "ShipFast for plugins") is unoccupied for a reason — ShipFast-class success rests on SaaS-sized pains (auth/payments/emails). |
| Differentiation | 3/5 | Commercially sold multi-target plugin boilerplates genuinely don't exist; the gap's existence may be rational. |
| Team Fit | 3/5 | Buildable, but maintenance across four unrelated ecosystems is a standing tax. |
| Excitement | 3/5 | Appeals to the research roots (compilation over interpretation), but the premise's failure dampens it. |

**Overall: 5.0/10** — `(2×.25 + 2×.25 + 3×.20 + 3×.15 + 3×.15) × 2 = 5.0`

**Verdict:** Mostly covered by free scaffolds plus horizontal licensing platforms, and the uncovered part (cross-ecosystem maintenance) is both the hardest and the least demanded. If any residue is worth pursuing, it is the research-verified micro-wedge — a license-gate SDK for Figma/VS Code sellers specifically (who have no native payments) — as a small $49–99 one-time product, not a "production line."

**Key risks:** premise broken as specified; four-ecosystem maintenance burden; free substitutes at every layer.

---

## 3. Summary Rankings

| Rank | Product | Overall Score | Feasibility | Market | Differentiation | Team Fit | Excitement |
|------|---------|---------------|-------------|--------|-----------------|----------|------------|
| 1 | **PulseDigest** | **8.0** | 5 | 3 | 4 | 5 | 3 |
| 2 | **MarketLoom** | **7.6** | 4 | 4 | 3 | 4 | 4 |
| 3 | **FirstHundred** | **7.2** | 4 | 3 | 4 | 4 | 3 |
| 4 | **Transmute** | **7.1** | 4 | 3 | 3 | 4 | 4 |
| 4 | **BenchData** | **7.1** | 5 | 2 | 3 | 5 | 3 |
| 6 | **KitForge** | **6.7** | 3 | 3 | 4 | 3 | 4 |
| 7 | **BundleBaker** | **6.0** | 4 | 2 | 3 | 4 | 2 |
| 8 | **MockMachine** | **5.6** | 3 | 3 | 2 | 3 | 3 |
| 9 | **RatePilot** | **5.5** | 3 | 2 | 3 | 3 | 3 |
| 10 | **PluginForge** | **5.0** | 2 | 2 | 3 | 3 | 3 |

---

## 4. Recommendations

### Tier 1: Strong Candidates for Step 2 (7.0+)

| Product | Rationale |
|---------|-----------|
| **PulseDigest** (8.0) | Highest score; fastest market contact; open lane verified. Fails the "most defensible build" criterion alone — recommend as MarketLoom's go-to-market layer, not the product bet. |
| **MarketLoom** (7.6) | **Recommended pick.** The most defensible build in the batch (accumulating evidence-tiered dataset = the only asset incumbents can't copy), self-serve dogfooding, one-time data packs viable alongside subscription, and it subsumes PulseDigest + BenchData as surfaces of the same asset. |
| **FirstHundred** (7.2) | **Runner-up.** Best one-time-pricing fit ($30–79 matches segment psychology and Chris's preference); verified open onboarding wedge; BundleBaker merges into it. WTP pre-revenue is the open question. |
| **Transmute** (7.1) | Solid but a feature-velocity race; its only defensible component is a subset of MarketLoom's asset. Hold. |
| **BenchData** (7.1) | Complement, not product: package as one-time CSV packs alongside whichever main product is picked. |

### Tier 2: Promising but Needs Refinement (6.0–6.9)

| Product | Rationale |
|---------|-----------|
| **KitForge** (6.7) | Verified unoccupied and highest-upside, but platform-dependent (Canva/Figma APIs) with unproven mass-production demand. Revisit if the picked product shares its stack, or as a later bet after observing the PLR-flood dynamics. |
| **BundleBaker** (6.0) | Merge into FirstHundred as a feature; never standalone. |
| **RatePilot** (5.5) | Park until the FRE stream surfaces willingness-to-pay signals. |

### Tier 3: Good Ideas, Limited Market or Differentiation (5.0–5.9)

| Product | Rationale |
|---------|-----------|
| **MockMachine** (5.6) | Feature of a broader seller workflow, not a product. |
| **PluginForge** (5.0) | Premise structurally broken; only the license-gate SDK micro-wedge survives, as a small side product at best. |

### Applying Chris's decision criteria (overlay, not score weights)

1. **"Most defensible build"** → **MarketLoom**. Its moat compounds daily (the ledger), it is the only idea whose differentiation *grows* with time, and it self-serves SWD-8's own research needs. PulseDigest (highest raw score) is repositioned as its funnel layer — the newsletter is how MarketLoom acquires sellers cheaply, not the product bet.
2. **"This batch is sufficient"** → confirmed; SWD-8 (conjunction analysis) appends to this doc as FRE/CRE data arrives, no new ideation round.
3. **"One-time pricing attractive"** → favors FirstHundred's model and BenchData's CSV packs; MarketLoom can launch with one-time data packs before any subscription. The Etsy-incumbent subscription standard ($6–99/mo) remains the ceiling for an app layer.

**Top-2 for the SWD-2 decision: MarketLoom (recommended) and FirstHundred.**

---

## 5. Key Insights

1. **Combination-level novelty is the batch's pattern.** Almost every component is commoditized somewhere (analytics per marketplace, mockups, rate data, scaffolds, brand-kit generation); what survived web verification is the *combination* — cross-marketplace + evidence tiers, marketplace-native SKUs + data pricing, onboarding + ops + ladder. Wave 1's insight inverted: here, dataset moats beat feature cleverness.
2. **The ledger is the only defensible asset in the whole conjunction.** Three independent research passes converged on it. Ideas that are *surfaces of the ledger* (MarketLoom, PulseDigest, BenchData) took 4 of the top 5 ranks.
3. **New sellers pay once, not monthly.** The incumbent SaaS model ($6–99/mo) serves established sellers; new sellers are monetized by courses at $197–247 one-time. Chris's one-time instinct matches the segment psychology — and suggests one-time-first pricing for whatever we ship to sellers.
4. **Empty spaces are ambiguous.** FirstHundred, the scope guard, and the ladder planner are verified unoccupied — which may mean open wedge or no demand. Mitigation: one-time pricing, pre-sell, and the prediction journal (thesis + falsifying signal before building).
5. **profitable.app is the incumbent to study first.** It occupies Gumroad-side intelligence at $29–49/mo with an MCP server, moves fast, and was invisible to our brainstorming doc's original framing. Any MarketLoom Phase 1 must start with its teardown.
6. **Platform-dependency clusters risk.** KitForge, MockMachine (Canva/Figma APIs) and any Etsy-API product carry existential platform risk — a reason to prefer products built on our own data.

---

## 6. Recommended Next Steps

1. **Chris decides SWD-2** between **MarketLoom (recommended)** and **FirstHundred**, decision recorded in the daily note `## Decisions`.
2. On the pick: lightweight **Step 2 building orientation** for the chosen product in this folder (`Wave 1/Stage 2/DMP-SWD/`), then **SWD-3** creates `TODO/Core/projects/SWD/plans/a.md` (MVP scope, repo home, phases with testable gates), then the **prediction journal before any code** (price, segment, expected sales at 30/60/90 days, falsifying signal — per the SWD-1 memo addendum).
3. If MarketLoom is picked: **Phase 1 task one = profitable.app teardown** (dataset quality, coverage gaps, our evidence-tier edge), and **launch PulseDigest as its free/cheap funnel layer** in parallel (it is a marketing asset here, not the product bet).
4. **SWD-8 conjunction analysis continues** (due 2026-10-12): folds in FRE/CRE data as streams start; appends to this document per the append-only rule.
5. **BenchData one-time CSV packs** ship as an experiment alongside the picked product once ≥2 weeks of multi-market ledger data exist — the cheapest real pricing test in the whole program.

---

*Sources (key anchors): erank.com/plans; everbee.io/pricing; profitable.app & profitable.app/pricing; explodingtopics.com (incl. API pricing); glimpsehq.io; brightdata.com/products/datasets/etsy; apify.com (Etsy scrapers, Upwork scraper); placeit.net/pricing; listybox.com/pricing; bulkmockup.com; canva.com (Brand Kit, Bulk Create); figma.com (AI brand guidelines generator); looka.com; brandpad.io; frontify pricing (via brandlife.io); saaspegasus.com; makerkit.dev; keygen.sh/pricing; docs.lemonsqueezy.com; gumroad fee comparison (stories.byburk.net); microgaps.com/gaps/scope-creep-change-order-freelancers; bonsai rate calculator (via a-wise.co.uk); piloterr.com; courseagent.ai 2026 roundup; castmagic pricing (podtools.cc); designrr; market.us creator-economy statistics; 3dxdev.com Blender seller guide. Estimate-grade caveats noted inline; full research notes held in session, key facts re-verifyable via the cited URLs.*

*Document version: 1.0 — formula-strict per `Evaluation_of_SoftwareIDEAS.md`; append-only thereafter.*
