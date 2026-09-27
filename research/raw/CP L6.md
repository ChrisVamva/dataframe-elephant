# The Shift from ETL to ELT in Modern Data

**Research type:** Source-grounded raw research brief  
**Accessed:** 2026-09-27  
**Scope:** Analytical data integration patterns, cloud warehouses and lakehouses, workflow roles, and implications for access to source-faithful data.

## 1. Executive synthesis

- **Documented fact:** ETL transforms data before loading it into the analytical target; ELT loads first and transforms in that target. The distinction is the location and sequence of transformation, not whether data is transformed at all. [S1]
- **Documented fact:** The infrastructure makes ELT practical at scale: BigQuery explicitly separates storage and compute, and its compute can scale independently of storage. Snowflake describes independently managed storage and compute clusters. [S2, S3]
- **Documented fact:** Modern platforms support several patterns at once: batch and streaming loads, CDC, federated/external queries, transformations on load, and transformations after landing. BigQuery recommends ELT for most customers while retaining ETL for existing transformations or reducing use of BigQuery resources. [S1, S4, S5]
- **Inference:** The important change is a shift in the default *location* of analytics transformation toward managed cloud platforms, enabled by scalable analytical compute and SQL-based transformation tooling; it is not the disappearance of ETL.
- **Documented fact:** Landing source-faithful data can preserve fidelity and enable reprocessing, auditing, and downstream refinement. Databricks' bronze-layer guidance recommends retaining raw state and source metadata, then validating and cleaning downstream. [S6]
- **Correction to the premise:** Loading raw data can make it queryable in the platform, but does not automatically grant analysts or research engineers access. IAM/RBAC, row and column controls, masking, policy, curated layers, and source agreements still determine who can see it. [S7, S8]
- **Inference:** More data is not automatically more usable data. ELT shifts effort toward warehouse cost control, model ownership, lineage, tests, access policies, schema drift handling, and safe promotion of raw to curated datasets.
- **Recommendation:** Use a hybrid design: preserve source-faithful inputs in a governed landing area; do only necessary pre-load work (for example, security filtering or format adaptation); then build tested, documented, incremental transformations in the warehouse/lakehouse. Keep raw access restricted by default and grant broader use through governed refined or curated models.

## 2. Lens findings

### Methodology

- **Definition and scope:** ETL is extract, transform, load; transformation occurs before data enters the target. ELT is extract, load, transform; the target receives data before downstream transformations run there. Loading a minimally parsed raw representation can still involve serialization, type inference, or ingestion-time conversion; real pipelines are rarely literally “no transformation.” [S1, S4, S5]
- **Workflow position:** In both patterns, extraction and ingestion precede analytical modeling. The change is whether the major integration/business transformations happen upstream or inside the analytical platform.
- **Relationships:** ELT depends on an analytical target capable of storing and processing landed data, appropriate ingestion, transformation orchestration, and governance. dbt is one example of a modeling framework: models transform raw/source data into analytics-ready datasets, with tests and project structure. [S9, S10]
- **Trade-offs/failure modes:** ELT can simplify pipeline stages and reduce duplicated transformation runtimes, but may increase target compute/storage spend, leave poor-quality raw data exposed, defer errors to later stages, and create inconsistent downstream definitions without shared models. ETL can filter or transform data before the target and reuse existing processing, but may constrain re-use of discarded fields and require separate transformation infrastructure. Cost and performance are workload- and pricing-model-specific; neither pattern is universally cheaper.
- **Evidence confidence:** High for definitions and documented product capabilities; medium for general trade-offs, which depend on workload and controls.

### Technology and software

