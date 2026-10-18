# TODO + DataframeElephant — Cross-System Protocol

**Version:** 1.6
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
- **Agent-only domain (2026-10-07, chat-approved):** Chris never edits either system's files. All writes are agent-made. His decisions arrive via chat; agents transcribe them into the daily note `## Decisions` (`todo decide`). Questions only Chris can answer are parked with `todo escalate` (⏳ Decisions Queue) and relayed in chat — they block nothing else.
- `@user` is retired as an owner token; every task line is owned by an agent.

## 3. Project Code Registry (as of 2026-10-10)

Canonical source: `TODO/Core/projects/_index.md` (generated). Statuses change; codes never do.

| Code | Name | Status | Purpose / primary location |
|---|---|---|---|
| **SWD** | Software Product (from Artifacts) | planned, high | Select a product from the artifact pipeline → plan A + repo. Bridge between this pipeline and real software. `TODO/Core/projects/SWD/` |
| **RWR** | Roster Work Record | active, high (goal 12) | Nightly evidence record per roster member: reports, closed tasks, artifacts, cron runs, commits. `Code/Hermes Cron Jobs/Roster work Record/` |
| **ARC** | Architect Record | active, high (goal 13) | Evaluation of Chris's own inputs from session transcripts; read by Claude. Plan: `Code/Hermes Plans/SessionReviewAndArchitectRecord.md` |
| **AUT** | Automation & Orchestration | active (goal 14) | Herdr / Oh My Pi and automated workflow targets, each decided by a dated scoped test. |
| **DMP** | Digital Markets and Products | **retired 2026-10-10** | Market research stream; cron paused (not deleted), job archived to `TODO/Legacy folder/Legacy Cron Jobs/DMP/` |
| **FRE** | Freelance Platforms | **retired 2026-10-10** | Research stream (never had a cron); capsule `TODO/Legacy folder/Legacy Goals/FRE/` |
| **CRE** | Content Creator Economy Research | planned | Creator-economy research stream (third leg of the seller/freelancer/creator conjunction; cron deliberately deferred until DMP stabilizes). |
| **CAM** | Coding Agents Market Scan | **retired 2026-10-10** | Scan cron paused, job archived; the roster mirror folded into RWR |
| **DE** | dataframe-elephant | active, high | Maintenance/implementation work inside the dataframe-elephant repo itself. |
| **SYS** | TODO System (this vault) | active | Vault/CLI maintenance. |
| TLM | Telemetry System | **aborted 2026-10-07** (Chris) | Capsule: `dataframe-elephant/Rules and Regulations/Commander Deck/Telemetry/` |
| OT | orange-tomato.com Revival | planned | Website revival. |
| GDEV | NotebookLM + Google Dev Landscape | **retired 2026-10-10** | Capsule `TODO/Legacy folder/Legacy Goals/GDEV/` |
| JEV | Jev / System One Models | **retired 2026-10-10** | Capsule `TODO/Legacy folder/Legacy Goals/JEV/` |
| MCP | MCP Servers Expertise | **retired 2026-10-10** | Capsule `TODO/Legacy folder/Legacy Goals/MCP/` |
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

| Agent | Role | Current assignment (2026-10-15) |
|---|---|---|
| **Chris** | Human owner; decides product picks via chat relay (agents transcribe) | — |
| **@hermes** | **Orchestrating agent — the main force responsible for TODO/Core**; research agent; runs the Roster Work Record | Vault upkeep, research, analysis, decisions, publishing, and cross-domain strategy |
| **@pi** | Active coding agent (pi-coding-agent 1.1.0; Herdr integration current) | Coding team; concrete work routed by project task owners |
| **@omp** | Active coding agent (Oh My Pi 18.10.3; Herdr integration current) | Coding team; concrete work routed by project task owners |
| **@claude** | **Retired 2026-10-15**; the Claude desktop app is uninstalled from the host | Out of roster |
| **@opencode** | Retired 2026-10-13; tool remains uninstalled | Out of roster |
| @zcode | Orchestrating coding agent (built this vault) — retired 2026-10-07 | Out of roster; authority over TODO/Core transferred to @hermes |
| @goose | CLI/desktop coding agent — retired 2026-10-06 | Out of roster |

## 6. TODO Vault Protocol Quick Reference

- **Task grammar:** `- [ ] DE-4 text ⏫ 📅 2026-10-06 @goose` — id `<CODE>-<n>` immutable, never renumbered. One writer per line; check off others' lines only when verifiably done (`✅ YYYY-MM-DD`).
- **Plans:** `projects/<CODE>/plans/<letter>.md`, steps are normal task lines; `todo start DE.a` activates.
- **CLI:** `bin/todo` — `today/add/done/start/plan/report/log/assign/review/sync/projects/agents/inbox/archive`. After any direct file edit: `todo sync`.
- **Reports:** every agent session ends with `todo report <agent> -p <CODE> -s ok|warn|fail -m "…"`; reports live in `reports/YYYY-MM-DD-<agent>[-<CODE>].md`.
- **Decisions:** recorded in the daily note (`daily/YYYY-MM-DD.md`) under `## Decisions`.

