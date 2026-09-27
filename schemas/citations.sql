-- DuckDB dialect. Executed by src/ingest_citations.py via duckdb.connect(); not T-SQL.
-- DuckDB-only syntax in this file: CREATE TABLE IF NOT EXISTS, CREATE OR REPLACE VIEW,
-- aggregate FILTER (WHERE ...), and NULLS FIRST/LAST ordering.
CREATE TABLE IF NOT EXISTS ingestion_run (
    run_id VARCHAR PRIMARY KEY,
    built_at TIMESTAMP NOT NULL,
    parser_version VARCHAR NOT NULL,
    input_root VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS ingestion_input (
    run_id VARCHAR NOT NULL REFERENCES ingestion_run(run_id),
    path VARCHAR NOT NULL,
    sha256 VARCHAR NOT NULL,
    modified_at TIMESTAMP,
    PRIMARY KEY (run_id, path)
);

CREATE TABLE IF NOT EXISTS research_document (
    document_id VARCHAR PRIMARY KEY,
    path VARCHAR NOT NULL UNIQUE,
    title VARCHAR NOT NULL,
    document_type VARCHAR NOT NULL,
    evaluation_date DATE,
    evaluation_decision VARCHAR CHECK (
        evaluation_decision IS NULL OR evaluation_decision IN
        ('accept', 'accept with limitations', 'revise', 'reject')
    ),
    quality_rating VARCHAR,
    is_internal BOOLEAN NOT NULL DEFAULT FALSE,
    content_sha256 VARCHAR NOT NULL,
    modified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS source (
    source_id VARCHAR PRIMARY KEY,
    canonical_url VARCHAR,
    title VARCHAR NOT NULL,
    publisher VARCHAR,
    author VARCHAR,
    source_type VARCHAR,
    evidence_class VARCHAR CHECK (
        evidence_class IS NULL OR evidence_class IN ('primary', 'secondary', 'internal')
    ),
    directness VARCHAR CHECK (
        directness IS NULL OR directness IN ('direct', 'indirect', 'unknown')
    ),
    publication_date DATE,
    access_date DATE,
    status VARCHAR,
    bias_notes VARCHAR,
    metadata_notes VARCHAR
);

CREATE TABLE IF NOT EXISTS citation_occurrence (
    occurrence_id VARCHAR PRIMARY KEY,
    local_label VARCHAR,
    raw_citation_text VARCHAR NOT NULL,
    source_id VARCHAR REFERENCES source(source_id),
    document_id VARCHAR NOT NULL REFERENCES research_document(document_id),
    locator VARCHAR,
    recorded_classification VARCHAR,
    extraction_method VARCHAR NOT NULL,
    resolution_status VARCHAR NOT NULL CHECK (
        resolution_status IN ('resolved', 'unresolved', 'ambiguous')
    )
);

CREATE TABLE IF NOT EXISTS source_alias (
    alias_id VARCHAR PRIMARY KEY,
    alias VARCHAR NOT NULL,
    source_id VARCHAR REFERENCES source(source_id),
    document_id VARCHAR NOT NULL REFERENCES research_document(document_id),
    normalization_notes VARCHAR,
    match_method VARCHAR NOT NULL CHECK (
        match_method IN ('canonical_url', 'unresolved', 'manual')
    )
);

CREATE TABLE IF NOT EXISTS claim (
    claim_id VARCHAR PRIMARY KEY,
    document_id VARCHAR NOT NULL REFERENCES research_document(document_id),
    claim_text VARCHAR NOT NULL,
    claim_type VARCHAR NOT NULL CHECK (
        claim_type IN ('documented fact', 'reported signal', 'inference', 'recommendation')
    ),
    confidence VARCHAR NOT NULL CHECK (confidence IN ('high', 'medium', 'low')),
    workflow_stage VARCHAR,
    falsifier VARCHAR,
    valid_from DATE,
    valid_to DATE,
    limitations VARCHAR,
    extraction_method VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS claim_source (
    claim_source_id VARCHAR PRIMARY KEY,
    claim_id VARCHAR NOT NULL REFERENCES claim(claim_id),
    source_id VARCHAR NOT NULL REFERENCES source(source_id),
    relationship VARCHAR NOT NULL CHECK (
        relationship IN ('supports', 'conflicts', 'contextualizes')
    ),
    evidence_locator VARCHAR,
    evidence_quote VARCHAR,
    independence_group VARCHAR
);

CREATE TABLE IF NOT EXISTS ingestion_warning (
    warning_id VARCHAR PRIMARY KEY,
    run_id VARCHAR NOT NULL REFERENCES ingestion_run(run_id),
    input_path VARCHAR NOT NULL,
    warning_type VARCHAR NOT NULL,
    message VARCHAR NOT NULL,
    raw_value VARCHAR
);

CREATE OR REPLACE VIEW source_recurrence AS
SELECT
    s.source_id,
    s.title,
    COUNT(DISTINCT d.document_id) AS distinct_documents,
    COUNT(co.occurrence_id) FILTER (WHERE d.document_id IS NOT NULL) AS total_occurrences
FROM source AS s
LEFT JOIN citation_occurrence AS co ON co.source_id = s.source_id
LEFT JOIN research_document AS d
    ON d.document_id = co.document_id
 AND d.is_internal = FALSE
GROUP BY s.source_id, s.title;

CREATE OR REPLACE VIEW source_reputation AS
SELECT
    s.source_id,
    s.title,
    s.evidence_class AS authority_class,
    s.directness,
    s.publication_date,
    s.access_date,
    s.status,
    s.bias_notes,
    s.metadata_notes AS limitations,
    COALESCE(r.distinct_documents, 0) AS recurrence_documents,
    COALESCE(r.total_occurrences, 0) AS recurrence_occurrences,
    COUNT(DISTINCT cs.independence_group) FILTER (
        WHERE cs.independence_group IS NOT NULL
    ) AS documented_independence_groups
FROM source AS s
LEFT JOIN source_recurrence AS r ON r.source_id = s.source_id
LEFT JOIN claim_source AS cs ON cs.source_id = s.source_id
GROUP BY
    s.source_id, s.title, s.evidence_class, s.directness,
    s.publication_date, s.access_date, s.status, s.bias_notes,
    s.metadata_notes, r.distinct_documents, r.total_occurrences;

CREATE OR REPLACE VIEW document_citation_coverage AS
SELECT
    d.document_id,
    d.path,
    COUNT(DISTINCT co.occurrence_id) AS citation_occurrences,
    COUNT(DISTINCT cl.claim_id) AS explicit_claims,
    COUNT(DISTINCT cs.claim_id) AS claims_with_source_mappings,
    COUNT(DISTINCT cl.claim_id) FILTER (
        WHERE cs.claim_id IS NULL
    ) AS claims_without_source_mappings
FROM research_document AS d
LEFT JOIN citation_occurrence AS co ON co.document_id = d.document_id
LEFT JOIN claim AS cl ON cl.document_id = d.document_id
LEFT JOIN claim_source AS cs ON cs.claim_id = cl.claim_id
GROUP BY d.document_id, d.path;

CREATE OR REPLACE VIEW source_conflicts AS
SELECT DISTINCT
    conflicting.claim_id,
    conflicting.source_id AS conflicting_source_id,
    related.source_id AS related_source_id,
    related.relationship AS related_relationship
FROM claim_source AS conflicting
JOIN claim_source AS related
  ON related.claim_id = conflicting.claim_id
 AND related.source_id <> conflicting.source_id
WHERE conflicting.relationship = 'conflicts'
  AND related.relationship IN ('supports', 'contextualizes');

CREATE OR REPLACE VIEW next_research_candidates AS
SELECT
    cl.claim_id,
    cl.document_id,
    cl.claim_text,
    cl.workflow_stage,
    cl.claim_type,
    cl.confidence,
    COUNT(DISTINCT cs.source_id) AS mapped_sources,
    COUNT(DISTINCT cs.source_id) FILTER (
        WHERE s.evidence_class = 'primary'
    ) AS mapped_primary_sources,
    CASE
        WHEN COUNT(DISTINCT cs.source_id) = 0 THEN 'no mapped sources'
        WHEN COUNT(DISTINCT cs.source_id) FILTER (
            WHERE s.evidence_class = 'primary'
        ) = 0 THEN 'no mapped primary evidence'
        WHEN cl.confidence = 'low' THEN 'low confidence'
        ELSE 'review'
    END AS research_reason
FROM claim AS cl
LEFT JOIN claim_source AS cs ON cs.claim_id = cl.claim_id
LEFT JOIN source AS s ON s.source_id = cs.source_id
GROUP BY
    cl.claim_id, cl.document_id, cl.claim_text, cl.workflow_stage,
    cl.claim_type, cl.confidence
HAVING cl.confidence = 'low'
    OR COUNT(DISTINCT cs.source_id) = 0
    OR COUNT(DISTINCT cs.source_id) FILTER (
        WHERE s.evidence_class = 'primary'
    ) = 0;