- **Definition and scope:** Cloud analytical warehouses/lakehouses provide managed storage and query/compute; ingestion tools move or expose source data; transformation frameworks coordinate reusable models and checks.
- **Representative examples:** BigQuery and Snowflake document cloud analytical storage/compute and multiple loading options. BigQuery lists Dataform and BigQuery pipelines for in-platform transformations; Snowflake lists SQL, Dynamic Tables, Streams/Tasks, Snowpark, and dbt. dbt models can transform loaded source data and tests assert properties of model outputs. [S1-S5, S9, S10]
- **Relationships:** Cloud infrastructure enables but does not require ELT; connectors, orchestration, transformation code, and storage formats determine the implementation. Federation/external tables query data in place and may avoid loading; that is a related access pattern, not strictly ELT because the data is not first loaded into the target. [S4, S5]
- **Trade-offs/failure modes:** Warehouse-native SQL is accessible to SQL-skilled analysts and keeps transformations near the data, but ties execution and often model behavior to the target platform. Federated reads avoid copies but introduce external-source performance/availability dependencies. Streaming and CDC add freshness while increasing operational complexity.
- **Evidence confidence:** High for documented features; medium for comparative performance or portability claims.

### Workflow

- **Definition and scope:** A governed pipeline from source capture through source-faithful landing, validated/refined data, business-oriented models, and consumption.
- **Representative pattern:** Databricks describes bronze as raw ingestion, silver as validated/cleaned/enriched data, and gold as business-oriented analytics. It calls this a recommended design pattern, not a requirement. [S6]
- **Relationships:** Ingestion establishes the landing record; transformations build dependent models; tests, lineage, and access controls govern transitions and consumption. Google documents table/column lineage and quality scans; dbt documents reusable data tests. [S7, S10]
- **Trade-offs/failure modes:** Treating “raw” as synonymous with “trusted” is a quality failure. Over-cleaning at ingestion can discard evidence; never promoting or validating raw data leaves consumers with unstable schemas and inconsistent logic.
- **Evidence confidence:** High for vendor-documented examples; medium for the generalized recommendation.

### Skills and market positions

- **Definition and scope:** The change redistributes work across data engineers, analytics engineers, and analysts; it does not establish that one job title owns the full pipeline.
- **Core capabilities:** Source/connector design, SQL and target-platform operation, incremental modeling, testing, version control/CI, lineage, permissions, privacy review, and cost/performance monitoring. dbt's documented workflow includes source definitions, models, tests, documentation, and downstream exposures. [S9, S10]
- **Relationships:** Data engineers commonly own reliable ingestion and platform operation; analytics engineers commonly encode reusable tested business logic; analysts and research engineers consume curated and, when authorized, source-faithful data for analysis. These are role-pattern inferences, not a universal division of labor.
- **Trade-offs/failure modes:** Moving transformations into a warehouse can bring analysts closer to source data and business logic, while also placing production responsibilities (tests, change management, cost, and access rules) nearer to them. Giving access without these skills or guardrails raises data misuse and inconsistent-metric risks.
- **Evidence confidence:** Medium. Product documentation demonstrates capabilities and workflow artifacts, not industry-wide role boundaries or hiring prevalence. Job-posting research is required to quantify labor-market change.

### Products and companies

- **Definition and scope:** Cloud platform vendors provide target storage/compute and native ingestion/governance features; transformation-framework vendors provide modeling, testing, and development workflows; connectors and ETL vendors provide extraction/loading and may also transform.
- **Representative examples:** Google Cloud BigQuery / Dataform; Snowflake / Snowpark and native loading; Databricks lakehouse / medallion guidance; dbt Labs' dbt framework. [S1-S10]
- **Relationships:** These are complementary ecosystem components rather than interchangeable products. A deployment may combine a source connector, cloud platform, transformation framework, orchestration, catalog/lineage, and BI layer.
- **Trade-offs/failure modes:** Vendor guidance is useful for product behavior but is not independent proof that its recommended architecture is best for every workload. Portability, existing contracts and infrastructure, residency, operational skills, price, and governance requirements affect selection.
- **Evidence confidence:** High for named product capabilities; low for comparative market share, adoption, or hiring trends, not evaluated here.

### Agents