## 7. Cross-System Flows (what connects the two)

1. **Market evidence (DMP cron — retired 2026-10-10).** *Historical:* Hermes scanned 3 markets/day into `Product Ledger.md` (append-only, P-####) and filed `Daily/YYYY-MM-DD.md`; the job is paused and archived to `TODO/Legacy folder/Legacy Cron Jobs/DMP/`, and the ledger data stays available for SWD. **Now:** into `Product Ledger.md` (append-only, P-####) and files `Daily/YYYY-MM-DD.md`; task-syncs via `todo log`/`todo report hermes -p DMP`.
2. **Market evidence → ideation.** DMP patterns seed market-seeded brainstorming (Stage 2/DMP-SWD track) with the three targeting fields mandatory per idea.
3. **Ideation → evaluation → pick.** `Evaluation_of_SoftwareIDEAS` rubric produces tiers; top candidates are escalated to Chris (SWD-2) via the chat relay and the agent records the pick with `todo decide` in the daily note.
4. **Pick → Step 2 → plan A.** `FromStep1toStep2` produces the building orientation; SWD-3 turns it into `projects/SWD/plans/a.md`; plan steps execute via the standard task grammar.
5. **Prediction journal (standing rule, SWD-1 memo addendum):** before any code, the picked product gets a one-page falsifiable thesis — price, segment, expected sales at 30/60/90 days, the signal that would prove it wrong; post-mortem regardless of outcome, lessons written back into the protocols.
6. **Learning loop.** Chris's SWD objective: even a $0-revenue product must build the judgment to recognize real prospects — every pick is a calibration rep, and DMP/FRE/CRE data make each rep better instrumented.

## 8. Rules of Engagement for Any Agent

1. Read this file, then the relevant system's constitution (`SYSTEM.md` / `README.md` + protocols) before editing anything.
2. Append-only for reports, logs, ledgers, and artifact track files; archive, never destroy.
3. Use the `bin/todo` CLI for all task operations; run `todo sync` after direct file edits.
4. Protocols under `Rules and Regulations/Protocols/` and `TODO/Core/SYSTEM.md` are law; amendments are **chat-approved by Chris, then applied and logged by an agent** (bump the version, append a change-log line).
5. Cite evidence tiers (Observed/Reported/Estimated/Unverified) when reusing DMP data — estimate-grade numbers are never presented as facts.
6. When in doubt, leave a trace (`todo log "…"`) rather than making an unrecorded decision.

---

*Change log: v1.0 — 2026-10-05, initial. v1.1 — 2026-10-07, agent-only domain (chat-approved): Chris interacts only via chat; `@user` retired; decisions transcribed by agents (`todo decide`); protocol amendments chat-approved then agent-applied. v1.2 — 2026-10-07, roster change (Chris, via chat relay): @zcode retired; orchestrator authority over TODO/Core transferred to @hermes; §5 roster table refreshed, canonical source remains `TODO/Core/agents/_index.md`. v1.3 — 2026-10-09, roster change (Chris, via chat): @pi retired; team = Hermes + Opencode (+ limited Claude desktop); §5 table refreshed.*

*Change log: v1.0 — 2026-10-05, initial. v1.1 — 2026-10-07, agent-only domain (chat-approved): Chris interacts only via chat; `@user` retired; decisions transcribed by agents (`todo decide`); protocol amendments chat-approved then agent-applied. v1.2 — 2026-10-07, roster change (Chris, via chat relay): @zcode retired; orchestrator authority over TODO/Core transferred to @hermes; §5 roster table refreshed, canonical source remains `TODO/Core/agents/_index.md`. v1.3 — 2026-10-09, roster change (Chris, via chat): @pi retired; team = Hermes + Opencode (+ limited Claude desktop); §5 table refreshed. v1.4 — 2026-10-10, retirement pass + roster hold (Chris, chat: "implement steps 0–6"): FRE/DMP/CAM cron jobs paused and their goals retired to `TODO/Legacy folder` (GDEV/JEV/MCP retired with them); CAM's roster mirror folded into RWR; §3 registry updated (RWR/ARC/AUT added as goals 12/13/14); §5 roster table corrected in place and the roster put ON HOLD — no seat granted or removed pending Chris's final announcement; evidence rule (pointers, not impressions) recorded in `TODO/Core/SYSTEM.md`.*

*Change log: v1.5 — 2026-10-13, roster finalized by Chris: Pi and Oh My Pi active; Claude remains limited desktop support; OpenCode retired; §5 refreshed to match TODO/Core, with project-level task ownership left per task line.*

*Change log: v1.6 — 2026-10-15, roster change (Chris, via chat): Claude desktop retired from the roster and uninstalled from the host (winget `Anthropic.Claude`; app data and `~/.claude.json` removed); §5 table refreshed to match `TODO/Core/agents/_index.md`. Reason recorded in `Hermes Notebook/01-MISSIONS/2026-10-15_claude-uninstall-and-roster-removal.md`.*
