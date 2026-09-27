-- DuckDB dialect. Applied by src/stage2_import_core.py via duckdb.connect(); not T-SQL.
-- DuckDB-only syntax in this file: CREATE TABLE IF NOT EXISTS, CREATE OR REPLACE VIEW,
-- and CHECK constraints. Mirrors the conventions of schemas/citations.sql.
CREATE TABLE IF NOT EXISTS stage2_run (
    run_id VARCHAR PRIMARY KEY,
    built_at TIMESTAMP NOT NULL,
    parser_version VARCHAR NOT NULL,
    input_root VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS stage2_input (
    run_id VARCHAR NOT NULL REFERENCES stage2_run(run_id),
    path VARCHAR NOT NULL,
    sha256 VARCHAR NOT NULL,
    modified_at TIMESTAMP,
    PRIMARY KEY (run_id, path)
);

CREATE TABLE IF NOT EXISTS stage2_document (
    document_id VARCHAR PRIMARY KEY,
    path VARCHAR NOT NULL UNIQUE,
    content_sha256 VARCHAR NOT NULL,
    modified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS entity (
    entity_id VARCHAR PRIMARY KEY,
    local_id VARCHAR NOT NULL,
    canonical_name VARCHAR NOT NULL,
    type VARCHAR,
    boundary VARCHAR,
    boundary_stated BOOLEAN NOT NULL DEFAULT TRUE,
    stage1_source VARCHAR,
    section VARCHAR,
    confidence VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS metric (
    metric_id VARCHAR PRIMARY KEY,
    local_id VARCHAR NOT NULL,
    metric_name VARCHAR NOT NULL,
    value VARCHAR,
    unit VARCHAR,
    scope_conditions VARCHAR,
    conditions_stated BOOLEAN NOT NULL DEFAULT TRUE,
    claim_type VARCHAR,
    confidence VARCHAR,
    source_ref VARCHAR,
    stage1_source VARCHAR,
    section VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS stage2_claim (
    claim_id VARCHAR PRIMARY KEY,
    local_id VARCHAR NOT NULL,
    claim_text VARCHAR NOT NULL,
    claim_type VARCHAR NOT NULL,
    confidence VARCHAR NOT NULL,
    falsifier VARCHAR,
    falsifier_stated BOOLEAN NOT NULL DEFAULT TRUE,
    workflow_stage VARCHAR,
    source_refs VARCHAR,
    stage1_source VARCHAR,
    section VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS source_mirror (
    source_id VARCHAR PRIMARY KEY,
    local_id VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    url VARCHAR,
    publisher VARCHAR,
    classification VARCHAR,
    publication_date VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS predicate (
    predicate_id VARCHAR PRIMARY KEY,
    predicate VARCHAR NOT NULL,
    subject_type VARCHAR,
    object_type VARCHAR,
    direction VARCHAR,
    example VARCHAR,
    stage1_source VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS workflow_stage (
    stage_id VARCHAR PRIMARY KEY,
    local_id VARCHAR NOT NULL,
    stage_name VARCHAR NOT NULL,
    inputs VARCHAR,
    activities VARCHAR,
    outputs VARCHAR,
    quality_gates VARCHAR,
    roles VARCHAR,
    tools VARCHAR,
    evidence VARCHAR,
    confidence VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS extraction_decision (
    decision_id VARCHAR PRIMARY KEY,
    local_id VARCHAR NOT NULL,
    step VARCHAR,
    stage1_source VARCHAR,
    decision_type VARCHAR NOT NULL CHECK (
        decision_type IN (
            'scope_boundary', 'entity_merge', 'entity_split',
            'label_resolution', 'classification_conflict',
            'evidence_downgrade', 'falsifier_absent',
            'boundary_absent', 'condition_absent',
            'open_question', 'omission'
        )
    ),
    description VARCHAR,
    resolution VARCHAR,
    document_id VARCHAR NOT NULL REFERENCES stage2_document(document_id)
);

CREATE TABLE IF NOT EXISTS stage2_warning (
    warning_id VARCHAR PRIMARY KEY,
    run_id VARCHAR NOT NULL REFERENCES stage2_run(run_id),
    input_path VARCHAR NOT NULL,
    warning_type VARCHAR NOT NULL,
    message VARCHAR NOT NULL,
    raw_value VARCHAR
);

CREATE OR REPLACE VIEW unstated_boundaries AS
SELECT entity_id, local_id, canonical_name, type, document_id
FROM entity
WHERE boundary_stated = FALSE;

CREATE OR REPLACE VIEW unstated_conditions AS
SELECT metric_id, local_id, metric_name, document_id
FROM metric
WHERE conditions_stated = FALSE;

CREATE OR REPLACE VIEW missing_falsifiers AS
SELECT claim_id, local_id, document_id
FROM stage2_claim
WHERE falsifier_stated = FALSE;

CREATE OR REPLACE VIEW open_questions AS
SELECT decision_id, local_id, decision_type, description, document_id
FROM extraction_decision
WHERE decision_type IN ('open_question', 'omission');
