# Telemetry System — Research & Recommendation (TLM)

**Date:** 2026-10-05 · **Author:** @zcode · **For:** Chris
**Project:** TLM — Telemetry System (TODO/Core vault) · **Feeds decision:** TLM-1 (scope + DB target, due 2026-10-08)
**Scope asked:** participants = OpenCode, Pi, Goose (Goose already has OpenTelemetry). Constraint: easy to build, efficient, and *more info than tokens*.

---

## TL;DR

All three agents already speak **OpenTelemetry (OTLP)** — Goose natively, OpenCode via a small plugin, Pi via a one-line extension. That means the hard part (instrumentation) is free, and the only real decision is the **receiver**. My recommendation:

> **Phase 1 — Arize Phoenix in one Docker container** as the receiver (single container, OTel-native, UI at `localhost:6006`, zero licence cost), fed by all three agents over `localhost:4318`.
> **Phase 2 — a nightly export from Phoenix into DuckDB** (`telemetry.duckdb`), which is what Goal 1 actually asks for: telemetry that *automatically informs a database* — and the vault's own reports/daily notes join the same DB later (TLM-2).
>
> Runner-up: **Jaeger all-in-one** if you'd rather avoid Docker. Upgrade path: **SigNoz** if you later want one platform for agent + infra telemetry; **Langfuse** if prompt-management/evals become the focus.

Nothing here costs money; everything runs localhost (privacy: telemetry can contain prompt/code fragments — keep it local-only, no cloud ingestion keys).

---

## 1. The supply side — what each participant emits today

