# Telemetry Field Manual (Jaeger.md) — what Chris does, where things live

**Date:** 2026-10-05 · **Maintained by:** @zcode · **Project:** TLM (Plan B — Batch Mode)
**Your daily part: nothing.** The system runs itself. This manual is for the two
optional actions (looking at data, watching live traces) and for knowing what to do
if something ever looks wrong.

---

## 1. How data reaches the database (automatic — no action from you)

Every night at **21:45** (not 21:30 — say the word if you want it moved), Windows Task
Scheduler runs task **"TLM Telemetry Ingest"**, which:

1. Reads three read-only sources — the agents were already writing these anyway:
   - OpenCode → `C:\Users\user\.local\share\opencode\opencode.db` (SQLite)
   - Goose → `C:\Users\user\AppData\Roaming\Block\goose\data\sessions\sessions.db` (SQLite)
   - Pi → `C:\Users\user\.pi\agent\sessions\<project>\*.jsonl`
   - plus the vault's `reports/` and `daily/` files
2. **Reloads everything** into `C:\Users\user\dataframe-elephant\telemetry.duckdb`
   (full reload each time — a missed night costs nothing; the next run catches up).
3. Leaves a trace in the vault daily note: *"TLM nightly ingest ok"* (or *FAILED*).

RAM cost while you work: zero. The script lives for a few seconds at 21:45 and exits.
Nothing is installed as a service, nothing listens on any port.

## 2. Where everything lives

