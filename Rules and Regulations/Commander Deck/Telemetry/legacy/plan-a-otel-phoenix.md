---
plan: a
title: Plan A — OTel spine → Phoenix receiver → DuckDB ledger
active: false
updated: 2026-10-05
---

# Plan A — Agent telemetry: OpenTelemetry → Phoenix → DuckDB

Wire all three participant agents (Goose, OpenCode, Pi) to emit standard OTLP to one
local receiver (recommended: Arize Phoenix, single Docker container), verify end-to-end
with a hard gate, then feed a DuckDB ledger (`telemetry.duckdb`) nightly — Goal 1's
"telemetry that automatically informs a database". Phase 2 folds the vault-artifact
ingest (TLM-2) + nightly cron (TLM-3) into the same DB, closing TLM-4.

**Gate before any step:** TLM-1 (tasks.md) — Chris picks the receiver and OKs Docker.
Report backing this plan: `dataframe-elephant\Rules and Regulations\Commander Deck\Telemetry\ReportTelemetryToday.md`.

## Steps
- [x] TLM-5 Provision receiver: install Docker (Desktop or Podman); run Phoenix with ports 6006/4317/4318 and a named volume for persistence (or Jaeger all-in-one binary if Chris declines Docker) ⏫ — closed 2026-10-07: obsolete, Batch Mode (Plan B) chosen 2026-10-05, no receiver @zcode ✅ 2026-10-07
- [ ] TLM-6 Wire Goose: set OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318 in goose config/shell profile ⏫ @zcode
- [ ] TLM-7 Wire OpenCode: pin otel plugin in ~/.config/opencode/opencode.json + OPENCODE_ENABLE_TELEMETRY=1, OPENCODE_OTLP_ENDPOINT ▲ @zcode
- [ ] TLM-8 Wire Pi: pi install npm:pi-otel; enable per-session /otel start (or config default) ⏫ @zcode
- [ ] TLM-9 PHASE-1 GATE: one live session per agent visible in the Phoenix UI — spans carry tokens, cost, model, tool calls; else stop and diagnose exporter config ⏫ @zcode
- [ ] TLM-10 DuckDB ledger: nightly export Phoenix traces → telemetry.duckdb (agent_sessions/agent_spans tables; script + schema note in this folder) ▲ @zcode
- [ ] TLM-11 Per-agent dashboard query: tokens/cost/tool-calls per day per agent (DuckDB SQL + optional VIS chart) ▲ @zcode
