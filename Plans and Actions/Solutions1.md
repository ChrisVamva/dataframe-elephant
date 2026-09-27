---
modified: 2026-09-27T19:05:00+03:00
---

## Solutions: Citation Intelligence Database defect remediation

  

This plan fixes the 15 findings recorded in `Problems/Report1.md` (2026-09-27) against the citation intelligence database. Each step names the finding it closes and the evidence that will show it is closed. The plan changes build safety, warning coverage, review queries, setup, and documentation. It changes no research content and no evidence classification.

  

**Constraints**

  

1. Keep the deterministic, auditable posture: identifiers stay content-derived, no fuzzy matching is introduced, and unresolved or ambiguous records stay visible instead of being auto-merged.
2. Keep the database shape stable: no table or view is removed and no column is renamed. The one value-level change is that "not recorded" stops being written as the sentinel string `unknown` (F5).
3. Every fix lands with a regression test that fails before it and passes after it. The reproductions already recorded in `Problems/Report1.md` are the failing cases.
4. Rebuild the snapshot once at the end and re-measure counts, so the before/after numbers are recorded rather than assumed.

  

**Steps**

  

### Phase 1: Make the build safe to fail (F1, F2)

  

1. **Wrap the whole rebuild in one transaction (F1).** Replace the three committed delete transactions and the separate insert transaction with a single `BEGIN TRANSACTION` that runs the child-before-parent delete list, then every insert, then `COMMIT`. Keep the existing `ROLLBACK` handler so that any failure leaves the previous snapshot byte-for-byte usable. Note the interaction with F13: the delete list contains the derived tables plus, until the run-history policy is decided in Phase 5, `ingestion_run` and `ingestion_input` as they are today.
2. **Decide and implement the duplicate-claim policy (F2).** Recommended default: rows whose normalized claim text is identical **and** whose claim type and confidence agree describe one claim, so keep one `claim` row, attach every distinct `claim_source` row, and emit a warning naming the extra source row. Rows that agree on text but disagree on type or confidence are not merged: give `claim_id` a discriminator (claim type, confidence, or source line) so both survive, and warn. Write the chosen policy into `data/README.md` so the behaviour is documented rather than implied.
3. **De-duplicate the mapping rows as well (F2).** `claim_source_id` derives from claim, source, relationship, and locator, and the locator cell is normally empty, so merging two claims while keeping both mappings recreates the same collision in `claim_source`. De-duplicate mappings by identifier before the insert.
4. **Regression tests for the build path (F1, F2).** Add a case where two claim rows differ only in case: assert the claim and mapping counts the policy predicts, and assert the warning. Add a failure case: build a snapshot, then build again over a corpus that raises, and assert the first snapshot's row counts are still present. The current reproduction aborts the build and leaves all tables at 0 rows.
5. **Evidence to record when the phase closes.** The reproduction from `Problems/Report1.md` F1, re-run after the change, showing the raised exception together with unchanged row counts in `data/citations.duckdb`.

### Phase 2: Remove corruption, stop silent data loss (F3, F4)

  

6. **Delete the corrupted dead line (F3).** Remove line 49 of `src/ingest_citations.py`, the assignment whose `rstrip` set contains a raw `0x05` byte, and keep line 50, which already carries the correct set `".,;:)]}"`. Do not merge the duplicated lines by keeping the corrupted one.
7. **Add a URL-boundary regression test (F3).** Assert that `normalize_url` preserves a trailing letter `d` (`https://example.org/docs/download`), strips a trailing `}` and `]`, and leaves the path otherwise intact. The corrupted set fails the first two of those assertions, as measured in `Problems/Report1.md` F3.
8. **Add a control-character guard (F3).** A check over the source tree that fails on any byte below `0x09` or between `0x0E` and `0x1F`, so a second encoding incident is caught at test time rather than by inspection.
9. **Hoist the classification check out of the URL branch (F4).** In `_source_row_data`, warn whenever `classification` is non-empty but `classify_evidence` returns `None`, regardless of whether a URL resolved. Leave an empty classification cell silent, since nothing was recorded to warn about. Keep `classification_conflict` in `_merge_source_metadata` unchanged for the exact-URL merge path.
10. **Regression test for the silent drop (F4).** A source row with a resolvable URL and the classification `Mixed` must produce one source with `evidence_class IS NULL` **and** one `weak_source_classification` warning. Today it produces the source and no warning at all.
11. **Rebuild and record the warning delta (F4).** Expect the total to rise above 604 by the number of unmapped classifications, at least 1 for the composite value `Mixed (Superset docs = Primary; metabase.com LP = Secondary)`, while the 21 sources whose classification cell is empty stay unwarned.
12. **Evidence to record when the phase closes.** The clean byte scan, the three `rstrip` assertions, and the before/after warning counts grouped by type.

  

