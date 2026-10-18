# TLM — Local Store Schemas (surveyed 2026-10-05, TLM-12)

> **Human?** This file is the agents' repair manual (exact schemas of each store).
> For your side of the system — how data flows, where to look, Jaeger how-to — read
> `dataframe-elephant\Rules and Regulations\Commander Deck\Telemetry\Jaeger.md`.

Ground truth for `ingest_telemetry.py`. Re-survey if an agent update changes formats —
a failed ingest is the signal to re-check this note.

## 1. OpenCode — `C:\Users\user\.local\share\opencode\opencode.db` (SQLite, read-only)

Rich schema (drizzle-managed). What we ingest:

- `session` (legacy, 21 rows) and `session_v2` (current, 60 rows) — **both have the
  same key fields**: `id, project_id, directory, title, model, agent, cost,
  tokens_input, tokens_output, tokens_reasoning, tokens_cache_read,
  tokens_cache_write, summary_additions, summary_deletions, summary_files,
  time_created, time_updated`. Ingest both, tagged `session_v1`/`session_v2` in a
  `variant` column (ids appear disjoint).
- `project` — `id, name, worktree` for project names.
- Tool calls: table `part`, one row per message part; `data` is JSON — tool parts
  have `$.type = 'tool'`, tool name at `$.tool`, status at `$.state.status`.
  Count per `session_id`.

## 2. Goose — `%APPDATA%\Block\goose\data\sessions\sessions.db` (SQLite, read-only)

- `sessions` (10 rows): `id, name, working_dir, created_at, updated_at,
  total_tokens, input_tokens, output_tokens, cache_read_tokens,
  cache_write_tokens, accumulated_cost, provider_name, model_config_json,
  goose_mode, archived_at`. Model id lives inside `model_config_json`.
- `usage_ledger` (153 rows) — **per-request**: `session_id, created_timestamp,
  model, input_tokens, output_tokens, total_tokens, cache_read_tokens,
  cache_write_tokens, cost, cost_source, is_compaction`. Best source for
  per-request cost/tokens.
- Tool calls: `messages.content_json` is a JSON array of blocks; tool-call blocks
  have `"type": "toolCall"` (also `thinking`, text blocks). Count per session.

## 3. Pi — `C:\Users\user\.pi\agent\sessions\<munged-cwd>\<ts>_<uuid>.jsonl`

One JSONL file per session; directory name munges the project cwd
(e.g. `--C--Users-user-dataframe-elephant--`). Line types:

- `session` — `id, timestamp, cwd` (cwd is the clean project path).
- `model_change` — `provider, modelId`; `thinking_level_change`.
- `message` — `message.role` (system/user/assistant/toolResult), `message.content`
  (list; items with `"type": "toolCall"` = tool calls), and on assistant messages
  `message.usage` = `{input, output, cacheRead, cacheWrite, reasoning, totalTokens,
  cost: {input, output, cacheRead, cacheWrite, total}}` — per-request tokens AND cost.

Note: only one session file existed at survey time (Pi is newly adopted); parser
must tolerate files that end mid-session.

## 4. Vault artifacts (already structured)

- `reports/YYYY-MM-DD-<agent>[-<CODE>].md` → date, agent, project code from filename.
- `daily/YYYY-MM-DD.md` → date only (v1).

## 5. DuckDB target

`C:\Users\user\dataframe-elephant\telemetry.duckdb` — DE repo root (house DB home).
Tables: `agent_sessions` (one row per agent session), `agent_usage` (per-request
rows where available: goose usage_ledger + pi assistant messages), `vault_events`
(reports/dailies). **Idempotency: full reload every run** (sources are tiny —
hundreds of rows; rebuild-from-source beats incremental bookkeeping and is immune
to clock/catch-up issues).

## 6. Jaeger (on-demand live traces — TLM-16)

Installed via scoop 2026-10-05 (v2.21.0; hash check skipped — stale manifest vs
re-released official GitHub asset). Start when debugging, close when done:

```bash
jaeger                          # UI at http://localhost:16686, OTLP gRPC :4317, HTTP :4318
```

Point an agent at it live: `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318` (Goose),
OpenCode `OPENCODE_OTLP_ENDPOINT=http://localhost:4318`, Pi `/otel start`.
Never resident — nothing listens when you close it.
