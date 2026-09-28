---
modified: 2026-09-28T15:00:00+03:00
---

# Maintaining Prosperity — how this workspace does not repeat its mistakes

## Status

Mandatory for every person, agent, or automation that edits prompts, protocols,
commands, or research artifacts in `dataframe-elephant`. This document is the
recurrence-prevention contract. The design rationale lives in
`Commander Deck/Active/Plans/OptimalSPrompt.md`; the enforcement lives in
`src/tests/test_prompts.py`.

## 1. What prosperity means here

A later agent can open this workspace and find: **one source of truth for every
rule, one copy of every reusable block, prompts that are assembled instead of
copied, and a green test suite that proves all three.** Prosperity is not the
absence of change — it is change that leaves no stale twin behind.

## 2. The failures we refuse to repeat

| # | Failure that actually happened | Where it is recorded | Cost |
| --- | --- | --- | --- |
| F1 | **Gate-identity collision.** Two protocols use bare letters A–F / A–D with different meanings; prompts invented their own "Gate A–E" while claiming protocol provenance ("Gate E falsification" — no such gate exists). | `Protocols/Research-Evaluation.md` §4 vs `Protocols/FollowUpResearch.md` §6 vs the former dispatch prompts | Agents self-checked against the wrong bar; "verified" dossiers were unverifiable |
| F2 | **Rule triplication.** Evidence rules, the claim taxonomy, and verification commands were copy-pasted across three prompts and `AGENTS.md`, and the copies drifted (gate names and test commands already disagreed). | Former `Commander Deck/Active/prompts/*` | Editing one copy left the others lying; nobody could say which text was authoritative |
| F3 | **Frozen dispatch data.** RQ tables, scores, URLs, and the `doc_cbce9d82fff1c44cb45a5063` hash were hand-copied into prompts while `scripts/formulate_research_questions.py` regenerates exactly that data. An agent once web-searched the local doc hash and stalled. | Former `NextResearchPrompt.md` §2 ("Why the Previous Prompt Failed") | Prompts silently contradict the agenda; sessions waste turns on dead ends |
| F4 | **Dead references.** Bare filenames (`Wave2_Entity_Boundaries.md`) with no path, and links to files that no longer exist. | Former `FollowUpPrompt.md` inputs list | Agents cannot find inputs; they improvise or stall |
| F5 | **Unmeasured prompt edits.** Prompt "improvements" were accepted with no lint and no golden set — failures were only diagnosed after the fact, in prose. | Same §2 table above | Regression roulette; every wave re-learned the same lesson |
| F6 | **Operational hazards (carried forward).** Non-atomic rebuilds, silent warnings, an archiver that deletes sources after roundtrip, derived artifacts at risk of being committed. | `Commander Deck/Active/Problems/Report1.md` (F1–F15), `AGENTS.md` gotchas | Data loss and untraceable state — the same class of preventable surprise |

## 3. Standing rules (the contract)

Each rule names what it prevents and how it is enforced. Enforcement that says
"lint" is a test in `src/tests/test_prompts.py`; it fails the build.
Numbering note: **R1–R12** below are the *standing rules*; *lint R1–R5* refers
to the separate check set implemented in `src/prompt_core.py` and is always
cited together with its checker function name.

**R1 — Protocols own the rules.** Evidence rules, claim taxonomy, confidence
rubric, and gate definitions live only in `Protocols/*.md`. Prompts *cite*
(`Protocols/Research-Evaluation.md` §2–§5) and may carry at most a short
reminder. Prevents: F2. Enforced by: lint R3 (`check_template_purity`).

**R2 — Gate IDs are always qualified.** Write `RE:Gate A`..`RE:Gate F`
(`Protocols/Research-Evaluation.md` §4), `FU:Gate A`..`FU:Gate D`
(`Protocols/FollowUpResearch.md` §6), `WB:n` (write-back checklist). Bare
letters are forbidden in every file under `prompts/`. Prevents: F1.
Enforced by: lint R2 (`check_bare_gates`).

**R3 — One copy under `prompts/`.** `lib/evidence_rules.md`,
`lib/claim_taxonomy.md`, and `lib/verification.md` are the only places those
blocks exist. Templates get them via include markers, never by copy-paste; the
claim-type vocabulary must appear in exactly one file. Prevents: F2.
Enforced by: lint R1+R3 (include resolution, purity, vocabulary uniqueness).

**R4 — Commands change in `AGENTS.md` first.** Any interpreter command quoted
under `prompts/` must appear verbatim in `AGENTS.md` (interpreter + script
path). Change AGENTS.md, mirror into `lib/verification.md`, then run the suite.
Prevents: drifted test/import commands. Enforced by: lint R5
(`check_commands`).

**R5 — Every named path must exist.** Frontmatter `inputs:`/`partials:` and
inline backtick paths are checked; no bare filenames — always the full
repo-relative path. Regenerable artifacts under `data/` are the only exemption.
Prevents: F4. Enforced by: lint R4 (`check_paths`).

