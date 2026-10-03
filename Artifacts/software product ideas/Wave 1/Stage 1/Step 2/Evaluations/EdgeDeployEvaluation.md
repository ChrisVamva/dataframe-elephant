# EdgeDeploy — Step 2 Evaluation

**Date:** 2026-10-02
**Source:** Evaluation of `Wave 1/Stage 1/Step 2/EdgeDeploy.md` (Step 2: Initial Product Approach)
**Evaluator:** Product Engineering Team
**Baseline:** Step 1 evaluation (`Wave 1/Stage 1/Step 1/NovelIdeasEvaluation1.md`) — recorded 7.8/10, rank #1 of 12

---

## 1. Evaluation Methodology

This evaluation re-scores EdgeDeploy using the same five criteria and weights as the Step 1 evaluation (per `Evaluation_of_SoftwareIDEAS.md`), so the scores are directly comparable:

| Criterion | Weight |
|-----------|--------|
| **Technical Feasibility** | 25% |
| **Market Potential** | 25% |
| **Differentiation** | 20% |
| **Team Fit** | 15% |
| **Excitement** | 15% |

**Formula:** `Overall = (Feasibility × 0.25 + Market × 0.25 + Differentiation × 0.20 + Team Fit × 0.15 + Excitement × 0.15) × 2`

Because Step 2 documents contain specific, verifiable claims (toolchains, competitor capabilities, performance targets), this evaluation adds two layers on top of the scoring:

1. **Fact-check** of the document's key technical and competitive claims (Section 2)
2. **Document quality assessment** against the `FromStep1toStep2.md` checklist (Section 7)

---

## 2. Fact-Check of Key Claims

Competitive-landscape information was re-verified via web search on 2026-10-02. Verdict scale: **Accurate / Partially accurate / Inaccurate / Unvalidated**.

### 2.1 Problem Statement and Competitive Claims

| Claim in Document | Verdict | Evidence |
|-------------------|---------|----------|
| "Edge computing platforms force developers into a single language — typically JavaScript or WebAssembly" | **Inaccurate (outdated)** | Cloudflare Workers has accepted WASM modules compiled from any language for years (Rust is first-class via `workers-rs`; Go via TinyGo; C/C++ via Emscripten). Fastly Compute is WASM/WASI-native with official SDKs for Rust, JavaScript, Go, and C++. |
| "Python developers cannot use their data science ecosystem at the edge" | **Inaccurate (as of Sept 2026)** | Cloudflare made **Python Workers generally available on 2026-09-22**, using Pyodide/CPython compiled to WASM — the same architecture EdgeDeploy proposes for Python in Challenge 1. |
| "Edge computing is only accessible to JavaScript developers" | **Inaccurate** | Follows from the two rows above. The accurate statement is: non-JS languages are *second-class* (weaker tooling, bindings, and DX), not *excluded*. |
| Competitive table: Cloudflare Workers — "No Python/Go/Rust ecosystem" | **Inaccurate** | See above. |
| Competitive table: Fastly Compute — "No TypeScript/Python" | **Partially accurate** | TypeScript runs via the JavaScript SDK / AssemblyScript; Python is possible via WASM but has no first-class SDK. The gap is maturity, not absence. |
| Competitive table coverage | **Gap** | Omits direct competitors for "language-agnostic edge compute": **Fermyon** (Spin / Wasm Functions), **Wasmer Edge**, **wasmCloud**, and near-substitutes **Koyeb** and **Fly.io** (polyglot containers in many locations). |
| Lambda@Edge — "Node.js/Python only" | **Accurate** | Lambda@Edge remains Node.js/Python only (full Lambda supports more languages, but not at the edge). |
| Deno Deploy, Vercel Edge — JS/TS only | **Accurate** | Both remain JavaScript/TypeScript runtimes (both can load WASM modules, but with JS-centric DX). |

### 2.2 Language Toolchain Claims