### Phase 3: Make the review workflow surface real gaps (F5, F6, F7)

  

13. **Stop writing sentinels for status and directness (F5).** In `_source_row_data`, write `NULL` when the source text does not state the value, instead of the string `unknown`, so "not recorded" and "recorded as unknown" stop being the same value. Leave `bias_notes` NULL until a curation pass supplies it. No existing test asserts `source.status` or `source.directness`, so this change needs only its own new test.
14. **Re-scope the completeness queries (F5).** Replace the single seven-way `OR` query in `analysis/citation_evaluator.sql` with named-gap queries: sources with no evidence class, sources whose recorded classification is unmapped, sources with no usable page URL, and sources whose text explicitly records an unknown status. Clearing the sentinels alone does not fix the query, because with NULLs a `status IS NULL` fallback would match every row.
15. **Teach the metadata reader the bold label style (F6).** Extend `_metadata_value` to accept a key wrapped in `**` or `__` with an optional trailing `:`, so `**Decision:** **Revise.**` resolves to `Revise` as `Decision: Revise` already does. Build the test from the exact style used in `analysis/On Research/First-Ratings.md`.
16. **Bring the evaluation decisions into the database (F6, F12).** Apply the single policy chosen in Phase 4 step 21: copy or move the file under `research/raw/`, or add a second input root or explicit extra-document option to `build_database`. It must land with `is_internal = TRUE` so `source_recurrence` keeps excluding it, and the run should then report `count(evaluation_decision) = 15`.
17. **Surface the review queue in the evaluator queries (F7).** Add two result sets: warnings grouped by `warning_type` and by input document with counts and one sample message, and unresolved aliases (`match_method = 'unresolved'`) grouped by document and local label. Both read tables that already exist, so no ingestion change is needed.
18. **Evidence to record when the phase closes.** The row count returned by each new triage query, which must be far below the 207 sources; `count(evaluation_decision) = 15` with the internal document flagged; and non-empty output for both new review result sets, against 604 warnings and 240 unresolved aliases.

### Phase 4: Setup, hygiene, and documentation (F8, F9, F10, F11, F12)

  

19. **Make bare `pytest` work (F8).** Add a `pyproject.toml` with `[tool.pytest.ini_options]` and `pythonpath = ["."]`, so the `pytest src/tests -q` form used by editors, task runners, and CI collects the suite instead of raising `ModuleNotFoundError: No module named 'src'`. `data/README.md` keeps documenting `python -m pytest`, which continues to work unchanged.
20. **Initialise the repository with ignore rules (F9).** Run `git init` and add a `.gitignore` excluding `.venv/`, `.pytest_cache/`, `data/citations.duckdb`, and `data/citation_ingestion_warnings.jsonl`. Decide explicitly whether a built snapshot is ever versioned; if it is, commit it as a deliberate release artifact rather than as build output. Commit the current source, documents, and reports as a baseline so later diffs are reviewable.
21. **Resolve the `First-Ratings.md` policy (F12; required by step 16).** Decide whether the file is ingested as an internal artifact or stays outside the corpus, record that decision in `data/README.md`, and correct the sentence that calls it absent while it sits in `analysis/On Research/`.
22. **Remove or repair the stale environment (F10).** Delete `.venv/`, since the documented setup is the `datascience` conda environment and the workspace pins conda. Alternatively install `requirements.txt` into `.venv/` so both paths work.
23. **Update the root README (F11).** Refresh the structure tree and directory guide to list `Plans and Actions/`, `Protocols/`, `Problems/`, `requirements.txt`, and `.vscode/`; describe `schemas/` as the DuckDB schema and `analysis/` as the evaluator queries plus evaluation notes; and add a short build section linking to `data/README.md` and `Protocols/Research-Evaluation.md`.
24. **Evidence to record when the phase closes.** `pytest src/tests -q` and `python -m pytest src/tests -q` both passing; `git status --short` showing no database, warnings, virtual environment, or pytest cache entries; and a README tree in which every named directory exists.

  

