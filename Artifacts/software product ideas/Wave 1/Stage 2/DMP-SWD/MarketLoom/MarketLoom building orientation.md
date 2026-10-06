# MarketLoom — Cross-Marketplace Intelligence for Digital-Product Sellers

**Step 2: Initial Product Approach**
**Source:** Derived from `Wave 1/Stage 2/DMP-SWD/DMP-SWD brainstorming.md` — Product 4.1, selected via `DMP-SWD Evaluated.md` (7.6/10, Tier 1) and Chris's SWD-2 decision (2026-10-05: "most defensible build" criterion)
**Date:** 2026-10-05
**Track principles (grounding):** "sell the shovel we already swing daily" — the DMP scanning infrastructure and append-only, evidence-tiered ledger are the product's foundation; the trust methodology (Observed/Reported/Estimated/Unverified) is the differentiator; one-time pricing first (Chris).

---

## 1. Product Vision

### 1.1 Problem Statement

Digital-product sellers on Etsy, Gumroad, and Creative Market decide **what to make and at what price** on gut feel, because the intelligence layer is fragmented:

- **Etsy tools are Etsy-locked and estimate-grade:** eRank ($5.99–29.99/mo), EverBee ($24.99–99/mo), Marmalead, Alura, Sale Samurai — none covers another marketplace, and all resell ~80%-accuracy estimates without saying how they know.
- **Gumroad intelligence exists but is one vertical of a broad product:** profitable.app ($29–49/mo, 3.7M Gumroad products, ships an MCP server) covers Gumroad plus 12 unrelated datasets — no Etsy, no Creative Market, no digital-product focus.
- **Creative Market has zero third-party analytics** — sellers there are fully blind.
- The market context makes an edge structural, not optional: only 2.4% of Gumroad products ever record a sale; median seller revenue ≈ $81 (profitable.app); yet sellers demonstrably pay $6–99/mo for intelligence.

### 1.2 Solution

MarketLoom is an intelligence layer spanning the three actual digital-product marketplaces:

