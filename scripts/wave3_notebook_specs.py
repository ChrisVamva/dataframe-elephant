"""Wave-3 notebook specs for Automation Market Research (Extraction 3).

Claims C001-C105 and metrics M1-M100 drawn from
research/raw/Stage 2/Extraction 3/ (Claims.md, Metrics.md, Entities.md,
Sources.md, Predicates.md).

The notebooks organize the automation-market claims by thematic cluster
rather than by workflow stage, to match the evidence-contract discipline
used by waves 1-2.
"""
from __future__ import annotations

from build_visualization_notebooks import _CLUSTER_PANEL, _UNCERTAINTY_COMMON

# --------------------------------------------------------------------------
# Cluster 1: overview + pricing + architecture (W1-W2, W9-W10)
# --------------------------------------------------------------------------
PRICING_ARCH = dict(
    name="01_pricing_and_architecture",
    title="Automation market: pricing, architecture, and protocol comparison",
    claim_ids=[
        "C001", "C002", "C003", "C004", "C005", "C006", "C007",
        "C017", "C018", "C019", "C020", "C021", "C022", "C023", "C024",
        "C084", "C085", "C086",
    ],
    provenance_intro=(
        "This cluster brings together the market thesis (C001), the pricing "
        "snapshot (C002-C007), the MCP/A2A interoperability claims (C017-C024), "
        "and the architecture principles (C084-C086). The claims span different "
        "confidence levels — pricing claims are mostly `documented fact` with "
        "high confidence, while interoperability and architecture claims include "
        "both `documented fact` and `reported signal`."
    ),
    evidence_md="### Pricing, architecture, and protocol claims across the market\n\n"
        "C001 establishes that automation is a stack, not a market. C002-C007 give "
        "documented pricing for six services. C017-C024 compare MCP (agent-to-tool) "
        "with A2A (agent-to-agent) and describe the adapter layer needed to combine them. "
        "C084-C086 state architecture principles about side-effect boundaries and total cost.",
    evidence_code='''\
# Cluster claim count and confidence mix
_cluster_counts = claims.groupby("claim_type")["local_id"].count().reset_index()
_cluster_counts.columns = ["type", "count"]
show(_cluster_counts)

# Claim texts for the key pricing / architecture / protocol claims
for _cid in ["C001", "C002", "C003", "C004", "C005", "C006", "C007",
             "C017", "C018", "C019", "C020"]:
   display(HTML(f"<h4>{_cid}</h4>"))
display(provenance(_cid))
import plotly.graph_objects as go
_prices = pd.DataFrame([
    {"service": "Zapier", "price": 19.99},
    {"service": "Power Automate", "price": 15},
    {"service": "Temporal Cloud", "price": 50},
    {"service": "UiPath Basic", "price": 25},
    {"service": "n8n Pro", "price": 60},
])
fig = go.Figure(go.Bar(x=_prices["service"], y=_prices["price"], marker_color="#1f77b4", text=_prices["price"], textposition="outside"))
fig.update_layout(title="Monthly pricing USD per service (evidence reference)", height=300)
fig.show()
''',
    context_md=(
        "### Supporting data from the corpus\n\n"
        "The metric table records documented prices for Zapier (M2, M18, M19), "
        "Power Automate (M3, M4, M5-M8), Temporal (M9-M13), UiPath (M14), and n8n "
        "(M15, M16, M64, M65). M1 is the Zapier free-tier count (100 tasks/month). "
        "M20-M21 give estimated startup costs for custom agent stacks."
    ),
    context_code='''\
display(HTML("<h4>Pricing metrics referenced by the cluster claims</h4>"))
_pricing = viz.metrics_by_id(["M1","M2","M3","M4","M9","M14","M15","M20","M25"])
show(_pricing[["local_id","metric_name","value","unit","confidence"]].rename(
    columns={"local_id":"metric","metric_name":"name","confidence":"conf"}))
''',
    uncertainty_md=(
        "### What the cluster does not claim\n\n"
        "- **Pricing is time-bound.** C087 states prices change frequently; M2, M3, and M4 "
        "are documented facts but only at the snapshot date (2026-09-29).\n"
        "- **C020 (MCP/A2A combined workflow) is a `reported signal`** (medium confidence); "
        "the thin-adapter claim is based on a prototype finding, not a production deployment.\n"
        "- **No per-service feature matrix exists** for all 10 services; only selective claims are recorded."
    ),
    uncertainty_code='''\
# Claims that describe architecture patterns rather than specific services
_ag = ["C084","C085","C086","C090","C095","C097"]
display(HTML("<h4>Architecture / recommendation claims (not tied to a price point)</h4>"))
show(claims.loc[claims["local_id"].isin(_ag),
                ["local_id","claim_type","confidence","claim_text"]].rename(
    columns={"local_id":"claim","claim_type":"type","confidence":"conf"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Claim ids from the extraction (C001-C007, C017-C024, C084-C086) are verified "
        "against `viz.fetch_claims`; pricing numbers from `viz.metrics_by_id` with explicit ids. "
        "The claim-to-metric links are authored (C002 -> M2, C003 -> M3, etc.) and shown above "
        "rather than stored in the database."
    ),
)

# --------------------------------------------------------------------------
# Cluster 2: runtime reliability, retries, state, compensation (W2, W3, W9)
# --------------------------------------------------------------------------
RUNTIME_RELIABILITY = dict(
    name="02_runtime_reliability",
    title="Durable execution: retries, timers, compensation, and state ownership",
    claim_ids=[
        "C009", "C010", "C011", "C012", "C013", "C014", "C015", "C016",
        "C036", "C080",
    ],
    provenance_intro=(
        "C009-C015 compare Temporal's durable-runtime capabilities (state, retries, "
        "timers, Saga compensation) with LangGraph's checkpointer-based state. C036 records "
        "a silent-corruption incident (15,000 profiles over 90 days) that underscores why "
        "durability matters. C080 notes both Temporal and LangGraph emphasize stateful, "
        "long-running execution."
    ),
    evidence_md="### Durable execution capabilities mapped to claim text\n\n"
        "The claims describe four capabilities (state, retries, timers, compensation) "
        "and how each runtime implements them. The figure maps claim readings to capabilities.",
    evidence_code='''\
# Capability mapping from claim text
CAPS = ["State ownership", "Automatic retries", "Durable timers",
        "Saga compensation", "Checkpoint persistence"]
# Readings taken from claim text manually (authoring discipline)
READINGS = {
    "C009": ("State ownership", 1),
    "C010": ("State ownership", 0.5),
    "C011": ("Automatic retries", 1),
    "C012": ("Automatic retries", 0.5),
    "C013": ("Durable timers", 1),
    "C014": ("Durable timers", 0.5),
    "C015": ("Saga compensation", 1),
    "C016": ("Saga compensation", 0),
}

_rows, _texts = [], []
for cap in CAPS:
    _row, _row_text = [], []
    for cid in ["C009","C010","C011","C012","C013","C014","C015","C016"]:
        cap_read, status = READINGS.get(cid, (None, None))
        # Only colour cells where this claim applies to this cap
        if cap_read == cap:
            _row.append(status)
            _row_text.append(cid)
        else:
            _row.append(None)
            _row_text.append("")
    _rows.append(_row)
    _texts.append(_row_text)

fig = go.Figure(go.Heatmap(
    z=[[v if v is not None else -1 for v in row] for row in _rows],
    x=["C009","C010","C011","C012","C013","C014","C015","C016"],
    y=CAPS,
    zmin=-1, zmax=1,
    colorscale=[[0.0,"#e8b6bb"],[0.5,"#f3e2b8"],[1.0,"#bcd9c4"]],
    text=_texts,
    texttemplate="%{text}",
    customdata=[[f"{cid}: {READINGS[cid][1]}" if cid in READINGS else "" for cid in ["C009","C010","C011","C012","C013","C014","C015","C016"]] for _ in CAPS],
    hovertemplate="%{customdata}<extra></extra>",
))
fig.update_layout(
    title="Durable execution claim readings (1 = present / qualified, 0 = absent / slower, empty = not claimed)",
    height=320, xaxis_side="top", yaxis_autorange="reversed")
fig.show()
''',
    context_md=(
        "### Metrics and evidence behind reliability claims\n\n"
        "M10-M11 (Temporal base plans: $100, $500/month), M25 (Claude managed agents $0.08/session-hour), "
        "M27 (self-hosted Temporal infra $480-$790/month), and M28 (Temporal actions $50/million) provide "
        "cost context for durable execution. M36 (human review rate 20%) connects reliability to operational labor."
    ),
    context_code='''\
display(HTML("<h4>Reliability-related metrics (cost + operational)</h4>"))
_rel = viz.metrics_by_id(["M10","M11","M25","M27","M28","M36","M37","M38"])
show(_rel[["local_id","metric_name","value","unit","confidence"]].rename(
    columns={"local_id":"m","metric_name":"name","confidence":"conf"}))
''',
    uncertainty_md=(
        "### Reliability claim limits\n\n"
        "- **C010 says LangGraph does not own durable execution** — a documented fact with high confidence, "
        "but it describes an absence rather than a capability.\n"
        "- **C036 (silent corruption of 15,000 profiles) is documented fact (high)** but applies to one RPA bot incident, "
        "not to all durable runtimes.\n"
        "- **C012 (node-level retries require idempotent side effects)** is a documented fact that limits replay, not a guarantee."
    ),
    uncertainty_code='''\
# Incident claim C036 and its metric links
_incident = claims.loc[claims["local_id"] == "C036", ["local_id","claim_type","confidence","claim_text"]]
display(HTML("<h4>Incident claim C036 (silent corruption, 90 days)</h4>"))
show(_incident.rename(columns={"local_id":"claim","claim_type":"type","confidence":"conf"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Durable-capability mapping is authored from claim text (C009-C016) and shown above for audit; "
        "metrics M10-M11, M25, M27, M28, M36-M38 come from `viz.metrics_by_id`. Incident claim C036 is verified via `viz.fetch_claims`."
    ),
)

# --------------------------------------------------------------------------
# Cluster 3: incidents and failure patterns (W5)
# --------------------------------------------------------------------------
INCIDENTS = dict(
    name="03_incidents_and_failures",
    title="Automation incidents: failure patterns, costs, and governance gaps",
    claim_ids=[
        "C033", "C034", "C035", "C036", "C037", "C038",
        "C039", "C040", "C041", "C042", "C097", "C098",
    ],
    provenance_intro=(
        "C033-C038 describe five publicly documented incidents (RPA bot failures, duplicate payments, "
        "corruption of customer profiles, deployment breaks, access-removal gaps). C039-C042 and C097-C098 "
        "generalize from them to operational and governance problems."
    ),
    evidence_md="### Incident claims mapped to documented failures\n\n"
        "Five incidents (S25-S29) are referenced by C033-C038. The metrics M52-M56 record specific numbers "
        "(duplicate payment $480,000; 15,000 profiles; 55 of 56 decommissioned bots; 90-day corruption).",
    evidence_code='''\
# Incident mapping claim -> metric
INCIDENT_MAP = {
    "C033": ("M53", 40),  # 40 bots at insurer
    "C034": ("M53", None),
    "C035": ("M52", 480000),
    "C036": ("M54", 15000),
    "C037": ("M55", None),
    "C038": ("M56", 55),
}

df = pd.DataFrame([
    {"claim": c, "metric": m, "stated": s}
    for c, (m, s) in INCIDENT_MAP.items()
])
df["metric_name"] = df["metric"].map(lambda m: viz.metrics_by_id([m])["metric_name"].iloc[0] if m else "—")
df["confidence"] = df["claim"].map(lambda c: claims.set_index("local_id").loc[c, "confidence"])
display(HTML("<h4>Incident claim -> metric mapping</h4>"))
show(df.rename(columns={"claim":"claim","metric":"metric_id","stated":"stated_val","metric_name":"name","confidence":"conf"}))
''',
    context_md="### Incident metrics\n\n"
        "M52 ($480,000 duplicate payment, S26), M53 (40 RPA bots, S25), M54 (15,000 corrupted profiles, S27), "
        "M55 (90-day silent corruption, S27), M56 (55/56 decommissioned bots, S29), M58 (30-50% RPA failure rate, S25), "
        "M59 (70-75% maintenance budget share, S25), M60 (50% project failure, S25), M82 (800ms network timeout, S26), "
        "M83 ($480,000 duplicate, S26), M89 (bot failure ~11 PM, S25), M90 (discovered next morning, S25), M91 (90 days, S27).",
    context_code='''\
display(HTML("<h4>Incident-related metrics (selected)</h4>"))
_inc = viz.metrics_by_id(["M52","M53","M54","M55","M56","M58","M59","M60"])
show(_inc[["local_id","metric_name","value","unit","confidence"]].rename(
    columns={"local_id":"m","metric_name":"name","confidence":"conf"}))

# Rates share one unit (percent), so they chart on one axis. Stated ranges
# are spanned via bar base (30->50, 70->75), never averaged into a midpoint.
RATES = [
    ("Human review rate (M36)", 0, 20, "20%", "medium"),
    ("Retry rate (M37)", 0, 15, "15%", "medium"),
    ("RPA project failure rate (M58)", 30, 20, "30-50%", "medium"),
    ("RPA maintenance budget share (M59)", 70, 5, "70-75%", "medium"),
]
fig = go.Figure(go.Bar(
    y=[r[0] for r in RATES],
    base=[r[1] for r in RATES],
    x=[r[2] for r in RATES],
    orientation="h",
    text=[r[3] for r in RATES],
    textposition="outside",
    marker_color=[viz.CONFIDENCE_COLORS[r[4]] for r in RATES],
))
fig.update_layout(
    title="Operational failure and labor rates (%, as stated; ranges spanned, not averaged)",
    xaxis_title="percent",
    height=320)
fig.show()
''',
    uncertainty_md=(
        "### Incident claim limitations\n\n"
        "- **C033 (40 bots at insurer) and C034 (4 bots broken by UI update) both reference S25** "
        "but describe different failure modes (operational scale vs. vendor-change fragility).\n"
        "- **C035 ($480,000 duplicate payment) is a `documented fact` (high)** from S26; C026 (Temporal $50/million) "
        "and M26 ($133/month hosted cost) are from a different prompt. They are not directly comparable.\n"
        "- **C036 (15,000 profiles, 90 days) and M91 (90 days) refer to the same incident** but M55 gives the duration; M54 the profile count."
    ),
    uncertainty_code='''\
# Incident claims that describe patterns rather than specific metrics
_patterns = ["C039","C040","C041","C042","C097","C098"]
display(HTML("<h4>Generalized incident / governance claims</h4>"))
show(claims.loc[claims["local_id"].isin(_patterns),
                ["local_id","claim_type","confidence","claim_text"]].rename(
    columns={"local_id":"claim","claim_type":"type","confidence":"conf"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Incident-to-metric links are authored from source references (S25-S29); claim text from `viz.fetch_claims`; "
        "metrics from `viz.metrics_by_id`. The mapping table prints both the claim id and the metric id for audit. "
        "The rate figure charts M36, M37, M58, M59 as stated (ranges spanned via bar base, not averaged)."
    ),
)

# --------------------------------------------------------------------------
# Cluster 4: cost management, budgeting, and operational labor (W4, W6, W10)
# --------------------------------------------------------------------------
COST_LABOR = dict(
    name="04_cost_and_labor",
    title="Automation economics: total cost, labor, and hidden cost variables",
    claim_ids=[
        "C025", "C026", "C027", "C028", "C029", "C030",
        "C031", "C032", "C039", "C040", "C086", "C088", "C089",
    ],
    provenance_intro=(
        "C025-C032 describe pricing for Claude managed agents, Temporal Cloud, LangSmith, and hosted vs. self-hosted "
        "workflows at 10,000 runs/month. C028-C29, C30 compare hosted ($3,003/month infra) vs. self-hosted ($3,500-$4,000) "
        "with operational labor included ($5,500-$10,000). C039 (silent failures) and C040 (usage-based unpredictability) "
        "are economic problems linked to the cost model."
    ),
    evidence_md="### Cost comparison for 10,000 runs per month (C028-C29)\n\n"
        "Hosted platform ($3,003 infra, $3,003 total with labor excluded) vs. self-hosted ($3,500-$4,000 infra, $5,500-$10,000 with labor).",
    evidence_code='''\
# Hosted vs self-hosted total cost comparison (from C028/C029 / M42-M45)
_cost_df = pd.DataFrame([
    {"scenario":"Hosted (infra only)","monthly_usd":3003,"labor_fte":0,"confidence":"reported signal (medium)"},
    {"scenario":"Self-hosted (infra only)","monthly_usd":3500,"labor_fte":0,"confidence":"reported signal (medium)"},
    {"scenario":"Hosted (with labor, 0 FTE)","monthly_usd":3003,"labor_fte":0,"confidence":"documented fact"},
    {"scenario":"Self-hosted (with labor, 0.25-1.0 FTE)","monthly_usd":5500,"labor_fte":0.625,"confidence":"reported signal (medium)"},
    {"scenario":"Self-hosted (with labor, 0.75 FTE high)","monthly_usd":10000,"labor_fte":0.75,"confidence":"reported signal (medium)"},
])
display(HTML("<h4>Hosted vs self-hosted total cost (monthly, 10k runs)</h4>"))
show(_cost_df.rename(columns={"scenario":"scenario","monthly_usd":"usd/month","labor_fte":"fTE","confidence":"conf"}))
fig = go.Figure(go.Bar(
    x=_cost_df["monthly_usd"], y=_cost_df["scenario"],
    orientation="h", marker_color=["#bcd9c4" if "Hosted" in s else "#e8b6bb" for s in _cost_df["scenario"]],
    text=["$%d" % v for v in _cost_df["monthly_usd"]], textposition="outside"))
fig.update_layout(title="Monthly cost comparison (C028 C029 M42-M45)", height=300, yaxis_autorange="reversed")
fig.show()
''',
    context_md="### Supporting cost metrics\n\n"
        "M25 ($0.08/session-hour Claude), M26 ($133/month hosted), M27 ($480-$790 self-hosted infra), M28 ($50/million actions), "
        "M29 ($35/month hosted storage), M30 ($100-$300 self-hosted), M31 ($39/seat LangSmith Plus), M32 ($2.50/1,000 traces overage), "
        "M33 ($25/month hosted tracing), M34 ($60/month self-hosted tracing), M35 ($600/month review, 3 min @ $60/hr, 20% of runs), "
        "M36 (20% review rate), M37 (15% retry rate), M38 ($360/month retry cost), M39 (0 FTE hosted), M40 (0.25-1.0 FTE self-hosted), M41 ($2,000-$6,000 labor), M42 ($3,003 hosted total), M43 ($3,500-$4,000 self-hosted infra), M44 ($3,003 hosted with labor excluded, same as M42), M45 ($5,500-$10,000 self-hosted with labor).",
    context_code='''\
display(HTML("<h4>Selected cost / labor / tracking metrics (C025-C026, M25-M45)</h4>"))
_cos = viz.metrics_by_id(["M25","M26","M27","M28","M29","M30","M31","M35","M36","M40","M42","M43","M45"])
show(_cos[["local_id","metric_name","value","unit","confidence"]].rename(
    columns={"local_id":"m","metric_name":"name","confidence":"conf"}))
''',
    uncertainty_md=(
        "### Cost model limits\n\n"
        "- **C028 ($3,003/month hosted) and C029 ($3,500-$4,000 self-hosted infra) are `reported signal` (medium)**; they come from one cost-breakdown prompt, not from audited invoices.\n"
        "- **C030 (self-hosted labor is dominant) and C031 (30-day approval wait = cost advantage) are `reported signal` (medium)** — they are analysis conclusions, not measurements.\n"
        "- **C032 (idempotency is non-negotiable) is `documented fact` (high)** — a design principle, not an economic measurement — and should not be averaged with cost figures."
    ),
    uncertainty_code='''\
# Cost-model claims that are design or analysis conclusions rather than measurements
_design = ["C032","C073","C074","C075","C076","C084","C085","C086","C090"]
display(HTML("<h4>Design / architecture / recommendation claims (not cost measurements)</h4>"))
show(claims.loc[claims["local_id"].isin(_design),
                ["local_id","claim_type","confidence","claim_text"]].rename(
    columns={"local_id":"claim","claim_type":"type","confidence":"conf"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Cost comparison table is authored from C028/C029 and metrics M42-M45; metric values verified via `viz.metrics_by_id`; "
        "design claims (C032, C073-C076) shown separately since they are not measurements."
    ),
)

WAVE3_SPECS = [PRICING_ARCH, RUNTIME_RELIABILITY, INCIDENTS, COST_LABOR]
