-- DuckDB dialect review queries. Run after src/ingest_citations.py builds
-- data/citations.duckdb from schemas/citations.sql; not T-SQL.

-- Recurrence is a count of appearances, not a source-quality score.
SELECT source_id, title, distinct_documents, total_occurrences
FROM source_recurrence
WHERE total_occurrences > 0
ORDER BY distinct_documents DESC, total_occurrences DESC, title;

-- Primary evidence is exposed as a separate filter from recurrence.
SELECT source_id, title, authority_class, recurrence_documents, recurrence_occurrences,
       directness, publication_date, documented_independence_groups, limitations
FROM source_reputation
WHERE authority_class = 'primary'
  AND recurrence_documents > 1
ORDER BY recurrence_documents DESC, recurrence_occurrences DESC;

-- Independence is reported only where an independence group was explicitly recorded.
SELECT source_id, independence_group, COUNT(DISTINCT claim_id) AS claims_supported
FROM claim_source
WHERE independence_group IS NOT NULL
GROUP BY source_id, independence_group
ORDER BY claims_supported DESC, source_id, independence_group;

-- Locate sources that are incomplete, weakly classified, or structurally under-specified.
SELECT source_id, title, canonical_url, evidence_class, source_type, status,
       directness, publication_date, bias_notes, metadata_notes
FROM source
WHERE evidence_class IS NULL
   OR canonical_url IS NULL
   OR source_type IS NULL
   OR (status IS NULL AND directness IS NULL)
   OR publication_date IS NULL
   OR publication_date < current_date - INTERVAL '2 years'
ORDER BY evidence_class NULLS FIRST, publication_date NULLS FIRST, title;

-- Review the warning stream that explains unresolved rows and weak classifications.
SELECT warning_type, COUNT(*) AS warning_count, MIN(message) AS sample_message
FROM ingestion_warning
GROUP BY warning_type
ORDER BY warning_count DESC, warning_type;

-- Unresolved alias labels remain inspectable without forcing a source identity.
SELECT document_id, alias, match_method, normalization_notes
FROM source_alias
WHERE match_method = 'unresolved'
ORDER BY document_id, alias;

-- Documents with citations but absent or incomplete explicit claim-source coverage.
SELECT document_id, path, citation_occurrences, explicit_claims,
       claims_with_source_mappings, claims_without_source_mappings
FROM document_citation_coverage
WHERE citation_occurrences > 0
  AND (explicit_claims = 0 OR claims_without_source_mappings > 0)
ORDER BY claims_without_source_mappings DESC, path;

-- Low-confidence claims, unsourced claims, and claims supported only by secondary sources.
SELECT cl.claim_id, cl.document_id, cl.claim_text, cl.claim_type, cl.confidence,
       COUNT(DISTINCT cs.source_id) AS mapped_sources,
       COUNT(DISTINCT cs.source_id) FILTER (WHERE s.evidence_class = 'primary') AS primary_sources,
       COUNT(DISTINCT cs.source_id) FILTER (WHERE s.evidence_class = 'secondary') AS secondary_sources
FROM claim AS cl
LEFT JOIN claim_source AS cs ON cs.claim_id = cl.claim_id
LEFT JOIN source AS s ON s.source_id = cs.source_id
GROUP BY cl.claim_id, cl.document_id, cl.claim_text, cl.claim_type, cl.confidence
HAVING cl.confidence = 'low'
    OR COUNT(DISTINCT cs.source_id) = 0
    OR (
        COUNT(DISTINCT cs.source_id) FILTER (WHERE s.evidence_class = 'secondary') > 0
        AND COUNT(DISTINCT cs.source_id) FILTER (WHERE s.evidence_class = 'primary') = 0
    )
ORDER BY cl.confidence, cl.document_id;

-- Group next steps by workflow stage, claim type, confidence, and primary-evidence gap.
SELECT workflow_stage, claim_type, confidence,
       CASE WHEN mapped_primary_sources = 0 THEN 'missing primary evidence'
            ELSE 'primary evidence mapped' END AS primary_evidence_status,
       research_reason, COUNT(*) AS candidate_claims
FROM next_research_candidates
GROUP BY workflow_stage, claim_type, confidence, primary_evidence_status, research_reason
ORDER BY candidate_claims DESC, workflow_stage NULLS FIRST, claim_type, confidence;

-- Conflicts remain explicit source-to-claim relationships; no conflict is inferred from repetition.
SELECT claim_id, conflicting_source_id, related_source_id, related_relationship
FROM source_conflicts
ORDER BY claim_id, conflicting_source_id, related_source_id;

-- Unresolved and ambiguous table rows remain inspectable without forced source identity.
SELECT document_id, local_label, locator, resolution_status,
       recorded_classification, raw_citation_text
FROM citation_occurrence
WHERE resolution_status <> 'resolved'
ORDER BY document_id, locator;