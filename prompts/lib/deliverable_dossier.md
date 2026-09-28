<!-- prompts/lib/deliverable_dossier.md — the standard follow-up dossier deliverable
    shape. Canonical question spec: Rules and Regulations/Protocols/FollowUpResearch.md §5. -->

Follow the dossier specification in `Rules and Regulations/Protocols/FollowUpResearch.md` §5 (core
question, In Scope / Out of Scope, intended use, minimum evidence class, target
sources, resolution + falsifier), plus:

- **Verdict per trigger:** `resolved` (with answer + citations) or `still open`
  (with what was tried and what would unblock it).
- **Exact write-back patch:** the `Entities.md` boundary sentence, the atomic
  `Sources.md` rows, or the alias → `source_id` mapping — formatted as the
  target Stage 2 table row, ready to paste.
- **Gate self-check (qualified IDs):** `FU:Gate A` (scope) / `FU:Gate B`
  (falsifier) / `FU:Gate C` (provenance) / `FU:Gate D` (score) / `WB:1`
  (write-back integrity).

Claim rows follow `prompts/lib/claim_taxonomy.md`. Source rows are atomic: one
URL per row, never bundled; every material claim carries supporting and
contradicting evidence plus its falsifier.