- **Definition and scope:** An agent is not required for ELT. In an agent-assisted ELT workflow, a research or coding agent might draft source documentation, transformation SQL, tests, or schema-change investigations; a human or controlled deployment pipeline should review and verify changes.
- **Workflow position:** Potential support for source profiling, model scaffolding, test generation, failure triage, and documentation; not a substitute for deterministic ingestion, permissions, or production acceptance checks.
- **Trade-offs/failure modes:** Incorrect assumptions about identifiers, nulls, units, event time, or sensitive fields can produce plausible but wrong models. Agent-generated SQL must be reviewed, tested against representative data, and run with least-privilege access.
- **Evidence confidence:** Low for ELT-specific productivity outcomes; recommendation based on workflow risk, not measured evidence in this source set.

## 3. Workflow map

| Stage | Inputs and activities | Outputs | Quality checks / gates | Likely tools and roles |
| --- | --- | --- | --- | --- |
| 1. Source and purpose | Source systems/files/events; define intended uses, legal basis, sensitivity, freshness, and retention | Approved source inventory and ingestion contract | Owner approval; allowed-use and retention review; source completeness expectations | Source owner, data engineer, security/privacy; catalog |
| 2. Extract and ingest | Batch files, APIs, streams, CDC; select load, streaming, or external/federated access | Landed source-faithful data plus load metadata, or governed external reference | Reconciliation/counts, timestamps, duplicate/replay behavior, schema-change alerts, failed-row handling | Connectors, BigQuery load/CDC options, Snowflake COPY/Snowpipe; data engineer |
| 3. Raw/landing zone | Preserve received records and source identifiers; add ingestion time, source, batch/offset, and schema/version metadata | Reprocessable raw tables/files | Restricted access; immutable/append strategy where appropriate; replay and retention policy; verify no unintended loss | Object storage, warehouse/lakehouse bronze; engineer, steward |
| 4. Refine and validate | Parse, type, normalize, deduplicate, resolve late data, quarantine invalid records | Stable non-aggregated, cleaned/refined models | Schema enforcement/evolution policy; null/uniqueness/referential/business-rule tests; rejected-row review | SQL, Dataform/dbt, warehouse-native tasks; analytics engineer/data engineer |
| 5. Business modeling | Join sources; define entities, dimensions, measures, and reusable semantics | Curated domain models and metrics | Metric-owner sign-off; lineage review; regression tests; freshness and cost thresholds | dbt/Dataform, warehouse SQL, semantic layer; analytics engineer/domain analyst |
| 6. Access and consume | Grant role-appropriate access; query, analyze, visualize, or train models | Governed datasets, analyses, reports | Least privilege; row/column policy and masking; audit logs; reproducibility and interpretation review | IAM/RBAC, catalog, SQL/BI/notebooks; steward, analyst, research engineer |
| 7. Operate and iterate | Monitor loads, models, freshness, quality, cost, and user needs; replay or revise | Alerted, maintained pipeline and new research questions | SLOs, lineage, rollback/reprocessing plan, cost budgets, incident response | Orchestration, logs/metrics, catalog; platform and data teams |

**Practical pattern:** preserve raw inputs, apply only required security/technical normalization before or during ingestion, then transform in governed warehouse/lakehouse layers. Keep an explicit exception path for cases needing pre-load transformation or federation. ELT does not mean granting universal raw-table access.

## 4. Entity and relationship candidates