| Claim in Document | Verdict | Evidence |
|-------------------|---------|----------|
| "TypeScript → WASM (via `wasm-pack` or `tsc` + `wasm-bindgen`)" | **Inaccurate** | `tsc` compiles TypeScript to JavaScript, not WASM. `wasm-pack` and `wasm-bindgen` are Rust tools. Realistic options: AssemblyScript (a TS-*like* language), embedding a JS engine as the WASM module (Javy-style), or running TS natively rather than via WASM. |
| "Python → WASM (via `pyodide` or `cryptography` + `wasm-pack`)" | **Partially accurate** | Pyodide is real and proven (Cloudflare uses it). "Cryptography + wasm-pack" is not a Python→WASM pipeline — this appears to be an error. Nuitka→C→`emcc` is correctly labeled experimental. |
| "Go → WASM (via `GOOS=js GOARCH=wasm go build`)" | **Partially accurate** | That target produces WASM for a *browser JavaScript host* (requires `wasm_exec.js`, no WASI). For a Wasmtime-based server runtime, the correct targets are `GOOS=wasip1` (Go 1.21+) or TinyGo. |
| "Rust → WASM (via `cargo build --target wasm32-unknown-unknown`)" | **Accurate** | Standard, proven path. |
| "C++ → WASM (via `emcc`)" | **Accurate** | Standard Emscripten path. |
| Wasmtime sandboxing: fuel metering, memory limits, WASI preview 1 subset | **Accurate** | Matches Wasmtime's actual capabilities; Challenge 4 is correctly rated Low risk. |
| Go example: goroutines/channels for "high-performance concurrent processing" | **Partially accurate** | Goroutines work in Go-WASM, but WASM threading support (wasi-threads) is immature and the `GOOS=js` target is single-threaded. The concurrency pitch oversells what WASM currently delivers. |

### 2.3 Performance and Infrastructure Targets

| Target | Assessment |
|--------|------------|
| Cold start < 50ms | **Achievable for small modules, not for Python.** Rust/Go/C++ WASM modules typically instantiate in single-digit milliseconds. Pyodide is ~10MB with a large heap — the document's own Challenge 1 notes this, yet the marquee use case (A.1: pandas at the edge) and the < 50ms target are internally inconsistent. Snapshotting may close part of the gap; memory density per tenant will still hurt unit economics. |
| Warm < 10ms p99, > 10K req/s per edge | **Plausible** for small WASI modules on commodity hardware. |
| 300+ edge locations | **Unvalidated — the largest unsolved dependency.** Open Question 1 acknowledges this, but understates it: CDN providers do not generally host third-party compute in their PoPs (that is their own product), and building/renting a global footprint is capital-intensive. A realistic Phase 3 outcome is 10–30 metros via hyperscaler regions and bare metal. |
| 12-month plan reaching 99.9% SLA + billing + security audit | **Aggressive.** Incumbents took years to reach this maturity; 18–24 months is more credible for a new team. |

### 2.4 Sources

