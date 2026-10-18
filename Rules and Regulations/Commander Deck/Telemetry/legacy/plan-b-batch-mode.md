---
plan: b
title: Plan B — Batch mode: local session stores → DuckDB (no receiver)
active: true
updated: 2026-10-05
---

# Plan B — Batch mode: local session stores → DuckDB

Zero-resident telemetry for Chris's constraint (no Docker, 16 GB RAM, machine already
loaded): all three agents already persist sessions locally — no receiver, no endpoint,
nothing running. A nightly script reads the three stores + vault artifacts and writes
`telemetry.duckdb`. Fulfils TLM-2 (ingest script) and folds TLM-3 (cron) into it;
TLM-4 closes at the dashboard step.

Local stores (verified on this machine 2026-10-05, see Revision 1 of the report):
OpenCode `~/.local/share/opencode/opencode.db` (SQLite — DuckDB `sqlite_scanner`),
Pi `~/.pi/agent/sessions/<project>/<session>.jsonl`, Goose `%APPDATA%\Block\goose\data\sessions\` (JSON).
Report: `dataframe-elephant\Rules and Regulations\Commander Deck\Telemetry\ReportTelemetryToday.md` (Revision 1).

**Gate before any step:** TLM-1 — Chris approves Batch Mode. Plan A (OTel → Phoenix)
stays on file for the day Docker ever returns; superseded in practice by this plan.

## Steps
- [x] TLM-12 Survey local stores: pin exact paths/schemas/fields (tokens, cost, model, tool calls, project attribution) of opencode.db, pi sessions JSONL, goose session JSON → schema note in projects/TLM/ ⏫ @zcode ✅ 2026-10-05
- [x] TLM-13 Ingest script v1: Python + DuckDB reads the three stores + vault reports/daily into telemetry.duckdb (tables: agent_sessions, agent_messages, vault_events); idempotent re-runs (fulfils TLM-2) ⏫ @zcode ✅ 2026-10-05
- [x] TLM-14 Nightly trigger: scheduled task runs ingest after `todo review` slot; failure = todo log line (folds TLM-3) @user ✅ 2026-10-05
- [x] TLM-15 PHASE GATE: one DuckDB query answers tokens + cost + tool-calls per agent per day across all three agents; else fix ingest ⏫ @zcode ✅ 2026-10-05
- [x] TLM-16 Optional, on-demand only: install Jaeger all-in-one via scoop for live waterfall views when debugging — never resident, closed after use ▲ @zcode ✅ 2026-10-05