| Entity | Name | Definition | Workflow stage | Related entities | Relationship type | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Methodology | ETL | Transform extracted data before loading to the target | Extract/transform/load | Source, transformation, target, ETL tool | transforms_before_loading | [S1] | High |
| Methodology | ELT | Load extracted data to the target, then transform there | Extract/load/transform | Source, target, model, warehouse compute | transforms_after_loading | [S1] | High |
| Technology | Cloud analytical warehouse | Managed analytical storage and query compute; some platforms decouple resources | Storage/query/transform | Cloud platform, table, compute | stores_and_executes | [S2, S3] | High |
| Methodology | Raw landing zone | Governed layer preserving source-faithful ingested records and metadata | Ingestion | Source, ingestion event, refined model | preserves/reprocesses | [S6] | High |
| Methodology | Medallion architecture | Optional layered data-quality design, commonly bronze/silver/gold | Landing/refinement/serving | Raw, refined, curated datasets | organizes_by_quality | [S6] | High |
| Software | dbt | Framework for transforming data through project models and engineering workflows | Transform/test/document | Warehouse, model, test, source | implements/transforms | [S9, S10] | High |
| Product | BigQuery | Managed analytics platform supporting load, stream, CDC, federation, ETL and ELT options | Ingest/query/transform | Google Cloud, Dataform, source | loads/queries/transforms | [S1, S4, S5] | High |
| Product | Snowflake | Cloud data platform with storage/compute architecture and multiple ingestion/transformation options | Ingest/query/transform | Cloud storage, virtual warehouse, Snowpark, dbt | stores/executes | [S2, S3, S8] | High |
| Quality control | Data test | Assertion over a source/model, with failing records when the assertion is false | Transform/promotion | Model, business rule, pipeline | validates | [S10] | High |
| Governance control | Access policy | Role/resource and row/column controls determining who can read data | All stages, especially consumption | User, role, dataset, table, sensitive field | restricts_access | [S7, S8] | High |
| Market position | Analytics engineer | Role-pattern inference for a practitioner creating tested, reusable analytical models | Transform/model | SQL, dbt/Dataform, warehouse, analyst | builds_models | [S9, S10] | Medium |
| Agent | Transformation assistant | Proposed agent that drafts or investigates pipeline artifacts under review | Transform/operate | Model, tests, human reviewer | assists/does_not_approve | Synthesis | Low |

## 5. Comparison tables

### ETL, ELT, and federation

| Criterion | ETL | ELT | Federation/external query |
| --- | --- | --- | --- |
| Where main transformation runs | Before target load | After load, in analytical target | Query-time over data remaining in external storage/source |
| Data copied to target | Usually transformed result; raw retention is optional | Raw/source-faithful landing is common but not mandatory | Often no full copy; metadata/reference is registered |
| Strong fit when | Existing upstream transformations, pre-target filtering, target/resource constraints | Target can store/process data; SQL-based refinement and multiple downstream uses matter | Avoiding copies or querying only a subset is useful and source access/performance suffice |
| Main risks | Upstream complexity; less retained source detail if discarded | Cost, access exposure, schema drift, inconsistent models if governance is weak | External latency/availability/format limitations; query consistency and source constraints |
| Evidence | BigQuery documents existing transformations and reducing BigQuery resource use as ETL reasons. [S1] | BigQuery recommends ELT to most customers; Databricks describes layered raw-to-curated refinement. [S1, S6] | BigQuery and Snowflake document external/federated data access. [S4, S5] |

### Common architectural choices

| Choice | Purpose | Strength | Limitation to evaluate |
| --- | --- | --- | --- |
| Batch load | Periodic/bulk ingestion | Simpler for non-real-time sources; BigQuery says it may be less expensive/resource-intensive when sources change infrequently | Data latency and batch failure/replay behavior |
| Streaming / CDC | Near-real-time changes | Timely data; CDC can replicate row-level changes | Ordering, replay, deletes, schema evolution, and ongoing operations |
| In-warehouse SQL models | Reusable transformations close to data | Familiar SQL workflow; versioned/tested models are supported by dbt/Dataform | Warehouse dialect coupling, compute consumption, dependency discipline |
| Layered raw/refined/curated data | Promote data quality and fit consumers | Preserve detail while providing stable analytics products | Layer count can become ceremony; define ownership and promotion criteria |

## 6. Research gaps and next investigations

