---
code: TLM
name: Telemetry System
status: active
priority: high
owner: "@zcode"
path: C:\Users\user\dataframe-elephant\Rules and Regulations\Commander Deck\Telemetry
updated: 2026-10-05
---

# TLM — Telemetry System

## Brief
- Long-term goal 1: a telemetry system that automatically informs a database.
- Natural fit: everything this vault produces (reports, daily notes, task events) plus cron/agent activity lands as rows in a queryable DB (DuckDB is already the house database in DE).

## Outcome
- Cron-safe ingest from vault artifacts → local database; simple queries answer "who did what, when, how much" across agents and projects.

## Plans
- [a](plans/a.md) — OTel spine → Phoenix receiver → DuckDB (gated on TLM-1; parked — needs Docker)
- [b](plans/b.md) — Batch mode: local session stores → DuckDB, zero resident RAM (recommended; awaits TLM-1 approval)

## Notes
- Depends on the vault protocol being followed (it is) — reports/ and daily/ are already structured.
- Research report + Revision 1 (2026-10-05): `C:\Users\user\dataframe-elephant\Rules and Regulations\Commander Deck\Telemetry\ReportTelemetryToday.md` — all three agents already store sessions locally (opencode.db SQLite, pi JSONL, goose JSON); recommended = Batch Mode nightly ingest → telemetry.duckdb, no Docker, 0 resident RAM. TLM-1 decision now just: approve Plan B.
