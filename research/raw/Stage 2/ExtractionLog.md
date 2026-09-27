---
stage: 2
created: 2026-09-27
extracted_from:
  - research/raw/Stage 1/CNE DPS 4.1 F.md
  - research/raw/Stage 1/CP L6.md
  - research/raw/Stage 1/C.md
  - research/raw/Stage 1/DC L5.6.md
  - research/raw/Stage 1/DPS.md
  - research/raw/Stage 1/FAI.md
  - research/raw/Stage 1/ANT GP H.md
  - research/raw/Stage 1/OP MS 1.3F.md
  - research/raw/Stage 1/Q.md
  - research/raw/Stage 1/G0.md
  - research/raw/Stage 1/G1.md
  - research/raw/Stage 1/G2.md
  - research/raw/Stage 1/G3.md
  - research/raw/Stage 1/Citations/Citation.md
  - research/raw/Stage 1/Citations/Report.md
extractor: stage2-extractor-agent
gate_results:
  gate_1_source_coverage: pass
  gate_2_claim_traceability: pass
  gate_3_evidence_class_integrity: pass
  gate_4_metric_conditions: pass
  gate_5_entity_completeness: pass
  gate_6_extraction_log_completeness: pass
  gate_7_ingestibility: pass
---

| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
| L001 | Step 2 | CNE DPS 4.1 F.md | omission | Multiple URLs found: https://docs.unstructured.io/ · https://docs.llamaindex.ai/ | Kept only the primary URL: https://docs.unstructured.io/ |
| L002 | Step 2 | CNE DPS 4.1 F.md | omission | Multiple URLs found: https://openlineage.io/docs/spec/object-model/ · https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html | Kept only the primary URL: https://openlineage.io/docs/spec/object-model/ |
| L003 | Step 2 | CNE DPS 4.1 F.md | omission | Multiple URLs found: https://openai.github.io/openai-agents-python/agents/ · https://openai.github.io/openai-agents-python/tracing/ · https://docs.crewai.com/ | Kept only the primary URL: https://openai.github.io/openai-agents-python/agents/ |
| L004 | Step 2 | CNE DPS 4.1 F.md | omission | Source '**Internal vault notes** (synthesis sources, not external evidence): [[ANT GP H]], [[C]], [[DPS]], [[FAI]], [[Q]], [[OP MS 1.3F]], [[DC L5.6]], [[CP L6]], [[G0]]–[[G3]], [[Citations/Citation]], [[Citations/Report]]' has no URL. | Created source entry with blank URL. |
| L005 | Step 2 | CNE DPS 4.1 F.md | omission | Multiple URLs found: https://www.w3.org/TR/sparql11-query/ · https://www.w3.org/TR/owl2-overview/ · https://www.w3.org/TR/shacl/ | Kept only the primary URL: https://www.w3.org/TR/sparql11-query/ |
| L006 | Step 2 | CNE DPS 4.1 F.md | omission | Multiple URLs found: https://docs.cloud.google.com/bigquery/docs/load-transform-export-intro · https://docs.snowflake.com/en/user-guide/intro-key-concepts · https://docs.databricks.com/aws/en/lakehouse/medallion | Kept only the primary URL: https://docs.cloud.google.com/bigquery/docs/load-transform-export-intro |
| L007 | Step 2 | CNE DPS 4.1 F.md | omission | Multiple URLs found: https://docs.jupyter.org/ · https://observablehq.com/documentation/notebooks · https://observablehq.com/plot/ | Kept only the primary URL: https://docs.jupyter.org/ |
| L008 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity DuckDB has no boundary | Assigned [boundary not stated in source] |
| L009 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity DuckDB (technology) has no boundary | Assigned [boundary not stated in source] |
| L010 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity DuckDB Foundation has no boundary | Assigned [boundary not stated in source] |
| L011 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity DuckLabs has no boundary | Assigned [boundary not stated in source] |
| L012 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity AWS has no boundary | Assigned [boundary not stated in source] |
| L013 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity DuckLake has no boundary | Assigned [boundary not stated in source] |
| L014 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity MotherDuck has no boundary | Assigned [boundary not stated in source] |
| L015 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity pandas has no boundary | Assigned [boundary not stated in source] |
| L016 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Polars has no boundary | Assigned [boundary not stated in source] |
| L017 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity dbt has no boundary | Assigned [boundary not stated in source] |
| L018 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Semantic layer has no boundary | Assigned [boundary not stated in source] |
| L019 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Metabase has no boundary | Assigned [boundary not stated in source] |
| L020 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Superset has no boundary | Assigned [boundary not stated in source] |
| L021 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity LangGraph has no boundary | Assigned [boundary not stated in source] |
| L022 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Microsoft Agent Framework has no boundary | Assigned [boundary not stated in source] |
| L023 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity MCP has no boundary | Assigned [boundary not stated in source] |
| L024 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity A2A has no boundary | Assigned [boundary not stated in source] |
| L025 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity PROV has no boundary | Assigned [boundary not stated in source] |
| L026 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity PRISMA 2020 has no boundary | Assigned [boundary not stated in source] |
| L027 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Research/scout agent has no boundary | Assigned [boundary not stated in source] |
| L028 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity AI/agent workflow specialist has no boundary | Assigned [boundary not stated in source] |
| L029 | Step 3 | CNE DPS 4.1 F.md | boundary_absent | Entity Claim has no boundary | Assigned [boundary not stated in source] |