| Agent | Built-in? | How to enable | Signals | Content worth having |
|---|---|---|---|---|
| **Goose** | ✅ Yes — native OTel | One env var: `OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318"` (OTLP/HTTP; also settable in goose's config file) | traces + metrics + logs | sessions, latency, tool calls, agent behavior; community-proven against Jaeger+ClickHouse, Dash0, Laminar, MLflow |
| **OpenCode** | ⚠️ Via plugin (native OTLP export is in motion upstream — merged PR, Dynatrace docs claim — but **not** in official docs yet; no `/docs/telemetry` page as of today) | Plugin in `~/.config/opencode/opencode.json` (`"plugin": ["@devtheops/opencode-plugin-otel"]`) + `OPENCODE_ENABLE_TELEMETRY=1`, `OPENCODE_OTLP_ENDPOINT=…`, optional `OPENCODE_OTLP_HEADERS=…` | traces + logs + metrics | per-session token usage, latency, **tool calls**, session performance; pre-built dashboards exist on the receiver side |
| **Pi** | ❌ By design minimal — extension ecosystem instead | `pi install npm:pi-otel` then `/otel start` in a session (alternatives: `pi-otlp`, `@desek/pi-opentelemetry`) | traces (+ optional metrics/logs) | **one trace tree per prompt** (`pi.interaction → pi.turn → pi.llm_request / pi.tool`), full `gen_ai.*` attributes: tokens in/out/**cache**, **cost**, model, finish reasons, tool-call ids, conversation id |

Verification level: Goose and Pi rows are Observed (official docs / primary writeups checked 2026-10-05); OpenCode's plugin wiring is Observed (SigNoz's official guide), the "native export" note is Reported — verify against your installed version before skipping the plugin.

Common denominator: **everything lands as standard OTLP** on one endpoint, so the receiver is swappable without touching the agents again. That is the architectural insurance policy.

## 2. The demand side — receiver options out there right now

| Option | Self-host weight | What you get | Fit for TLM |
|---|---|---|---|
| **Arize Phoenix** ⭐ recommended | **Lowest** — one container (`docker run -p 6006:6006 -p 4317:4317 -p 4318:4318 arizephoenix/phoenix`) | OTel-native trace UI, sessions, LLM-focused attributes, evals later; Python client exports traces as **pandas DataFrames** → perfect feed for DuckDB | Easiest build; UI for humans *and* a clean pipe to the database goal |
| **Jaeger all-in-one** | Very low — single binary/container | Trace waterfall UI only (no metrics/log dashboards) | Best zero-Docker / zero-friction fallback |
| **Aspire Dashboard** | Very low — standalone local viewer | OTLP viewer at `localhost:18888`; pi-otel auto-detects it | Great 10-minute trial, ephemeral storage — not a keeper |
| **SigNoz** | Medium — docker compose (ClickHouse + collector + UI) | Unified traces+metrics+logs, ready-made guides for OpenCode/Claude Code/Codex, dashboards | Pick if you want *one* platform for agents + machine + later cron infra |
| **Grafana LGTM stack** | Medium-high — several containers | Industry-standard dashboards (Grafana charts = VIS-grade visuals) | Pick only if you already want a Grafana stack for other reasons |
| **Langfuse** | **Highest** — Postgres + ClickHouse + Redis + MinIO (~4 cores / 16 GiB recommended) | Richest LLM workbench: traces, evals, prompt management, LLM-as-judge; direct OTLP ingest since v3.22 (`/api/public/otel`) | Overkill for "easy and efficient" today; revisit when evals matter |
| **Roll-your-own (OTel Collector → JSONL → DuckDB)** | Zero infra, moderate build | Full control, exactly Goal 1's shape, no UI | Best as *Phase 2 flavor*, not as the only receiver — you'd hand-build the dashboards |

(Comparison grounded in 2026 vendor docs/community writeups; sources §7.)

## 3. "More info than tokens" — the actual signal inventory

Once wired, the DB answers per session / per day / per agent / per project:

- **Volume & money:** tokens (in/out/cache), **cost in USD**, model + provider per request.
- **Work shape:** sessions, prompts, turns per prompt, tool calls (which tools, durations, error rates, call ids), files/commands touched (agent-dependent).
- **Health:** latency and durations per span, finish reasons, errors/diagnostics, retry patterns.
- **Join keys:** conversation/session ids (agents) + dates/project codes (vault reports, daily notes, task transitions once TLM-2 lands) → "who did what, when, how much" across the whole roster, queryable in DuckDB, plottable by VIS.

That last line is the payoff: cross-agent comparisons (Goose vs Pi vs OpenCode cost-per-completed-task) that no single agent's UI gives you.

## 4. Recommended architecture

```
goose ──────OTLP/HTTP :4318──┐
opencode ───OTLP :4318───────┼──▶ Phoenix (Docker, UI :6006) ──nightly export──▶ telemetry.duckdb
pi (+pi-otel) ─:4318─────────┘                                                         ▲
vault reports/ daily/ task events ── ingest script (TLM-2, later phase) ──────────────┘
```

- **Why Phoenix first:** single-container build cost, OTel-native (no vendor SDK lock-in), human-readable UI on day one, and a DataFrame export path that turns "dashboard tool" into "database feeder" — which is literally Goal 1.
- **Why not Langfuse now:** 4-service stack for features you didn't ask for; revisit at evals stage.
- **Why not roll-your-own only:** you'd rebuild UI and exporters by hand; the hybrid gets both for ~zero extra code.
- **Privacy:** keep every endpoint on `localhost`; spans can embed prompt text/code fragments — never point `OTEL_EXPORTER_OTLP_*` at a cloud ingestion key.

**Gotchas (small but real):** exporters batch — allow 10–30 s before data appears; Goose speaks OTLP/HTTP → use port **4318**; OpenCode's plugin env-var naming varies by plugin — pin one plugin and keep its README; OTel's GenAI semantic conventions are still officially "Development" status, so attribute names may drift (the conversation/session ids we rely on are stable in practice).

## 5. Decision required (TLM-1) — three yes/no questions

1. **Receiver:** Phoenix as recommended? (or Jaeger if no Docker / SigNoz if you want the all-in-one platform)
2. **Docker** (Desktop or Podman) on this machine — acceptable? Phase 1 needs it for Phoenix; Jaeger runs as a bare binary if not.
3. **Sequencing:** agents-only first (recommended), vault-artifact ingest (TLM-2) folded in as Phase 2?

On approval: `todo start TLM.a` runs the drafted plan (`TODO/Core/projects/TLM/plans/a.md`, steps TLM-5…TLM-11) — provision receiver → wire the three agents → verification gate (one live session per agent visible with tokens/cost/tool spans) → DuckDB ledger → per-agent dashboard.

## 6. Cost & footprint summary

All options free (self-host licences: Phoenix Elastic-2.0 free, SigNoz AGPL, Langfuse MIT core, Jaeger/Apache-2.0, Aspire MIT). Disk/RAM: Phoenix ≈ one container, a few hundred MB; Jaeger trivial; SigNoz ≈ 2–4 GiB; Langfuse ≈ 16 GiB recommended. Agent-side cost: one env var (Goose), one plugin + env (OpenCode), one `pi install` (Pi).

## 7. Sources

- Goose telemetry (official): [Telemetry & Observability — Goose docs](https://block-goose.mintlify.app/advanced/telemetry) · [Goose env-vars guide](https://goose-docs.ai/docs/guides/environment-variables) · [Goose + OTel + Jaeger + ClickHouse walkthrough](https://aaif.io/blog/trace-and-analyze-goose-sessions-with-opentelemetry-jaeger-and-clickhouse) · [Dash0: observing Goose](https://www.dash0.com/guides/observing-goose-on-ollama-with-opentelemetry) · [MLflow tracing for Goose](https://mlflow.org)
- OpenCode: [SigNoz official OpenCode observability guide](https://signoz.io/docs/opencode-observability) · [opencode-plugin-otel (npm)](https://www.npmjs.com) · native-export PR discussion (GitHub, opencode repo, PR #5245) · [Dynatrace OpenCode docs](https://www.dynatrace.com)
- Pi: [pi-otel writeup (nikiforovall.blog)](https://nikiforovall.blog) · [pi-otlp (npm)](https://www.npmjs.com) · [Pi extension writeup (prokopov.me)](https://prokopov.me) · [pi repo (badlogic/pi-mono)](https://github.com)
- Receivers: [Phoenix Docker self-hosting](https://arize.com/docs/phoenix/self-hosting/deployment-options/docker) · [SigNoz AI observability](https://signoz.io) · [Langfuse self-hosting](https://langfuse.com) · [Langfuse vs Phoenix comparison (zenml)](https://www.zenml.io) · [12-platform comparison (morphllm)](https://www.morphllm.com)
- Standards: [OTel GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) · [OTLP exporter env-var spec](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter) · [OTel agent-observability best practices](https://opentelemetry.io)

---

*Append-only file — later entries go below, never overwrite. Next vault-side step: Chris decides TLM-1 → `todo start TLM.a`.*


---

# REVISION 1 - 2026-10-05 (same day): no Docker, 16 GB RAM, "lightest or skip"

**Chris's constraint:** Docker is uninstalled and stays uninstalled; the machine runs a lot already; only the lightest option (or nothing) qualifies. This revision supersedes the original recommendation.

## Revised recommendation - Batch Mode (zero resident processes)

The original report missed the cheapest source of all: **all three agents already persist their sessions on this machine.** No receiver, no endpoint, nothing running - a nightly script reads the local stores and writes `telemetry.duckdb`.

| Agent | Local store (verified on this machine 2026-10-05) | Format |
|---|---|---|
| OpenCode | C:\Users\user\.local\share\opencode\opencode.db | **SQLite** (sessions/messages incl. tokens & cost) - DuckDB reads SQLite directly via its `sqlite_scanner` extension |
| Pi | C:\Users\user\.pi\agent\sessions\<project>\<session>.jsonl | JSONL, one file per session, already split per project directory |
| Goose | C:\Users\user\AppData\Roaming\Block\goose\data\sessions (+ `logs`) | JSON session files |

**RAM cost: 0 resident.** The script runs for seconds at night (scheduled after `todo review`, same slot TLM-3 already assumed) and exists otherwise. No Docker, no binaries, no new services - this is the "skip" option that still delivers the database, which is what Goal 1 actually asks for.

What you give up vs. the original OTel design: no live waterfall UI, and local store formats can drift across agent updates (mitigation: the survey step pins exact schemas before the script is written; drift shows up as a failed ingest, not silent corruption). What you keep: tokens, cost, model, tool calls, per-project attribution (Pi is already project-split; OpenCode's DB has the rest), joined with vault reports/daily/task events in one DuckDB.

## If you ever want to *look* at live traces (optional, never resident)

- **Jaeger all-in-one** - single Windows binary (installable via scoop), ~100 MB RAM *while running*, start manually when debugging, close when done. Traces only.
- Phoenix without Docker (`pip install arize-phoenix`) exists but costs several hundred MB and a pile of Python deps - not worth it under this constraint. Keep it parked.

## Vault changes from this revision

- **Plan B drafted** (`TODO/Core/projects/TLM/plans/b.md`, steps TLM-12..16): survey local stores -> ingest script v1 (fulfils TLM-2) -> nightly trigger (folds TLM-3) -> query gate -> optional Jaeger-on-demand.
- **Plan A stays on file unchanged** (steps TLM-5..11, gated on TLM-1) - only relevant if Docker ever returns; superseded in practice by Plan B.
- Decision needed (TLM-1, now simpler): approve **Batch Mode** -> `todo start TLM.b`.