### Phase 5: Policy, coverage, and latent mapping (F13, F14, F15)

  

25. **Decide the run-history policy and apply it consistently (F13).** **Option A, retain history:** remove `ingestion_run` and `ingestion_input` from the delete list and insert them with `ON CONFLICT DO NOTHING`, which also preserves the original `built_at` for a given input set; this needs a conflict-clause parameter on `_insert_rows` and must be applied together with the delete list chosen in step 1. **Option B, single snapshot:** keep today's behaviour and state it explicitly in `data/README.md`, naming the warnings file and the recorded input hashes as the audit trail. Option A fits `Protocols/Research-Evaluation.md` section 9 better, which asks that history not be silently overwritten.
26. **Close the coverage gaps (F14).** Add one test per uncovered branch: truncated-URL and missing-title warnings, the classification-conflict merge path, claim label resolution failure, `document_citation_coverage` and `source_conflicts` with non-empty claims, and the claim de-duplication policy from step 2. The three reproductions in `Problems/Report1.md` F2, F3, and F4 are the first three of these.
27. **Remove the claim-type alias (F15).** Drop `status` from the claim-type header set in `_claim_columns`, keeping the explicit `claim type` and `type` headers, so a future Status column is not silently read as a claim type. Prove it with a fixture carrying `Claim | Status | Confidence` columns, which must warn instead of parsing.
28. **Evidence to record when the phase closes.** Each new test failing against the pre-fix code and passing after the fix; and `select count(*) from ingestion_run` either growing across builds or covered by the documented single-snapshot policy.

  

**Order and dependencies**

  

1. Phase 1 first: every other phase that touches `build_database` assumes the single-transaction form.
2. Step 21 must be settled before step 16, because it chooses where `First-Ratings.md` is read from.
3. Step 25 changes the delete list written in step 1. If Option A is chosen, change both in the same commit so the build never runs with a mismatched delete and insert pair.
4. Phases 2 and 3 are independent of Phase 1 and can be worked in parallel, but each ends with a rebuild, and two rebuilds over the same corpus must not be interleaved.
5. Phase 4 touches no parser code and can land at any time.
6. Finish with one rebuild after the last code change in Phases 1 to 3, since Phase 2 changes warning totals and Phase 3 changes stored source values. Record the final counts as the new baseline.

**Relevant files**

  

- `Problems/Report1.md` — the source of the 15 findings. The reproductions in F1, F2, F3, and F4 become the first failing test cases.
- `src/ingest_citations.py` — transaction form (step 1), claim de-duplication (steps 2 and 3), corrupted line (step 6), classification warning (step 9), status sentinels (step 13), bold metadata labels (step 15), run history (step 25), claim-type headers (step 27).
- `src/tests/test_ingest_citations.py` — new regression tests in steps 4, 7, 10, 26, and 27. The existing warning assertion uses `any(...)` rather than an exact count, so additional warning types do not break it.
- `schemas/citations.sql` — not modified. It is referenced only to confirm that the duplicate-key failure is fixed in Python rather than by weakening the primary key.
- `analysis/citation_evaluator.sql` — triage queries (step 14) and review result sets (step 17).
- `data/README.md` — documents the claim policy (step 2), the status semantics (step 13), the `First-Ratings.md` policy (step 21), and the run-history policy (step 25).
- `README.md` — structure tree, directory guide, and build pointer (step 23).
- `pyproject.toml` — new file, pytest configuration (step 19).
- `.gitignore` — new file, ignore rules for generated artifacts (step 20).
- `.vscode/settings.json` — already carries the DuckDB dialect setting; no change planned here.
- `requirements.txt` — already aligned with the installed pytest; no change planned here.
- `.venv/` — to be deleted or repaired (step 22).

  

**Verification**

  

