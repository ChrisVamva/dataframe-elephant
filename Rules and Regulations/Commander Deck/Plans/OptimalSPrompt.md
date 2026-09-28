---
modified: 2026-09-28T12:30:00+03:00
---

# Optimal Prompt System for dataframe-elephant

## 1. Purpose

This document proposes the prompt system for this project: where prompts live, what
they contain, how they stay consistent with `Protocols/`, how dispatch data enters
them, and how prompt versions are validated and improved. It consolidates the
research collected in
`C:\Users\user\Documents\Obsidian Vaults\Code\Prompts and Research Frameworks`
(POML, DSPy, automatic prompt optimizers, Python-native options, Prompt example 1)
and applies it to the actual constraints of this workspace.

## 2. What "optimal" means for this project

The prompts in this repo are not invoked through an LLM API from Python. They are
Markdown files read by AI coding/research agents (Cline, Kiro, VS Code) that then
write paste-ready Stage 2 rows and run the repo's verification commands. The
optimal system therefore optimizes for:

1. **Gate-passing outputs** — dossiers that pass `Protocols/Research-Evaluation.md`
   and `Protocols/FollowUpResearch.md` checks on the first or second pass.
2. **Paste-ready write-backs** — output tables matching Stage 2 schema shapes
   (claim rows need `claim` + `claim type` + `confidence`; source rows must be
   atomic single-URL rows) so `scripts/import_stage2.py` and
   `src/ingest_citations.py` accept them without schema-drift warnings.
3. **Zero rule drift** — evidence rules, claim taxonomy, and gate definitions exist
   in exactly one place; prompts reference them instead of restating them.
4. **Determinism and auditability** — consistent with the repo's posture:
   reproducible builds, content-derived IDs, warnings never silent.
5. **Low tooling cost** — `requirements.txt` is `duckdb pytest hypothesis
   cryptography`; the venv is Python 3.13.12 with no `jinja2` and no `poml`.
   Any system proposed here must work with zero new dependencies first.

**Non-goals:** a programmatic prompt-optimization pipeline (DSPy/SAMMO class) and
any LLM dependency in `requirements.txt`. Both are deferred to Phase 4 behind an
explicit trigger (see §11).

## 3. Current inventory and findings

| Asset | Role today | Observed defect |
| --- | --- | --- |
| `Commander Deck/Active/prompts/Research Prompt.md` | Wave 1 research brief (nine lenses, evidence rules, deliverable) | No gate self-check section at all; evidence rules duplicated verbatim in three files |
| `Commander Deck/Active/prompts/FollowUpPrompt.md` | Wave 2 dispatch (Track A/B/C, RQ tables, scores) | Cites "Gate A scope, Gate E falsification" — but Research-Evaluation Gate E is *completeness and counterevidence*; falsifier checking is Gate B of `FollowUpResearch.md` |
| `Commander Deck/Active/prompts/NextResearchPrompt.md` | Batched execution protocol (Batches 1–4) | Declares "Quality Gates (Protocols/Research-Evaluation.md): Gate A Scope, B Falsifier, C Provenance, D Method, E Write-Back Integrity" — Research-Evaluation defines **A–F** with different names; B is source quality, C is claim/citation alignment, E is counterevidence, F is data readiness |
| `Commander Deck/Active/prompts/The components to investigate.md` | Lens reference table + diagrams | Reference material mixed into the prompts folder with no status/version marker |
| `Protocols/Research-Evaluation.md` | Evaluation gates A–F (item evaluation) | — |
| `Protocols/FollowUpResearch.md` | Question-acceptance gates A–D (scope, falsifier, provenance, score) | Same letters, different meanings than Research-Evaluation — the root cause of the collision above |

Three concrete problems follow from this inventory:

- **P1 — Gate identity collision.** Two protocols both use bare letters A–D/F with
  different meanings, and both dispatch prompts have invented local gate names
  while claiming protocol provenance. An agent cannot know which "Gate E" a
  self-check refers to.
- **P2 — Rule triplication.** Evidence rules, claim taxonomy
  (`documented fact` / `reported signal` / `inference` / `recommendation`), and
  verification commands are copy-pasted across the three prompts and
  `AGENTS.md`. Editing one leaves the others stale (already visible: command
  blocks and gate names disagree).
