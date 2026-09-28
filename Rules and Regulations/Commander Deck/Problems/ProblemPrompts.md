---
id: PP-001
status: open
reported_date: 2026-09-28
reported_by: workspace maintainer
severity: medium (provisional)
evidence_basis: user-reported; not independently reproduced
---

# Problem: Prompts Require Workspace Access

## Summary

The workspace maintainer reports that prompt products have asked the
researcher to access `C:\Users\user\dataframe-elephant` to complete their
steps. The maintainer reports that this dependency has stalled research
quality and progress. The exact prompt versions, number of occurrences, and
affected research sessions have not yet been identified.

**Status:** open. This is a user-reported workflow problem, not a claim that
all current prompts fail outside the repository.

### Initial corrective artifact

On 2026-09-28, a standalone smart-home market research prompt was created at
the maintainer's requested path,
[`prompts/prompts/smart-homemarketpromp.md`](../../../prompts/prompts/smart-homemarketpromp.md).
A source scan found no repository path, repo-local command, or prompt-library
include in that file, and the prompt taxonomy-purity test passes. This is a
partial mitigation, not reproduction or closure: no clean-context research
run has been completed, and the canonical long-term location for portable
outputs remains open in [PromptReformPlan.md](../Plans/PromptReformPlan.md).

## Scope and Impact

- **Affected workflow:** research prompts intended to be copied into another
  research medium or used in a session without the dataframe-elephant checkout.
- **Reported impact:** research could not proceed as expected when the prompt
  requested inaccessible local material; the maintainer reports stalled
  progress and degraded research quality.
- **Quantification:** not recorded. Frequency, delay, affected prompts, and
  research outcomes have not been measured.
- **Severity:** medium, provisional. The impact is material to independent
  research, but the incident count and scope are unknown.

## Evidence and Limitations

### User-reported observation

The maintainer directly reports the access request and its impact. No prompt
version, transcript, session date, or reproduction was supplied with the
report, so the specific occurrence cannot yet be tied to a line or release.

### Repository observations

The prompt library has both repository-connected and potentially portable
uses. Current `followup_dispatch` and `next_research` templates declare
repository-local research agenda, Stage 2, and protocol inputs. Shared
verification instructions refer to local scripts and the project virtual
environment. These dependencies may be correct for repository write-back, but
they must be labeled and must not be imposed on a portable research task
without the user's permission.

The nested `prompts/prompts/` copy contains three stubs explicitly marked
`superseded` and an authority document whose recorded scope points to the now
absent `Rules and Regulations/Commander Deck/prompts/` path. These are
separate structure/path issues tracked by
[PromptReformPlan.md](../Plans/PromptReformPlan.md); they do not alone prove
the reported user incident.

## Provisional Cause

**Hypothesis:** prompt types and operating modes are not clearly separated.
Repository-native workflows legitimately expect local data and scripts, while
portable prompts may carry or expose those prerequisites as if they were
required for research itself.

**Confidence:** medium-low. Current template metadata confirms some local
inputs; the specific access request reported by the user has not been
reproduced.

## Reproduction Plan

1. Ask the reporter for one exact prompt/version and, if available, the
   relevant transcript or the step that requested workspace access.
2. Run the candidate prompt in a clean context with no repository files,
   scripts, environment variables, or database access.
3. Record whether it asks for a local path, blocks on missing input, silently
   assumes unavailable research results, or proceeds with the accessible
   research media and reports limitations.
4. Repeat with a repository-connected prompt in its intended workspace to
   distinguish a valid local workflow from accidental portability coupling.

## Required Resolution

- Declare prompt profiles in the root prompt-library index. A
  `repository-connected` prompt lists its required workspace inputs and must
  be run in that workspace. A `portable` prompt must be self-contained and
  must not require repository access.
- Make portable use the default for research prompts that do not need
  repository write-back; make any repo integration an explicit opt-in step.
- Resolve the conflict between standalone output and
  `MaintainingProsperity.md` R1/R3/R9 before duplicating protocol rules. The
  portable artifact must obtain its approved standards from a single canonical
  source or a controlled generated export.
- Add a portability validation that rejects local workspace paths,
  repo-specific inputs, unresolved local includes, and required local
  commands in the assembled portable artifact.
- For the smart-home market prompt, produce and validate a self-contained
  prompt usable with web search, browser tools, academic indexes, reports, or
  user-provided sources, while clearly reporting unavailable sources and
  methods.

## Acceptance / Closure Criteria

Close this problem only when:

1. At least one previously affected prompt is identified or the report is
   explicitly closed as un-reproduced with that limitation recorded.
2. A portable prompt passes a clean-context test without access to
   `C:\Users\user\dataframe-elephant`.
3. The prompt returns useful, traceable research or clearly states its
   limitations instead of blocking on private files.
4. Repository-connected prompts remain functional for their declared use.
5. Prompt lint and full tests pass, and the relevant checks are recorded in a
   dated state-change report.

## Related Records

- [PromptReformPlan.md](../Plans/PromptReformPlan.md) defines the reform,
  archive, portability, and validation sequence.
- [`prompts/README.md`](../../../prompts/README.md) is the current prompt
  library index of record.
- [`MaintainingProsperity.md`](../../Core%20Rules/MaintainingProsperity.md)
  owns the one-source, history, validation, and generated-artifact rules.
- [`Research-Evaluation.md`](../../Protocols/Research-Evaluation.md) owns
  research scope, evidence, claim support, uncertainty, and counterevidence
  requirements.

## Review Record

| Date | Reviewer | Result | Notes |
| --- | --- | --- | --- |
| 2026-09-28 | GitHub Copilot | Open; user-reported | Repository dependencies inspected at the template/index level; no incident transcript or exact failing prompt supplied, so no reproduction is claimed. |