# Verification Protocol (Deliverable)

_Status: skeleton — drafted only after 03 and 04 are researched. Target: a versioned, standalone protocol any publisher, library, or fact-checking organization can implement without project-specific tooling._

## Planned sections

1. **Scope and actors** — who runs verification (publisher, library, fact-checker, platform) and at which chain layer.
2. **Chain representation** — mapping scholarly citation chains onto W3C PROV entities/activities/agents `[S02]`.
3. **Checks** — lightweight per-link checks (retraction status via `[S01]`, DOI resolution, intermediary-layer flagging).
4. **Scoring** — a chain-integrity score (draft definition from 04_Methods decay model).
5. **Cost and limitations** — what the protocol does not catch; adversarial failure modes.
