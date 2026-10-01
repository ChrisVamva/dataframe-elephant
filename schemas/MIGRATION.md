# Schema Migration History

## citations.sql (v1)
- Created: 2026-09-30
- Purpose: Citation database (claims, sources, metrics)
- Tables: `claims`, `sources`, `metrics`, `claim_sources`, `occurrences`, `aliases`, `documents`

## stage2.sql (v1)
- Created: 2026-09-27
- Purpose: Stage 2 extraction data (shared by Extraction 1, 2, 3)
- Tables: `stage2_run`, `stage2_input`, `stage2_document`, `entity`, `metric`, `stage2_claim`, `source_mirror`, `predicate`, `workflow_stage`, `extraction_decision`, `stage2_warning`
- Views: `unstated_boundaries`, `unstated_conditions`, `missing_falsifiers`, `open_questions`

## Migration Rules
- Schema files are never forked per extraction; `stage2.sql` is shared.
- To change schema: edit `schemas/*.sql`, update this file, and re-run imports.