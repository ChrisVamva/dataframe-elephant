<!-- src/prompt_templates/lib/claim_taxonomy.md — THE single copy of the claim-type vocabulary
     under src/prompt_templates/. Canonical source: Rules and Regulations/Protocols/Research-Evaluation.md §4
     (`RE:Gate C`) and §5. Keep the enumeration here only; templates must not
     repeat it. -->

## Claim taxonomy and confidence

Claim types — the only four allowed in write-backs:

| Type | Meaning |
| --- | --- |
| `documented fact` | Directly stated or directly observable in a reliable source |
| `reported signal` | An observed report or indication, insufficient to establish a general fact |
| `inference` | Your reasoned conclusion from cited evidence — labeled as such |
| `recommendation` | A proposed action or judgment — never presented as a source-established fact |

Confidence — `high` / `medium` / `low`, assigned **per material claim** with a
one-line reason (rubric: `Rules and Regulations/Protocols/Research-Evaluation.md` §5). A high-confidence
source does not make every conclusion drawn from it high confidence.

Claim row shape (Stage 2 `Claims.md`):

| claim | claim type | confidence | supporting evidence | contradicting evidence | falsifier |
| --- | --- | --- | --- | --- | --- |