1. **Collect** — a scheduled collector pipeline extends the existing DMP/Hermes scanning into programmatic collection (marketplace pages, secondary sources, Etsy Open API where granted, profitable.app as a purchased source), normalizing everything into one append-only ledger.
2. **Analyze** — price ladders per category, category velocity (rising signals), and a whitespace finder (category × platform × price band) computed over the accumulating data.
3. **Deliver** — three surfaces on one dataset: a **free weekly digest** (the PulseDigest layer — the funnel), a **read-only dashboard** with evidence labels on every number, and **one-time data packs** (CSV/Parquet — the BenchData layer, Chris's preferred pricing model).

**Honest scope note:** the dashboard is phase-3-plus economics. Phase 1 ships data + digest + a pre-sell gate, because the riskiest assumption is *demand*, not technology.

### 1.3 Value Proposition

| Stakeholder | Benefit |
|-------------|---------|
| New seller (<100 sales) | "What to make next" answered in minutes from observed demand, not guru courses — with honest evidence labels instead of fake precision |
| Established seller | Price ladders and category velocity across three marketplaces at once; whitespace they can't see from inside one platform |
| Chris / SWD | The tool consumes the dataset we already build daily (self-serve dogfooding via SWD-8); the moat compounds with every scan; one-time revenue model matches stated preference |
| Other tool-builders | (Later) BenchData packs/API — trust-labeled commerce data that raw scraped feeds don't carry |

---

## 2. Technical Architecture

### 2.1 High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        SOURCES (tiered)                          │
│  Own scans (CM/Gumroad pages) · profitable.app (purchased) ·     │
│  Etsy Open API v3 (applied) · secondary published data · manual  │
└──────────────────────────┬───────────────────────────────────────┘
                           │ scheduled runs (APScheduler / Hermes pattern)
┌──────────────────────────▼───────────────────────────────────────┐
│                 COLLECTOR LAYER (Python 3.12)                    │
│  per-marketplace collectors → normalize → TIER-LABEL → append    │
└──────────────────────────┬───────────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────────┐
│        LEDGER STORE (PostgreSQL 16; SQLite in dev)               │
│  append-only products/observations; corrections = new rows       │
│  every row: source_url, evidence_tier, observed_at               │
└──────────────────────────┬───────────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────────┐
│              ANALYTICS LAYER (Python, pandas/Polars)             │
│  price ladders · category velocity · whitespace matrix ·         │
│  rising-signal alerts                                            │
└───────┬──────────────────────┬─────────────────────┬─────────────┘
        ▼                      ▼                     ▼
┌──────────────┐   ┌──────────────────────┐   ┌──────────────────┐
│ Weekly Digest│   │ Dashboard (read-only)│   │ Data Packs       │
│ email funnel │   │ Next.js 15+Tailwind  │   │ CSV/Parquet,     │
│ (free)       │   │ evidence labels in UI│   │ one-time $       │
└──────────────┘   └──────────────────────┘   └──────────────────┘
        (API + MCP server: Phase 4, parity with profitable.app)
```

### 2.2 Core Components

**A. Collector Layer (Python 3.12, Playwright + httpx + BeautifulSoup)**
- `cm_collector` — Creative Market bestseller/category pages (greenfield: zero third-party analytics exists; start here).
- `gumroad_collector` — own discovery-page scans **plus** profitable.app data (purchased subscription — buying the incumbent's dataset for $29–49/mo is cheaper and safer than replicating 3.7M-product coverage).
- `etsy_collector` — layered: Etsy Open API v3 (OAuth-gated, application required) where granted; secondary published data (eRank/EverBee public pages, attributed) otherwise.
- Shared: normalization → dedup → **evidence-tier assignment** (Observed = read off the page; Reported = platform/vendor estimate; Estimated = our model; Unverified = single anonymous source) → append.

**B. Ledger Store (PostgreSQL 16, SQLite during development)**
- Append-only, mirroring the DMP `Product Ledger.md` discipline: `observations(product_id, marketplace, category, title, price, sales_signal, evidence_tier, source_url, observed_at)`. Corrections are new rows, never updates — the audit trail *is* the trust feature.

**C. Analytics Layer (Python, pandas/Polars, scheduled)**
- Price ladders per (marketplace × category); velocity = rank/signal deltas over rolling windows; whitespace matrix = category × platform × price-band occupancy; rising-signal alerts (threshold + human review before publishing).

**D. Delivery Surfaces**
- **Digest** — Buttondown or Resend (pick in Phase 1), weekly, free: the PulseDigest layer and the funnel.
- **Dashboard** — Next.js 15 + Tailwind, **read-only, no accounts** in v1: public pages per marketplace with evidence badges.
- **Data packs** — static CSV/Parquet exports sold one-time (Gumroad — our own market, dogfooding DMP).
- **API/MCP** — Phase 4 only.

### 2.3 Data Flow

1. Scheduled collectors run daily (extending the Hermes 11:00 pattern; ultimately one cron).
2. New observations are tier-labeled and appended; nothing is ever mutated.
3. Nightly analytics job recomputes ladders/velocity/whitespace.
4. Surfaces read the *computed* layer: digest rendered weekly, dashboard on demand, packs cut on schedule.
5. Chris (and later pilot sellers) validate signals before anything is published — a human review gate, not auto-published claims.

| Component A | Component B | Mechanism | Format | Challenge |
|---|---|---|---|---|
| Collectors | Ledger | direct SQL append (SQLAlchemy 2.x) | rows | dedup across runs |
| Ledger | Analytics | SQL views + pandas/Polars | DataFrames | honest handling of sparse estimate data |
| Analytics | Dashboard | JSON (Next.js server components) | JSON | staleness labeling |
| Analytics | Digest/Packs | static render | HTML / CSV / Parquet | reproducible cuts (date-stamped) |

---

## 3. Language Integration Strategy

### 3.1 Why These Languages?

| Language | Role | Rationale |
|---|---|---|
| **Python 3.12** | Collectors + analytics | Existing DMP/Hermes scanning patterns are Python; pandas/Polars/Playwright are the ecosystem's best tools for exactly this workload |
| **PostgreSQL 16 / SQLite** | Storage | Append-only audit pattern maps to plain tables; SQLite for zero-ops dev, PostgreSQL when the dashboard is public |
| **TypeScript (Next.js 15 + Tailwind)** | Dashboard | Read-only rendering with server components keeps it simple; one language for UI |
| **CSV / Parquet** | Data packs | The product buyers' lingua franca; Parquet for larger cuts later |

### 3.2 Data Marshaling

Single-process, single-language-per-layer — deliberately boring. SQLAlchemy 2.x models are the one schema definition; JSON to the dashboard; static files to buyers. No cross-runtime marshaling problem exists **by design** (contrast with Wave-1's platform bets; the Step-1 principle "grounded in what the team actually runs" applies).

### 3.3 Transaction Coordination

Not applicable in the ACID-across-runtimes sense. The integrity mechanism is the **append-only discipline**: every observation carries source + tier + timestamp; corrections append; analytics always compute from the full history. Consistency = reproducible, date-stamped cuts.

---

## 4. Development Phases

> **Riskiest assumption first:** *sellers will pay for cross-marketplace intelligence.* Technology risk here is low; demand risk is the one that kills the product. Phase 1 therefore ends in a demand gate before any dashboard is built.

### Phase 1: Data Foundation & Demand Gate (Weeks 1–4)

**Goal:** one unified, tier-labeled tri-marketplace dataset — and a pay-validated demand signal before building product surfaces.

**Deliverables:**
- [ ] profitable.app teardown note (dataset quality, coverage, gaps, MCP surface) + subscribe decision
- [ ] Creative Market collector v1 (greenfield; easiest defensible edge)
- [ ] DMP manual ledger unified into the MarketLoom schema (SQLite) with evidence tiers backfilled
- [ ] **Prediction journal published** (per SWD-1 memo addendum: price, segment, expected 30/60/90-day sales, falsifying signal) — before the gate launches
- [ ] **Demand gate:** free weekly digest live + $29 one-time CSV pack opened for pre-orders

**Tech stack:** Python 3.12, Playwright, SQLite, Buttondown/Resend, Gumroad (pre-orders).

**Success criteria:** ≥2 weeks continuous tri-market data; **≥25 digest subscribers and ≥5 pack pre-orders within 3 weeks.** Miss the gate → stop, run the post-mortem, revisit positioning (this is the falsifying signal working as designed).

**Estimated duration:** 2–4 weeks.

### Phase 2: Analytics & Dashboard v1 (Months 2–3)

**Goal:** turn the ledger into answers — and verify the analytics can actually find known winners.

**Deliverables:**
- [ ] Price ladders, whitespace matrix, rising signals (pandas/Polars)
- [ ] Read-only Next.js dashboard, public pages per marketplace, evidence badges in the UI
- [ ] **Backtest:** run the whitespace finder on weeks-1–2 data; check whether it surfaces categories that produced bestsellers by week 4 — document hits and misses honestly
- [ ] 10-seller pilot recruited from the digest list

**Tech stack:** Python (analytics), Next.js 15 + Tailwind, PostgreSQL migration.

**Success criteria:** a new seller gets a defensible "what to make next" answer in <5 minutes; pilot satisfaction ≥4/5; backtest results published (hits *and* misses) in the digest.

**Estimated duration:** 1–2 months. *Depends on Phase 1 gate passing.*

### Phase 3: Monetization & Breadth (Months 4–6)

**Goal:** revenue on Chris's terms — one-time first.

**Deliverables:**
- [ ] Data packs GA (date-stamped, tier-labeled CSV/Parquet cuts; $29/$79 ladder)
- [ ] Dashboard monetization (tiered subscription only if pack revenue proves the base)
- [ ] Rising-signal alerts (digest upgrade)
- [ ] Category coverage expansion (16-market registry feeds in as collectors mature)

**Tech stack:** as Phase 2 + Stripe/Gumroad checkout, APScheduler for pack cuts.

**Success criteria:** ≥$500/mo revenue equivalent *or* ≥50 one-time pack sales; digest→paid conversion ≥5%; churn/repurchase signal understood.

**Estimated duration:** 1–3 months. *Depends on Phase 2 pilot.*

### Phase 4: API & Agent Surface (Months 7+, optional)

**Goal:** parity with profitable.app's MCP server; serve the agent-builder segment.

**Deliverables:** FastAPI read API; MCP server; BenchData-style subscriptions for tool-builders.

**Success criteria:** only start if Phase 3 revenue exists; otherwise this stays a backlog idea.

**Estimated duration:** open.

---

## 5. Technical Challenges & Solutions

### Challenge 1: Data acquisition legality & fragility — **High**
Etsy's ToS prohibits automated access; its Open API v3 is OAuth-gated and vetted; Creative Market has no API. No enforcement case against an analytics product was found (the eRank/EverBee/Apify/Bright Data ecosystem operates openly in a tolerated gray zone), but tolerance is not a right.
**Approach:** layered sources — official API where granted; purchased data (profitable.app) where sensible; own scanning of public pages rate-limited and respectful; secondary published data with attribution; manual verification for anything Tier-A. The practical risk is **breakage, not litigation** — collectors must degrade gracefully and say so publicly (that honesty is on-brand).

### Challenge 2: Estimate-grade data quality — **High**
All marketplace revenue figures are estimates (EverBee ~80% accuracy; Gumroad publishes nothing). The product's currency is trust.
**Approach:** evidence tiers on every published number (Observed/Reported/Estimated/Unverified), "how we know" methodology pages, confidence language in the digest, and a hard rule: never fabricate precision. This is the differentiation incumbents structurally won't copy — their marketing depends on fake precision.

### Challenge 3: profitable.app competitive response — **Medium**
They move fast, already ship an MCP server, and could add Etsy/Creative Market datasets.
**Approach:** depth on the digital-product triangle (not 13 verticals), the evidence-tier methodology, self-use credibility (we run DMP — we are the customer), and indie pricing including one-time. Check their dataset quarterly (standing task).

### Challenge 4: Demand risk — **High**
Willingness to pay is unproven for the cross-marketplace wedge specifically; incumbents' free tiers cap pricing power.
**Approach:** Phase-1 demand gate *before* building the dashboard; one-time pricing per Chris; near-zero burn (the collector infrastructure exists); the prediction journal fixes expectations before launch so the gate is falsifiable, not vibes.

### Challenge 5: Solo-with-agents bandwidth — **Medium**
One human + coding agents; every hour on the dashboard is an hour not collecting.
**Approach:** read-only dashboard (no auth/paywall complexity until Phase 3); agents own collectors/analytics implementation under plan steps; Chris owns voice, distribution, and decisions; boring architecture on purpose.

---

## 6. Competitive Landscape

| Product | Approach | Limitation | MarketLoom advantage |
|---|---|---|---|
| eRank ($5.99–29.99/mo) | Etsy keyword/analytics, 2M+ claimed users | Etsy-locked; estimate-grade, no methodology labels | Tri-marketplace view; honest tiers; not competing on Etsy keyword depth |
| EverBee ($24.99–99/mo) | Etsy product analytics Chrome extension, 206M listings | Etsy-locked; subscription only | Cross-marketplace; one-time packs |
| profitable.app ($29–49/mo) | Cross-vertical revenue intelligence incl. 3.7M Gumroad products + MCP | No Etsy/CM; no digital-product focus; no evidence methodology | Depth + trust + the actual digital-product triangle; self-use credibility |
| Bright Data / Apify | Raw scraped datasets (~$4.50/1k records) | No curation, no tiers, no seller lens | Curated, tier-labeled, seller-oriented analysis vs raw plumbing |
| Exploding Topics ($39–249/mo) | Generic trend intelligence | Consumer/generic; API $1–4k/mo | Marketplace-specific, evidence-labeled, indie-priced |
| Listadum (~$10/mo) | Etsy shop audits | Etsy-only; indie-scale (~$1.3K ARR) | Validates indie viability; different wedge |
| **Creative Market** | *(nothing — zero third-party analytics)* | Sellers fully blind | Greenfield; our first collector |

**Gap statement (verified 2026-10-05):** no product joins Etsy + Gumroad + Creative Market into one digital-product-seller view; no one sells evidence-tiered estimate data as a trust feature; Creative Market is untouched. The claim is *narrower than "no cross-marketplace index exists"* — profitable.app holds the Gumroad side — which is why positioning is "the only intelligence layer covering the three actual digital-product marketplaces, with honest evidence labels."

---

## 7. Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Data continuity (Phase 1) | ≥2 weeks tri-market, no gaps >24h | ledger `observed_at` audit |
| Digest subscribers (Phase 1 gate) | ≥25 in 3 weeks | Buttondown/Resend stats |
| Pack pre-orders (Phase 1 gate) | ≥5 × $29 | Gumroad |
| Time-to-answer (Phase 2) | <5 min for "what to make next" | pilot task timing |
| Pilot satisfaction (Phase 2) | ≥4/5 from 10 sellers | structured feedback |
| Backtest honesty (Phase 2) | hits *and* misses published | digest issue |
| Revenue (Phase 3) | ≥$500/mo equiv. or ≥50 pack sales | Gumroad/Stripe |
| Digest→paid conversion (Phase 3) | ≥5% | funnel stats |
| Data trust (standing) | 100% of published rows tier-labeled; 0 fabricated numbers | audit query |

---

## 8. Team & Responsibilities

| Role | Responsibility | Who |
|---|---|---|
| Product owner | decisions, positioning, distribution, digest voice, community presence | **Chris** |
| Architecture & implementation | collectors, ledger, analytics, dashboard; plan-step execution | **@zcode** (+ @goose/@opencode/@claude as implementation pods on plan steps) |
| Scheduled collection | extending the daily DMP scan patterns into programmatic collectors | **@hermes** (per his Job Rules pattern) |
| Verification | manual Tier-A checks of high-stakes published numbers | Chris + zcode (shared) |

Honest note: this is a solo-with-agents project sized as such — each phase's deliverables assume ~10–15 focused hours/week, not a startup team.

---

## 9. Open Questions

1. **profitable.app subscription** — recommended: yes, $29–49/mo buys the Gumroad dataset *and* recon on the incumbent. Chris approves spend.
2. **Etsy Open API v3 application** — vetting is limited and slow; apply early in Phase 1 even though Phase 1 can proceed without it.
3. **Name availability** — "MarketLoom" must clear a domain/trademark collision check (loom.com is a large video company; the full compound name is likely distinct but this is unverified). Standing task before any public launch.
4. **Digest platform** — Buttondown (paid, simplest) vs Resend (free tier, more plumbing) vs Notion page + email; pick at Phase-1 start.
5. **Creative Market scraping posture** — zero third-party analytics exists there *possibly because* their ToS is enforced differently; confirm before making CM the flagship edge.
6. **Repo home** — proposed: `C:\Users\user\Documents\Obsidian Vaults\Code\MarketLoom` (standalone git repo, alongside the DMP vault); Chris confirms.

---

## 10. Next Steps

1. **Chris reviews** this document and `TODO/Core/projects/SWD/plans/a.md`.
2. **Prediction journal** (SWD-10) — written and published *before* the demand gate launches, per the standing rule: expected 30/60/90-day sales at $29, the segment, and the falsifying signal.
3. **`todo start SWD.a`** activates the plan; first work items are the profitable.app teardown (SWD-11) and the name check (SWD-12).
4. Phase-1 demand gate (SWD-14) is the checkpoint that decides everything after it — miss it, and the post-mortem, not the roadmap, is the next document.
5. SWD-8 (conjunction analysis, due 2026-10-12) continues independently and may append FRE/CRE-informed ideas to the track folder — append-only.

---

*Track file — append-only. Step-2 evaluation (fact-check of this document, EdgeDeployEvaluation-style) recommended before Phase-2 investment; phases 3–4 are contingent on gates, not commitments.*
