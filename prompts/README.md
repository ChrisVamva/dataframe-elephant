# `prompts/` — prompt library (index of record)

The single home for reusable prompt assets. The Commander Deck folder
(`Rules and Regulations/Commander Deck/prompts/`) holds only stubs and session pointers.

```
prompts/
├── README.md        ← this file: index, lifecycle, dispatch how-to
├── lib/             ← shared partials (single copy of rules, shapes, commands)
├── templates/       ← dispatchable prompt skeletons (frontmatter + includes)
├── dispatch/        ← generated session prompts (regenerable; see dispatch/README.md)
└── archive/         ← superseded versions (never delete history)
```

## Templates

| id | File | Purpose |
| --- | --- | --- |
| `research_brief` | `templates/research_brief.md` | Evidence-grounded atlas research brief (nine lenses) |
| `followup_dispatch` | `templates/followup_dispatch.md` | Wave dispatch over the follow-up agenda (tracks A/B/C) |
| `next_research` | `templates/next_research.md` | Batched gap-closure protocol (batches 1–4) |

## Partials (`lib/`)

| Partial | Holds |
| --- | --- |
| `role_research_agent.md` | Shared agent role/spine |
| `evidence_rules.md` | Single copy of the working evidence rules (pointer to `Rules and Regulations/Protocols/Research-Evaluation.md` §2/§4/§5) |
| `claim_taxonomy.md` | THE single copy of the four claim types + confidence rubric pointer |
| `deliverable_brief.md` | 7-section research-brief shape |
| `deliverable_dossier.md` | Follow-up dossier shape + write-back + gate self-check |
| `quality_bar.md` | Closing standard (pointer to Eval §10) |
| `verification.md` | THE single copy of verification commands (must match `AGENTS.md`) |
| `lens_reference.md` | Nine-lens reference table (formerly `The components to investigate.md`) |

## Conventions

- **Frontmatter** on every template: `id`, `version`, `status`
  (`draft`/`active`/`superseded`), `protocol_refs`, `inputs`, `partials`.
- **Includes:** a marker `<!-- include:` + `lib/<name>.md` + `-->` (path
  relative to `prompts/`); resolved by `scripts/assemble_prompt.py`. Partials
  never carry `##` headings — the template owns the section heading.
- **Gate IDs are always qualified:** `RE:Gate A`–`RE:Gate F`
  (`Rules and Regulations/Protocols/Research-Evaluation.md` §4), `FU:Gate A`–`FU:Gate D`
  (`Rules and Regulations/Protocols/FollowUpResearch.md` §6), `WB:n` (write-back checklist).
  Bare letters fail lint.
- **Numbers** (RQ counts, scores, URLs, aliases) are dispatch data — never
  baked into a template; regenerate them into `dispatch/`.
- **Lifecycle:** edit → lint (`.\.venv\Scripts\python.exe -m pytest src/tests -q`)
  → bump `version` only if the golden set agrees → supersede old versions into
  `archive/`, never delete.
