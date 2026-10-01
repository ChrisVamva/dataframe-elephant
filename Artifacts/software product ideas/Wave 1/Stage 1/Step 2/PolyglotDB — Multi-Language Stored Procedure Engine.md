# PolyglotDB — Multi-Language Stored Procedure Engine

**Step 2: Initial Product Approach**
**Source:** Derived from `Step 1/NovelProductSuggestions1.md` — Product #5
**Date:** 2026-10-01

---

## 1. Product Vision

### 1.1 Problem Statement

Modern data-intensive applications need to perform diverse operations within database transactions:
- **Set-based operations** (joins, aggregations, window functions) — best expressed in SQL
- **Data science logic** (statistical analysis, ML inference, feature engineering) — best expressed in Python
- **High-performance transforms** (streaming aggregations, custom data structures, concurrent processing) — best expressed in Go

Current databases force developers to choose **one** procedural language (PL/pgSQL, T-SQL, PL/SQL). This creates an impedance mismatch: either you push application logic into the database (and lose ecosystem richness), or you pull data out to application servers (and lose transactional integrity, network round-trips, and data locality).

### 1.2 Solution

PolyglotDB is a database extension that allows stored procedures to be written in **multiple languages** within a single query plan. The engine:

1. **Compiles** Go procedures to native shared libraries (via CGO)
2. **Embeds** Python interpreters in isolated sub-processes (with resource limits)
3. **Optimizes** SQL queries alongside procedural extensions in a unified planner
4. **Coordinates** all three within a single ACID transaction boundary

### 1.3 Value Proposition

| Stakeholder | Benefit |
|-------------|---------|
| **Data Engineers** | Write ETL logic in the language best suited for each step — no context switching |
| **ML Engineers** | Run inference inside the database — no data movement, no serialization overhead |
| **Platform Teams** | One database, one transaction model, multiple language runtimes |
| **CTOs** | Reduced infrastructure (no separate stream processing + DB + ML serving) |

---

## 2. Technical Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Application                       │
│              (SQL with embedded procedure calls)              │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                   PolyglotDB Engine                          │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   SQL Planner │  │  Procedure   │  │   Transaction    │  │
│  │   & Optimizer │  │  Router      │  │   Coordinator    │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘  │
│         │                  │                    │            │
│  ┌──────▼───────┐  ┌──────▼───────┐  ┌────────▼─────────┐  │
│  │  SQL Engine  │  │  Go Runtime  │  │  Python Runtime  │  │
│  │  (Native)    │  │  (CGO/Plugin)│  │  (Embedded)      │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Storage Engine (RocksDB/PostgreSQL)      │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Core Components

#### A. Procedure Router

The router is the brain of PolyglotDB. It:
- Parses procedure calls in SQL (e.g., `CALL ml_inference('model_v2', data)`)
- Determines which runtime should execute the procedure
- Manages data marshaling between runtimes
- Enforces transactional consistency across runtimes

**Implementation:** Go (for performance and concurrency)

#### B. Go Runtime (Native Plugin System)

Go procedures are compiled as C-compatible shared libraries (`.so`/`.dll`) and loaded via CGO. This provides:
- **Near-native performance** — no serialization overhead
- **Type safety** — Go's type system prevents data marshaling errors
- **Concurrency** — goroutines for parallel processing within a procedure

**Interface contract:**
```go
// Procedure is the interface all Go procedures must implement
type Procedure interface {
    Name() string
    InputType() reflect.Type
    OutputType() reflect.Type
    Call(ctx context.Context, input []byte) ([]byte, error)
}
```

#### C. Python Runtime (Embedded Interpreter)

Python procedures run in an embedded CPython interpreter with:
- **Resource limits** — CPU time, memory, and syscall restrictions
- **Isolation** — each procedure runs in a sub-interpreter (PEP 554)
- **Data exchange** — Apache Arrow for zero-copy data transfer

