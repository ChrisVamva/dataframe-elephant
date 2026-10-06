# AnalyseTelemetryduckdb — Telemetry Analysis Protocol

**Version:** 1.0 · **Created:** 2026-10-05 · **Owner:** Chris
**Purpose:** guidelines for any agent asked to analyze the telemetry database — ad-hoc
questions, periodic digests, deep dives — so every analysis is reproducible, honest
about its limits, and leaves the database untouched.

**Companion protocols:** `exportTelemetryduckdb.md` (delivering markdown exports),
field manual `Commander Deck/Telemetry/Jaeger.md`, schema reference
`TODO/Core/projects/TLM/schema-notes.md`.

---

## 1. Scope

- **Database:** `C:\Users\user\dataframe-elephant\telemetry.duckdb`
  - `agent_sessions` — one row per agent session (OpenCode, Goose, Pi): project,
    model, tokens in/out/cache, `cost_usd`, tool-call count, code additions/deletions.
  - `agent_usage` — per-request rows (Goose `usage_ledger`, Pi per-message usage):
    finest grain of cost/tokens over time.
  - `vault_events` — one row per vault report/daily note (date, agent, project code).
- **Triggers:** Chris asks; weekly ritual (SYS-7); follow-up on a failed ingest.

## 2. Rules

1. **Read-only, always.** Connect with `read_only=True`. The only writer to this
   database is the nightly ingest (21:45, task "TLM Telemetry Ingest"). Never create
   tables, views, or "helper" columns in it.
2. **Freshness check first.** Before analyzing, confirm the last *"TLM nightly
   ingest ok"* trace in the vault daily note (or run the ingest manually if Chris
   wants same-day data), and state the data window (min/max `started_at`) in the
   analysis header. Stale data is fine if declared; silent staleness is not.
3. **Absence ≠ zero.** No rows for an agent/date means *no data* (agent unused,
   machine off, store absent) — never report it as "0 usage". Known edges: Pi data
   begins 2026-10-04; OpenCode tool-call counts are NULL before mid-September 2026;
   Goose has no reasoning-token column.
4. **NULL ≠ 0.** `cost_usd` NULL = the agent didn't record a cost (unknown); a free
   model recording $0.00 = "recorded $0". Phrase accordingly.
5. **Reproducibility.** Every number in an analysis carries the SQL that produced it
   (inline fenced block or appendix). A number without its query doesn't ship.
6. **Grain discipline.** State which table backs each figure; don't mix session
   grain (`agent_sessions`) with request grain (`agent_usage`) in one column.
7. **Privacy: aggregate first.** The database holds no prompt/message content by
   design — don't add sources that do, don't republish per-session raw rows in
   shared artifacts, and never send telemetry to a cloud service. Analyses stay on
   this machine / in the vault.
8. **Honest limits.** This is one machine, one user, batch-grain data. It answers
   *who / what / how much / when*. It cannot answer latency or waterfall questions —
   that is Jaeger's job, live only (see Jaeger.md §4).
9. **Output home.** Analyses live in `Commander Deck/Telemetry/` as
   `TelemetryAnalysis-<topic>-<YYYY-MM-DD>.md` — append-only, one file per analysis,
   never rewritten. (Markdown exports for Chris follow `exportTelemetryduckdb.md`
   into `Telemetry\exports\` instead.) Agent-internal summaries can go through
   `todo report` into the vault.
10. **Leave a trace.** `todo log` (or `todo report`) with the analysis path when done.

## 3. Standard analysis header

```markdown
# Telemetry Analysis — <topic>
**Date:** YYYY-MM-DD · **By:** <agent> · **Data window:** YYYY-MM-DD → YYYY-MM-DD
**Last ingest trace:** YYYY-MM-DD ("TLM nightly ingest ok")
**Tables used:** agent_sessions (N rows in window), …
**Caveats:** <e.g. Pi has 1 session; OpenCode tools NULL before 2026-09>
```

## 4. Red flags — check before trusting any number

- A *FAILED* ingest trace, or an `ingest.log` with recent entries → fix data first
  (re-survey per `schema-notes.md`), analyze after.
- A day gap during a week Chris remembers working → machine was off/asleep at
  21:45; rerun ingest before concluding "no activity".
- Totals that mix free and paid models — always show cost alongside tokens, never
  tokens as a proxy for cost.

## 5. Changing this protocol

Protocols are law; changes only through Chris (per `TODO+DataframeElephant.md` §8).
Bump the version and append a change note below.

---

*Change log: v1.0 — 2026-10-05, initial (created on Chris's request after TLM build).*