1. `python -m pytest src/tests -q` and `pytest src/tests -q` both pass, with the new tests present. Baseline is 7 passing tests.
2. The F1 reproduction raises and the previous snapshot survives: after a failed rebuild, `select count(*) from source` is still 207.
3. The F2 fixture builds instead of raising: one claim row, every distinct mapping retained or the alternative documented by the chosen policy, and a warning naming the extra row.
4. The `normalize_url` boundary assertions hold for a trailing `d`, `}`, and `]`.
5. A byte scan of `src/` reports zero control characters.
6. The F4 fixture produces one `weak_source_classification` warning, the warnings artifact contains at least one row of that type, and the sources whose classification cell is empty remain unwarned.
7. Every triage query returns fewer rows than `select count(*) from source` (207).
8. If step 21 chooses ingestion, `select count(evaluation_decision) from research_document` equals 15 and the internal document is flagged.
9. Both new review result sets return rows: 604 warnings and 240 unresolved aliases before grouping.
10. `git status --short` lists no database, warnings file, virtual environment, or pytest cache entry.
11. Every directory named in the README tree exists, and every top-level directory that exists is named.
12. One rebuild after the last code change in Phases 1 to 3 records the new baseline counts, and the counts are written down rather than remembered.

The plan is complete when all 15 findings are either closed with the evidence above, or explicitly deferred with the reason and the owner decision recorded in the table below. Re-run the checks written in `Problems/Report1.md` as the closing review, and record the outcome there rather than editing the findings out of history.

**Decisions**

  

| # | Decision | Options | Recommended default | Steps |
| --- | --- | --- | --- | --- |
| D1 | Duplicate claim policy | Merge identical text when type and confidence agree, or always keep a discriminator | Merge and warn | 2, 3, 26 |
| D2 | Unmapped classification | Warn only, or warn and route the row into a separate review queue | Warn only; step 17 already exposes the queue | 9, 17 |
| D3 | Status and directness semantics | NULL when not recorded, or an explicit `not_recorded` value | NULL | 13, 14 |
| D4 | `First-Ratings.md` | Ingest it as an internal artifact, or keep it outside the corpus | Ingest; the protocol requires a decision field and the snapshot has none | 16, 21 |
| D5 | Run history | Retain run and input rows, or keep the single-snapshot behaviour | Retain (Option A) | 25 |
| D6 | Versioning the built database | Never by default, or commit deliberate snapshots | Never by default | 20 |
| D7 | `.venv` | Delete, or repair | Delete | 22 |

  

**Further Considerations**

  

1. **Warning volume.** Step 9 deliberately raises the warning count above 604, and the artifact is already large. Prefer grouping in the review query (step 17) over suppressing the new signal, and only add a summary line if a human has to read the file end to end.
2. **Identifier migration.** The snapshot holds 0 claims, so changing how duplicate claims are identified needs no migration now. If anything ever stores `claim_id` values, changing the identifier scheme becomes a breaking change and should be signalled through `PARSER_VERSION`.
3. **Write volume in one transaction.** The single-transaction fix commits roughly 455 occurrences, 455 aliases, 207 sources, and the warnings at once, which is trivial at this size. If the corpus grows by orders of magnitude, prefer the temporary-database-and-swap variant described in `Problems/Report1.md` F1.
4. **`_insert_rows` shape.** The helper derives its column list from the first row's key order. Adding a conflict clause should not disturb that, but a mixed-shape row list would silently mis-insert, so keep each table's rows built by one function.
5. **Artifact growth under Option A.** Retaining runs makes `data/citations.duckdb` grow with every build. A `CHECKPOINT` after commit, or a separate history table, is a reasonable follow-up rather than part of this plan.
6. **Follow-up review.** `Problems/Report1.md` sets the precedent for evidence-first problem reports. A short second report recording the before and after counts would close the loop and keep the decision trail continuous, consistent with `Protocols/Research-Evaluation.md` section 9.
7. **Keep unrelated fixes out of these diffs.** The DuckDB dialect editor setting and the dependency pin are already resolved. Each commit should map to one finding, so that the review that found it can be referenced in the message.

  

**Definition of done**

  

1. All 15 findings are closed with recorded evidence, or deferred with the reason and the owner decision recorded in the table above.
2. Both pytest invocation forms pass, including the new tests added in steps 4, 7, 10, 26, and 27.
3. One rebuild is recorded with before and after counts, and the counts are written into `data/README.md` or the follow-up report.
4. Each commit maps to one finding, and the review that found it is referenced in the commit message.
5. `Problems/Report1.md` is left intact as history, with its Open status section updated to point at the closing evidence instead of being rewritten.
