# exportTelemetryduckdb — Telemetry Export Protocol

**Version:** 1.0 · **Created:** 2026-10-05 · **Owner:** Chris
**Purpose:** standardized markdown exports of `telemetry.duckdb` into the Commander
Deck, so Chris can read the state of the agent system without touching DuckDB, and
exports stay comparable over time.

**Companion protocols:** `AnalyseTelemetryduckdb.md` (analysis rules — its §2 rules
apply to exports too), field manual `Commander Deck/Telemetry/Jaeger.md`.

---

## 1. Destination & format

- **Directory:** `C:\Users\user\dataframe-elephant\Rules and Regulations\Commander Deck\Telemetry\exports\`
  (create it if missing — the exporting agent owns that mkdir).
- **Markdown only.** One file per export. **Never overwrite or edit an existing
  export** — the folder is append-only history; a correction is a new file whose
  header notes which export it supersedes.

## 2. Naming

```
telemetry-export-<scope>-<YYYY-MM-DD>.md
```

- `<scope>`: `daily` | `weekly` | `monthly` | `models` | `projects` | `agents` | a
  kebab-case custom scope.
- The date is the **as-of date** of the export, not the data window (that lives
  inside the file).

## 3. Required structure (in order)

1. **Header block** — exporting agent, as-of timestamp, data window (min/max
   `started_at`), tables used with row counts, date of the last *"TLM nightly
   ingest ok"* trace.
2. **TL;DR** — 3–5 bullets a human reads in 20 seconds.
3. **Data** — markdown tables (per agent/day, model costs, project breakdown — as
   the scope dictates). Include empty agents with "no data yet" rather than omitting
   them; presence/absence is itself telemetry.
4. **Method** — the exact SQL behind each table (fenced blocks).
5. **Caveats** — the absence/NULL notes required by `AnalyseTelemetryduckdb.md` §2.3–4.

## 4. Rules

1. Read-only connection; the nightly ingest remains the only writer to the database.
2. Every number carries its SQL (same rule as the analysis protocol).
3. Exports are **snapshots**: always state the as-of moment; older exports are
   history, not errors — never "fix" them in place.
4. **Frequency:** on demand; a weekly export is suggested at the weekly ritual
   (SYS-7). At most one file per scope per day — don't spam the folder.
5. After exporting: `todo log` the file name, and cross-link from the analysis note
   if one exists.
6. Keep exports lean: aggregate tables, no raw row dumps (privacy rule §2.7 of the
   analysis protocol applies).

## 5. Suggested starter scopes

- **weekly** — per agent per day: sessions, tokens, cost, tool calls; model cost
  table; vault event count. The default digest.
- **models** / **projects** / **agents** — full-history pivots for the respective cut.

## 6. Changing this protocol

Protocols are law; changes only through Chris. Bump the version and append a change
note below.

---

*Change log: v1.0 — 2026-10-05, initial (created on Chris's request after TLM build).*