- [Cloudflare makes Python Workers generally available](https://wire.vakker.pro) (2026-09-22)
- [Fastly developer documentation — Compute languages and SDKs](https://developer.fastly.com)
- [Fastly compute-actions CI plugins (Rust, JavaScript, Go, C++)](https://www.fastly.com)

---

## 3. Scored Evaluation

| Criterion | Score | Notes |
|-----------|-------|-------|
| Technical Feasibility | 3/5 | The core runtime stack is proven (Wasmtime/Rust, Go control plane, Hyper, gRPC). But the multi-language plan — the product's whole point — rests on partially wrong toolchain choices (TS→WASM, Go target), the Python story conflicts with the cold-start target, and WASI Preview 1 / Component Model churn guarantees rework. "Any language, first-class" is significantly harder than the document implies; "Rust/Go/C++ + one scripting story" is feasible. |
| Market Potential | 4/5 | Edge/serverless compute is a large, growing market with proven willingness to pay. But the wedge is narrower than claimed: the "excluded non-JS developer" population is now largely served by Cloudflare (WASM from any language + GA Python) and Fastly (polyglot WASI). The remaining pain — second-class DX and Python performance — is real but less acute, and incumbents own the distribution and the networks. |
| Differentiation | 3/5 | The central claim ("edge is JS-only") does not survive fact-checking, and Fastly/Fermyon/Wasmer already run "any WASI language at the edge." What remains is genuine but narrower: one unified, first-class DX across languages (same KV/cache/HTTP bindings everywhere), best-in-class Python performance, and an open-source runtime (incumbents are closed). Better in some ways, similar in others. |
| Team Fit | 4/5 | Rust, Go, and TypeScript are mainstream with good hiring pools, matching the Step 1 assessment. Specialized knowledge (Wasmtime internals, Pyodide, TinyGo, WASI spec evolution) is rarer but learnable. |
| Excitement | 5/5 | "Deploy any language to the edge" remains a compelling engineer-facing vision, and WASM attracts strong open-source community gravity. Unchanged from Step 1. |

**Overall: 7.4/10** — `(3×0.25 + 4×0.25 + 3×0.20 + 4×0.15 + 5×0.15) × 2 = 7.4`

### Score Movement vs. Step 1

| Criterion | Step 1 | This Evaluation | Δ | Primary Reason |
|-----------|--------|------------------|---|----------------|
| Technical Feasibility | 4 | 3 | −1 | Toolchain errors; Python/cold-start conflict; 300-PoP dependency |
| Market Potential | 5 | 4 | −1 | Wedge narrowed by Cloudflare Python GA and polyglot WASI incumbents |
| Differentiation | 4 | 3 | −1 | "JS-only edge" premise factually eroded; Fastly/Fermyon already polyglot |
| Team Fit | 4 | 4 | 0 | — |
| Excitement | 5 | 5 | 0 | — |
| **Overall** | **7.8 (recorded)** | **7.4** | **−0.4** | |

> **Note on the baseline:** applying the protocol formula strictly to Step 1's recorded scores for EdgeDeploy (4, 5, 4, 4, 5) yields **8.8/10**, not the recorded 7.8/10. The Step 1 overall scores appear to have been judgment-adjusted rather than formula-derived (the same discrepancy affects other Step 1 scores, e.g., Convex and PolyglotDB). Against the formula-strict baseline, this evaluation's 7.4 represents a **−1.4** correction, driven almost entirely by the fact-check in Section 2. The Step 1 document's scores should be recomputed before they are cited again.

---

## 4. What the Step 2 Document Gets Right

1. **A sound, mainstream architecture.** Rust+Wasmtime edge runtime, Go control plane, TypeScript CLI, gRPC/Protobuf internal APIs — this is a credible, well-understood split, and the language-role rationale (Section 3.1) is well argued.
2. **Correct sandboxing mechanics.** Fuel metering, linear-memory limits, wall-clock timeouts, and WASI-subset syscall restriction are exactly how Wasmtime-based multi-tenancy is done; Challenge 4 is correctly rated low-risk.
3. **The right riskiest-assumption-first plan.** Phase 1 (PoC + benchmark against Cloudflare Workers before anything else) is the correct sequencing, and the phase gates have measurable success criteria.
4. **Genuine self-awareness in places.** The Challenge 1 honesty about Pyodide's ~10MB size, the recommendation to keep the WIT/raw-ABI interface swappable, and Open Question 1 (edge footprint) show the document knows where its bodies are buried — the problem is that the marketing framing (Sections 1 and 6) ignores what Sections 5 and 9 admit.

---

## 5. Key Weaknesses

### 5.1 The differentiation premise no longer holds

The problem statement ("edge computing is only accessible to JavaScript developers") was already weakened by Fastly's polyglot WASI runtime and Cloudflare's long-standing WASM support, and was invalidated for Python by Cloudflare's Python Workers GA on 2026-09-22 — one week before this evaluation, using the same Pyodide→WASM approach EdgeDeploy proposes. A new entrant cannot win on *language availability*; it can only win on *language experience* (DX, bindings, performance) — a much thinner wedge against incumbents with existing networks, billing relationships, and brand trust.

### 5.2 The Python story conflicts with the performance targets

Pyodide's ~10MB runtime and heavy memory footprint sit directly against the < 50ms cold-start target and multi-tenant edge economics. The document knows this (Challenge 1) but still leads with "run pandas/scikit-learn at the edge" as the flagship value proposition (Section 1.3, Appendix A.1). Either the Python targets need to be honest and different (e.g., pre-warmed isolates, snapshot restore, a stated 200ms+ cold-start class), or Python should be de-scoped to a later phase. As written, the success metrics table would be failed by the headline use case.

### 5.3 The language toolchain plan needs correction

Three of five compilation paths contain errors (Section 2.2): the TypeScript path names tools that cannot do the job, the Python path cites a nonexistent "cryptography + wasm-pack" pipeline, and the Go path targets the browser-JS environment rather than WASI (`GOOS=wasip1` or TinyGo is required for a Wasmtime host). These are fixable, but they mean Phase 2's deliverables as written are not executable without rework — and they signal that the hardest part of the product (the polyglot toolchain) has not yet been seriously de-risked.

### 5.4 The edge footprint is the unsolved dependency

300+ locations is presented in the architecture diagram as a given, while Open Question 1 treats it as undecided. Partnering with CDN providers for third-party compute is not a standard offering; hyperscaler edge services yield dozens of locations, not hundreds. The plan should assume 10–30 metros at launch and treat broader coverage as a business-development milestone, not an engineering one.

### 5.5 Timeline and competitive omissions

The 12-month path to a 99.9% SLA, usage-based billing, and a passed security audit is aggressive for a team that does not yet exist (Section 8 is aspirational). The competitive table omits Fermyon, Wasmer Edge, and wasmCloud — the closest architectural siblings — plus container-based near-edge alternatives (Koyeb, Fly.io) that already offer "any language, many locations."

---

## 6. Risk Register

### 6.1 Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Pyodide-based Python cannot meet < 50ms cold start or multi-tenant memory density | High | High | Snapshot restore, per-tenant warm pools, or de-scope Python to Phase 5+; publish honest per-language cold-start classes |
| Language toolchain rework (TS path nonexistent, Go path wrong target) | High | Medium | Re-plan: `GOOS=wasip1`/TinyGo for Go; AssemblyScript or Javy-style engine embedding for TS; validate each path in a Phase 1 spike |
| WASI Preview 1 / Component Model churn forces interface rework | Medium | Medium | Swappable interface layer (already recommended in Challenge 2) |
| Multi-tenant sandbox escape or resource exhaustion | Low–Medium | High | Fuel metering + memory caps (planned), defense-in-depth seccomp, external security audit before GA |

### 6.2 Market Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Incumbents close the DX gap (Cloudflare already shipped GA Python during this evaluation window) | High | High | Compete on unified cross-language DX + open-source trust, never on "languages supported" alone |
| Edge network capital intensity blocks the 300-location promise | High | High | Launch with 10–30 hyperscaler/bare-metal metros; treat scale-out as a funding milestone |
| Developer-platform network effects favor incumbents (existing billing, bindings, ecosystem) | Medium | High | Target a sharp wedge first (e.g., data/ML teams wanting Python at the edge) rather than general-purpose edge compute |

### 6.3 Execution Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| 12-month plan to SLA + billing + audit slips | High | Medium | Re-baseline to 18–24 months or narrow Phase 4 scope |
| Five specialized roles required before funding | Medium | High | Phase 1 needs 2–3 engineers (Rust + Go); defer DevRel and infra hires |
| Scope creep across five languages simultaneously | Medium | Medium | Ship 2 languages first (Rust + Go), add others behind the same contract |

---

## 7. Step 2 Document Quality Assessment

Assessed against the `FromStep1toStep2.md` quality criteria:

| Criterion | Verdict | Notes |
|-----------|---------|-------|
| **Specific** | ⚠️ Partial | Names exact tools, but several specifics are wrong (Section 2.2) — specificity without verification |
| **Grounded** | ❌ Fail | Competitive claims were not current at time of writing; closest competitors (Fermyon, Wasmer, wasmCloud) missing |
| **Feasible** | ⚠️ Partial | Core runtime feasible; polyglot scope and 12-month timeline overstated |
| **Complete** | ✅ Pass | All template sections present, with appendices and examples |
| **Honest** | ⚠️ Partial | Risks are acknowledged in Section 5, but Sections 1 and 6 oversell a market gap that no longer exists |
| **Actionable** | ✅ Pass | Phased plan with measurable gates; a reader could start Phase 1 |
| **Structured** | ✅ Pass | Follows the template structure exactly |
| **Measurable** | ✅ Pass | Every phase has success criteria; metrics table is concrete |

**Document verdict:** well-structured and actionable, but not yet *grounded*. The internal tension between the honest Challenge sections and the outdated marketing framing is the document's defining flaw.

---

## 8. Verdict

**Overall: 7.4/10 — Tier 1 (conditional).**

The engineering core is credible, the team fit and excitement are real, and the market exists. But the fact-check changes the strategy, not just the score: the premise that edge computing excludes non-JS developers is no longer true, and it was invalidated for the flagship language (Python) days before this evaluation by an incumbent using the identical technical approach. EdgeDeploy as written is a "language availability" play against competitors that already have language availability. It survives as a **"language experience" play**: one unified, first-class DX across languages, honest and best-in-class Python performance, and an open-source runtime — aimed first at the teams the incumbents serve worst (data/ML teams), on a realistic footprint of 10–30 metros.

Proceed to Phase 1 **only after the conditions in Section 9 are met**. Phase 1 itself is well designed and should include an explicit Pyodide cold-start benchmark, since that single number decides the product's flagship claim.

---

## 9. Recommendations

### Conditions Before Phase 1 Funding

1. **Rewrite the differentiation** around verified gaps (unified cross-language DX and bindings; Python performance; open-source runtime) — remove all "edge is JS-only" framing.
2. **Correct the language toolchain plan**: `GOOS=wasip1`/TinyGo (Go), AssemblyScript or Javy-style embedding (TS), Pyodide + snapshotting with honest cold-start classes (Python); drop the nonexistent "cryptography + wasm-pack" path.
3. **Update the competitive table** to include Fermyon, Wasmer Edge, wasmCloud, Koyeb, and Fly.io, with accurate Cloudflare and Fastly capabilities.
4. **Re-baseline the edge footprint** to 10–30 metros at launch and the overall timeline to 18–24 months.
5. **Add a Python cold-start benchmark** (Pyodide + snapshot restore vs. 50ms target) to Phase 1 deliverables — it is the riskiest assumption in the plan.

### Positioning Options (in recommended order)

| Option | Description | Trade-off |
|--------|-------------|-----------|
| **A. Python-first edge platform** | Lead with best-in-class Python at the edge (warm pools, snapshots, pandas/scikit-learn support), add other languages later | Sharpest wedge; concedes the "all languages" headline |
| **B. Open-source runtime + managed control plane** | Open-source the Wasmtime edge runtime from day 1; monetize the control plane (Fermyon-style model) | Community gravity vs. closed incumbents; smaller near-term revenue |
| **C. General-purpose polyglot edge** | The current document's positioning | Requires beating Cloudflare/Fastly at their own game with less capital — not recommended |

### Immediate Next Steps

1. Revise `EdgeDeploy.md` (v1.1) per the five conditions above.
2. Run the Phase 1 spike: Wasmtime runtime + one Rust and one Go (`wasip1`) function + Pyodide cold-start benchmark.
3. Benchmark the same workloads on Cloudflare Workers (including GA Python Workers) and Fastly Compute to size the real performance gap.
4. Re-verify the competitive landscape immediately before any funding conversation — this market moved within the last month.

---

*Document version: 1.0*
*Last updated: 2026-10-02*
*Evaluator: Product Engineering Team*