**Interface contract:**
```python
# Python procedures use a decorator-based registration
@procedure(name="ml_inference", input_type="arrow", output_type="arrow")
def ml_inference(batch: pa.RecordBatch) -> pa.RecordBatch:
    model = load_model("model_v2")
    return model.predict(batch)
```

#### D. SQL Engine Integration

PolyglotDB extends the SQL planner to treat procedure calls as first-class query operators:
- Procedures can appear in `SELECT`, `WHERE`, `JOIN`, and `INSERT` clauses
- The optimizer can push down predicates into procedures
- Procedures can be composed in CTEs (Common Table Expressions)

**Example query:**
```sql
WITH features AS (
    SELECT customer_id, feature_vector FROM customer_events
    WHERE event_date > NOW() - INTERVAL '30 days'
),
predictions AS (
    CALL ml_inference('churn_model_v3', features) AS (customer_id INT, churn_score FLOAT)
)
SELECT c.name, p.churn_score
FROM customers c
JOIN predictions p ON c.id = p.customer_id
WHERE p.churn_score > 0.8;
```

---

## 3. Language Integration Strategy

### 3.1 Why These Three Languages?

| Language | Role | Rationale |
|----------|------|-----------|
| **SQL** | Set-based operations | Declarative, optimized by decades of research, universal in data |
| **Python** | Data science & ML | Unmatched ecosystem (pandas, scikit-learn, PyTorch), readable |
| **Go** | High-performance transforms | Fast compilation, excellent concurrency, static binaries, CGO for native interop |

### 3.2 Data Marshaling

The biggest challenge in multi-language systems is data exchange. PolyglotDB uses a tiered approach:

| Scenario | Mechanism | Overhead |
|----------|-----------|----------|
| SQL ↔ Go | Direct C structs via CGO | Near-zero |
| SQL ↔ Python | Apache Arrow (columnar) | Low (zero-copy for numeric) |
| Go ↔ Python | Apache Arrow via C bridge | Low |
| Complex types | Protocol Buffers | Medium (serialization cost) |

**Apache Arrow** is the universal interchange format because:
- It has native bindings for Go, Python, and C
- It supports zero-copy reads for columnar data
- It integrates with pandas, Polars, and DuckDB

### 3.3 Transaction Coordination

All three runtimes participate in a single ACID transaction:

1. **BEGIN** — The transaction coordinator acquires locks and starts a write-ahead log entry
2. **Procedure execution** — Each runtime executes within the transaction context:
   - Go: participates via CGO callbacks into the storage engine
   - Python: holds a transaction-scoped snapshot, writes to a temp buffer
   - SQL: normal transactional semantics
3. **COMMIT/ROLLBACK** — Two-phase commit across all runtimes:
   - Phase 1: All runtimes prepare (flush buffers, validate constraints)
   - Phase 2: If all succeed, commit; otherwise, rollback all

---

## 4. Development Phases

### Phase 1: Proof of Concept (Months 1-3)

**Goal:** Demonstrate that a Python procedure can run inside a SQL query with correct transactional semantics.

**Deliverables:**
- [ ] Embedded CPython interpreter in a Go host process
- [ ] Arrow-based data exchange between Go and Python
- [ ] Single procedure call: `CALL py_hello()` returns a value
- [ ] Basic transaction rollback on Python exception

**Tech stack:** Go (host), CPython (embedded), Apache Arrow (data exchange)

**Success criteria:** A Python function that processes 1M rows in < 2 seconds within a transaction.

---

### Phase 2: Go Native Procedures (Months 4-6)

**Goal:** Add Go as a first-class procedure language with CGO-based native execution.

**Deliverables:**
- [ ] Go procedure compiler (Go source → shared library)
- [ ] CGO bridge for direct struct passing
- [ ] Procedure registry and discovery
- [ ] Concurrent procedure execution with goroutines

**Tech stack:** Go (procedures + runtime), CGO (FFI), plugin package (dynamic loading)

**Success criteria:** A Go procedure that performs 10x faster than equivalent Python for CPU-bound transforms.

