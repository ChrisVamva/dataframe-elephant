"""Wave-2 notebook specs for the SmartHome visualization catalogue.

Wave 1 (``notebooks/1``) published the index plus one notebook per domain.
Wave 2 (``notebooks/2``) publishes the remaining claim clusters that
``data/smarthome.duckdb`` can actually support, and it deliberately does not
repeat a wave-1 figure: the cluster and metric ids below were chosen by first
listing what wave 1 already charts.

Cluster and metric selection rules used here:

* every declared claim id and metric id must exist in the database -- enforced
  by ``src/tests/test_viz_notebooks.py``;
* a figure may only draw numbers the database contains, so a quantity the
  corpus never recorded is shown as "not recorded" rather than as zero;
* a cell, bar or label that comes from a claim carries that claim's id, so a
  reader can go back to the provenance panel and check it;
* rates with different denominators are never multiplied into a funnel.

This module is pure data. The cell contract (``build_notebook``), the bootstrap
cell and the shared evidence fragments live in
``scripts/build_visualization_notebooks.py`` and are imported from there, so
both waves keep one evidence discipline.
"""
from __future__ import annotations

from build_visualization_notebooks import _CLUSTER_PANEL, _UNCERTAINTY_COMMON

ECOSYSTEM_SUPPORT = dict(
    name="02_ecosystem_support_and_commissioning",
    title="Matter by ecosystem: who supports what, and how far the test evidence reaches",
    claim_ids=[
        "C007", "C008", "C009", "C010", "C011", "C012", "C013", "C014",
        "C015", "C016", "C017", "C018", "C097",
    ],
    provenance_intro=(
        "The claims below are unevenly evidenced on purpose: `C008` and `C011` "
        "are documented facts about specification content, while `C016`, "
        "`C017` and `C097` are reported signals from third-party device "
        "testing. The panels show which is which before any cell of the "
        "matrix is coloured, because a capability map built from reported "
        "signal is not the same object as one built from conformance tests."
    ),
    evidence_md=(
        "### The corpus has no support matrix, so this one is built from claims\n\n"
        "There is no per-ecosystem capability table in the database. What "
        "exists instead is a set of claims, each naming an ecosystem and a "
        "capability in prose. The figure therefore encodes *claims*, not "
        "support: every coloured cell carries the id of the claim it comes "
        "from, and a cell no claim covers is left blank and marked "
        "`no claim in this cluster records this cell`. Blank is not the same "
        "as absent, and the figure never implies it is."
    ),
    evidence_code='''\
# The cell readings are an explicit, three-point reading of the claim text:
#   1   the claim states the capability is present
#   0.5 the claim states it with a recorded qualification
#   0   the claim states it is absent, failing, or slower
# A cell with no entry stays unrecorded. The mapping is written out in full so
# that each reading can be checked against the claim text shown on hover.
ECOSYSTEMS = ["Apple", "Google", "Amazon", "Samsung SmartThings"]
CAPABILITIES = ["Matter cameras", "In-platform automation rules", "Multi-admin"]

CELLS = {
    ("Matter cameras", "Samsung SmartThings"): ("C008", 1),
    ("Matter cameras", "Amazon"): ("C009", 1),
    ("Matter cameras", "Apple"): ("C010", 0),
    ("Matter cameras", "Google"): ("C010", 0),
    ("In-platform automation rules", "Samsung SmartThings"): ("C014", 1),
    ("In-platform automation rules", "Amazon"): ("C014", 0),
    ("In-platform automation rules", "Apple"): ("C014", 0),
    ("In-platform automation rules", "Google"): ("C014", 0),
    ("Multi-admin", "Apple"): ("C017", 1),
    ("Multi-admin", "Amazon"): ("C016", 0.5),
    ("Multi-admin", "Samsung SmartThings"): ("C097", 0.5),
}

_claims_by_id = claims.set_index("local_id")
_rows, _texts, _hovers = [], [], []
for _capability in CAPABILITIES:
    _row, _row_text, _row_hover = [], [], []
    for _ecosystem in ECOSYSTEMS:
        _cid, _status = CELLS.get((_capability, _ecosystem), (None, None))
        _row.append(_status)
        _row_text.append(_cid or "")
        if _cid is None:
            _row_hover.append(f"{_ecosystem}<br>{_capability}"
                              "<br>no claim in this cluster records this cell")
            continue
        _claim = _claims_by_id.loc[_cid]
        _row_hover.append(
            f"{_ecosystem}<br>{_capability}<br><b>{_cid}</b>"
            f" [{_claim['claim_type']}, {_claim['confidence']} confidence]"
            f"<br>{_claim['claim_text']}"
        )
    _rows.append(_row)
    _texts.append(_row_text)
    _hovers.append(_row_hover)

fig = go.Figure(go.Heatmap(
    z=_rows,
    x=ECOSYSTEMS,
    y=CAPABILITIES,
    zmin=0,
    zmax=1,
    colorscale=[[0.0, "#e8b6bb"], [0.5, "#f3e2b8"], [1.0, "#bcd9c4"]],
    xgap=3,
    ygap=3,
    text=_texts,
    texttemplate="%{text}",
    textfont=dict(size=12),
    customdata=_hovers,
    hovertemplate="%{customdata}<extra></extra>",
    colorbar=dict(
        title="claim reading",
        tickmode="array",
        tickvals=[0, 0.5, 1],
        ticktext=["absent / slower", "qualified", "present"],
    ),
))
fig.update_layout(
    title=("Ecosystem capability map, one claim per cell "
           "(blank = no claim in this cluster)"),
    height=380,
    xaxis=dict(side="top"),
    yaxis=dict(autorange="reversed"),
)
fig.show()
''',
    context_md=(
        "### How far does the evidence behind the map actually reach?\n\n"
        "Two claims bound the test evidence: `C013` states that Samsung "
        "SmartThings supports 58 Matter device types while other platforms "
        "'may support fewer', and `C097` reports an Allion Labs functional "
        "test of multi-admin. The metrics below record the scale of that test "
        "inventory (`M086`) and the minimum device inventory the corpus's own "
        "interoperability protocol calls for (`M087`). `M004` is the only "
        "per-ecosystem device-type count anywhere in the corpus, so the "
        "breadth chart has exactly one counted bar and three unrecorded ones."
    ),
    context_code='''\
display(HTML(
    "<h4>The test inventory behind the interoperability claims</h4>"
    "<p><code>M086</code> is the scale of the Allion Labs functional test; "
    "<code>M087</code> is the minimum device inventory the corpus's own "
    "interoperability protocol proposes. Both are read from the database.</p>"
))
_inventory = viz.metrics_by_id(["M004", "M005", "M086", "M087"])
show(_inventory[["local_id", "metric_name", "value", "unit", "confidence",
                 "source_ref", "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))

# M004 is the only per-ecosystem device-type count recorded anywhere in this
# corpus. C013 states that other platforms "may support fewer", which is a
# statement about the absence of a count, not a count of zero, so the other
# three bars are labelled unrecorded and drawn at zero height.
_types = viz.metrics_by_id(["M004"])
_samsung = viz.numeric_value(_types["value"].iloc[0]) if not _types.empty else None
_breadth = pd.DataFrame([
    {"ecosystem": "Samsung SmartThings", "device_types": _samsung,
     "reading": "counted in M004"},
    {"ecosystem": "Amazon", "device_types": None,
     "reading": "no count recorded; C013 says 'may support fewer'"},
    {"ecosystem": "Google", "device_types": None,
     "reading": "no count recorded; C013 says 'may support fewer'"},
    {"ecosystem": "Apple", "device_types": None,
     "reading": "no count recorded; C013 says 'may support fewer'"},
])
show(_breadth)
fig = go.Figure(go.Bar(
    x=[value if value is not None else 0 for value in _breadth["device_types"]],
    y=_breadth["ecosystem"],
    orientation="h",
    marker_color=["#1f77b4" if value is not None else "#d9d9d9"
                  for value in _breadth["device_types"]],
    text=["%g" % value if value is not None else "not recorded"
          for value in _breadth["device_types"]],
    textposition="outside",
    customdata=list(zip(_breadth["reading"], _breadth["device_types"])),
    hovertemplate="%{y}<br>%{customdata[0]}<extra></extra>",
))
fig.update_layout(
    title=("Matter device types supported, as recorded: one counted value, "
           "three ecosystems unrecorded (M004, C013)"),
    xaxis_title="device types",
    height=300,
    yaxis=dict(autorange="reversed"),
)
fig.show()
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### What the matrix is not\n\n"
        "- **It is a claim map, not a test report.** Ten of the thirteen "
        "claims in this cluster are `reported signal` from third-party "
        "testing, one is an `inference` (`C015`: certification confirms "
        "conformance but does not guarantee ecosystem compatibility), and only "
        "two (`C008`, `C011`) are documented facts about specification "
        "content rather than about shipping behaviour.\n"
        "- **Two claims cover several ecosystems each.** `C010` ('Apple and "
        "Google have been slower to implement camera support than Samsung and "
        "Amazon') and `C014` ('Amazon, Apple, and Google lack native support "
        "for creating automation rules ... while Samsung supports it') are "
        "single sentences mapped to several cells. The same claim id appears "
        "in each of those cells so the shallowness of the attribution stays "
        "visible on screen.\n"
        "- **Only one ecosystem has a device-type count.** `M004` counts "
        "Samsung SmartThings; the corpus records no equivalent for Apple, "
        "Google or Amazon, so a four-row parity matrix would be invented. "
        "That is why wave 1 deferred this notebook and why this one runs on "
        "claims instead.\n"
        "- **An unresolved conformance question sits inside the cluster.** "
        "`C015` says certification does not guarantee compatibility and "
        "`C097` records first-pairing success followed by a failure to "
        "operate the paired device. Both are kept; neither is averaged away.\n"
        "- **`C017` carries no falsifier** (`falsifier_stated = false`), so "
        "the claim that Apple's HomePod Mini 'exhibited robust multi-admin "
        "support' has no recorded observation that would disconfirm it."
    ),
    uncertainty_code='''\
# Claims that cannot be placed in a matrix cell without inventing an
# attribution: they are ecosystem-agnostic, or describe a failure mode rather
# than a capability. Listing them is the honest alternative to colouring a cell
# the corpus never filled.
_agnostic = ["C007", "C011", "C012", "C015", "C018"]
display(HTML(
    "<h4>Cluster claims deliberately left out of the matrix</h4>"
    "<p>Each claim below applies to several ecosystems, or describes "
    "behaviour rather than a capability.</p>"
))
show(claims.loc[claims["local_id"].isin(_agnostic),
                ["local_id", "claim_type", "confidence", "falsifier_missing",
                 "claim_text"]].rename(
    columns={"local_id": "claim", "claim_type": "type", "confidence": "conf",
             "falsifier_missing": "no_falsifier"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Claim text, evidence class, confidence and falsifier status come from "
        "`viz.fetch_claims`; the test-inventory numbers from "
        "`viz.metrics_by_id` by explicit local id. The cell readings are "
        "notebook-level data, printed as a table above and cross-checked "
        "claim by claim in the provenance panels, so the mapping is "
        "inspectable even though it is authored here rather than stored in "
        "the corpus."
    ),
)

OFFLINE_FAILURE = dict(
    name="03_offline_failure_and_cloud_dependency",
    title="Resilience: what breaks when the border router, the internet or the vendor goes away",
    claim_ids=["C019", "C020", "C021", "C022", "C026", "C027", "C070"],
    provenance_intro=(
        "This cluster is almost entirely prose evidence: the corpus records one "
        "quantified number about losing device control (`M006`, `about 1` "
        "minute) and describes the rest in claims. The provenance panels are "
        "therefore the substance of this page, not an appendix to it."
    ),
    evidence_md=(
        "### Three outage states, four capabilities, one claim per cell\n\n"
        "The corpus distinguishes local infrastructure failure (the Thread "
        "border router), network failure (the WAN link) and lifecycle failure "
        "(the vendor retiring a cloud service). Those are three different "
        "failure classes with different consequences, and the corpus's own "
        "recommendation claim `C076` argues manufacturers should publish "
        "failures in exactly this classified way. The map below applies that "
        "structure to the claims that exist: it is a reading of the claims, "
        "and an unrecorded cell stays blank."
    ),
    evidence_code='''\
# Reading scale, as in the ecosystem notebook:
#   1   the claim states the capability keeps working in that state
#   0   the claim states it fails, is lost, or is blocked
#   no entry = no claim in this cluster records that combination
STATES = ["Border router removed / replaced", "Internet (WAN) down",
          "Vendor cloud retired"]
CAPABILITIES = ["Basic control of commissioned devices",
                "Commissioning new devices", "Firmware updates",
                "Local Matter/Thread paths"]
FAILURE_CELLS = {
    ("Basic control of commissioned devices",
     "Border router removed / replaced"): ("C020", 0),
    ("Commissioning new devices",
     "Border router removed / replaced"): ("C021", 0),
    ("Firmware updates", "Border router removed / replaced"): ("C019", 0),
    ("Local Matter/Thread paths",
     "Border router removed / replaced"): ("C026", 0),
    ("Basic control of commissioned devices", "Internet (WAN) down"): ("C027", 1),
    ("Local Matter/Thread paths", "Internet (WAN) down"): ("C027", 1),
    ("Basic control of commissioned devices", "Vendor cloud retired"): ("C070", 0),
}

_claims_by_id = claims.set_index("local_id")
_rows, _texts, _hovers = [], [], []
for _capability in CAPABILITIES:
    _row, _row_text, _row_hover = [], [], []
    for _state in STATES:
        _cid, _status = FAILURE_CELLS.get((_capability, _state), (None, None))
        _row.append(_status)
        _row_text.append(_cid or "")
        if _cid is None:
            _row_hover.append(f"{_state}<br>{_capability}"
                              "<br>no claim in this cluster records this cell")
            continue
        _claim = _claims_by_id.loc[_cid]
        _row_hover.append(
            f"{_state}<br>{_capability}<br><b>{_cid}</b>"
            f" [{_claim['claim_type']}, {_claim['confidence']} confidence]"
            f"<br>{_claim['claim_text']}"
        )
    _rows.append(_row)
    _texts.append(_row_text)
    _hovers.append(_row_hover)

fig = go.Figure(go.Heatmap(
    z=_rows,
    x=STATES,
    y=CAPABILITIES,
    zmin=0,
    zmax=1,
    colorscale=[[0.0, "#e8b6bb"], [0.5, "#f0f0f0"], [1.0, "#bcd9c4"]],
    xgap=3,
    ygap=3,
    text=_texts,
    texttemplate="%{text}",
    textfont=dict(size=12),
    customdata=_hovers,
    hovertemplate="%{customdata}<extra></extra>",
    colorbar=dict(title="claim reading", tickmode="array", tickvals=[0, 1],
                  ticktext=["fails / blocked", "keeps working"]),
))
fig.update_layout(
    title=("Failure map by outage state, one claim per cell "
           "(blank = no claim in this cluster)"),
    height=420,
    xaxis=dict(side="top"),
    yaxis=dict(autorange="reversed"),
)
fig.show()

# The same cells, counted: how much of the map the corpus actually filled.
_coverage = []
for _state in STATES:
    _recorded = [FAILURE_CELLS[(_cap, _state)]
                 for _cap in CAPABILITIES if (_cap, _state) in FAILURE_CELLS]
    _fails = sum(1 for _cid, _status in _recorded if _status == 0)
    _coverage.append({
        "state": _state,
        "capabilities_in_map": len(CAPABILITIES),
        "recorded_as_failing": _fails,
        "recorded_as_working": len(_recorded) - _fails,
        "no_claim_recorded": len(CAPABILITIES) - len(_recorded),
    })
coverage = pd.DataFrame(_coverage)
show(coverage)
fig = go.Figure()
fig.add_trace(go.Bar(name="recorded as failing", x=coverage["state"],
                     y=coverage["recorded_as_failing"], marker_color="#b32637"))
fig.add_trace(go.Bar(name="recorded as still working", x=coverage["state"],
                     y=coverage["recorded_as_working"], marker_color="#1a7f37"))
fig.add_trace(go.Bar(name="no claim recorded", x=coverage["state"],
                     y=coverage["no_claim_recorded"], marker_color="#d9d9d9"))
fig.update_layout(
    barmode="stack",
    title=("How much of the failure map the corpus fills "
           "(four capabilities per state)"),
    yaxis_title="capabilities",
    height=340,
)
fig.show()
''',
    context_md=(
        "### The one quantity, and two figures that are not comparable with it\n\n"
        "`M006` is the only recorded measurement of how quickly control is "
        "lost when the border router disappears. The corpus also records a "
        "protocol-maturity figure (`M007`, Z-Wave's about 20 years) and an "
        "onboarding response expectation from its own test procedure (`M088`, "
        "2 seconds). They are drawn together to show the *scale* of the "
        "response-time language the corpus uses, each on its own unit: they "
        "are not three points on one measurement axis."
    ),
    context_code='''\
display(HTML(
    "<h4>Recorded time figures in the resilience cluster</h4>"
    "<p><code>M006</code> is a measured consequence; <code>M007</code> is a "
    "protocol-maturity statement; <code>M088</code> is the corpus's own test "
    "expectation. The units differ, so each bar is labelled with its own.</p>"
))
_timed = viz.metrics_by_id(["M006", "M007", "M088"])
show(_timed[["local_id", "metric_name", "value", "unit", "confidence",
             "source_ref", "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))

fig = go.Figure(go.Bar(
    x=[viz.numeric_value(value) for value in _timed["value"]],
    y=[f"{record['local_id']} {record['metric_name']} ({record['unit']})"
       for record in _timed.to_dict("records")],
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in _timed["confidence"]]),
    customdata=list(zip(_timed["value"], _timed["unit"], _timed["confidence"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]} %{customdata[1]}"
                   "<br>confidence: %{customdata[2]}<extra></extra>"),
))
fig.update_layout(
    title=("Three recorded time figures, each in its own unit "
           "(one axis, three clocks: minutes, years, seconds)"),
    xaxis_title="value, in the unit named on the bar",
    height=300,
    yaxis=dict(automargin=True),
)
fig.show()
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### Two claims that look contradictory and are not\n\n"
        "`C020` states that Matter-over-Thread devices lose the ability to "
        "communicate with each other when the border router is down. `C027` "
        "states that local Matter/Thread paths work without internet for basic "
        "operations. Both are in the map, and they are not in conflict: `C027` "
        "is about an internet outage on a working mesh, `C020` is about the "
        "mesh losing its route to the IP network. Merging them into one "
        "'does local control work?' verdict would destroy that distinction, so "
        "the map keeps the two outage states separate.\n\n"
        "Other limits on this page:\n\n"
        "- **One measurement, several relayed observations.** `M006` is medium "
        "confidence; the cell readings come from `reported signal` claims "
        "(`C019`, `C020`, `C021`, `C027`) rather than from controlled trials.\n"
        "- **`C022` is a low-confidence inference** that Z-Wave remains the "
        "most reliable option for mission-critical applications. It is kept "
        "because it is the corpus's only comparative reliability statement, "
        "and it is labelled as an inference wherever it appears.\n"
        "- **`C070` names vendors without dates.** Neato, Wemo and Nest are "
        "recorded as having ended cloud support earlier than promised, but the "
        "corpus records no shutdown dates, so no timeline is drawn.\n"
        "- **The vendor-lifecycle column is one cell deep.** Only basic "
        "control is claimed against a retired cloud; commissioning, firmware "
        "and local-path behaviour after a cloud shutdown are simply not "
        "recorded."
    ),
    uncertainty_code='''\
# The 'still works / fails' distinction is re-checked against the claim text
# here rather than trusted from the mapping: the table prints the wording the
# reading was made from.
_cell_claims = sorted({cid for cid, _status in FAILURE_CELLS.values()})
display(HTML(
    "<h4>The claims the map is read from</h4>"
    "<p>Each reading in the failure map comes from one of these claims. The "
    "quotations are the claim text as stored in the database.</p>"
))
show(pd.DataFrame([
    {"claim": cid, "type": claims.set_index("local_id").loc[cid, "claim_type"],
     "confidence": claims.set_index("local_id").loc[cid, "confidence"],
     "no_falsifier": claims.set_index("local_id").loc[cid, "falsifier_missing"],
     "claim_text": claims.set_index("local_id").loc[cid, "claim_text"]}
    for cid in _cell_claims
]))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "All claim text comes from `viz.fetch_claims`; the three time figures "
        "from `viz.metrics_by_id`, parsed with `viz.numeric_value`. The map's "
        "cell readings are notebook-level data and are printed with the claim "
        "text they were read from, so the mapping can be audited without "
        "leaving the page."
    ),
)


HOME_AI_BENCHMARKS = dict(
    name="06_home_ai_safety_benchmarks",
    title="Home-AI safety benchmarks: what the reported numbers measure, and what they miss",
    claim_ids=[
        "C031", "C032", "C033", "C037", "C038", "C039", "C040", "C041",
        "C042", "C106", "C107", "C108", "C119",
    ],
    provenance_intro=(
        "Every result here comes from a research artefact the corpus "
        "registered as a source, not from testing of a commercial assistant: "
        "`C042` states that no commercial assistant publishes safety benchmark "
        "results. The provenance panels name the artefact behind each number, "
        "which is the only way to read the comparison chart honestly."
    ),
    evidence_md=(
        "### Reported success rates, against a baseline that does nothing\n\n"
        "`M079` records a baseline of 29.98% exact match and a SAGE system at "
        "1.77%; `M077` and `M078` record DS-IA at 58.56% exact match with a "
        "74.90 F1 score. `M083` then records the finding that matters most for "
        "reading those numbers: a constant 'never act' predictor already "
        "reaches 82% accuracy. The reference line below is that critic, drawn "
        "on the same axis as the results it undermines."
    ),
    evidence_code='''\
# M079 states two values in one cell ("29.98 and 1.77"), so parse_numbers keeps
# them in the order the cell writes them and the labels say which is which.
# Both DS-IA figures are drawn because exact match and F1 are different
# measures of the same system, not two systems.
_results = viz.metrics_by_id(["M079", "M077", "M078", "M083"])
_by_id = _results.set_index("local_id")
_ms = viz.parse_numbers(_by_id.loc["M079", "value"])
_systems = pd.DataFrame([
    {"system": "Baseline (M079, value 1 of 2)", "pct": _ms[0] if _ms else None,
     "measure": "exact match", "source": _by_id.loc["M079", "source_ref"]},
    {"system": "SAGE (M079, value 2 of 2)",
     "pct": _ms[1] if len(_ms) > 1 else None,
     "measure": "exact match", "source": _by_id.loc["M079", "source_ref"]},
    {"system": "DS-IA (M077)", "pct": viz.numeric_value(_by_id.loc["M077", "value"]),
     "measure": "exact match", "source": _by_id.loc["M077", "source_ref"]},
    {"system": "DS-IA (M078)", "pct": viz.numeric_value(_by_id.loc["M078", "value"]),
     "measure": "F1 score", "source": _by_id.loc["M078", "source_ref"]},
])
show(_systems)

_never_act = viz.numeric_value(_by_id.loc["M083", "value"])
fig = go.Figure(go.Bar(
    x=_systems["system"],
    y=_systems["pct"],
    marker_color=["#757575", "#757575", "#1f77b4", "#7aa6d2"],
    text=["%g%%" % value for value in _systems["pct"]],
    textposition="outside",
    customdata=list(zip(_systems["measure"], _systems["source"])),
    hovertemplate=("%{x}<br>%{customdata[0]}: %{y}%"
                   "<br>source: %{customdata[1]}<extra></extra>"),
))
if _never_act is not None:
    fig.add_hline(
        y=_never_act,
        line_dash="dot",
        line_color="#b06000",
        annotation_text=(f"M083: constant 'never act' predictor already "
                         f"reaches {_never_act:g}%"),
        annotation_position="bottom right",
    )
fig.update_layout(
    title=("Reported accuracy on home-AI intent benchmarks, with the "
           "do-nothing baseline drawn (M077-M079, M083)"),
    yaxis_title="percent as stated (exact match or F1, per bar)",
    height=380,
    xaxis=dict(tickangle=-15),
)
fig.show()

# Counts of what the benchmarks contain. These bars are deliberately not read
# as a comparison: they count different objects recorded by different artefacts.
DESIGN_IDS = ["M071", "M072", "M073", "M084", "M085"]
design = viz.metrics_by_id(DESIGN_IDS)
show(design[["local_id", "metric_name", "value", "unit", "confidence",
             "source_ref", "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))
fig = go.Figure(go.Bar(
    x=design["local_id"] + " " + design["metric_name"],
    y=[viz.numeric_value(value) for value in design["value"]],
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in design["confidence"]],
    text=[viz.numeric_value(value) for value in design["value"]],
    textposition="outside",
    customdata=list(zip(design["value"], design["unit"], design["source_ref"])),
    hovertemplate=("%{x}<br>stated: %{customdata[0]} %{customdata[1]}"
                   "<br>source: %{customdata[2]}<extra></extra>"),
))
fig.update_layout(
    title=("Scale of the recorded test designs: five counts of five different "
           "objects (not a comparison)"),
    yaxis_title="count of the unit named in the hover",
    height=380,
    xaxis=dict(tickangle=-20),
)
fig.show()
''',
    context_md=(
        "### Safety-relevant measures that are not accuracies\n\n"
        "Four recorded quantities in this cluster are not success rates: the "
        "Cascade verifier's rejection rate for invalid instructions (`M080`), "
        "a dependency-satisfaction ratio (`M081`), an unsafe-execution rate "
        "(`M082`) and a direct-command accuracy for local models (`M076`). "
        "They are kept as a table with their own units because a ratio, a rate "
        "and a percentage cannot share an axis without implying a common "
        "scale. `M074` and `M075` record the benchmark rubric's weights, which "
        "is why the cluster's scoring is not a single number."
    ),
    context_code='''\
display(HTML(
    "<h4>Safety measures recorded in units other than percent</h4>"
    "<p>Each row is one metric; the unit column is the corpus's own. A ratio "
    "and a rate are not percentages, so they are not drawn on the percent "
    "axis above.</p>"
))
_measures = viz.metrics_by_id(["M080", "M081", "M082", "M076", "M074", "M075"])
show(_measures[["local_id", "metric_name", "value", "unit", "confidence",
                "source_ref", "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))

display(HTML("""
<h4>What the cluster does not contain</h4>
<p><code>C041</code> states that no unified harness evaluates all fourteen
scenario categories across systems with a consistent rubric, and
<code>C042</code> states that commercial assistants publish no benchmark
results at all. The corpus therefore records research artefacts and
methodology claims (<code>C106</code>, <code>C107</code>, <code>C108</code>),
not comparative product results.</p>
"""))
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### The numbers above come from five different artefacts\n\n"
        "DS-IA (`S47`), PromptShield Home (`S48`), the dependency-aware "
        "orchestration work (`S49`), SimVerity (`S52`) and the Evil-AI "
        "adversarial corpus (`S78`) are separate research efforts with "
        "separate test sets. The bars on the first chart compare systems "
        "*within* one artefact's evaluation; the design-count chart spans all "
        "of them and is explicitly not a comparison. The corpus records no "
        "common test set, which is exactly what `C041` complains about.\n\n"
        "Other limits on this page:\n\n"
        "- **A high accuracy can be a red flag.** `M083` records that a "
        "constant 'never act' predictor reaches 82% accuracy, which is why "
        "unsafe-execution rates (`M082`, `0.02`) matter more than aggregate "
        "accuracy when the task is safety-critical.\n"
        "- **`C031`'s failure modes are low confidence.** Hallucinated device "
        "state, mistaken identity and over-broad automation are recorded as "
        "reported signal at low confidence, so they are described rather than "
        "charted.\n"
        "- **`C119` records a framework with no implementation.** The "
        "'Circles of Trust' privilege model is proposed in research; the "
        "corpus records no commercial product that ships it.\n"
        "- **Nothing here measures a shipping assistant.** `C042` is explicit "
        "that Alexa, Google Home, Siri and SmartThings publish no safety "
        "benchmark results, so no figure on this page can be used to rank "
        "them."
    ),
    uncertainty_code='''\
# Benchmark-existence and methodology claims are separated from the results,
# so a claim that a benchmark exists is never read as a result from it.
display(HTML(
    "<h4>Methodology claims in this cluster, with their evidence class</h4>"
    "<p>A claim that a benchmark exists is not a claim about what it "
    "found.</p>"
))
show(claims.loc[claims["local_id"].isin(
        ["C041", "C042", "C106", "C107", "C108", "C119"]),
    ["local_id", "claim_type", "confidence", "workflow_stage",
     "source_refs", "falsifier_missing", "claim_text"]].rename(
    columns={"local_id": "claim", "claim_type": "type", "confidence": "conf",
             "workflow_stage": "stage", "source_refs": "sources",
             "falsifier_missing": "no_falsifier"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Every number is read by explicit metric id with `viz.metrics_by_id` "
        "and parsed with `viz.parse_numbers` / `viz.numeric_value`, because "
        "the value cells are authored strings ('29.98 and 1.77', 'up to "
        "86.7'). Claim text and evidence classes come from "
        "`viz.fetch_claims`. No result is transcribed from the markdown "
        "corpus by hand."
    ),
)


ENERGY_MODEL = dict(
    name="12_flexibility_model_and_field_economics",
    title="Energy flexibility: the model's baseline, its emissions, and the two programme results",
    claim_ids=["C051", "C052", "C053", "C056", "C059", "C060", "C090", "C117", "C118"],
    provenance_intro=(
        "This cluster mixes modelled inputs with measured programme outcomes, "
        "and the extraction log records the model's baseline, sensitivity and "
        "payback values as scenario assumptions rather than measurements "
        "(decision `L034`). The panels below keep the two apart: everything in "
        "the model's baseline section is an input, and only the "
        "demand-response results are field measurements."
    ),
    evidence_md=(
        "### What the flexibility model assumes a household consumes\n\n"
        "The model's baseline section records annual consumption for five "
        "loads on one unit (kWh per year), which is the only part of the model "
        "that can share an axis. `M107` states a daily figure for the same "
        "household (30 kWh/day) and `M113`/`M114` state generation and storage "
        "capacity rather than consumption; all three are shown in the table "
        "and kept off the chart, and no total is computed, because the corpus "
        "records none and the daily and annual figures are different bases."
    ),
    evidence_code='''\
# Only rows whose unit says kWh/year belong on this axis. M107 (kWh/day),
# M113 (kW; kWh/year generation) and M114 (kWh; kW capacity) are different
# quantities and stay in the table below.
BASELINE_SECTION = "1. System Boundary and Baseline"
baseline_rows = viz.section_metrics(BASELINE_SECTION)
show(baseline_rows[["local_id", "metric_name", "value", "unit", "confidence",
                    "conditions_stated"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "conditions_stated": "cond_stated"}))

CONSUMPTION_IDS = ["M108", "M109", "M110", "M111", "M112"]
consumption = viz.metrics_by_id(CONSUMPTION_IDS)
consumption["kwh_year"] = [viz.numeric_value(value)
                           for value in consumption["value"]]
consumption = consumption.dropna(subset=["kwh_year"])
show(consumption[["local_id", "metric_name", "value", "unit", "kwh_year",
                  "confidence"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "confidence": "conf"}))

fig = go.Figure(go.Bar(
    x=consumption["local_id"] + " " + consumption["metric_name"],
    y=consumption["kwh_year"],
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in consumption["confidence"]],
    text=["%g" % value for value in consumption["kwh_year"]],
    textposition="outside",
    customdata=list(zip(consumption["value"], consumption["unit"],
                        consumption["confidence"])),
    hovertemplate=("%{x}<br>stated: %{customdata[0]} %{customdata[1]}"
                   "<br>confidence: %{customdata[2]}<extra></extra>"),
))
fig.update_layout(
    title=("Modelled baseline annual consumption by load (kWh/year). Model "
           "inputs, not measurements; no total is computed"),
    yaxis_title="kWh per year, as stated",
    height=380,
    xaxis=dict(tickangle=-20),
)
fig.show()
''',
    context_md=(
        "### Emissions are modelled; the two programme results are not\n\n"
        "`M127` records the emission factors the model applies, all in kg CO2 "
        "per kWh, so the three factors can share an axis; the reductions that "
        "follow from them (`M128`-`M130`) are modelled outputs and are shown "
        "as text. Against those stand the two field results in this cluster: "
        "the UK demand-flexibility programme reduced peak demand by `23.1%` "
        "among compliers (`M089`, recorded in wave 1's energy notebook) and by "
        "`28.1%` among all participants (`M090`). They are shown together "
        "because the gap between them is the participation effect, and the "
        "corpus states both populations explicitly."
    ),
    context_code='''\
# Emission factors share one unit (kg CO2 per kWh), so they can be charted.
# The three labels are the three readings the value cell writes, in order.
_factors = viz.metrics_by_id(["M127"])
_numbers = viz.parse_numbers(_factors["value"].iloc[0]) if not _factors.empty else []
_factor_labels = ["average", "peak marginal", "off-peak marginal"][:len(_numbers)]
_factor_rows = pd.DataFrame({
    "reading": _factor_labels,
    "kg_co2_per_kwh": _numbers,
    "metric": _factors["local_id"].iloc[0] if not _factors.empty else "",
    "confidence": _factors["confidence"].iloc[0] if not _factors.empty else None,
})
show(_factor_rows)

fig = go.Figure(go.Bar(
    x=_factor_rows["reading"],
    y=_factor_rows["kg_co2_per_kwh"],
    marker_color=["#1f77b4", "#b06000", "#1a7f37"][:len(_factor_rows)],
    text=["%g" % value for value in _factor_rows["kg_co2_per_kwh"]],
    textposition="outside",
    customdata=list(zip(_factor_rows["metric"], _factor_rows["confidence"])),
    hovertemplate=("%{x}<br>%{y} kg CO2 per kWh (metric %{customdata[0]},"
                   " confidence %{customdata[1]})<extra></extra>"),
))
fig.update_layout(
    title=("Emission factors applied by the model (M127): one unit, three "
           "stated marginalities"),
    yaxis_title="kg CO2 per kWh",
    height=320,
)
fig.show()

# The modelled reductions are stated in different units (kg per year, tonnes
# per year, percent per household), so they are a table, not a chart.
display(HTML("<h4>Modelled emissions reductions</h4>"
             "<p>Modelled outputs: they follow from the factors above and the "
             "baseline consumption, not from measurement.</p>"))
show(viz.metrics_by_id(["M128", "M129", "M130"])[
    ["local_id", "metric_name", "value", "unit", "confidence", "source_ref"]]
     .rename(columns={"local_id": "metric", "metric_name": "name",
                      "source_ref": "source", "confidence": "conf"}))

display(HTML("<h4>Peak-demand reduction: compliers against all participants</h4>"
             "<p>Both figures come from the same nationwide UK field "
             "experiment; the populations differ, and the corpus states "
             "both.</p>"))
_peak = viz.metrics_by_id(["M089", "M090"])
_peak["population"] = ["compliers", "all participants"]
show(_peak[["local_id", "population", "metric_name", "value", "unit",
            "confidence", "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))

fig = go.Figure(go.Bar(
    x=_peak["population"],
    y=[viz.numeric_value(value) for value in _peak["value"]],
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in _peak["confidence"]],
    text=["%g%%" % viz.numeric_value(value) for value in _peak["value"]],
    textposition="outside",
    customdata=list(zip(_peak["local_id"], _peak["value"], _peak["source_ref"])),
    hovertemplate=("%{x}<br>stated: %{customdata[1]}% "
                   "(metric %{customdata[0]}, source %{customdata[2]})"
                   "<extra></extra>"),
))
fig.update_layout(
    title=("Measured peak-demand reduction in the UK flexibility programme, "
           "by stated population (M089, M090)"),
    yaxis_title="percent reduction",
    height=320,
)
fig.show()

display(HTML("<h4>The rest of the programme economics, as recorded</h4>"))
show(viz.metrics_by_id(["M091", "M092", "M093", "M153", "M125", "M126"])[
    ["local_id", "metric_name", "value", "unit", "confidence", "source_ref",
     "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### Which numbers on this page are measured, and which are inputs\n\n"
        "Only the two peak-demand figures come from a field experiment. The "
        "baseline consumption rows, the emission factors and the modelled "
        "reductions are model inputs or outputs, recorded at medium confidence "
        "because the extraction log classifies the model as scenario "
        "assumptions rather than measurements.\n\n"
        "Other limits on this page:\n\n"
        "- **Two consumption bases for one household.** `M107` states 30 "
        "kWh/day while `M108`-`M112` state annual figures for individual "
        "loads. The corpus never reconciles them, so this page does not "
        "either: no total is computed and the daily figure stays a table "
        "row.\n"
        "- **No universal savings claim is available.** `C090` (a documented "
        "fact, recorded under interpretation warnings) states that the "
        "research does not prove universal energy savings: results hold under "
        "particular tariffs, climates, equipment and participation "
        "conditions.\n"
        "- **`C056` is an inference, not a measurement.** The claim that "
        "demand-response compensation dominates the economics rather than "
        "energy arbitrage alone is the corpus's own reading of its scenario "
        "model.\n"
        "- **The fleet emissions figure is not a forecast.** `M129` states "
        "792,000 tonnes CO2/year by scaling a per-household figure, so it "
        "inherits every assumption in the model.\n"
        "- **Solar and battery rows mix two units in one cell.** `M113` and "
        "`M114` state capacity and output together (kW and kWh), which is why "
        "they stay in the table rather than on an axis."
    ),
    uncertainty_code='''\
# Model inputs are separated from field results by section, so a reader can see
# how much of the page rests on scenario assumptions rather than measurement.
display(HTML(
    "<h4>Where each modelled quantity sits in the corpus</h4>"
    "<p>The model spans four sections; the field results sit outside them.</p>"
))
_MODELLED_SECTIONS = ["1. System Boundary and Baseline",
                      "4. Core Financial Model", "7. Stress Tests",
                      "Payback and NPV"]
_modelled = pd.concat([viz.section_metrics(section)
                       for section in _MODELLED_SECTIONS], ignore_index=True)
show(_modelled.groupby("section").agg(
    metrics=("local_id", "count"),
    medium_confidence=("confidence", lambda s: int((s == "medium").sum())),
).reset_index().rename(columns={"section": "modelled_section"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Section-scoped rows come from `viz.section_metrics`; named rows from "
        "`viz.metrics_by_id`. Numbers are parsed with `viz.numeric_value` and "
        "`viz.parse_numbers`, and the three emission-factor labels are the "
        "three readings the value cell writes, in cell order."
    ),
)

LIFECYCLE_GAPS = dict(
    name="16_lifecycle_practice_gaps",
    title="Lifecycle security: the scorecard's calibration, and the gap between policy and practice",
    claim_ids=["C062", "C063", "C071", "C072", "C073", "C074", "C102", "C104"],
    provenance_intro=(
        "Wave 1 charted stated support periods by device category. This "
        "notebook looks at the other half of the same subject: what the "
        "scorecard is calibrated to measure, and which practical gaps the "
        "corpus records around it. The claims below run from documented facts "
        "(`C062`, `C063`, `C074`) to reported signals about specific findings "
        "(`C071`, `C072`, `C073`, `C102`, `C104`), so the panels keep the two "
        "apart."
    ),
    evidence_md=(
        "### The scorecard's own calibration, before any product is scored\n\n"
        "`M066` records 14 lifecycle controls, `M067` and `M068` record the "
        "highest and lowest control weights, and `M064`/`M065` record the "
        "composite scale: a maximum of 3.00 and a passing score of 2.00 on a "
        "weighted average. That is the framework the corpus proposes. The "
        "database holds no per-control scores, so this figure shows "
        "*calibration*, not results, and the uncertainty section says so "
        "explicitly."
    ),
    evidence_code='''\
# Framework rows, read by id. M064/M065 share the unit "weighted average", so
# they may share an axis; M066-M068 are counts and weights and are annotated
# instead of plotted on that axis.
_scale = viz.metrics_by_id(["M064", "M065"])
_scale["reading"] = ["composite maximum", "minimum passing score"]
show(_scale[["local_id", "reading", "value", "unit", "confidence",
             "source_ref"]].rename(
    columns={"local_id": "metric", "source_ref": "source",
             "confidence": "conf"}))

_structure = viz.metrics_by_id(["M066", "M067", "M068"])
show(_structure[["local_id", "metric_name", "value", "unit", "confidence",
                 "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))

_passing = viz.numeric_value(_scale.loc[_scale["local_id"] == "M065", "value"].iloc[0])
fig = go.Figure(go.Bar(
    x=[viz.numeric_value(value) for value in _scale["value"]],
    y=_scale["reading"] + " (" + _scale["local_id"] + ")",
    orientation="h",
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in _scale["confidence"]],
    text=["%g" % viz.numeric_value(value) for value in _scale["value"]],
    textposition="outside",
    customdata=list(zip(_scale["value"], _scale["unit"], _scale["source_ref"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]} %{customdata[1]}"
                   "<br>source: %{customdata[2]}<extra></extra>"),
))
if _passing is not None:
    fig.add_vline(x=_passing, line_dash="dot", line_color="#333333",
                  annotation_text="M065: minimum passing score",
                  annotation_position="top right")
fig.update_layout(
    title=("The scorecard's calibration as recorded: 14 controls, weights "
           "1.0 and 0.7, composite out of 3.00 (M064-M068)"),
    xaxis_title="weighted-average composite",
    height=320,
    yaxis=dict(autorange="reversed"),
)
fig.show()
''',
    context_md=(
        "### Where the corpus's lifecycle-security evidence actually sits\n\n"
        "The count below is computed, not estimated: every claim recorded "
        "against workflow stage `W9` (Lifecycle Security and Privacy Scoring), "
        "grouped by the section it was written in. It answers a different "
        "question from the scorecard: not 'how secure is a product' but "
        "'which lifecycle-security subjects did this corpus spend its evidence "
        "on'. Sections are document sections, not control areas."
    ),
    context_code='''\
_corpus_claims = viz.fetch_all_claims()
_w9 = (_corpus_claims[_corpus_claims["workflow_stage"] == "W9"]
       .groupby("section").size().reset_index(name="claims")
       .sort_values("claims", ascending=False))
display(HTML(
    f"<h4>W9 claims by section ({int(_w9['claims'].sum())} claims in total)</h4>"
    "<p>Computed by grouping the full claim table; no count is typed in by "
    "hand.</p>"
))
show(_w9)
fig = go.Figure(go.Bar(
    x=_w9["claims"],
    y=_w9["section"],
    orientation="h",
    marker_color="#4c78a8",
    text=_w9["claims"],
    textposition="outside",
    hovertemplate="%{y}<br>%{x} claims at stage W9<extra></extra>",
))
fig.update_layout(
    title=("Where the corpus put its lifecycle-security claims "
           "(workflow stage W9, by section)"),
    xaxis_title="claims",
    height=380,
    yaxis=dict(autorange="reversed", automargin=True),
)
fig.show()

# The practical gaps that are recorded as numbers, each with its own kind of
# unit: a count of product models, a duration in months, and an explicit "none".
display(HTML(
    "<h4>Recorded practice gaps</h4>"
    "<p><code>M069</code> counts product models found transmitting video in "
    "plaintext; <code>M063</code> records AI-assistant data-retention "
    "defaults; <code>M070</code> records that UK PSTI mandates no minimum "
    "support period at all, which is a different statement from mandating a "
    "short one.</p>"
))
show(viz.metrics_by_id(["M069", "M063", "M070"])[
    ["local_id", "metric_name", "value", "unit", "confidence", "source_ref",
     "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### This page cannot rank any product\n\n"
        "The corpus stores the scorecard's shape (`M064`-`M068`) and no "
        "per-control scores, so a 14-control radar or a product league table "
        "would be invented rather than drawn. Wave 1 reached the same "
        "conclusion from the support-period side; this notebook reaches it "
        "from the calibration side.\n\n"
        "Other limits on this page:\n\n"
        "- **The section counts measure documentation, not security.** The "
        "chart above counts where claims were written, which is a statement "
        "about this corpus's attention, not about any product's lifecycle "
        "controls.\n"
        "- **`M070` cannot be drawn as a zero bar.** UK PSTI mandating no "
        "minimum period is a different statement from mandating a short one, "
        "so it stays a table row.\n"
        "- **`M069` is two product models from one publication.** It is a "
        "finding, not an incidence rate, and the corpus records no sample "
        "frame behind it.\n"
        "- **`C071` (prompt injection with physical consequences) and `C072` "
        "(biometric spoofing with no liveness standard) are reported signals "
        "at medium confidence.** Both describe demonstrated attacks without a "
        "measured base rate.\n"
        "- **`C074` is the counterweight and is kept visible.** Matter secure "
        "commissioning (PASE) and device attestation are recorded as robust "
        "and mandatory for certified devices, so this page is not a claim that "
        "nothing works.\n"
        "- **`C102` records adoption without enforcement.** Vulnerability "
        "disclosure programmes are spreading, but the corpus records no "
        "response SLAs, so the claim is described rather than charted."
    ),
    uncertainty_code='''\
# The framework rows and the practice findings are separated here, because one
# is a proposed measurement instrument and the others are observations.
display(HTML(
    "<h4>Framework or finding? Each claim in the cluster, labelled</h4>"
    "<p>A claim that defines a control is not evidence that the control is "
    "met.</p>"
))
_framework_claims = ["C062", "C063", "C104"]
show(claims.loc[claims["local_id"].isin(_framework_claims),
                ["local_id", "claim_type", "confidence", "workflow_stage",
                 "source_refs", "falsifier_missing", "claim_text"]].rename(
    columns={"local_id": "claim", "claim_type": "type", "confidence": "conf",
             "workflow_stage": "stage", "source_refs": "sources",
             "falsifier_missing": "no_falsifier"}))
_finding_claims = ["C071", "C072", "C073", "C074", "C102"]
show(claims.loc[claims["local_id"].isin(_finding_claims),
                ["local_id", "claim_type", "confidence", "workflow_stage",
                 "source_refs", "falsifier_missing", "claim_text"]].rename(
    columns={"local_id": "claim", "claim_type": "type", "confidence": "conf",
             "workflow_stage": "stage", "source_refs": "sources",
             "falsifier_missing": "no_falsifier"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Framework rows and practice findings are read by explicit metric id "
        "with `viz.metrics_by_id`; the section counts come from "
        "`viz.fetch_all_claims` grouped in pandas. This notebook deliberately "
        "reuses no figure from `notebooks/1/15_support_period_landscape.ipynb`, "
        "which covers mandated and stated support periods."
    ),
)


AI_HUB_LANDSCAPE = dict(
    name="19_ai_hub_landscape",
    title="AI hubs and local compute: price, capacity and the adoption the corpus records",
    claim_ids=["C081", "C083", "C084", "C095", "C096"],
    provenance_intro=(
        "Nothing in this cluster is a documented fact: `C083`, `C084` and "
        "`C095` are reported signals at medium confidence, while `C081` and "
        "`C096` are inferences (`C096` at low confidence, from the trade "
        "press). The product figures behind them are recorded at low "
        "confidence in the metric table, and the panels make that visible "
        "before any bar is drawn."
    ),
    evidence_md=(
        "### Price is the only attribute three of the four products share\n\n"
        "`M011` prices the (rumoured) Apple Home Hub at 349-400 USD, `M015` "
        "prices Home Assistant Green at 199 USD and `M016` prices MasterAgent "
        "MA100 at 20,000 USD. Compute is recorded for only two products "
        "(`M013`, `M016`), so a price-versus-compute scatter would contain a "
        "single complete point and is not drawn. The price axis is logarithmic "
        "because the recorded range spans two orders of magnitude, and Anker "
        "MindBase is listed as 'no price recorded' rather than drawn at zero."
    ),
    evidence_code='''\
# Price is written three different ways in this section, so each row states how
# its number was read:
#   M011  one range in one cell ("349-400")  -> viz.range_value
#   M015  one number in one cell ("199")     -> viz.range_value
#   M016  compute and price together ("2,070 TOPS; 20,000" with unit
#         "TOPS; USD")                       -> positional pairing by unit token
# The positional pairing is safe because the unit cell lists its units in the
# same order as the value cell lists its numbers, and it is stated here rather
# than left implicit.
hub_metrics = viz.metrics_by_id(["M011", "M013", "M015", "M016"])
hub_by_id = hub_metrics.set_index("local_id")


def _number_for_unit(metric_id, unit_token):
    """Number whose position matches the unit token in the metric's unit cell."""
    record = hub_by_id.loc[metric_id]
    numbers = viz.parse_numbers(record["value"])
    units = [token.strip() for token in str(record["unit"] or "").split(";")]
    if unit_token in units and units.index(unit_token) < len(numbers):
        return numbers[units.index(unit_token)]
    return None


_price_rows = []
for _mid, _product in (("M011", "Apple Home Hub (J490)"),
                       ("M015", "Home Assistant Green"),
                       ("M016", "MasterAgent MA100")):
    _low, _high = viz.range_value(hub_by_id.loc[_mid, "value"])
    if _mid == "M016":
        # range_value refuses a cell that holds two quantities, so the price is
        # taken by its unit token instead.
        _price = _number_for_unit("M016", "USD")
        _low, _high = _price, _price
        _reading = "price paired by unit token (cell holds compute and price)"
    else:
        _reading = "stated range" if _low != _high else "single stated value"
    _price_rows.append({
        "metric": _mid, "product": _product,
        "stated": hub_by_id.loc[_mid, "value"],
        "price_low": _low, "price_high": _high,
        "unit": hub_by_id.loc[_mid, "unit"],
        "confidence": hub_by_id.loc[_mid, "confidence"],
        "reading": _reading,
    })
priced = pd.DataFrame(_price_rows)
priced["compute_recorded"] = [
    "not recorded", "not recorded",
    hub_by_id.loc["M016", "value"] if "M016" in hub_by_id.index
    else "not recorded",
]
show(priced)

# The fourth product has compute but no recorded price, which is why it cannot
# appear on the price axis even though it is described in the same section.
if "M013" in hub_by_id.index:
    _anker = hub_by_id.loc["M013"]
    show(pd.DataFrame([{
        "metric": "M013", "product": "Anker MindBase",
        "stated": _anker["value"], "unit": _anker["unit"],
        "note": "no price recorded in the corpus",
        "confidence": _anker["confidence"],
    }]))

fig = go.Figure(go.Bar(
    x=[(low + high) / 2 for low, high in
       zip(priced["price_low"], priced["price_high"])],
    y=priced["product"] + " (" + priced["metric"] + ")",
    orientation="h",
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in priced["confidence"]],
    error_x=dict(type="data",
                 array=[(high - low) / 2 for low, high in
                        zip(priced["price_low"], priced["price_high"])],
                 arrayminus=[(high - low) / 2 for low, high in
                             zip(priced["price_low"], priced["price_high"])],
                 visible=True),
    customdata=list(zip(priced["stated"], priced["compute_recorded"],
                        priced["reading"], priced["confidence"])),
    hovertemplate=("%{y}<br>stated cell: %{customdata[0]}"
                   "<br>compute recorded: %{customdata[1]}"
                   "<br>price reading: %{customdata[2]}"
                   "<br>confidence: %{customdata[3]}<extra></extra>"),
))
fig.update_layout(
    title=("Recorded hub prices, log scale (M011, M015, M016). Anker MindBase "
           "has no recorded price"),
    xaxis=dict(title="USD, as stated", type="log"),
    height=340,
    yaxis=dict(automargin=True),
)
fig.show()
''',
    context_md=(
        "### What the corpus records about the market around the hardware\n\n"
        "`M017` records private-label and utility-bundle brands at 30-35% of "
        "smart-plug unit shipments and `M018` puts the top five specialist "
        "brands at about 40%; the corpus records no figure for the remainder, "
        "so the two recorded shares are shown without a third bar and without "
        "a normalised pie. `C095` and `C096` add the two platform shifts the "
        "corpus noticed: a consumer router shipping as a Matter bridge, and "
        "camera support described in the trade press as a catalyst. `M012` "
        "records a modelled subscription breakeven of 20 months for the Apple "
        "hub, which is a business-model figure rather than a product one."
    ),
    context_code='''\
display(HTML(
    "<h4>Recorded shares of smart-plug unit shipments</h4>"
    "<p>Two shares are recorded; the corpus records no figure for the rest of "
    "the market, so no remainder is drawn.</p>"
))
_shares = viz.metrics_by_id(["M017", "M018"])
show(_shares[["local_id", "metric_name", "value", "unit", "confidence",
              "conditions_stated", "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "conditions_stated": "cond_stated", "source_ref": "source",
             "confidence": "conf"}))

fig = go.Figure(go.Bar(
    x=[viz.numeric_value(value) for value in _shares["value"]],
    y=[f"{record['local_id']} {record['metric_name']}"
       for record in _shares.to_dict("records")],
    orientation="h",
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in _shares["confidence"]],
    text=[record["value"] for record in _shares.to_dict("records")],
    textposition="outside",
    customdata=list(zip(_shares["value"], _shares["unit"],
                        _shares["conditions_stated"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]} %{customdata[1]}"
                   "<br>conditions stated: %{customdata[2]}<extra></extra>"),
))
fig.update_layout(
    title=("Recorded share of smart-plug shipments (M017, M018). The "
           "remainder is not recorded and is not drawn"),
    xaxis_title="percent of unit shipments",
    height=300,
    yaxis=dict(automargin=True, autorange="reversed"),
)
fig.show()

display(HTML(
    "<h4>Hub adoption and platform-shift claims</h4>"
    "<p><code>M008</code> (5% of US internet households) is the corpus's "
    "hub-adoption figure; <code>M010</code> (52%) and <code>M009</code> (19%) "
    "are the adjacent ownership and attach rates, drawn in wave 1's business "
    "notebook and echoed here only as context, each against its own "
    "denominator.</p>"
))
show(viz.metrics_by_id(["M008", "M010", "M009", "M012", "M014"])[
    ["local_id", "metric_name", "value", "unit", "confidence", "source_ref"]]
     .rename(columns={"local_id": "metric", "metric_name": "name",
                      "source_ref": "source", "confidence": "conf"}))
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### Prices are estimates, and compute is a vendor claim\n\n"
        "`M011` is recorded at low confidence and the Apple Home Hub entity "
        "itself is typed `Product (rumoured)`; `M013`, `M014` and `M016` are "
        "vendor-stated capacity and compute figures. The chart above is "
        "therefore a picture of what the market was reported to be launching, "
        "not a price list.\n\n"
        "Other limits on this page:\n\n"
        "- **No unit shipments are recorded.** The corpus holds two shares "
        "(`M017`, `M018`) and no volumes, so nothing here can be scaled to a "
        "market size.\n"
        "- **`M017` has no stated conditions** (`conditions_stated = false`), "
        "so the 30-35% figure carries a geography, a period and a measurement "
        "method that the corpus never recorded.\n"
        "- **Compute figures are not comparable.** `M013` states 26 TOPS and "
        "`M016` states 2,070 TOPS for devices in different classes; they are "
        "kept in one table only because the corpus records both in the same "
        "section.\n"
        "- **`C096` is a low-confidence inference** that camera support could "
        "act as a catalyst for Matter adoption. It is a trade-press reading, "
        "not a measurement.\n"
        "- **`C095` has no counterpart in the metric table.** The router that "
        "acts as a Matter bridge is described in a claim; no metric records "
        "its share, price or reach."
    ),
    uncertainty_code='''\
# Vendor-claim metrics are separated from survey metrics, because 'a vendor
# states' and 'a survey found' are different kinds of number.
_vendor_ids = ["M011", "M012", "M013", "M014", "M016", "M018"]
_survey_ids = ["M008", "M017"]
display(HTML(
    "<h4>Vendor-stated figures against survey or market figures</h4>"
    "<p>The split is by source, not by confidence level.</p>"
))
_provenance = viz.metrics_by_id(_vendor_ids + _survey_ids)
_provenance["kind"] = ["vendor or trade statement"] * len(_vendor_ids) + \\
                      ["survey or market report"] * len(_survey_ids)
show(_provenance[["local_id", "metric_name", "kind", "value", "unit",
                  "confidence", "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Prices and shares are read by explicit metric id and parsed with "
        "`viz.range_value` (ranges) and `viz.numeric_value` (single values). "
        "The survey rows (`M008`, `M009`, `M010`) are shown as context only; "
        "wave 1's business notebook charts them. No figure is transcribed from "
        "the vendor announcements in the corpus."
    ),
)


HOUSEHOLD_ECONOMICS = dict(
    name="22_household_economics_and_barriers",
    title="Why households stall: recorded barriers, setup friction, and what ownership costs",
    claim_ids=["C082", "C087", "C088", "C113", "C114"],
    provenance_intro=(
        "The claims in this cluster are where the corpus does its own "
        "summarising: `C082` is an inference that device counts overstate "
        "engagement by 2-3x, `C087` is an inference that the post-purchase gap "
        "is a product-design problem, `C088` is a documented fact warning that "
        "the business analysis cannot yet support company-level conclusions, "
        "and `C113` is a reported insurer-pilot figure. The panels below keep "
        "the survey numbers and the corpus's own judgements apart."
    ),
    evidence_md=(
        "### Barriers, each against the population it was measured in\n\n"
        "The corpus records barrier rates against different populations and in "
        "different countries: adopters and non-adopters (`M025`, 46 vs 52), a "
        "general respondent pool (`M026`, 42), a privacy-and-security pair "
        "stated together (`M027`, about 45 each), a Spanish sample (`M028`, "
        "53) and a French sample (`M029`, 82 price and 78 hacking). Each bar "
        "carries the denominator from its own `unit` cell in the hover; the "
        "bars are not averaged, because there is no single population behind "
        "them."
    ),
    evidence_code='''\
# (metric id, bar label, index of the number to use). Some value cells state two
# populations in one string ("46 vs 52"); parse_numbers keeps the order the cell
# writes them, and the label says which population that position is.
BARRIER_ROWS = [
    ("M025", "Cost barrier, adopters", 0),
    ("M025", "Cost barrier, non-adopters", 1),
    ("M026", "Cost makes connected products less appealing", 0),
    ("M027", "Privacy and security concerns (stated as 'about 45% each')", 0),
    ("M028", "Cost barrier, Spain", 0),
    ("M029", "Price concern, France", 0),
    ("M029", "Hacking concern, France", 1),
]
_barrier_metrics = viz.metrics_by_id(["M025", "M026", "M027", "M028", "M029"])
_barrier_metrics = _barrier_metrics.set_index("local_id")
_rows = []
for _mid, _label, _index in BARRIER_ROWS:
    if _mid not in _barrier_metrics.index:
        continue
    _record = _barrier_metrics.loc[_mid]
    _numbers = viz.parse_numbers(_record["value"])
    if _index >= len(_numbers):
        continue
    _rows.append({"metric": _mid, "barrier": _label, "pct": _numbers[_index],
                  "stated": _record["value"], "unit": _record["unit"],
                  "confidence": _record["confidence"],
                  "source": _record["source_ref"]})
barriers = pd.DataFrame(_rows).sort_values("pct", ascending=False)
show(barriers)

fig = go.Figure(go.Bar(
    x=barriers["pct"],
    y=barriers["barrier"] + " (" + barriers["metric"] + ")",
    orientation="h",
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in barriers["confidence"]],
    text=["%g%%" % value for value in barriers["pct"]],
    textposition="outside",
    customdata=list(zip(barriers["stated"], barriers["unit"],
                        barriers["source"], barriers["confidence"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]} (unit: %{customdata[1]})"
                   "<br>source: %{customdata[2]}"
                   "<br>confidence: %{customdata[3]}<extra></extra>"),
))
fig.update_layout(
    title=("Recorded adoption barriers, each against its own stated "
           "population (not one shared denominator)"),
    xaxis_title="percent, as stated",
    height=420,
    yaxis=dict(automargin=True, autorange="reversed"),
)
fig.show()
''',
    context_md=(
        "### What ownership costs, and what setup costs in frustration\n\n"
        "Three recorded money figures describe the same household on three "
        "different clocks: `M036` is one-off upfront spend (3,750 USD), "
        "`M037` is monthly ongoing spend (70 USD per month) and `M035` is "
        "annual frustration spending (340 USD). They are drawn with their "
        "clocks on the labels rather than added together. The setup rows "
        "(`M019`-`M024`) are a different unit family again: rates, a count of "
        "usability issues, Net Promoter Scores and a repair cost."
    ),
    context_code='''\
display(HTML(
    "<h4>Recorded household money, each on its own clock</h4>"
    "<p>One-off, monthly and annual figures are not summed: the corpus "
    "records no conversion between them and no household profile to convert "
    "with.</p>"
))
_money = viz.metrics_by_id(["M036", "M037", "M035"])
show(_money[["local_id", "metric_name", "value", "unit", "confidence",
             "conditions_stated", "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "conditions_stated": "cond_stated", "source_ref": "source",
             "confidence": "conf"}))

fig = go.Figure(go.Bar(
    x=[viz.numeric_value(value) for value in _money["value"]],
    y=[f"{record['local_id']} {record['metric_name']} ({record['unit']})"
       for record in _money.to_dict("records")],
    orientation="h",
    marker_color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                  for c in _money["confidence"]],
    text=["%g" % viz.numeric_value(value) for value in _money["value"]],
    textposition="outside",
    customdata=list(zip(_money["value"], _money["unit"],
                        _money["conditions_stated"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]} %{customdata[1]}"
                   "<br>conditions stated: %{customdata[2]}<extra></extra>"),
))
fig.update_layout(
    title=("Recorded household spend by clock (one-off, per month, per year): "
           "three different quantities, not a total"),
    xaxis_title="value, in the unit named on the bar",
    height=320,
    yaxis=dict(automargin=True, autorange="reversed"),
)
fig.show()

display(HTML("<h4>Setup and connectivity friction, as recorded</h4>"))
show(viz.metrics_by_id(["M019", "M020", "M021", "M022", "M023", "M024",
                        "M030"])[
    ["local_id", "metric_name", "value", "unit", "confidence", "source_ref"]]
     .rename(columns={"local_id": "metric", "metric_name": "name",
                      "source_ref": "source", "confidence": "conf"}))

display(HTML(
    "<h4>Market sizes, with currencies as stated</h4>"
    "<p>Five market and revenue figures are recorded with different units and "
    "two currencies. They are not converted or summed.</p>"
))
show(viz.metrics_by_id(["M047", "M049", "M050", "M051", "M052"])[
    ["local_id", "metric_name", "value", "unit", "confidence",
     "conditions_stated", "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "conditions_stated": "cond_stated", "source_ref": "source",
             "confidence": "conf"}))
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### Six metrics in the corpus have no stated conditions\n\n"
        "The extraction log records `M017`, `M034`, `M035`, `M038`, `M049` and "
        "`M104` as carrying the placeholder 'conditions not stated in source'. "
        "Two of them (`M035` frustration spending, `M049` market size) appear "
        "on this page, so the list is printed in full below rather than only "
        "where it is convenient.\n\n"
        "Other limits on this page:\n\n"
        "- **Barrier rates are not one measurement.** A share of adopters, a "
        "share of non-adopters, a share of Spanish respondents and a share of "
        "French respondents cannot be averaged into one barrier index, so the "
        "figure keeps them separate.\n"
        "- **`C113` is a single pilot figure.** The insurer paying 47 EUR per "
        "policy comes from one Samsung/HSB pilot, recorded as reported signal "
        "at low confidence, and is not a market price.\n"
        "- **`C088` warns against the conclusion this page invites.** The "
        "corpus states its business analysis cannot yet support company-level "
        "investment conclusions without audited metrics and comparable "
        "definitions of active users, churn, service revenue and support "
        "cost.\n"
        "- **`C082` and `C087` are inferences.** 'Device counts overstate "
        "engagement by 2-3x' and 'the post-purchase gap is a product-design "
        "problem' are the corpus's readings, not measurements.\n"
        "- **`M027` states two concerns in one cell.** Privacy and security "
        "concerns are recorded as 'about 45% each', so they share one bar here "
        "rather than being split into two bars the corpus did not separate."
    ),
    uncertainty_code='''\
# The full unstated-conditions list comes from the schema's own view, so this
# page does not depend on which metrics happen to link to this cluster.
_con = viz.connect_db()
try:
    _unstated = pd.DataFrame(
        _con.execute("SELECT local_id, metric_name FROM unstated_conditions "
                     "ORDER BY local_id").fetchall(),
        columns=["metric", "name"],
    )
    _unstated_total = _con.execute(
        "SELECT COUNT(1) FROM unstated_conditions").fetchone()[0]
finally:
    _con.close()
display(HTML(
    f"<h4>Every metric the corpus records without conditions "
    f"({_unstated_total} in total)</h4>"
    "<p>Source: the <code>unstated_conditions</code> view, which reads "
    "<code>conditions_stated = false</code>.</p>"
))
show(_unstated)
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Barrier, money and market rows are read by explicit metric id with "
        "`viz.metrics_by_id` and parsed with `viz.parse_numbers`, so a value "
        "cell holding two populations ('46 vs 52') is split by position with "
        "the label stating which position is which. The "
        "`unstated_conditions` view is queried directly for the gap list."
    ),
)


GAP_AUDIT = dict(
    name="24_corpus_gap_audit",
    title="Corpus gap audit: missing falsifiers, unstated conditions, and the questions left open",
    claim_ids=["C075", "C076", "C077", "C078", "C088", "C089", "C090", "C091"],
    provenance_intro=(
        "This is the meta notebook of the catalogue: its subject is the corpus "
        "itself. The cluster is the set of claims in which the corpus states "
        "what it does not claim (`C088`-`C091`, all documented facts) and what "
        "it recommends next (`C075`-`C078`, all recommendations). Four of the "
        "eight carry no falsifier, which is the point of the page."
    ),
    evidence_md=(
        "### The corpus's own gap flags, counted from the schema's views\n\n"
        "Three views in `schemas/stage2.sql` expose the gaps directly: "
        "`missing_falsifiers`, `unstated_conditions` and `unstated_boundaries`. "
        "The fourth bar counts rows in `stage2_warning`, the ingestion-warning "
        "table. Nothing on this chart is estimated: each bar is a `COUNT(1)` "
        "over a view or table."
    ),
    evidence_code='''\
# Every count below is a COUNT(1) against a schema view or table, read in one
# connection so the numbers are from a single point in time.
_con = viz.connect_db()
try:
    gap_counts = pd.DataFrame([
        {"gap": "claims with falsifier_stated = false",
         "source": "missing_falsifiers",
         "count": _con.execute("SELECT COUNT(1) FROM missing_falsifiers").fetchone()[0]},
        {"gap": "metrics with conditions_stated = false",
         "source": "unstated_conditions",
         "count": _con.execute("SELECT COUNT(1) FROM unstated_conditions").fetchone()[0]},
        {"gap": "entities with boundary_stated = false",
         "source": "unstated_boundaries",
         "count": _con.execute("SELECT COUNT(1) FROM unstated_boundaries").fetchone()[0]},
        {"gap": "ingestion warnings recorded",
         "source": "stage2_warning",
         "count": _con.execute("SELECT COUNT(1) FROM stage2_warning").fetchone()[0]},
    ])
    decisions = pd.DataFrame(
        _con.execute(
            "SELECT decision_type, COUNT(1) AS decisions FROM extraction_decision "
            "GROUP BY decision_type ORDER BY decisions DESC, decision_type"
        ).fetchall(),
        columns=["decision_type", "decisions"],
    )
    open_rows = pd.DataFrame(
        _con.execute(
            "SELECT decision_type, COUNT(1) AS rows FROM open_questions "
            "GROUP BY decision_type ORDER BY rows DESC"
        ).fetchall(),
        columns=["decision_type", "open_view_rows"],
    )
    stages = pd.DataFrame(
        _con.execute(
            "SELECT local_id, stage_name FROM workflow_stage ORDER BY local_id"
        ).fetchall(),
        columns=["stage", "stage_name"],
    )
finally:
    _con.close()

show(gap_counts)
fig = go.Figure(go.Bar(
    x=gap_counts["count"],
    y=gap_counts["gap"] + " (" + gap_counts["source"] + ")",
    orientation="h",
    marker_color="#b06000",
    text=gap_counts["count"],
    textposition="outside",
    hovertemplate="%{y}<br>%{x} rows<extra></extra>",
))
fig.update_layout(
    title=("Recorded gaps, straight from the schema views "
           "(no gap is estimated from text)"),
    xaxis_title="rows",
    height=320,
    yaxis=dict(automargin=True, autorange="reversed"),
)
fig.show()

display(HTML(
    "<h4>What the <code>open_questions</code> view actually returns</h4>"
    "<p>The view unions two decision types, so its own contents are shown "
    "before the full decision profile.</p>"
))
show(open_rows)
show(decisions)
_open_types = {"open_question", "omission"}
fig = go.Figure(go.Bar(
    x=decisions["decisions"],
    y=decisions["decision_type"],
    orientation="h",
    marker_color=["#b32637" if t in _open_types else "#4c78a8"
                  for t in decisions["decision_type"]],
    text=decisions["decisions"],
    textposition="outside",
    hovertemplate="%{y}<br>%{x} decisions<extra></extra>",
))
fig.update_layout(
    title=("Every extraction decision type, counted (red = the two types the "
           "open_questions view exposes)"),
    xaxis_title="decisions",
    height=420,
    yaxis=dict(automargin=True, autorange="reversed"),
)
fig.show()
''',
    context_md=(
        "### Where the corpus's claims sit in its own workflow\n\n"
        "Every claim carries a workflow stage (`W3`-`W12`). Counting claims "
        "per stage is the most direct measure of where this corpus spent its "
        "research effort, and the stage names come from `workflow_stage` rather "
        "than from this notebook. The second table is what the corpus proposes "
        "to do about the gaps: the mixed-method study design behind stage `W10` "
        "(`M145`-`M152`), which is a plan rather than a result."
    ),
    context_code='''\
_corpus = viz.fetch_all_claims()
_stage_counts = (_corpus.groupby("workflow_stage").size()
                 .reset_index(name="claims"))
_stage_view = stages.merge(_stage_counts, left_on="stage",
                           right_on="workflow_stage", how="left")
_stage_view["claims"] = _stage_view["claims"].fillna(0).astype(int)
_stage_view = _stage_view.sort_values("stage")
show(_stage_view.rename(columns={"stage_name": "name"}))

fig = go.Figure(go.Bar(
    x=_stage_view["claims"],
    y=_stage_view["stage"] + " " + _stage_view["stage_name"],
    orientation="h",
    marker_color="#4c78a8",
    text=_stage_view["claims"],
    textposition="outside",
    hovertemplate="%{y}<br>%{x} claims<extra></extra>",
))
fig.update_layout(
    title=("Claims per workflow stage, with the stage names taken from the "
           "workflow_stage table"),
    xaxis_title="claims",
    height=470,
    yaxis=dict(automargin=True, autorange="reversed"),
)
fig.show()

display(HTML(
    "<h4>The follow-up study design the corpus proposes (M145-M152)</h4>"
    "<p>These rows describe a study that has not been run: sample sizes, "
    "instrument design, incentives, cost and the corpus's own quality "
    "self-assessment.</p>"
))
show(viz.metrics_by_id(["M145", "M146", "M147", "M148", "M149", "M150",
                        "M151", "M152"])[
    ["local_id", "metric_name", "value", "unit", "confidence", "source_ref",
     "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))
''' + _CLUSTER_PANEL,
    uncertainty_md=(
        "### These counts measure flags, not quality\n\n"
        "A claim without a falsifier is not automatically a bad claim: "
        "`C001`-`C005` are documented facts about a specification, and some "
        "claims are recommendations (`C075`-`C078`) for which a falsifier is "
        "not the right instrument. What the counts measure is the corpus's "
        "*discipline in recording disconfirming observations*, which is what "
        "the extraction log tracks.\n\n"
        "Other limits on this page:\n\n"
        "- **The ingestion-warning table is empty.** `stage2_warning` holds no "
        "rows in this database, so the gap mechanism that is actually "
        "populated is `extraction_decision` (56 rows across 11 types).\n"
        "- **The `open_questions` view is a union, not a backlog.** It returns "
        "`open_question` and `omission` decisions together, and most of its "
        "rows are omissions recorded during ingestion rather than research "
        "questions.\n"
        "- **`C088`-`C091` are the corpus's own caution.** Four documented "
        "facts state that the research does not prove Matter is unreliable, "
        "does not prove universal energy savings, does not establish security "
        "rankings as fact, and does not support company-level investment "
        "conclusions. They are why this page reports gaps rather than a "
        "quality score.\n"
        "- **The study design is a proposal.** `M150` (285,000-340,000 USD "
        "over 11 months) and `M151` (quality scores out of 5) describe a plan; "
        "nothing in this database shows it was executed.\n"
        "- **Recommendations carry no falsifiers by design.** `C075`-`C078` "
        "are `recommendation` claims and appear in the no-falsifier list, "
        "which is expected rather than a defect."
    ),
    uncertainty_code='''\
# Two independent readings of 'no falsifier' are compared rather than merged:
# the stored boolean flag and the literal placeholder text. They agree in this
# database, and stating that out loud is worth more than assuming it.
_all = viz.fetch_all_claims()
_flag_missing = set(_all.loc[~_all["falsifier_stated"], "local_id"])
_text_missing = set(_all.loc[_all["falsifier_missing"], "local_id"])
_compare = pd.DataFrame([{
    "flag_says_missing": len(_flag_missing),
    "cell_text_says_missing": len(_text_missing),
    "disagreements": len(_flag_missing ^ _text_missing),
}])
display(HTML(
    "<h4>Flag against placeholder text</h4>"
    "<p>The view <code>missing_falsifiers</code> reads the stored flag; "
    "<code>viz_core</code> also treats the literal placeholder "
    "<code>[falsifier not stated]</code> as a missing falsifier. The two "
    "readings are compared here, not merged.</p>"
))
show(_compare)

display(HTML("<h4>Which claim types the no-falsifier claims are</h4>"))
show(_all.loc[~_all["falsifier_stated"]]
     .groupby(["claim_type", "confidence"]).size()
     .reset_index(name="claims")
     .rename(columns={"claim_type": "type", "confidence": "conf"}))

display(HTML("<h4>The claims themselves</h4>"))
show(_all.loc[~_all["falsifier_stated"],
              ["local_id", "claim_type", "confidence", "workflow_stage",
               "falsifier_missing"]].rename(
    columns={"local_id": "claim", "claim_type": "type", "confidence": "conf",
             "workflow_stage": "stage", "falsifier_missing": "no_falsifier"}))
''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Gap counts are `COUNT(1)` queries against `missing_falsifiers`, "
        "`unstated_conditions`, `unstated_boundaries` and `stage2_warning`; "
        "the decision profile against `extraction_decision` and "
        "`open_questions`; stage names against `workflow_stage`. Claim-level "
        "counts come from `viz.fetch_all_claims`. Every number is computed at "
        "run time, so a re-import changes the page."
    ),
)


WAVE2_SPECS = [
    ECOSYSTEM_SUPPORT,
    OFFLINE_FAILURE,
    HOME_AI_BENCHMARKS,
    ENERGY_MODEL,
    LIFECYCLE_GAPS,
    AI_HUB_LANDSCAPE,
    HOUSEHOLD_ECONOMICS,
    GAP_AUDIT,
]


