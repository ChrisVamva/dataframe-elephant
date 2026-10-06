# Idea: Codes + natural language — stop typing full paths

*Captured 2026-10-05. Status: idea, not yet law. For future projects.*

## The problem

Instructions to agents are dominated by typed directory paths, all day:

> "Go to `C:\...\Rules and Regulations\Protocols`, read and follow FromStagetoDatabases, create `BlahBlahBlah.duckdb` in `...\data`, create `analysis.md` in `...\Obsidian Vaults\Code`."

The work requires human judgement and can't be standardised — but the
**directories are pretty standard**. Split the two: encode the plumbing,
keep the judgement.

## The idea

A tiny shared vocabulary (codes) that agents expand to full paths.
The agent is the parser — codes + natural language is enough, no tooling.

| Code | Expands to |
|---|---|
| `RP` | Rules and Regulations\Protocols |
| `DATA` | dataframe-elephant\data |
| `CODE` | Obsidian Vaults\Code |
| `P1` | protocol: FromStagetoDatabases |
| `+C` / `+R` / `+A` | create / read-and-follow / append |

Example becomes: `P1 + blah.duckdb → DATA, analysis.md → CODE`.

Rules that keep it from rotting:

- The decoder table lives in a file every agent auto-loads (e.g. `AGENTS.md`
  or a `PLACES.md` it points to) — not in the human's head.
- Agents echo the **full expanded path** back in task lines and reports, so
  the canonical record stays diffable and a mistyped code is caught in the log.
- Add codes lazily: any path typed three times earns a line in the table.

## The judgement part: defaults + proposal, not prediction

Don't try to think three moves ahead and predict every judgement call.
Instead: agents know the default destinations and protocol list, the human
only specifies deltas, and the **agent proposes the plan before acting**.
Each correction the human makes reveals a convention → that correction
becomes one new line in the decoder. Corrections are the capture mechanism
for processes that aren't stabilised yet.

## Promotion pipeline

```
ad-hoc instruction → registry line → protocol doc → skill
```

Promote each stage only when it stops changing. "Read and follow protocol X"
becomes a single code; a stabilised protocol becomes a skill that encodes
the read step, defaults and verification.

## Refinement for future projects (the real lesson)

The hesitation above — "I'd have to memorise a large folder structure I
created with no clear patterns" — is the actual root cause. Fix it at
creation time: **structure folders purposefully so codes are intuitive.**

- Simple, patterned layouts: `research/1/2`, `data/raw`, `data/processed`.
- Codes that almost read themselves: `r1` + create → `research/1/structure.md`.
- A recipe runner (`just`) with `just -l` can list the actions so nothing
  needs memorising — but the deeper win is a structure that doesn't need a
  cheat sheet in the first place.
- Retro-fitting codes onto an organically grown tree (like this one) works,
  but memorability is designed in from day one.

## Update 2026-10-05 (2): the consumer is the agent — an MCP vocabulary server

GUI dashboards rejected. The right interface: a small custom **MCP server**
that holds the project vocabulary as structured tools, so agents — not the
human — resolve codes. All six agents (zcode, goose, claude, hermes, pi,
opencode) speak MCP; write the decoder once, every agent gets identical
semantics. Enforcement beats convention: a tool that can only write inside
coded places, with templates applied and canonical paths echoed back.

```
dataframe-elephant/mcp/
├── server.py        # FastMCP, stdio — ~200 lines
├── places.json      # the decoder table: RP, DATA, CODE, P1...
└── templates/       # script.py, analysis.md, new-db.sql skeletons
```

- Resource: project map + protocol list (agents load the vocabulary as data)
- Tool `create(kind, place, name)`: resolve path → apply template → enforce
  naming → return expanded path (echo-back enforced by the tool)
- Optional: `todo` passthrough to the vault CLI
- Generic layer exists off the shelf: official filesystem MCP server
  (@modelcontextprotocol/server-filesystem). The vocabulary layer is custom
  by definition — it is the project's DNA. See also: "Building a custom
  MCP server for Goose.md" (Code vault) — this generalizes that to the fleet.

## Update 2026-10-05 (3): BUILT — v1 is live

The vocabulary server + instruction composer exists: `dataframe-elephant/commander/`.
- **Dashboard** (`start.bat` → http://127.0.0.1:8765): three palettes
  (Folders / Actions / Files) + optional name + judgement sentence.
  Create with no sentence = instant; otherwise it composes one coherent
  message, copies it, and can send it headless to goose.
- **MCP server** (`mcp_server.py`, FastMCP stdio): tools `places`, `create`,
  `compose` — registered in goose config as a stdio extension. Goose
  experiment: ZCode deliberately not wired.
- Decoder table: `places.json` — one JSON line adds a folder. Current codes:
  RP, RR, DATA, SCRATCH, DE, CODE, TD.
- Verified end-to-end 2026-10-05: goose called `places()` and `create()`;
  templated file landed correctly.

## Update 2026-10-05 (4): goose wiring removed at Chris's request

Commander unregistered from goose config (config.yaml) — "delete commander
from Goose for now." The code stays in `dataframe-elephant/commander/`
(dashboard, MCP server, places.json), unwired; re-registering later is one
config block. Dashboard remains available locally via `start.bat`.

## Tools mentioned

- **zoxide** (`z dataframe`): solves the human's own shell navigation, not
  agent instructions. Worth installing; not the main fix.
- **just**: command runner / recipe lister (`just -l`) — a candidate for
  exposing project actions as discoverable recipes.
