# Commander Deck prompts — operational index

This folder is the **operational layer**: session dispatches and thin pointers.
The prompt **assets** (templates and shared partials) live in the repository
library at `prompts/` — see `prompts/README.md` for the index of record.

| This folder (stub) | Library target |
| --- | --- |
| `Research Prompt.md` | `prompts/templates/research_brief.md` |
| `FollowUpPrompt.md` | `prompts/templates/followup_dispatch.md` |
| `NextResearchPrompt.md` | `prompts/templates/next_research.md` |
| `The components to investigate.md` (moved) | `prompts/lib/lens_reference.md` |

Rules that keep this folder from rotting (see
`Rules and Regulations/Core Rules/MaintainingProsperity.md`):

1. Never edit prompt content here — edit the library template or partial.
2. New session dispatches are generated into `prompts/dispatch/`, not written here.
3. Gate references always use qualified IDs (`RE:Gate A`, `FU:Gate B`, `WB:1`).