| Thing | Location |
|---|---|
| **The database (the point of it all)** | `C:\Users\user\dataframe-elephant\telemetry.duckdb` |
| Ingest script | `TODO\Core\projects\TLM\ingest_telemetry.py` |
| Nightly trigger | Scheduled task "TLM Telemetry Ingest" (21:45 daily, runs `projects\TLM\ingest_task.cmd`) |
| Ingest log (errors land here) | `TODO\Core\projects\TLM\ingest.log` |
| Schemas of the sources (agents' repair manual) | `TODO\Core\projects\TLM\schema-notes.md` |
| Research report + revision | this folder, `ReportTelemetryToday.md` |
| Jaeger (on-demand live traces) | installed via scoop — just type `jaeger` |

Three tables inside the database:
- `agent_sessions` — one row per agent session: agent, project, model, tokens (in/out/cache), **cost USD**, tool-call count, code lines added/removed (OpenCode).
- `agent_usage` — per-request rows (Goose's ledger, Pi's per-message usage): the finest grain of cost/tokens over time.
- `vault_events` — one row per vault report/daily note: date, agent, project code.

## 3. How to look at the data (pick whichever is easiest)

**Easiest — ask an agent.** "Query telemetry.duckdb: cost per agent this week" — any
agent can run DuckDB against it. Zero setup.

**Do it yourself — one-liner (Python is already installed):**

```python
python -c "import duckdb; print(duckdb.connect(r'C:\Users\user\dataframe-elephant\telemetry.duckdb', read_only=True).sql('SELECT agent, COUNT(*) sessions, SUM(tokens_total) tokens, ROUND(SUM(cost_usd),2) usd FROM agent_sessions GROUP BY 1').fetchall())"
```

**Starter queries worth running** (paste into the `sql('...')` above):

```sql
-- tokens + cost + tool calls per agent per day (the Plan-B gate query)
SELECT agent, CAST(started_at AS DATE) day, COUNT(*) sessions,
       SUM(tokens_total) tokens, ROUND(SUM(COST_USD),2) usd, SUM(TOOL_CALLS) tools
FROM agent_sessions GROUP BY 1,2 ORDER BY 2,1;

-- most expensive models overall
SELECT model, COUNT(*) sessions, ROUND(SUM(cost_usd),2) usd
FROM agent_sessions GROUP BY 1 ORDER BY 2 DESC NULLS LAST LIMIT 10;

-- which projects eat the tokens
SELECT agent, project, SUM(tokens_total) tokens FROM agent_sessions
GROUP BY 1,2 ORDER BY 3 DESC NULLS LAST LIMIT 10;
```

(Any DuckDB-capable viewer — e.g. DBeaver — also works; open the file **read-only**.)

## 4. Jaeger — watching an agent live (optional, rare)

Jaeger is the "trace waterfall" viewer: while it runs, an instrumented agent sends
its live traces to it and you see every LLM call and tool call as nested spans with
timings. **Two things to know: it is in-memory (everything vanishes when you close
it) and it is never running unless you start it.**

Your part, when you want it:

1. Open PowerShell, type `jaeger`, leave the window open. (It serves: UI → browser at
   `http://localhost:16686`; OTLP receivers on ports 4317 gRPC / 4318 HTTP — **you
   never visit those ports**, they're for the agents to send to.)
2. Wire the agent you want to watch to it (only needed for the live view — the
   nightly database ingest does **not** use Jaeger at all):
   - Goose: set `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318` before starting it
   - OpenCode: `OPENCODE_OTLP_ENDPOINT=http://localhost:4318` + `OPENCODE_ENABLE_TELEMETRY=1`
   - Pi: inside a session, `/otel start`
3. Use the agent; traces appear in the Jaeger UI (allow ~10–30 s — exporters batch).
4. **Close Jaeger when done** (Ctrl+C in its window). Memory it used is freed; the
   traces are gone by design. Your database is unaffected — it comes from the local
   stores, not from Jaeger.

## 5. What to be careful about

- **Jaeger storage is in-memory** — don't expect traces to survive; don't leave it
  running for days (memory grows with every span). On-demand, then close.
- **Nothing in this system touches the internet.** Keep it that way: never point an
  agent's OTLP endpoint at a cloud URL with an ingestion key — spans can contain
  prompt text and code fragments. Localhost only.
- **Don't move or rename `telemetry.duckdb`** — the script and scheduled task have
  the path hardcoded. Don't hand-edit the DB; it's rebuilt from sources nightly, so
  manual edits wouldn't survive anyway.
- **The ingest runs only while you're logged on.** Machine off/asleep at 21:45 = that
  night is skipped, and the next run reloads everything — no data is lost, only
  delayed. (Logon mode is "Interactive only" by design; it's a personal machine.)
- **Jaeger was installed with scoop's hash-check skipped** (`-s` flag): the scoop
  manifest was stale against Jaeger's re-released official tarball. Source is the
  official CNCF GitHub release over HTTPS — low risk, documented here and in
  schema-notes.md. A future `scoop update jaeger` may fail the same way; same fix.
- **Format drift is the one real failure mode.** If an agent update changes its local
  store format, the nightly run fails and you'll see *"TLM nightly ingest FAILED"* in
  the daily note. That's a loud failure, not silent corruption. See §6.

## 6. When something looks wrong

| Symptom | Meaning | What to do |
|---|---|---|
| Daily note says *"TLM nightly ingest FAILED"* | A source format changed (agent update) or a file is locked | Tell any agent: "TLM ingest is failing — re-survey per schema-notes.md and fix ingest_telemetry.py" |
| No *"ingest ok"* trace for a night | Machine was off/asleep at 21:45 | Nothing — next run catches up |
| Numbers look stale in the DB | You're looking before 21:45 | Ingest runs nightly; or ask an agent to run `ingest_telemetry.py` now |
| Jaeger UI empty | Nothing sent traces while it was open | Wire the agent per §4 step 2 first; Jaeger only shows what arrives while it runs |
| Data missing for one agent | That agent has no sessions yet (Pi is new) — or its store moved | Check the paths in §1; Pi had exactly 1 session at first load |

**Current state at handover (2026-10-05):** 92 sessions loaded (OpenCode 81, Goose 10,
Pi 1); biggest single day so far ≈ 16.2M tokens (OpenCode, 2026-09-30); most expensive
model so far: mistral-medium-latest ($4.36 over 4 sessions).

---

*Append-only. Update this file when the pipeline changes (new agent added, schedule
moved, new table). Last updated 2026-10-05 by @zcode.*