- **Adoption and history:** This brief establishes current platform support, not a measured timeline or rate of migration. Compare archived architecture guidance and survey data; avoid vendor adoption claims without independent evidence.
- **Economics:** Benchmark representative pipelines under comparable data volume, query frequency, retention, egress, and pricing. Storage/compute separation enables independent scaling but does not by itself prove ELT costs less.
- **Access outcomes:** Interview research engineers and analysts about whether landing raw data actually expanded usable access, what permissions were granted, and how often raw data was used directly versus through refined models.
- **Regulated/legacy cases:** Investigate privacy minimization, residency, encryption/key controls, deletion obligations, auditability, and systems where data must be transformed or tokenized before entering a general-purpose warehouse.
- **Data quality and drift:** Compare incident and recovery practices for raw preservation, schema evolution, CDC correctness, late-arriving data, replay, and quarantine across platforms.
- **Role boundaries:** Analyze recent job postings and team structures to test whether ELT increased demand for analytics engineering or shifted production ownership toward analysts. Current evidence here is architectural, not labor-market data.
- **Tool neutrality:** Expand platform comparisons to Redshift, Synapse/Fabric, open lakehouse stacks, and self-managed/on-prem systems; current product examples are selective and vendor documentation has positioning bias.
- **Falsification tests:** The thesis weakens if a workload cannot query landed data efficiently, policy requires pre-load redaction, the source is too sensitive/large/costly to retain, or a measured end-to-end comparison shows upstream transformation is simpler, safer, and cheaper.

## 7. Sources

Access date for all sources: **2026-09-27**. Vendor documentation is primary evidence for each product's own features and recommendations, but carries vendor-positioning bias. No independent adoption statistics or job-market measurements were gathered.

| ID | Source | Publisher / date | Claims supported |
| --- | --- | --- | --- |
| S1 | [Introduction to loading, transforming, and exporting data](https://docs.cloud.google.com/bigquery/docs/load-transform-export-intro) | Google Cloud BigQuery documentation; last updated 2026-09-24 | ETL/ELT definitions; BigQuery's recommendation of ELT to most customers; ETL reasons; reverse ETL distinction |
| S2 | [Overview of BigQuery storage](https://docs.cloud.google.com/bigquery/docs/storage_overview) | Google Cloud BigQuery documentation; last updated 2026-09-24 | Independent scaling of storage and compute; batch, streaming, and table storage patterns |
| S3 | [Snowflake key concepts and architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts) | Snowflake documentation; publication/update date not shown in fetched page | Storage and compute layers; independently operating virtual warehouses; ingestion and transformation options |
| S4 | [Introduction to loading data](https://docs.cloud.google.com/bigquery/docs/loading-data) | Google Cloud BigQuery documentation; last updated 2026-09-24 | Batch, streaming, CDC, and federation/external-data access options |
| S5 | [Overview of data loading](https://docs.snowflake.com/en/user-guide/data-load-overview) | Snowflake documentation; publication/update date not shown in fetched page | Load-time casts/column operations; Snowpipe staging and transformations; external-table alternative; error logging and limits |
| S6 | [What is the medallion lakehouse architecture?](https://docs.databricks.com/aws/en/lakehouse/medallion) | Databricks documentation; last updated 2026-09-11 | Bronze raw retention/provenance; silver validation/cleaning; gold business models; architecture is recommended, not required |
| S7 | [Introduction to data governance in BigQuery](https://docs.cloud.google.com/bigquery/docs/data-governance) | Google Cloud BigQuery documentation; last updated 2026-09-24 | IAM, row/column access, masking, audit, lineage, quality scans, stewardship |
| S8 | [Overview of Access Control](https://docs.snowflake.com/en/user-guide/security-access-control-overview) | Snowflake documentation; publication/update date not shown in fetched page | RBAC/DAC, securable objects, privileges, role-based authorization |
| S9 | [What is dbt?](https://docs.getdbt.com/docs/introduction) | dbt Labs documentation; last updated 2026-09-10 | dbt transformation workflow, modular SQL/Python models, deployment, tests and documentation |
| S10 | [Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests) | dbt Labs documentation; last updated 2026-09-16 | Data-test assertions, common constraints, failing-row semantics and reusable tests |

### Evidence labels used

- **Documented fact:** Explicitly described by a cited first-party source; scope is limited to what that source documents.
- **Reported signal:** A source's recommendation or characterization, attributed to its publisher rather than treated as consensus.
- **Inference:** Synthesis from cited capabilities or workflow implications, not a directly measured fact.
- **Recommendation:** Proposed operating guidance derived from the evidence and identified risks.