---

### Phase 3: SQL Planner Integration (Months 7-9)

**Goal:** Integrate procedure calls into the SQL query planner as first-class operators.

**Deliverables:**
- [ ] SQL parser extension for `CALL` syntax
- [ ] Query optimizer that can push predicates into procedures
- [ ] CTE support for procedure composition
- [ ] EXPLAIN output showing procedure execution plans

**Tech stack:** SQL parser (lib_query or custom), optimizer (cost-based), EXPLAIN (visualization)

**Success criteria:** A complex query joining SQL tables with Python and Go procedures, optimized correctly.

---

### Phase 4: Production Hardening (Months 10-12)

**Goal:** Make PolyglotDB production-ready with monitoring, security, and operational tooling.

**Deliverables:**
- [ ] Resource limits (CPU, memory, execution time per procedure)
- [ ] Procedure sandboxing (seccomp, AppArmor for Python)
- [ ] Monitoring and observability (Prometheus metrics, OpenTelemetry tracing)
- [ ] Backup/restore with procedure definitions
- [ ] Documentation and SDKs

**Tech stack:** Prometheus (metrics), OpenTelemetry (tracing), seccomp (sandboxing)

**Success criteria:** 99.9% uptime under load, < 5ms overhead per procedure call, security audit passed.

---

## 5. Technical Challenges & Solutions

### Challenge 1: Python GIL and Concurrency

**Problem:** CPython's Global Interpreter Lock (GIL) prevents true parallelism in Python procedures.

**Solution:** 
- Use Python sub-interpreters (PEP 554) for isolation
- For CPU-bound work, recommend Go procedures instead
- For I/O-bound work, release the GIL during Arrow data transfer

### Challenge 2: Memory Management Across Runtimes

**Problem:** Go uses garbage collection, Python uses reference counting, SQL uses manual memory management. Coordinating these is complex.

**Solution:**
- Use Apache Arrow's memory pool for all cross-runtime data exchange
- Each runtime manages its own memory within its boundary
- The transaction coordinator tracks all allocations for rollback

### Challenge 3: Error Handling and Recovery

**Problem:** A panic in Go or an exception in Python must not crash the database.

**Solution:**
- Go procedures run in a separate process (crash isolation)
- Python procedures run in a sub-interpreter (exception isolation)
- The transaction coordinator catches all errors and rolls back cleanly

### Challenge 4: Query Optimization with Opaque Procedures

**Problem:** The SQL optimizer cannot see inside procedures to optimize them.

**Solution:**
- Procedures declare their selectivity and cost model
- The optimizer uses these estimates for planning
- Future: ML-based cost estimation based on runtime statistics

---

## 6. Competitive Landscape

| Product | Approach | Limitation |
|---------|----------|------------|
| **PostgreSQL + PL/pgSQL** | Single procedural language | No Python/Go ecosystem |
| **PostgreSQL + PL/Python** | Python in database | No Go, GIL limits, no Arrow |
| **SQL Server + CLR** | .NET in database | Windows-only, no Python |
| **External ETL (Airflow + Spark)** | Data leaves the database | Network overhead, no transactions |
| **PolyglotDB** | Multi-language in one engine | New, unproven |

---

## 7. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Procedure call overhead | < 5ms | Benchmark vs. native SQL |
| Python ↔ Go data transfer | < 1ms per 1M rows | Arrow zero-copy benchmark |
| Transaction throughput | > 10K TPS | TPC-C variant with procedures |
| Query planning with procedures | < 50ms | EXPLAIN ANALYZE |
| Crash isolation | 0 data corruption | Fault injection testing |

---

## 8. Team & Responsibilities

