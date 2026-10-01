<!-- src/prompt_templates/lib/evidence_rules.md — single copy of the working evidence rules.
    Canonical source: Rules and Regulations/Protocols/Research-Evaluation.md §2 (non-negotiable rules),
     §4 (`RE:Gate B`, source quality), §5 (confidence rubric). Do not fork this
     file; edit the protocol first, then mirror the change here. -->

1. **Evidence class hierarchy:**
   - **Tier 1 (Primary / Authoritative):** official technical specifications
     (W3C, IETF), vendor product documentation, first-party engine codebases,
     peer-reviewed publications.
   - **Tier 2 (Secondary / Documented signal):** engineering blog posts by core
     maintainers, verified benchmarks with reproducible configurations.
   - **Tier 3 (Synthesis / Internal):** local vault notes and exploratory
     designs — explicitly labeled internal synthesis, never external evidence.
   - **Forbidden:** SEO marketing summaries, vendor advertorials, unattributed
     listicles.
2. **Record provenance for every source:** URL, title, publisher/author,
   publication date when available, and access date.
3. **Classify evidence** as `primary`, `secondary`, or `internal synthesis`
  (per `RE:Gate B` in `Rules and Regulations/Protocols/Research-Evaluation.md`).
4. **Type every claim** per `src/prompt_templates/lib/claim_taxonomy.md`. Never promote an
   evidence class; never present vendor positioning as established fact.
5. **Quote or paraphrase only what the source supports.** Note uncertainty,
   conflicting evidence, missing data, and likely source bias.
6. **Date-sensitive claims** carry `as of [date]`; prefer current evidence but
   preserve historical context that explains a transition.
7. **Independent corroboration** for material claims (market, company, product,
   role claims). Multiple pages repeating one originating claim are not
   independent confirmation.

