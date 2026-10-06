# TODO + DataframeElephant — Cross-System Protocol

**Version:** 1.0 · **Created:** 2026-10-05 · **Owner:** Chris
**Purpose:** the reference point connecting the two systems — the **TODO/Core vault** (task & agent command center) and **dataframe-elephant** (research workspace & artifact pipeline) — so that any agent reading this understands the codes, the structures, and how work flows between them. Read `TODO/Core/SYSTEM.md` and `dataframe-elephant/README.md` for each system's internal constitution.

---

## 1. The Two Systems

| | TODO/Core vault | dataframe-elephant |
|---|---|---|
| **Path** | `C:\Users\user\Documents\Obsidian Vaults\TODO\Core\` | `C:\Users\user\dataframe-elephant\` |
| **Role** | Command center: tasks, plans, projects, agents, reports, daily log | Research workspace: `research/`, artifact generation pipeline, protocols, code |
| **Law** | `SYSTEM.md` + `AGENTS.md` (task grammar is law; CLI preferred; append-only history) | `Rules and Regulations/` (protocols are law; artifacts follow templates) |
| **Automation** | `bin/todo` CLI (`python bin/todo.py`) | Agent skills + protocols; generation is protocol-driven |
| **Generated (never hand-edit)** | `TODAY.md`, `projects/_index.md`, `agents/_index.md` | — |

## 2. The Human

- The owner is **Chris**. Refer to him as **Chris** in all prose, reports, and documents.
- `@user` is a *task-grammar token only* (task-line ownership, `-o user`, `owner:` frontmatter). Do not use it in prose.

## 3. Project Code Registry (as of 2026-10-05)

Canonical source: `TODO/Core/projects/_index.md` (generated). Statuses change; codes never do.

| Code | Name | Status | Purpose / primary location |
|---|---|---|---|
| **SWD** | Software Product (from Artifacts) | planned, high | Select a product from the artifact pipeline → plan A + repo. Bridge between this pipeline and real software. `TODO/Core/projects/SWD/` |
| **DMP** | Digital Markets and Products | planned, normal | Daily market research on digital-product marketplaces. Vault: `Documents\Obsidian Vaults\Code\Digital Markets and Products\` (Job Rules, Market Registry, Product Ledger, Run Log, Daily reports). Executed by **@hermes** cron, daily 11:00 Europe/Athens. |
| **FRE** | Freelance Platforms | planned | Freelance-market research stream (same pattern as DMP, not yet initiated). |
| **CRE** | Content Creator Economy Research | planned | Creator-economy research stream (third leg of the seller/freelancer/creator conjunction; cron deliberately deferred until DMP stabilizes). |
| **CAM** | Coding Agents Market Scan | planned | Coding-agent market research (serves the developer customer-base view). |
| **DE** | dataframe-elephant | active, high | Maintenance/implementation work inside the dataframe-elephant repo itself. |
| **SYS** | TODO System (this vault) | active | Vault/CLI maintenance. |
| TLM | Telemetry System | planned | Telemetry build goal. |
| OT | orange-tomato.com Revival | planned | Website revival. |
| GDEV | NotebookLM + Google Dev Landscape | planned | Landscape research. |
| JEV | Jev / System One Models | planned | Research project. |
| MCP | MCP Servers Expertise | planned | MCP expertise build-out. |
| VIS | Data Visualization Expertise | planned | Expertise build-out. |

**The customer-base conjunction (Chris, 2026-10-05):** DMP (digital-market sellers) + FRE (freelancers) + CRE (content creators) research streams feed **SWD-8**, which synthesizes them into customer-base profiles and tool propositions. Thesis: sellers/freelancers/creators are the customer base for tools; the tool-seller earns more reliably than the activity-seller ("sell shovels").

## 4. The Artifact Pipeline (dataframe-elephant side)

```
research/<domain>/                     ← deep research notes (e.g., Programming Languages)
        │  NovelProductSuggestor.md (protocol)
        ▼
Artifacts/software product ideas/Wave N/Stage 1/Step 1/     ← ideas (5 fields: Name/Principle/Concept/Why novel/Languages)
        │  Evaluation_of_SoftwareIDEAS.md (weighted rubric, formula-strict)
        ▼
   Evaluation doc (e.g., NovelIdeasEvaluation1.md)             ← tiers: T1 ≥7.0, T2 6.0–6.9, T3 5.0–5.9, T4 <5.0
        │  FromStep1toStep2.md (selection + building orientation)
        ▼
Wave N/Stage 1/Step 2/<Product>.md                            ← full building orientation (10-section template)
        │  (+ Evaluation in Step 2/Evaluations/ — fact-check + re-score, e.g., EdgeDeployEvaluation.md)
        ▼