| Role | Responsibility | Skills Needed |
|------|---------------|---------------|
| **Database Engine Engineer** | SQL planner, storage engine, transactions | C/Rust, database internals |
| **Go Runtime Engineer** | Go procedure runtime, CGO bridge | Go, CGO, systems programming |
| **Python Runtime Engineer** | CPython embedding, Arrow integration | Python internals, C API |
| **Query Optimizer Engineer** | Cost-based optimization with procedures | Database theory, statistics |
| **DevOps/Security Engineer** | Sandboxing, monitoring, deployment | Linux, seccomp, Prometheus |

---

## 9. Open Questions

1. **Should we build on PostgreSQL or create a new storage engine?**
   - Building on PostgreSQL gives us a mature storage engine and ecosystem
   - A new engine (RocksDB-based) gives more control but less compatibility

2. **How do we handle Python package dependencies?**
   - Option A: Pre-installed packages (limited)
   - Option B: Procedure-specific virtual environments (complex)
   - Option C: WASM-compiled Python packages (future)

3. **What is the licensing model?**
   - Open source (Apache 2.0) with commercial support
   - Open core with enterprise features (monitoring, security)

4. **How do we ensure backward compatibility?**
   - Versioned procedure APIs
   - Migration tools for procedure upgrades

---

## 10. Next Steps

1. **Validate the concept** — Build a minimal prototype (Phase 1) and benchmark against PostgreSQL + PL/Python
2. **Engage the community** — Present at database conferences (PGCon, SIGMOD) and gather feedback
3. **Secure funding** — Apply for grants or seek venture capital based on prototype results
4. **Build the team** — Hire database engine and Go/Python runtime engineers
5. **Establish partnerships** — Partner with cloud providers (AWS, GCP) for managed PolyglotDB offerings

---

## Appendix A: Example Use Cases

### A.1 Real-Time ML Inference

```sql
-- Score transactions for fraud in real-time
INSERT INTO fraud_alerts (transaction_id, score, flagged)
SELECT t.transaction_id, f.score, f.score > 0.9
FROM transactions t
CALL fraud_model_v4(t.amount, t.merchant_id, t.user_id, t.timestamp) AS (score FLOAT)
WHERE t.processed = FALSE;
```

### A.2 Feature Engineering

```sql
-- Compute ML features within the same transaction
WITH user_features AS (
    SELECT
        user_id,
        COUNT(*) AS transaction_count,
        AVG(amount) AS avg_amount,
        STDDEV(amount) AS stddev_amount
    FROM transactions
    WHERE created_at > NOW() - INTERVAL '90 days'
    GROUP BY user_id
),
engineered AS (
    CALL feature_engineering(user_features) AS (
        user_id INT,
        risk_score FLOAT,
        activity_bucket TEXT
    )
)
SELECT * FROM engineered WHERE risk_score > 0.7;
```

### A.3 High-Performance Aggregation

```sql
-- Go procedure for streaming aggregation
SELECT
    date_trunc('hour', event_time) AS hour,
    CALL hyperloglog_count(user_id) AS unique_users,
    CALL approx_percentile(latency, 0.99) AS p99_latency
FROM events
WHERE event_time > NOW() - INTERVAL '24 hours'
GROUP BY 1;
```

---

## Appendix B: Reference Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     PolyglotDB Architecture                  │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                  SQL Frontend                        │    │
│  │  Parser → Analyzer → Planner → Optimizer → Executor  │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐    │
│  │               Procedure Router                       │    │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────────────────┐  │    │
│  │  │ SQL     │  │ Go      │  │ Python              │  │    │
│  │  │ Handler │  │ Handler │  │ Handler             │  │    │
│  │  └────┬────┘  └────┬────┘  └──────────┬──────────┘  │    │
│  └───────┼────────────┼───────────────────┼─────────────┘    │
│          │            │                   │                  │
│  ┌───────▼────────────▼───────────────────▼─────────────┐    │
│  │              Apache Arrow (Data Exchange)             │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐    │
│  │           Transaction Coordinator (2PC)              │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐    │
│  │         Storage Engine (PostgreSQL/RocksDB)          │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

*Document version: 1.0*
*Last updated: 2026-10-01*
*Author: Product Engineering Team*