- **P3 — Dispatch data frozen into prose.** `NextResearchPrompt.md` and
  `FollowUpPrompt.md` hard-code RQ tables, scores, URLs, and the `S5`/`S6` alias
  resolution. `scripts/formulate_research_questions.py` regenerates exactly this
  data into `research/processed/FollowUps/` — when the agenda changes, the
  prompts silently lie. `NextResearchPrompt.md` §2 ("Why the Previous Prompt
  Failed") documents three failure modes that are all instances of P1–P3.

## 4. Diagnosis: every prompt mixes three kinds of content

| Content class | Example | Correct home |
| --- | --- | --- |
| **Standing rules** | Evidence tiers, claim taxonomy, gate definitions, confidence rubric | `Protocols/*.md` only; prompts *reference* |
| **Task definitions** | Deliverable sections, dossier/table shapes, quality bar, role statement | Shared **partials** in a prompt library, composed into templates |
| **Dispatch data** | RQ lists, scores, batch membership, URLs, alias targets | **Generated** from `ResearchAgenda.md` / DuckDB at dispatch time |

The optimal system separates these three classes. Everything else (versioning,
validation, evaluation) exists to keep the separation true over time.

## 5. Proposed architecture: a four-layer prompt system

```
Layer 0  Protocols (rules — single source of truth)
         Protocols/Research-Evaluation.md · Protocols/FollowUpResearch.md · AGENTS.md
              ▲ referenced by, never duplicated in
Layer 1  Prompt library (task definitions — reusable partials + templates)
         prompts/lib/ partials · prompts/templates/
              ▲ composed with
Layer 2  Dispatch (generated context — RQ batches from the agenda/DB)
         prompts/dispatch/ (build artifacts, regenerated per session)
              ▲ validated by
Layer 3  Verification & evaluation (deterministic checks + scored loop)
         src/tests/test_prompts.py (lint) · evals/ golden set · gate self-checks
```

### Layer 0 — Protocols stay the only place rules live

- Prompts **cite** gate IDs instead of renumbering them (see §6 for the fix).
- No evidence rule, claim-type list, or confidence rubric is ever inlined in a
  prompt; a prompt says "apply `Protocols/Research-Evaluation.md` §2–§5" and
  carries only a one-line reminder of intent.

### Layer 1 — Prompt library (new directory `prompts/` at repo root)

The root `README.md` already reserves `prompts/` for "Reusable LLM prompts and
templates" but the directory does not exist; the actual prompts live under
`Commander Deck/Active/prompts/` with no status, version, or ownership markers.
Proposed layout:

```
prompts/
├── README.md                    # index, lifecycle states, how to dispatch
├── lib/                         # Layer 1: partials (the reusable atoms)
│   ├── role_research_agent.md   # role statement (from Research Prompt §Role)
│   ├── evidence_rules.md        # pointer + 6-line summary of Eval §2; NOT a copy
│   ├── claim_taxonomy.md        # the four claim types + confidence rubric pointer
│   ├── deliverable_brief.md     # the 7-section research brief shape
│   ├── deliverable_dossier.md   # FollowUpResearch §5 dossier spec + patch shapes
│   ├── quality_bar.md           # closing standard (Eval §10 wording)
│   └── verification.md          # canonical test/import commands (single copy)
├── templates/                   # Layer 1: composed prompt skeletons
│   ├── research_brief.md        # = Research Prompt, partials referenced
│   ├── followup_dispatch.md     # = FollowUpPrompt, dispatch tables externalized
│   └── next_research.md         # = NextResearchPrompt, batches externalized
└── dispatch/                    # Layer 2: generated, per-session (gitignored or committed)
    └── 2026-09-28_wave2.md      # template + injected RQ table from ResearchAgenda.md
```

**Format decision — Markdown, not POML, for now.** POML (Microsoft, `pip install
poml`, v0.0.8, Python 3.9+) is the strongest candidate for structured prompts:
semantic components (`<role>`, `<task>`, `<example>`, `<output-format>`), data
tags (`<document>`, `<table>`, `<img>`), a CSS-like stylesheet separating content
from presentation, `{{ }}` templating with loops/conditionals, a Python SDK
(`poml.poml(path, context, format="openai_chat")` renders straight to provider
message dicts), and a VS Code extension with live preview. It is the right tool
**when prompts become code** — i.e. when a script calls an LLM API. Today prompts
are read by agents as files, the venv lacks `poml`, and a ~30 MB dependency
conflicts with the minimal, deterministic posture. Decision: keep Markdown
partials with `<!-- include: lib/x.md -->` markers resolved by a small
compositor; re-evaluate POML at the Phase 4 trigger (§11).

### Layer 2 — Dispatch data is generated, never hand-copied

`scripts/formulate_research_questions.py` already produces the RQ table, scores,
gap codes, and wave packs. The dispatch prompt should be assembled, not edited:

1. Take `prompts/templates/followup_dispatch.md`.
2. Inject the P1/P2 rows from `research/processed/FollowUps/ResearchAgenda.md`
   (or query `data/citations.duckdb` view `next_research_candidates`) for the
   selected tracks.
3. Write the session prompt to `prompts/dispatch/<date>_<wave>.md`.

This kills the failure class recorded in `NextResearchPrompt.md` §2 (stale
hard-coded batches, opaque `doc_cbce9d82fff1c44cb45a5063` hash): the generator
resolves the hash from the DB instead of narrating it in prose. A compositor
(`scripts/assemble_prompt.py`, stdlib only — `pathlib` plus simple
`{{var}}` substitution, no Jinja2 required) keeps assembly reproducible, lives in
`scripts/` beside the other thin CLIs, and is covered by `src/tests/`.

### Layer 3 — Verification and evaluation

Two tiers, following the MVES idea from *"When Generic Prompt Improvements Hurt"*
(arXiv:2601.22025): cheap deterministic checks first, scored judgment only where
determinism runs out.

**Tier 1 — deterministic prompt lint (no LLM; a pytest file):**

- every `<!-- include: -->` target resolves;
- no bare gate letter anywhere — qualified IDs only (see §6);
- evidence-rule, claim-type, and command blocks appear only in `lib/`, never in
  templates (hash check fails on re-introduced duplication);
- every file path named in a prompt exists (catches the `Wave2_*.md` and
  `doc_…` dead-reference class);
- verification commands in prompts match `AGENTS.md` verbatim.

**Tier 2 — output evaluation (Define → Test → Diagnose → Fix per wave):**

- **Golden set:** freeze 3–5 already-accepted dossiers (e.g. RQ-001 boundary,
  RQ-023 atomic source split) under `evals/golden/` as regression cases.
- **Automated checks per dossier:** required sections present; every material
  claim row has type + confidence + evidence + falsifier; source rows are
  single-URL; provenance fields (URL, publisher, publication date, access date)
  non-empty; table shape matches the Stage 2 schema; the paste-ready patch parses.
- **LLM-as-judge only for what scripts cannot check** (boundary quality,
  overstatement, counterevidence searched), with the paper's documented failure
  modes as guardrails: position bias, verbosity bias, self-preference, style
  bias, instruction leakage (rubric-hacking). Judge anonymized orderings, keep
  the rubric out of the judged text, prefer relative comparisons to absolute
  scores.
- **Promotion gate:** a template version is promoted only if it beats the active
  one on the golden set — the version-gating rule `evx` implements (file-native
  `cases/*.json` + `system_prompt.j2` + `user_prompt.j2` + `eval.md` criteria,
  deterministic cycles; `pip install evx`, Python ≥ 3.12 ✓ on this venv). Log
  results to `data/prompt_evals.jsonl` (gitignored) so waves stay comparable.

## 6. Fix P1 now: canonical gate identifiers

Adopt qualified gate IDs everywhere (prompts, protocols, self-checks):

| ID | Source | Meaning |
| --- | --- | --- |
| `RE:Gate A` … `RE:Gate F` | `Protocols/Research-Evaluation.md` §4 | question/scope → source quality → claim alignment → method → counterevidence → data readiness |
| `FU:Gate A` … `FU:Gate D` | `Protocols/FollowUpResearch.md` §6 | scope → falsifier → provenance → score coverage |
| `WB:1` … `WB:n` | write-back integrity checklist (new, lives in `lib/verification.md`) | schema shape, single-URL rows, import + test commands green |

Migration (no protocol text changes — only references are repaired):

1. `NextResearchPrompt.md` §3 re-labels its five "quality gates" as
   `FU:Gate A/B/C` + `RE:Gate D` (method) + `WB:1` and drops the false claim
   that they come from Research-Evaluation's A–E.
2. `FollowUpPrompt.md` corrects "Gate E falsification" → `FU:Gate B` (falsifier)
   and "Gate D scores" → `FU:Gate D`.
3. `Research Prompt.md` gains the missing self-check line: "report `RE:Gate A`–
   `RE:Gate F` results per lens."

This is a ~30-minute edit that removes the largest ambiguity in the current
system, and Tier 1 lint (§5) prevents regression.

## 7. Anatomy of a template (the standard all prompts follow)

Every template in `prompts/templates/` uses the same section order — this is the
skeleton distilled from `Prompt example 1.md`, `Research Prompt.md`, and
`NextResearchPrompt.md`, which already converge on it informally:

1. **Frontmatter** — `id`, `version`, `status` (`draft` / `active` /
   `superseded`), `protocol_refs`, `generated_from` (for dispatch files),
   `partial_list`.
2. **Role** → 3. **Objective** → 4. **Scope / batches (dispatch only)**
   → 5. **Evidence rules** (include marker, never a copy)
   → 6. **Deliverable shape** (include marker + schema tables)
   → 7. **Verification** (include marker; commands identical to `AGENTS.md`)
   → 8. **Quality bar** (include marker).
3. A **self-check block** naming qualified gate IDs — mandatory, not optional.

Rules for authors: one idea per section; every cross-reference is a repo-relative
path; numbers (counts, scores, URLs) belong to dispatch data, never to a
template; `status: superseded` files move to `prompts/archive/` rather than being
deleted (same no-silent-overwrite principle as `Protocols/Research-Evaluation.md`
§9).

## 8. Tooling survey and why (research summary)

Sources: the vault folder `Prompts and Research Frameworks` plus follow-up
verification performed 2026-09-28 (PyPI, official docs, arXiv).

| Tool | What it offers | Verdict for this project |
| --- | --- | --- |
| **Markdown partials + compositor** (chosen) | Zero deps, agent-readable, diff-friendly, matches repo posture | **Adopt — Phases 1–2** |
| **POML** (Microsoft, v0.0.8) | Structured markup, stylesheets, templating, Python SDK, VS Code preview; arXiv:2508.13948 | **Hold** — revisit when prompts are rendered by code (Phase 4 trigger) |
| **evx** (`ev` CLI, v0.1.3.3) | File-native eval loop: JSON cases + Jinja2 prompt templates + `eval.md` criteria, deterministic cycles, version gating; Python ≥3.12 | **Adopt for Tier 2** once a golden set exists and an API key is available; it fits the file-native, version-gated philosophy already used for the DB |
| **SAMMO** (Microsoft Research) | Symbolic prompt programs, beam-search mutation over Markdown prompts, compression | Watch — useful only after metrics exist |
| **DSPy** (Stanford) | Program-not-prompt: signatures, modules, optimizers (BootstrapFewShot, MIPROv2, GEPA); heavy abstraction | **Reject for now** — would require rewriting agent-facing Markdown prompts as Python programs; no metric yet to compile against |
| **Opik Agent Optimizer / promptolution / Promptline / MLflow optimize** | Algorithmic prompt search, statistical promotion gates | Reject for now (same reason: no dataset/metric; revisit after golden set) |
| **flompt** | Visual block editor in browser extensions | Optional design aid only; contributes nothing to the repo |
| **arXiv:2601.22025 (MVES)** | Define→Test→Diagnose→Fix loop, tiered minimum eval suite, golden sets, LLM-judge failure modes | **Adopt the method** — it is the backbone of Layer 3 |
| **Anthropic engineering guidance** (tool/prompt iteration) | Prototype → evaluate → let the agent improve against the eval | Adopt the discipline: never accept a prompt edit that wasn't measured |

Key research takeaways applied here: (a) generic "improved" prompt recipes can
*degrade* task behavior — measure, don't assume; (b) evaluation suites should be
minimum-viable and tiered (deterministic first); (c) structure (POML-style
components) pays off when prompts are programmatically rendered; (d) optimizers
need a dataset and a metric before they need a framework.

## 9. Adoption roadmap

**Phase 0 — Correct the record (no tooling, ~30 min)**
Fix the gate-ID collisions in the three existing prompts (§6). Immediately
removes ambiguity for any agent dispatched today.

**Phase 1 — Library skeleton (half a day)**
Create `prompts/{README.md,lib/,templates/,dispatch/,archive/}`; migrate the
three prompts into templates; extract the seven partials; move
`The components to investigate.md` to `prompts/lib/lens_reference.md`. Keep
`Commander Deck/Active/prompts/` as a thin index that links to the library —
the Commander Deck stays the operational layer (plans, problems, dispatch),
`prompts/` becomes the asset layer.

**Phase 2 — Compositor + Tier 1 lint (one day)**
`scripts/assemble_prompt.py` (stdlib only) plus
`src/tests/test_prompts.py` implementing the five lint rules of §5. Wire into
the existing command `.\.venv\Scripts\python.exe -m pytest src/tests -q`.

**Phase 3 — Golden set + Tier 2 eval (one wave later)**
Freeze 3–5 accepted dossiers as golden cases; add deterministic output checks;
run one Define → Test → Diagnose → Fix cycle on the dispatch template; only then
introduce `evx` (needs an API key in `.env`, which is already gitignored for
`ARCHIVE_PASSPHRASE`).

**Phase 4 — see §11 (conditional, explicit trigger only).**

## 10. Decisions and trade-offs (explicit)

- **Markdown over POML today** — prompts are consumed by agents as files; POML's
  benefits (stylesheets, SDK rendering) start mattering only at the API-call
  boundary. Cost accepted: we hand-roll a trivial compositor.
- **Qualified gate IDs over renumbering protocols** — changing protocol text
  would ripple through every document citing it; repairing references is smaller
  and safer. Cost accepted: identifiers look less pretty.
- **Deterministic lint before LLM judging** — mirrors the repo's entire
  deterministic posture (`stable_id`, no fuzzy matching, temp-file + atomic
  replace). Cost accepted: boundary *quality* stays unmeasured until Phase 3.
- **Dispatch files are generated artifacts** — regenerable, may be gitignored;
  templates and partials are the reviewable source. Cost accepted: one more
  directory.
- **No new runtime dependencies in Phases 0–3** — `requirements.txt` unchanged
  until Phase 4; `evx` at Phase 3 is an optional dev tool, never an import of
  `src/`.

## 11. Phase 4 — conditional future (explicit trigger)

**Trigger:** the repo starts calling an LLM API from a script (automated dossier
drafting, LLM judge scoring, or extraction assistance). Not before.

When the trigger fires, in this order:

1. **POML** — move templates to `.poml` with `poml` in `requirements.txt`;
   render via `poml.poml(path, context, format="openai_chat")`; keep the
   stylesheet to switch verbosity between dispatch and evaluation modes; use the
   VS Code extension for previews while editing.
2. **evx Tier 2 automation** — `ev run` against the golden set with criteria in
   `eval.md` mapped from the dossier checks; rely on its version gating so a
   regression can never replace the active template.
3. **DSPy / optimizers** — only if a stable metric exists after steps 1–2.
   DSPy's signatures (`question -> boundary`) replace Markdown role/objective
   sections only for the *scripted* path; agent-facing prompts stay Markdown.

## 12. Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Two homes for prompts (`prompts/` vs Commander Deck) confuse operators | Commander Deck keeps only links + session dispatches; `prompts/README.md` is the index of record |
| Partials drift from protocol wording while summarizing | Partials hold pointers + ≤6-line reminders; lint fails on a partial that restates a full rule list |
| Golden set too small → overfitting to 3–5 cases | Rotate one golden case per wave; record the selection rule (one per gap code) in `evals/golden/README.md` |
| LLM judge rubber-stamps outputs | Judge only qualitative axes, anonymized orderings, rubric excluded from judged text (MVES guardrails) |
| Prompt edits bypass the loop under time pressure | Tier 1 lint runs inside `pytest`, which AGENTS.md already mandates per session |
| Dispatch generation silently drops RQs | Generator prints counts (like `run_formulation` does) and fails loudly on a mismatch with the agenda totals |

## 13. Definition of done

The system exists when all five hold:

1. No template contains a bare gate letter or a copied evidence-rule block —
   enforced by a test that fails before the fix and passes after.
2. A dispatch prompt regenerates from `ResearchAgenda.md` with one command.
3. The three legacy prompts live in `prompts/templates/`; the Commander Deck
   folder holds an index and current session dispatches only.
4. A golden set of ≥3 dossiers exists with recorded scores in
   `data/prompt_evals.jsonl`.
5. `.\.venv\Scripts\python.exe -m pytest src/tests -q` stays green, including
   the new prompt tests.

---

**Sources consulted.** Vault notes: `DSPy.md`, `POML Documentation.md`,
`🤖 Automatic Prompt Optimizers.md`, `🐍 Other Python-Native Options for Your
Stack.md`, `Prompt example 1.md`. Repo: `AGENTS.md`, `README.md`,
`Protocols/Research-Evaluation.md`, `Protocols/FollowUpResearch.md`,
`Protocols/Hook-Based-Auto-Trigger-Extraction.md`,
`scripts/formulate_research_questions.py`, `Commander Deck/Active/prompts/*`.
External (verified 2026-09-28): microsoft.github.io/poml (overview, quickstart,
components, Python SDK), PyPI `poml` 0.0.8 and `evx` 0.1.3.3,
microsoft.github.io/sammo, DSPy README (stanfordnlp/dspy), arXiv:2601.22025
*When Generic Prompt Improvements Hurt* (MVES, golden sets, LLM-judge failure
modes), anthropic.com/engineering *Writing effective tools for agents*.