TODO/Core/projects/SWD/plans/a.md                             ← plan A: MVP, repo home, phases (SWD-3, after Chris's SWD-2 pick)
```

**Stage 2 — the DMP-SWD market-seeded track** (new, 2026-10-05): `Artifacts/software product ideas/Wave 1/Stage 2/DMP-SWD/` contains `DMP-SWD brainstorming.md` (10 tool ideas for the seller/freelancer/creator bases, grounded in DMP evidence, with three added targeting fields: Customer base / Evidence / Distribution) and `DMP-SWD Evaluated.md` (rubric evaluation with web-verified competitive research). This track ideates from **market data** (DMP ledger) rather than research folders; both tracks converge at SWD-2 (Chris's pick) and Step 2.

**Standing results (2026-10-05):**
- Wave 1 Stage 1: 12 ideas; Tier 1 = EdgeDeploy (7.4 fact-checked conditional — premise invalidated by Cloudflare Python Workers GA 2026-09-22; **parked**), Convex (unevaluated, name collision with convex.dev), PolyglotDB (8.1 formula-strict; **parked platform candidate**). Step-1 recorded scores were judgment-adjusted; formula-strict recomputation lives in `TODO/Core/projects/SWD/SWD-1-decision-memo.md` §2 (republish = SWD-5).
- DMP-SWD Stage 2: 10 ideas evaluated; top 2 for SWD-2 = **MarketLoom** (recommended — cross-marketplace intelligence; the accumulating evidence-tiered ledger is the moat) and **FirstHundred** (one-time-pricing fit). PulseDigest (8.0, highest raw score) repositioned as MarketLoom's funnel layer; BenchData as one-time CSV packs; BundleBaker → merges into FirstHundred.

**Decision criteria overlay (Chris):** prefer the most defensible build; this batch is sufficient (SWD-8 may append, no new ideation rounds); one-time pricing currently preferred.

## 5. Agent Roster

Canonical source: `TODO/Core/agents/_index.md` (generated) + `agents/<name>.md` cards.

| Agent | Role | Current assignment (2026-10-05) |
|---|---|---|
| **Chris** | Human owner; decides SWD-2 and all product picks | — |
| **@zcode** | Orchestrating coding agent; runs SWD analysis/evaluations, vault bootstrap | SWD-5..9 queue; built the TODO vault |
| **@hermes** | Research agent with cron jobs | Daily 11:00 DMP scan (`Code\Digital Markets and Products\`); slated for FRE-1, CAM-1, GDEV-1, DMP-1/4 |
| @goose | CLI/desktop coding agent | Standby (DE plan A ready) |
| @claude, @opencode, @pi | Coding agents | Standby |

## 6. TODO Vault Protocol Quick Reference

- **Task grammar:** `- [ ] DE-4 text ⏫ 📅 2026-10-06 @goose` — id `<CODE>-<n>` immutable, never renumbered. One writer per line; check off others' lines only when verifiably done (`✅ YYYY-MM-DD`).
- **Plans:** `projects/<CODE>/plans/<letter>.md`, steps are normal task lines; `todo start DE.a` activates.
- **CLI:** `bin/todo` — `today/add/done/start/plan/report/log/assign/review/sync/projects/agents/inbox/archive`. After any direct file edit: `todo sync`.
- **Reports:** every agent session ends with `todo report <agent> -p <CODE> -s ok|warn|fail -m "…"`; reports live in `reports/YYYY-MM-DD-<agent>[-<CODE>].md`.
- **Decisions:** recorded in the daily note (`daily/YYYY-MM-DD.md`) under `## Decisions`.

## 7. Cross-System Flows (what connects the two)

1. **DMP cron → market evidence.** Hermes scans 3 markets/day into `Product Ledger.md` (append-only, P-####) and files `Daily/YYYY-MM-DD.md`; task-syncs via `todo log`/`todo report hermes -p DMP`.
2. **Market evidence → ideation.** DMP patterns seed market-seeded brainstorming (Stage 2/DMP-SWD track) with the three targeting fields mandatory per idea.
3. **Ideation → evaluation → pick.** `Evaluation_of_SoftwareIDEAS` rubric produces tiers; top candidates go to Chris (SWD-2, decision in daily note).
4. **Pick → Step 2 → plan A.** `FromStep1toStep2` produces the building orientation; SWD-3 turns it into `projects/SWD/plans/a.md`; plan steps execute via the standard task grammar.
5. **Prediction journal (standing rule, SWD-1 memo addendum):** before any code, the picked product gets a one-page falsifiable thesis — price, segment, expected sales at 30/60/90 days, the signal that would prove it wrong; post-mortem regardless of outcome, lessons written back into the protocols.
6. **Learning loop.** Chris's SWD objective: even a $0-revenue product must build the judgment to recognize real prospects — every pick is a calibration rep, and DMP/FRE/CRE data make each rep better instrumented.

## 8. Rules of Engagement for Any Agent

1. Read this file, then the relevant system's constitution (`SYSTEM.md` / `README.md` + protocols) before editing anything.
2. Append-only for reports, logs, ledgers, and artifact track files; archive, never destroy.
3. Use the `bin/todo` CLI for all task operations; run `todo sync` after direct file edits.
4. Protocols under `Rules and Regulations/Protocols/` and `TODO/Core/SYSTEM.md` are law; change them only through Chris.
5. Cite evidence tiers (Observed/Reported/Estimated/Unverified) when reusing DMP data — estimate-grade numbers are never presented as facts.
6. When in doubt, leave a trace (`todo log "…"`) rather than making an unrecorded decision.