**R6 — Dispatch data is assembled, never hand-copied.** Session prompts are
produced by `scripts/assemble_prompt.py` from the template plus
`ResearchAgenda.md`/DuckDB state, written to `prompts/dispatch/`. RQ tables,
scores, aliases, and doc hashes are never pasted into a template by hand.
Prevents: F3. Enforced by: process (templates carry no session numbers) plus
R4/R5 catching the fallout when they do.

**R7 — A red suite means the change is not done.** Every edit ends with
`.\.venv\Scripts\python.exe -m pytest src/tests -q` — the same command for
prompt edits, protocol edits, schema edits, and code edits. Prevents: F5.
Enforced by: this rule itself; session discipline in `AGENTS.md`.

**R8 — Version and archive; never delete.** Templates and partials carry
frontmatter `id`/`version`/`status`. Superseded versions move to
`prompts/archive/` with their date; history is never silently overwritten
(same principle as `Protocols/Research-Evaluation.md` §9). Prevents: F5 and
"when did this change?". Enforced by: review.

**R9 — Protocol first, mirror second.** To change a rule: edit the protocol,
then mirror into the `lib/` partial, then run the suite. Never fork new rule
text into a template to get a session moving. Prevents: F1, F2. Enforced by:
lint R3 (the fork fails purity) and review.

**R10 — No claimed improvement without a measurement.** A prompt edit that
claims to be "better" states what was measured (golden set, gate pass rate, or
at minimum the failing case it fixes). Follow Define → Test → Diagnose → Fix;
generic rewrites are rejected — arXiv:2601.22025 showed generic
"improvements" measurably *hurt* task behavior. Prevents: F5. Enforced by:
review now; the Tier 2 golden set when it lands.

**R11 — Destructive operations are dry-run first.**
`scripts/archive_stage1.py` runs with `--dry-run` or `--keep-originals` before
touching real data; database builds stay single-transaction and atomic; hooks
stay scoped to `research/raw/.*\.md`. Prevents: F6. Enforced by:
`Protocols/Encryption-Compression-Archiving.md`,
`Protocols/Hook-Based-Auto-Trigger-Extraction.md`, and the Report1 remediation
tests.

**R12 — Derived artifacts stay generated.** `*.duckdb`, `*.jsonl`, `.env`, and
`prompts/dispatch/*.md` are gitignored and regenerable. Never commit them,
never hand-edit them to "fix" output — fix the source and regenerate.
Prevents: F3, F6. Enforced by: `.gitignore` and review.

## 4. The working loop (every session)

1. **Edit the library, not the deck.** Change `prompts/templates/` or
   `prompts/lib/`; `Commander Deck/Active/prompts/` holds only stubs and
   pointers (see its `README.md`).
2. **Run the suite:** `.\.venv\Scripts\python.exe -m pytest src/tests -q`.
   The lint checks (`check_includes` … `check_commands`) are inside it.
3. **Assemble dispatches:**
   `.\.venv\Scripts\python.exe scripts/assemble_prompt.py --template <id> --out prompts/dispatch/<date>_<wave>.md`.
4. **Bump `version`, archive the superseded file** when a template changes.
5. **Record what happened** in `Commander Deck/Active/State changes/` — state,
   not prompt copies.

## 5. When a check fails — smallest correct fix

| Failure | Meaning | Fix |
| --- | --- | --- |
| `unresolved include` | A partial was renamed/removed | Restore the file or fix the marker — never inline the content |
| `bare gate reference` | Someone wrote a naked `Gate X` | Qualify it (`RE:`/`FU:`) or point at `WB:n` |
| `claim-type vocabulary … found:` | The taxonomy was copy-pasted | Delete the copy; keep it only in `lib/claim_taxonomy.md` |
| `command block outside lib/` | Verification commands pasted into a template | Replace with the `lib/verification.md` include |
| `frontmatter input missing` / `referenced path missing` | A dead reference (F4) | Fix the path or regenerate the missing artifact |
| `command not verbatim in AGENTS.md` | Command drift | Update `AGENTS.md` first (R4), then mirror |

Never make a failure green by weakening the check.

## 6. Update triggers

Revise this document when: a gate set is added or renamed in a protocol; the
lint rule set in `src/prompt_core.py` changes; a new asset location (e.g. a
Tier 2 `evals/` directory) comes into use; or a new failure mode is recorded in
`Commander Deck/Active/Problems/` that no rule here prevents. Preserve the
existing rule IDs when appending — the standing R-numbers are cited from this
file, the prompts, and the tests.

## 7. Final principle

> The standard is not that nothing ever changes. The standard is that a later
> agent can see one source of truth, one copy of every rule, a prompt that says
> exactly what the protocol says, and a green suite that proves it.
