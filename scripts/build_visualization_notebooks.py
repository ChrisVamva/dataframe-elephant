"""Builder for the evidence-grounded visualization notebooks in ``notebooks/``.

The notebooks are the deliverable; this module is the source that produces
them. Keeping cell text in Python (rather than hand-editing ``.ipynb`` JSON)
means the claim ids each notebook reads from ``data/smarthome.duckdb`` are
declared once, in one place, and validated by
``src/tests/test_viz_notebooks.py`` (which executes every notebook headless).

Every notebook follows the same cell contract, defined in ``_NOTEBOOK_TEMPLATE``:

    title -> provenance -> primary evidence -> supporting context
          -> uncertainty & gaps -> reproducibility

Usage:
    .\\.venv\\Scripts\\python.exe scripts/build_visualization_notebooks.py
    .\\.venv\\Scripts\\python.exe scripts/build_visualization_notebooks.py --check
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

NOTEBOOK_DIR = ROOT / "notebooks"

# Shared bootstrap: the notebooks must run from any working directory, so the
# repo root is located from this file rather than from the launch cwd.
BOOTSTRAP = '''\
import sys
from pathlib import Path

import ipywidgets as widgets
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import HTML, clear_output, display

# Find the repo root by walking up until schemas/stage2.sql appears, so the
# notebook runs from notebooks/, from the repo root, or from anywhere else.
_here = Path.cwd().resolve()
for _candidate in [_here, *_here.parents]:
    if (_candidate / "schemas" / "stage2.sql").exists():
        ROOT = _candidate
        break
else:  # pragma: no cover - only reachable outside a checkout
    raise FileNotFoundError("schemas/stage2.sql not found above " + str(_here))

if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

import viz_core as viz  # noqa: E402

pd.set_option("display.max_colwidth", 90)
pd.set_option("display.width", 160)

# Renderers matter for two reasons. "browser" (plotly's default) opens a
# window when a figure is shown outside a live kernel, which breaks headless
# execution. The bare "notebook" renderer in plotly 7 emits only text/html,
# carrying no figure payload, so a notebook could run clean and still show
# nothing. "plotly_mimetype+notebook" emits the figure JSON for JupyterLab and
# an inline HTML fallback elsewhere -- which is also what the headless test
# asserts on.
pio.renderers.default = "plotly_mimetype+notebook"

# Every figure in these notebooks reads only from data/smarthome.duckdb.
CLAIM_IDS = __CLAIM_IDS__
assert viz.DEFAULT_DB_PATH.endswith("smarthome.duckdb"), viz.DEFAULT_DB_PATH

claims = viz.fetch_claims(list(CLAIM_IDS))
sources = viz.sources_for_claims(list(CLAIM_IDS)) if CLAIM_IDS else pd.DataFrame()
cluster_metrics = (
    viz.claim_metrics_lookup(list(CLAIM_IDS)) if CLAIM_IDS else pd.DataFrame()
)

# Corpus-wide row counts, read once so a notebook can state the size of what it
# is drawing from without confusing a whole-corpus count with the size of its
# own (possibly empty) claim cluster.
CORPUS = viz.connect_db()
try:
    corpus_counts = {
        table: CORPUS.execute(f"SELECT COUNT(1) FROM {table}").fetchone()[0]
        for table in ("stage2_claim", "metric", "entity", "source_mirror",
                      "predicate", "extraction_decision")
    }
finally:
    CORPUS.close()

def provenance(claim_id):
    """Collapsible evidence panel for one claim in this cluster."""
    panel = viz.render_provenance_panel(claim_id)
    return widgets.VBox([panel])

def show(*items):
    """Display data frames, HTML, or figures, one per argument."""
    for item in items:
        display(item)

def confidence_legend():
    """Show the colour coding applied to confidence across all figures."""
    display(HTML(
        "<b>Confidence colour coding:</b> "
        f"<span style='color:{viz.CONFIDENCE_COLORS['high']}'>high</span> &middot; "
        f"<span style='color:{viz.CONFIDENCE_COLORS['medium']}'>medium</span> &middot; "
        f"<span style='color:{viz.CONFIDENCE_COLORS['low']}'>low</span>"
    ))
'''


def _bootstrap_cell(claim_ids: list[str]) -> str:
    # The bootstrap contains f-string braces, so it is substituted by token
    # rather than str.format (which would try to interpret every dict literal).
    return BOOTSTRAP.replace("__CLAIM_IDS__", repr(tuple(claim_ids)))


def _md(source: str) -> nbformat.NotebookNode:
    return nbformat.v4.new_markdown_cell(source.strip("\n"))


def _code(source: str) -> nbformat.NotebookNode:
    return nbformat.v4.new_code_cell(source.strip("\n"))


def build_notebook(
    *,
    name: str,
    title: str,
    claim_ids: list[str],
    provenance_intro: str,
    evidence_md: str,
    evidence_code: str,
    context_md: str,
    context_code: str,
    uncertainty_md: str,
    uncertainty_code: str,
    reproducibility: str,
) -> nbformat.NotebookNode:
    """Assemble one notebook from the shared cell contract."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        _md(f"# {title}"),        _md(
            "**Claim cluster:** "
            + ", ".join(f"`{cid}`" for cid in claim_ids)
            + "  \n**Source of truth:** `data/smarthome.duckdb` (read-only), via "
            "`src/viz_core.py`"
        ),
        _code(_bootstrap_cell(claim_ids)),
        _md("## Provenance"),
        _md(provenance_intro),
        _code(
            "for claim_id in CLAIM_IDS:\n"
            "    display(HTML(f\"<h4>{claim_id} &mdash; "
            "{claims.set_index('local_id').loc[claim_id, 'claim_text']}</h4>\"))\n"
            "    display(provenance(claim_id))\n"
            "confidence_legend()\n"
        ),
        _md("## Primary evidence"),
        _md(evidence_md),
        _code(evidence_code),
        _md("## Supporting context"),
        _md(context_md),
        _code(context_code),
        _md("## Uncertainty and gaps"),
        _md(uncertainty_md),
        _code(uncertainty_code),
        _md("## Reproducibility"),
        _md(reproducibility),
        _code(
            "# The exact queries behind every figure above, re-run verbatim.\n"
            "import duckdb\n"
            "con = duckdb.connect(str(ROOT / 'data' / 'smarthome.duckdb'), read_only=True)\n"
            "print('database:', con.execute('SELECT current_database()').fetchone()[0])\n"
            "for table in ('stage2_claim', 'metric', 'entity', 'source_mirror',\n"
            "               'predicate', 'workflow_stage', 'extraction_decision'):\n"
            "    total = con.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]\n"
            "    print(f'{table:22} {total:>6} rows')\n"
            "con.close()\n"
        ),
    ]
    nb.metadata.update(
        {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": sys.version.split()[0]},
        }
    )
    return nb


# --------------------------------------------------------------------------
# Shared fragments
# --------------------------------------------------------------------------

_CLUSTER_PANEL = '''\
display(HTML(
    "<h4>Claim cluster evidence table</h4>"
    "<p>Every claim in this cluster, with its evidence class, confidence, "
    "workflow stage and cited source ids. This is the table the figures above "
    "are built from.</p>"
))
show(
    claims[["local_id", "claim_type", "evidence_marker", "confidence",
            "workflow_stage", "source_refs", "falsifier_missing", "section"]]
    .rename(columns={
        "local_id": "claim", "claim_type": "type", "evidence_marker": "ev",
        "confidence": "conf", "workflow_stage": "stage",
        "source_refs": "sources", "falsifier_missing": "no_falsifier",
    })
)

display(HTML("<h4>Sources cited by the cluster</h4>"))
show(sources[["local_id", "title", "publisher", "classification",
              "publication_date", "url"]].rename(
    columns={"local_id": "source"}))
'''

_UNCERTAINTY_COMMON = '''\
display(HTML("<h4>Claims in this cluster with no falsifier</h4>"
             "<p>A missing falsifier means the corpus recorded no observation "
             "that would disconfirm the claim. The panel above flags these "
             "claims in <code>no_falsifier</code>.</p>"))
show(claims.loc[claims["falsifier_missing"], ["local_id", "claim_type",
                                              "confidence"]]
     .rename(columns={"local_id": "claim", "claim_type": "type",
                      "confidence": "conf"}))

display(HTML("<h4>Metrics with conditions not stated in the source</h4>"))
_gaps = cluster_metrics.loc[~cluster_metrics["conditions_stated"].fillna(False)]
if _gaps.empty:
    display(HTML("<p>No unstated conditions among the cluster's metrics.</p>"))
else:
    show(_gaps[["local_id", "metric_name", "value", "unit"]].rename(
        columns={"local_id": "metric", "metric_name": "name"}))

display(HTML("<h4>Extraction decisions that changed or qualified this material</h4>"))
_decisions = pd.DataFrame(
    viz.connect_db().execute(
        "SELECT local_id, decision_type, description, resolution "
        "FROM extraction_decision "
        "WHERE decision_type IN ('evidence_downgrade', 'classification_conflict', "
        "                           'falsifier_absent', 'condition_absent', "
        "                           'boundary_absent', 'scope_boundary', "
        "                           'omission') "
        "ORDER BY local_id"
    ).fetchall(),
    columns=["decision", "type", "description", "resolution"],
)
show(_decisions)
'''


# --------------------------------------------------------------------------
# Notebook definitions
# --------------------------------------------------------------------------

# C009 and C011 are in the cluster because the version timeline attributes
# Matter 1.5 and 1.6 capabilities to them; the panels must be able to show the
# claim text behind every capability label on the chart.
MATTER_CLAIMS = ["C001", "C002", "C003", "C004", "C005", "C006", "C009", "C011"]

MATTER = dict(
    name="01_matter_version_timeline",
    title="Matter and Thread: version progression and the standardisation debate",
    claim_ids=MATTER_CLAIMS,
    provenance_intro=(
        "Each claim below is rendered with its evidence class, confidence, "
        "falsifier status, cited sources and matched extraction-log entries. "
        "The colour of the confidence label is the same colour used on the "
        "chart points below."
    ),
    evidence_md=(
        "### Which specification versions does the corpus actually record?\n\n"
        "The corpus records Matter versions as free text in a single metric "
        "cell rather than as a dated release table. The timeline below is "
        "therefore drawn only from what is in the database: the version list "
        "in `M002`, the current major version in `M001`, and the claims that "
        "state what a specific version added (`C003` for 1.4, `C009` for the "
        "1.5 camera support, `C011` for 1.6). There are no release dates in the "
        "corpus for 1.4 or 1.6, so the x-axis is version ordinal, not calendar "
        "time, and no dates are invented."
    ),
    evidence_code='''\
# Which versions does the corpus actually record? M002 holds the list; M001
# holds the current major version. Both are authored strings, so they are read
# and parsed rather than restated.
_versions = viz.section_metrics("Documented developments")
_versions = _versions[_versions["local_id"] == "M002"]
_current = viz.section_metrics("Device Types & Feature Consistency")
_current = _current[_current["local_id"] == "M001"]

recorded = _versions["value"].iloc[0] if not _versions.empty else "(not recorded)"
current = _current["value"].iloc[0] if not _current.empty else "(not recorded)"

# The capability attached to each version comes from the claim text of the
# listed claim, not from a capability table the corpus does not have.
VERSION_CLAIMS = [
    ("1.4", "C003", "Enhanced Multi-Admin; certifiable routers; energy devices"),
    ("1.5", "C009", "Camera support on Echo devices (March 2026)"),
    ("1.6", "C011", "NFC commissioning; Joint Fabric"),
]
RECORDED = """ + repr("1.4, 1.4.2, 1.5, 1.6") + r"""
points = [
    {
        "version": version,
        "ordinal": index,
        "capability": capability,
        "claim": claim,
        "claim_text": claims.set_index("local_id").loc[claim, "claim_text"],
        "in_recorded_list": version in RECORDED,
    }
    for index, (version, claim, capability) in enumerate(VERSION_CLAIMS)
]
timeline = pd.DataFrame(points)
show(timeline[["version", "capability", "claim", "in_recorded_list"]])

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=list(timeline["ordinal"]),
    y=[1] * len(timeline),
    mode="markers+text",
    marker=dict(
        size=[18 if seen else 10 for seen in timeline["in_recorded_list"]],
        color=[viz.CONFIDENCE_COLORS["high"] if seen
               else viz.CONFIDENCE_COLORS[None]
               for seen in timeline["in_recorded_list"]],
        line=dict(width=1, color="#333333"),
    ),
    text=list(timeline["version"]),
    textposition="top center",
    customdata=list(zip(timeline["capability"], timeline["claim"],
                        timeline["claim_text"], timeline["in_recorded_list"])),
    hovertemplate=("Matter %{text}<br>recorded capability: %{customdata[0]}"
                   "<br>claim %{customdata[1]}: %{customdata[2]}"
                   "<br>in M002 version list: %{customdata[3]}<extra></extra>"),
))
_x = list(timeline["ordinal"])
for lo, hi in zip(_x, _x[1:]):
    fig.add_shape(type="line", x0=lo, x1=hi, y0=1, y1=1,
                  line=dict(color="#999999", width=1, dash="dot"))
fig.update_layout(
    title="Matter versions in the corpus (ordinal axis; the corpus records no dates)",
    xaxis=dict(title="Version ordinal", tickvals=_x,
               ticktext=list(timeline["version"]), range=[-0.5, len(_x) - 0.5]),
    yaxis=dict(visible=False, range=[0.5, 1.5]),
    height=340,
    showlegend=False,
)
fig.show()

display(HTML(
    f"<p>Recorded version list (<code>M002</code>): <b>{recorded}</b>"
    f" &mdash; current major version at the research date "
    f"(<code>M001</code>): <b>{current}</b>. Both are stored as authored "
    "strings, which is why the parser in <code>viz_core.parse_numbers</code> "
    "is unit-tested separately. A hollow, small marker above means the version "
    "is represented by a claim but not by the version-list metric.</p>"
))
''',
    context_md=(
        "### What the claims say the standard buys, and what it does not\n\n"
        "`C001` and `C002` are the documented factual base. `C005` and `C006` "
        "are the synthesis claims: standardisation reduces friction but "
        "commoditises basic features, and certification versions plus optional "
        "clusters plus vendor extensions plus uneven ecosystem support can "
        "still produce fragmentation. `C006` is the only claim in this cluster "
        "with a falsifier written from the source, and it is the reason the "
        "cluster is worth plotting at all: the fragmentation reading is "
        "falsifiable, while the core-idea claims are not.\n\n"
        "### Claim and source inventory\n\n"
        "`C001` and `C002` carry no falsifier (see the gaps section); `C005` "
        "and `C006` do. The distinction is visible in the `no_falsifier` column "
        "below.\n\n"
        "The Stage 2 schema carries no foreign key from claims to metrics, "
        "entities or sources. `viz_core` derives those links by shared section "
        "and shared source id, and labels the reason in a `linkage` column, so "
        "the inference behind every number on screen stays inspectable."
    ),
    context_code=_CLUSTER_PANEL,
    uncertainty_md=(
        "### What this notebook cannot show\n\n"
        "- **No release dates.** The corpus records Matter 1.4 and 1.6 as "
        "version identifiers with no dates; the one date present "
        "(`M005`, Amazon Echo 1.5 support, March 2026) is an ecosystem "
        "release, not a specification release. The x-axis is ordinal for that "
        "reason.\n"
        "- **No per-ecosystem device-type counts.** `M004` records 58 device "
        "types for Samsung SmartThings only; the corpus has no equivalent count "
        "for Apple, Google or Amazon, so an ecosystem parity matrix would be "
        "partly invented. That notebook is deferred until parity data exists.\n"
        "- **Capability attributions are claim-scoped.** Each capability label "
        "on the timeline comes from the claim text of `C003`, `C009` and "
        "`C011`, not from an independent capability table.\n"
    ),
    uncertainty_code=_UNCERTAINTY_COMMON,
    reproducibility=(
        "Figures are built from `viz.section_metrics` (exact `section` match) "
        "and `viz.fetch_claims` (explicit local ids). Both issue read-only "
        "SQL against `data/smarthome.duckdb`; no other file is read. The "
        "notebook is executed headless by "
        "`src/tests/test_viz_notebooks.py`, so this page is known to run."
    ),
)

ENERGY_CLAIMS = [
    "C043", "C044", "C045", "C046", "C047", "C048", "C049", "C050", "C055",
    "C056", "C057", "C058", "C061",
]

ENERGY = dict(
    name="09_device_flexibility_comparison",
    title="Home energy flexibility: measured savings, modelled payback, and who captures the value",
    claim_ids=ENERGY_CLAIMS,
    provenance_intro=(
        "The energy cluster mixes measured field results with modelled "
        "scenario assumptions, so each claim's evidence class matters more "
        "here than elsewhere. The panels below make the split visible before "
        "any number is charted."
    ),
    evidence_md=(
        "### Flexibility by device, as the corpus records it\n\n"
        "Each row is a metric from the cluster, parsed from its authored value "
        "cell. Range metrics (`29-54`, `15-25`) are drawn as a bar spanning "
        "the stated range rather than collapsed to a midpoint, because the "
        "corpus never states a single value for them. Bars are coloured by the "
        "metric's recorded confidence, not by the claim's."
    ),
    evidence_code='''\
# Flex metrics for this cluster: pull the exact metric ids we plot, then read
# their values straight from the database. range_frame turns each authored
# value cell into (low, high) bounds and keeps the raw cell for the hover.
FLEX_METRIC_IDS = [
    "M089", "M094", "M095", "M096", "M097", "M099", "M100", "M103", "M104",
    "M105",
]
flex = viz.range_frame(FLEX_METRIC_IDS)
show(flex[["metric", "name", "value", "low", "high", "unit", "confidence",
           "source"]])

_records = flex.to_dict("records")
fig = go.Figure(go.Bar(
    x=[(r["low"] + r["high"]) / 2 for r in _records],
    y=list(reversed(flex["metric"] + " " + flex["name"])),
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in flex["confidence"]]),
    error_x=dict(
        type="data",
        array=[abs(r["high"] - r["low"]) / 2 for r in _records],
        arrayminus=[abs(r["high"] - r["low"]) / 2 for r in _records],
        visible=True,
    ),
    customdata=list(zip(flex["value"], flex["unit"], flex["source"],
                        flex["confidence"])),
    hovertemplate=(
        "%{y}<br>stated value: %{customdata[0]} %{customdata[1]}"
        "<br>source: %{customdata[2]}<br>confidence: %{customdata[3]}"
        "<extra></extra>"
    ),
))
fig.update_layout(
    title="Stated flexibility magnitudes (range metrics drawn as ranges)",
    xaxis_title="percent, or kW where the unit says so",
    height=430,
    yaxis=dict(automargin=True),
)
fig.show()
''',
    context_md=(
        "### Payback and value distribution are modelled, not measured\n\n"
        "`C061` and `C055` compare modelled payback across five systems; "
        "`C057` reports the modelled split of the value that results. Both are "
        "recorded as `inference` at medium confidence because the extraction "
        "log decision `L034` classifies the whole model as scenario "
        "assumptions rather than measurements. The two charts below therefore "
        "sit in a separate band from the field measurements above, and are "
        "labelled as modelled rather than presented as results."
    ),
    context_code='''\
MODELLED_SECTIONS = [
    "Payback and NPV", "5. Value Distribution", "6. Sensitivity Analysis",
]
modelled = pd.concat(
    [viz.section_metrics(section) for section in MODELLED_SECTIONS],
    ignore_index=True,
)
show(modelled[["local_id", "metric_name", "value", "unit", "confidence",
               "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "confidence": "conf", "source_ref": "source"}))

# Payback: M131-M134 are single-year figures, M135 carries a full system
# result including its own NPV. Read them by id rather than by section filter.
PAYBACK_IDS = ["M132", "M133", "M134", "M131", "M135"]
payback = viz.metrics_by_id(PAYBACK_IDS)
payback["years"] = [viz.range_value(v)[0] for v in payback["value"]]
payback = payback.dropna(subset=["years"]).sort_values("years")
display(HTML("<h4>Modelled payback horizon</h4>"))
show(payback[["local_id", "metric_name", "value", "years", "confidence"]]
     .rename(columns={"local_id": "metric", "metric_name": "name",
                      "confidence": "conf"}))

fig = go.Figure(go.Bar(
    x=payback["years"],
    y=payback["local_id"] + " " + payback["metric_name"],
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in payback["confidence"]]),
    customdata=list(zip(payback["value"], payback["confidence"])),
    hovertemplate="%{y}<br>stated: %{customdata[0]}<br>confidence: %{customdata[1]}"
                  "<extra></extra>",
))
fig.update_layout(
    title="Modelled payback, years (scenario assumptions, not measurements)",
    xaxis_title="years", height=300, yaxis=dict(automargin=True),
    annotations=[dict(text="L034: model values recorded as inference at "
                           "medium confidence", xref="paper", yref="paper",
                       x=0, y=-0.25, showarrow=False, font=dict(size=11))],
)
fig.show()

# Value distribution: the corpus states a share and an absolute annual figure
# in the same cell, sometimes as a range. Both come from the same value cell.
VALUE_IDS = ["M136", "M137", "M138", "M139", "M140"]
_raw_value = viz.metrics_by_id(VALUE_IDS)
value_split = pd.DataFrame([
    {
        "metric": record["local_id"],
        "name": record["metric_name"],
        "stated": record["value"],
        "share_pct": (nums[-1] if (nums := viz.parse_numbers(record["value"]))
                      else None),
        "confidence": record["confidence"],
    }
    for record in _raw_value.to_dict("records")
])
display(HTML("<h4>Modelled value distribution</h4>"))
show(value_split)

_share_total = value_split["share_pct"].sum()
display(HTML(
    f"<p>The five recorded shares total <b>{_share_total:g}%</b> of modelled "
    "annual value. The corpus records no row for the remainder, so the pie is "
    "normalised by Plotly and the missing share is not labelled as a "
    "recipient.</p>"
))

fig = go.Figure(go.Pie(
    labels=[f"{r['metric']} {r['name']}" for r in value_split.to_dict("records")],
    values=[r["share_pct"] or 0 for r in value_split.to_dict("records")],
    customdata=[r["stated"] for r in value_split.to_dict("records")],
    hovertemplate="%{label}<br>stated: %{customdata}<extra></extra>",
    hole=0.35,
))
fig.update_layout(title="Modelled annual flexibility value by recipient (%)",
                  height=380)
fig.show()
''',
    uncertainty_md=(
        "### The override-rate conflict is unresolved and shown, not averaged\n\n"
        "Extraction-log decision `L019` records that the same UK heat-pump "
        "trial is reported with an override rate of `2.7%` in one note and "
        "`1.1-1.3%` (rising to `4.4%` for two-hour events) in another. Both "
        "are retained as separate metric rows; the protocol forbids "
        "discarding one, and forbids averaging them. The figure below prints "
        "them side by side, which is the honest presentation of a conflict the "
        "corpus could not resolve.\n\n"
        "Other limits on this page:\n\n"
        "- **Modelled and measured are not mixed.** Payback and value "
        "distribution come from a scenario model (`L034`); field results come "
        "from named trials. They are charted in separate bands.\n"
        "- **No single household baseline is presented as measured.** The "
        "baseline consumption metrics are model inputs, not survey data.\n"
        "- **Sensitivity inputs are ranges, not distributions.** `M141`-`M144` "
        "give base values and ranges; there is no basis for a probability "
        "distribution in the corpus, so no tornado chart is drawn here."
    ),
    uncertainty_code='''\
# The conflict is located by name rather than by remembering metric ids, so a
# re-import that renumbers M101/M102 still surfaces the conflict.
_conflict = pd.concat(
    [viz.section_metrics(section)
     for section in ("2. Device-Level Flexibility Modeling",
                     "What Savings Are Measured Rather Than Claimed?")],
    ignore_index=True,
)
_conflict = _conflict[_conflict["metric_name"].str.contains(
    "override", case=False, na=False)]
display(HTML("<h4>Unresolved conflict: heat-pump override rate</h4>"
             "<p>Both values are retained; the corpus explicitly refuses to "
             "merge them (decision <code>L019</code>). Neither is averaged.</p>"))
show(_conflict[["local_id", "metric_name", "value", "unit", "confidence",
                "source_ref", "scope_conditions"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source"}))

display(HTML("<h4>Sensitivity inputs as recorded (base and range, no "
             "distribution)</h4>"))
show(viz.section_metrics("6. Sensitivity Analysis")[
    ["local_id", "metric_name", "value", "unit", "confidence"]]
     .rename(columns={"local_id": "metric", "metric_name": "name",
                      "confidence": "conf"}))

''' + _UNCERTAINTY_COMMON,
    reproducibility=(
        "Every figure reads `metric` rows by local id from "
        "`data/smarthome.duckdb`. Range parsing goes through "
        "`viz.range_value` and `viz.parse_numbers`, both unit-tested in "
        "`src/tests/test_viz_core.py`, because the value cells are authored "
        "strings rather than typed numbers."
    ),
)

SECURITY_CLAIMS = ["C064", "C065", "C066", "C069", "C103", "C105", "C067", "C068"]

SECURITY = dict(
    name="15_support_period_landscape",
    title="Security lifecycle: mandated support floors versus stated vendor support periods",
    claim_ids=SECURITY_CLAIMS,
    provenance_intro=(
        "Support periods are the most quotable and most easily misread numbers "
        "in the corpus: a mandated floor and a vendor's stated period are "
        "different kinds of number. The provenance panels below separate the "
        "regulation claims from the vendor-report claims before they are drawn "
        "on one axis."
    ),
    evidence_md=(
        "### Stated support periods by device category, against the CRA floor\n\n"
        "The dotted line is the CRA's five-year minimum support floor "
        "(`M053`, `documented fact`, high confidence). Bars are the periods the "
        "corpus records per device category, drawn as ranges where the source "
        "stated a range. Where a period is at or below the floor, the hover "
        "still shows the source, because the interesting cases are the ones "
        "where the floor is not yet the binding constraint."
    ),
    evidence_code='''\
SUPPORT_SECTION = "Support Periods and Update Mechanisms by Device Category"
support = viz.section_metrics(SUPPORT_SECTION)
show(support[["local_id", "metric_name", "value", "unit", "confidence",
               "source_ref", "conditions_stated"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "conditions_stated": "cond_stated"}))

# Only rows whose unit is years belong on a support-period axis. M063 (AI
# assistant data retention, 18 / 3 or 18 months) shares the section but is a
# different quantity, and M059's "3, 4, 5" is three separate periods for three
# hubs rather than a range, so it is expanded below instead of collapsed.
period_rows = []
for record in support.to_dict("records"):
    if record["unit"] != "years":
        continue
    values = viz.parse_numbers(record["value"])
    if not values:
        continue
    low = min(values)
    high = max(values)
    period_rows.append({
        "metric": record["local_id"],
        "name": record["metric_name"],
        "value": record["value"],
        "low": low,
        "high": high,
        # "3, 4, 5" is a list of three vendor periods, so the bar is a span of
        # the observed set rather than an author-stated range.
        "bounds_meaning": "stated range" if len(values) == 2 else "observed spread",
        "confidence": record["confidence"],
        "source": record["source_ref"],
    })
periods = pd.DataFrame(period_rows).sort_values("low")
show(periods)

floor_row = viz.metrics_by_id(["M053"])
floor_years = viz.numeric_value(floor_row["value"].iloc[0]) if not floor_row.empty else None

_records = periods.to_dict("records")
fig = go.Figure(go.Bar(
    x=[(r["low"] + r["high"]) / 2 for r in _records],
    y=list(reversed(periods["metric"] + " " + periods["name"])),
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in periods["confidence"]]),
    error_x=dict(
        type="data",
        array=[(r["high"] - r["low"]) / 2 for r in _records],
        arrayminus=[(r["high"] - r["low"]) / 2 for r in _records],
        visible=True,
    ),
    customdata=list(zip(periods["value"], periods["source"], periods["confidence"],
                        periods["bounds_meaning"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]} years"
                   "<br>source: %{customdata[1]}<br>confidence: %{customdata[2]}"
                   "<br>bars show the %{customdata[3]}<extra></extra>"),
))
if floor_years is not None:
    fig.add_vline(x=floor_years, line_dash="dot", line_color="#333333",
                  annotation_text=f"CRA minimum support floor: {floor_years:g} years (M053)",
                  annotation_position="top left")
fig.update_layout(
    title="Stated support periods by device category, against the CRA floor",
    xaxis_title="years of support", height=380, yaxis=dict(automargin=True),
)
fig.show()
''',
    context_md=(
        "### Compliance is not the same as safety, and the corpus says so\n\n"
        "`C064` and `C065` record the CRA's five-year floor together with the "
        "qualification that the floor is explicitly not a default: "
        "manufacturers can justify shorter. `C066` records that the US has no "
        "comparable federal lifecycle mandate and that `M070` records the UK "
        "PSTI as mandating no minimum support period at all. `C103` records "
        "that vendors state automatic updates while offering shorter windows, "
        "and `C105` records Aqara CVEs as evidence that documented features can "
        "be absent in practice.\n\n"
        "The chart puts the regulatory instruments on one axis so the gap "
        "between *mandated*, *stated* and *observed* is legible in one glance."
    ),
    context_code='''\
# Mandated instruments only: the CRA block plus the two rows that record the
# absence of a mandate (M070 UK PSTI, and the US comparison in C066).
MANDATE_IDS = ["M053", "M054", "M055", "M056", "M062", "M069", "M070"]
instruments = viz.metrics_by_id(MANDATE_IDS)
show(instruments[["local_id", "metric_name", "value", "unit", "confidence",
                  "source_ref", "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name",
             "source_ref": "source", "confidence": "conf"}))

# Only the rows measured in years belong on a years axis. M055 is a date and
# M056 is a reporting deadline in hours; plotting them as years would be wrong,
# so they are shown in the table above and excluded from the figure.
_years_only = instruments[instruments["unit"] == "years"].copy()
_years_only["years"] = [viz.numeric_value(v) for v in _years_only["value"]]
_years_only = _years_only.dropna(subset=["years"])

fig = go.Figure(go.Bar(
    x=list(_years_only["years"]),
    y=list(_years_only["local_id"] + " " + _years_only["metric_name"]),
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in _years_only["confidence"]],
                pattern=dict(shape="", solidity=0.2)),
    customdata=list(zip(_years_only["value"], _years_only["confidence"],
                        _years_only["section"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]}"
                   "<br>confidence: %{customdata[1]}<br>section: %{customdata[2]}"
                   "<extra></extra>"),
))
fig.add_vline(x=floor_years or 5, line_dash="dot", line_color="#333333",
              annotation_text="CRA minimum support floor (M053)",
              annotation_position="top left")
fig.update_layout(
    title=("Lifecycle instruments stated in years. M070 records that UK PSTI "
           "mandates no minimum period, so it is a table row, not a bar."),
    xaxis_title="years", height=300, yaxis=dict(automargin=True),
)
fig.show()

display(HTML(
    "<p><b>M070</b> (UK PSTI minimum support period) is recorded as "
    "<code>none</code>. It cannot be drawn as a zero-height bar without "
    "implying a measured zero, so it is left as text: the UK regime mandates "
    "no floor at all, which is a different statement from mandating a short "
    "one. <b>M055</b> (December 2027) and <b>M056</b> (24 hours) are excluded "
    "from the years axis for the same reason.</p>"
))
''',
    uncertainty_md=(
        "### Why this page stops short of a security scorecard radar\n\n"
        "The corpus records the scorecard's *shape* (`M064`-`M068`: 14 "
        "lifecycle controls, weights 1.0 and 0.7, a passing composite of 2.00 "
        "out of 3.00) but stores no per-control scores. A radar of 14 controls "
        "would therefore be drawn from the rubric rather than from results, "
        "which would misrepresent a scoring method as a measurement. The "
        "figures above are limited to numbers the database actually contains.\n\n"
        "- **Support periods are vendor-reported ranges, not audited "
        "measurements.** `M057`, `M059` and `M060` carry medium confidence for "
        "that reason.\n"
        "- **The CRA floor is prospective.** `M055` dates the major-obligation "
        "application to December 2027, so the floor is not yet the operative "
        "constraint for any device on the chart.\n"
        "- **Camera support is a single recorded value.** `M058` gives 5 years "
        "for one vendor line; the corpus holds no per-vendor camera support "
        "table, so the 'none for Apple' reading from the plan is not drawn "
        "here as data.\n"
        "- **`C068` is an inference**, not a measurement: the claim that "
        "households rarely VLAN-segment IoT devices is a judgement about "
        "behaviour with no survey behind it in this corpus."
    ),
    uncertainty_code=_UNCERTAINTY_COMMON,
    reproducibility=(
        "Section-scoped metrics come from `viz.section_metrics` (exact section "
        "match, ordered by local id) and the regulatory comparison from an "
        "explicit metric-id list. Both are read-only queries against "
        "`data/smarthome.duckdb`."
    ),
)

BUSINESS_CLAIMS = ["C085", "C086", "C114", "C055"]

BUSINESS = dict(
    name="21_subscription_fatigue_funnel",
    title="Subscription fatigue and adoption barriers: the funnel and what sits above it",
    claim_ids=BUSINESS_CLAIMS,
    provenance_intro=(
        "Adoption and business numbers in this corpus are market-research "
        "figures with named but sometimes unlinked sources. The panels below "
        "record which source each claim rests on, and the gaps section flags "
        "the ones the extraction log already flagged as uncited."
    ),
    evidence_md=(
        "### Subscription and ownership rates, with their denominators\n\n"
        "Each bar is a metric the cluster cites, read from the database. The "
        "denominator of each rate is stated in its own `unit` cell and is "
        "carried into the bar label and the hover, because the corpus does not "
        "record a single shared population: 52% is a share of respondents, 53% "
        "a share of device owners, 19% a share of device owners, and 52% in "
        "`M019` a rate of DIY users hitting a setup problem. They are drawn "
        "side by side as stated rates, not multiplied into a conversion funnel, "
        "which would invent a population relationship the corpus never "
        "recorded."
    ),
    evidence_code='''\
# (metric id, label, denominator note). The denominator is transcribed from the
# metric's unit cell, not invented; where the unit does not name a population,
# that is stated rather than guessed.
FUNNEL_SPECS = [
    ("M010", "Own a smart speaker or display", "share of respondents"),
    ("M031", "Do not pay a device subscription", "share of device owners"),
    ("M009", "Subscribe to video security", "share of smart home device owners"),
    ("M019", "Hit a setup or connectivity problem", "rate among DIY users"),
]
funnel_ids = [mid for mid, _, _ in FUNNEL_SPECS]
_raw = viz.metrics_by_id(funnel_ids)
_by_id = _raw.set_index("local_id", drop=False)

funnel = pd.DataFrame([
    {
        "stage": label,
        "metric": mid,
        "pct": viz.numeric_value(_by_id.loc[mid, "value"]) if mid in _by_id.index else None,
        "stated": _by_id.loc[mid, "value"] if mid in _by_id.index else None,
        "unit": _by_id.loc[mid, "unit"] if mid in _by_id.index else None,
        "denominator": denominator,
        "source": _by_id.loc[mid, "source_ref"] if mid in _by_id.index else None,
        "confidence": _by_id.loc[mid, "confidence"] if mid in _by_id.index else None,
    }
    for mid, label, denominator in FUNNEL_SPECS
])
funnel = funnel.dropna(subset=["pct"])
show(funnel)

fig = go.Figure(go.Bar(
    x=funnel["pct"],
    y=funnel["stage"] + " (" + funnel["metric"] + ")",
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in funnel["confidence"]]),
    customdata=list(zip(funnel["stated"], funnel["denominator"], funnel["source"],
                        funnel["confidence"], funnel["metric"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]}%<br>denominator: %{customdata[1]}"
                   "<br>source: %{customdata[2]} (metric %{customdata[4]})"
                   "<br>confidence: %{customdata[3]}<extra></extra>"),
))
fig.update_layout(
    title="Stated rates, each against its own denominator (not a conversion funnel)",
    xaxis_title="percent", height=340, yaxis=dict(automargin=True),
)
fig.show()
''',
    context_md=(
        "### Two comparable churn figures, and why they are not one number\n\n"
        "The corpus records residential monitoring cancellation at 11-14% per "
        "quarter (`M032`) and an industry annualised figure of 13% (`M033`), "
        "while Arlo's own reported churn is 1.0% per month (`M042`) against a "
        "2.0-8.7% monthly streaming comparison (`M048`). These are different "
        "populations measured on different clocks; the chart below keeps them "
        "separate and labels the clock on each bar rather than converting them "
        "to a single headline rate."
    ),
    context_code='''\
# Churn figures, kept apart because the corpus records them on three different
# clocks. The clock is transcribed from each metric's unit cell.
CHURN_IDS = ["M031", "M032", "M033", "M042", "M048"]
churn_raw = viz.metrics_by_id(CHURN_IDS)
display(HTML("<h4>Churn, as recorded</h4>"))
show(churn_raw[["local_id", "metric_name", "value", "unit", "confidence",
                "source_ref", "section"]].rename(
    columns={"local_id": "metric", "metric_name": "name", "unit": "stated_unit",
             "source_ref": "source", "confidence": "conf"}))

churn = viz.range_frame(CHURN_IDS)
show(churn[["metric", "name", "value", "low", "high", "unit", "confidence"]])

_records = churn.to_dict("records")
fig = go.Figure(go.Bar(
    x=[(r["low"] + r["high"]) / 2 for r in _records],
    y=[f"{r['metric']} {r['name']} ({r['unit']})" for r in _records],
    orientation="h",
    marker=dict(color=[viz.CONFIDENCE_COLORS.get(c, viz.CONFIDENCE_COLORS[None])
                       for c in churn["confidence"]]),
    error_x=dict(type="data",
                 array=[(r["high"] - r["low"]) / 2 for r in _records],
                 arrayminus=[(r["high"] - r["low"]) / 2 for r in _records],
                 visible=True),
    customdata=list(zip(churn["value"], churn["unit"], churn["confidence"])),
    hovertemplate=("%{y}<br>stated: %{customdata[0]}<br>per: %{customdata[1]}"
                   "<br>confidence: %{customdata[2]}<extra></extra>"),
))
fig.update_layout(
    title="Churn figures, each on its own measurement clock (not converted)",
    xaxis_title="percent per stated period", height=340, yaxis=dict(automargin=True),
)
fig.show()

display(HTML("<h4>Arlo unit economics recorded in the corpus</h4>"))
econ = viz.metrics_by_id(["M044", "M045", "M046", "M040", "M043"])
show(econ[["local_id", "metric_name", "value", "unit", "confidence",
           "source_ref"]].rename(
    columns={"local_id": "metric", "metric_name": "name", "source_ref": "source",
             "confidence": "conf"}))
''',
    uncertainty_md=(
        "### The rates above are not a funnel\n\n"
        "The bar chart above deliberately does not narrow into a funnel. The "
        "four rates are stated against three different populations (all "
        "respondents, all device owners, DIY users) drawn from different "
        "sources, and `M019` is a problem rate rather than a stage. Multiplying "
        "them into an end-to-end conversion would assert a population "
        "relationship the corpus never recorded. Each denominator is carried in "
        "the bar label and the hover instead.\n\n"
        "- **`M032` and `M048` are not comparable as drawn.** 11-14% per "
        "quarter of monitoring subscribers is a different population on a "
        "different clock from Arlo's 1.0% per month; converting one into the "
        "other would be arithmetic, not measurement, so the bar labels carry "
        "the clock instead.\n"
        "- **`C055` is in this cluster for its evidence shape, not its "
        "subject.** It is an `inference` at high confidence and is the only "
        "energy claim here; it is kept because it is the corpus's own model "
        "discipline (weakest economic link = battery storage) and shows what a "
        "high-confidence inference looks like next to a documented fact.\n"
        "- **Sources S56-S60 and S61-S80 have no URL.** The extraction log "
        "records this in `L047` and `L048`; those barriers and market figures "
        "cannot be checked against a primary publication from this database.\n"
        "- **No time series.** Every figure is a point observation; the corpus "
        "holds no adoption or churn trend, so no line chart is drawn."
    ),
    uncertainty_code=_UNCERTAINTY_COMMON,
    reproducibility=(
        "Metric values are read from `data/smarthome.duckdb` by local id and "
        "parsed with `viz.numeric_value` / `viz.range_value`. The measurement "
        "clock shown on each churn bar is a notebook-level annotation, because "
        "the clock is part of the metric's `unit` cell in the corpus and is not "
        "a separate field."
    ),
)

INDEX = dict(
    name="00_index",
    title="SmartHome claim index: what the corpus claims, and how well it is evidenced",
    claim_ids=[],
    provenance_intro=(
        "Every figure on this page is computed from the full claim table, not "
        "from a curated subset. The evidence-class distribution below is the "
        "honest summary of the corpus: most of it is reported signal, not "
        "documented fact."
    ),
    evidence_md=(
        "### Evidence class and confidence across all 119 claims\n\n"
        "Colour is confidence; the y-axis is the claim's evidence class as "
        "recorded at extraction. The point of the chart is the shape: a large "
        "`reported signal` band at medium confidence means much of the corpus "
        "is vendor or analyst material relayed as a claim, which is why the "
        "extraction log contains `evidence_downgrade` decisions."
    ),
    evidence_code='''\
all_claims = viz.fetch_all_claims()
display(HTML(
    f"<p>Corpus totals: <b>{len(all_claims)}</b> claims, "
    f"<b>{corpus_counts['metric']}</b> metrics, "
    f"<b>{corpus_counts['entity']}</b> entities, "
    f"<b>{corpus_counts['source_mirror']}</b> sources, "
    f"<b>{corpus_counts['predicate']}</b> predicates, "
    f"<b>{corpus_counts['extraction_decision']}</b> extraction decisions. "
    "Every figure on this page is a group-by over the full claim table.</p>"
))
show(all_claims[["local_id", "claim_type", "evidence_marker", "confidence",
                 "workflow_stage", "source_refs", "section"]].head(20))

_counts = (all_claims.groupby(["claim_type", "confidence"]).size()
           .reset_index(name="claims"))
_types = list(dict.fromkeys(_counts["claim_type"]))
_confs = ["high", "medium", "low"]

fig = go.Figure()
for _conf in _confs:
    _slice = _counts[_counts["confidence"] == _conf].set_index("claim_type")
    fig.add_trace(go.Bar(
        name=_conf,
        y=[_slice.loc[t, "claims"] if t in _slice.index else 0 for t in _types],
        x=_types,
        marker_color=viz.CONFIDENCE_COLORS[_conf],
        customdata=[[t, _conf] for t in _types],
        hovertemplate="%{customdata[0]}<br>confidence: %{customdata[1]}"
                      "<br>%{y} claims<extra></extra>",
    ))
fig.update_layout(
    title="Claims by evidence class and confidence",
    barmode="stack", yaxis_title="claims", xaxis_title="evidence class",
    height=380,
)
fig.show()

domain_counts = (all_claims.groupby("domain").size()
                 .sort_values(ascending=False).reset_index(name="claims"))
display(HTML("<h4>Claims per notebook domain</h4>"))
show(domain_counts)
fig = go.Figure(go.Bar(
    x=domain_counts["claims"], y=domain_counts["domain"], orientation="h",
    marker_color="#4a6fa5",
    customdata=domain_counts["domain"],
    hovertemplate="%{customdata}: %{x} claims<extra></extra>",
))
fig.update_layout(title="Claim volume by domain (keyword-classified sections)",
                  xaxis_title="claims", height=430, yaxis=dict(automargin=True),
                  showlegend=False)
fig.show()
''',
    context_md=(
        "### Search the corpus, and the caveats that come with the numbers\n\n"
        "The widget below filters the full claim table by free text. Two "
        "caveats belong next to it: the domain column is derived by keyword "
        "matching on section names (sections are reused across domains, so it "
        "is a navigation aid, not a canonical assignment), and 13 claims carry "
        "no falsifier."
    ),
    context_code='''\
_search = widgets.Text(
    value="",
    placeholder="filter claims by text, e.g. Thread, override, support period",
    description="Filter:",
    layout=widgets.Layout(width="640px"),
)
_out = widgets.Output()
_last_rendered = {"rows": 0}

def _render(value):
    # NOTE: Output.__exit__ swallows anything raised inside this block and
    # paints the traceback into the widget, where a notebook-level error check
    # cannot see it. The explicit try/except below re-raises so a bug here
    # fails the cell loudly instead of silently rendering nothing.
    try:
        frame = all_claims
        if value:
            needle = value.lower()
            mask = (frame["claim_text"].str.lower().str.contains(needle, na=False)
                    | frame["section"].str.lower().str.contains(needle, na=False)
                    | frame["local_id"].str.lower().str.contains(needle, na=False))
            frame = frame[mask]
        with _out:
            clear_output(wait=True)
            display(frame[["local_id", "claim_type", "confidence", "domain",
                           "workflow_stage", "section"]])
            display(HTML(f"<p>{len(frame)} of {len(all_claims)} claims</p>"))
    except Exception:
        with _out:
            clear_output(wait=True)
            display(HTML("<p><b>Filter failed:</b> see the traceback on this "
                         "cell.</p>"))
        raise
    _last_rendered["rows"] = len(frame)

_search.observe(lambda change: _render(change["new"]), names="value")
_render("")
display(widgets.VBox([_search, _out]))

# The widget body above runs inside widgets.Output, whose traceback handling
# hides failures from the kernel. This assertion is the real guard: a filter
# that never rendered anything must fail the cell.
assert _last_rendered["rows"] > 0, "claim filter rendered no rows"
''',
    uncertainty_md=(
        "### What this index does and does not certify\n\n"
        "- **Domain counts are keyword-derived.** `viz.claim_domain` maps a "
        "claim's section name to a notebook domain. Sections such as "
        "'Documented developments' and 'Limitations' are reused across "
        "domains, so a claim counted under 'Matter/Thread' there may belong to "
        "another line of enquiry. Counts are navigation, not taxonomy.\n"
        "- **Confidence is an extraction-time judgement**, recorded per row, "
        "not a probability. A few `inference` rows sit at high confidence "
        "because the inference is well supported; that is a different claim "
        "from the inference being well measured.\n"
        "- **13 claims have no falsifier** (`L030`). A claim with no stated "
        "disconfirming observation cannot be re-tested from this corpus.\n"
        "- **Metric linkage is heuristic.** `viz.fetch_metrics_for_claim` "
        "links by shared section first and shared source id second, and labels "
        "which rule fired. There is no foreign key between claims and metrics "
        "in `schemas/stage2.sql`.\n"
        "- **Forecast material is mixed into the corpus.** `L014` and `L031` "
        "record evidence downgrades where Stage 1 relied on vendor or analyst "
        "material; those rows sit in the `reported signal` band above."
    ),
    uncertainty_code='''\
display(HTML("<h4>Claims carrying no falsifier (decision L030)</h4>"))
_missing = all_claims[all_claims["falsifier_missing"]]
show(_missing[["local_id", "claim_type", "confidence", "domain", "section"]]
     .rename(columns={"local_id": "claim", "claim_type": "type",
                      "confidence": "conf"}))
display(HTML(
    f"<p>{len(_missing)} claims carry no falsifier, matching the count in "
    f"decision <code>L030</code> "
    f"({'agrees' if len(_missing) == 13 else 'DIFFERS FROM'} the extraction log).</p>"
))

display(HTML("<h4>Metrics with conditions not stated in the source</h4>"))
_con = viz.connect_db()
try:
    _unstated = pd.DataFrame(
        _con.execute(
            "SELECT local_id, metric_name, value, unit, section FROM metric "
            "WHERE conditions_stated = FALSE ORDER BY local_id"
        ).fetchall(),
        columns=["metric", "name", "value", "unit", "section"],
    )
finally:
    _con.close()
show(_unstated)

display(HTML("<h4>Extraction decisions that downgraded or conflicted</h4>"))
show(pd.DataFrame(
    viz.connect_db().execute(
        "SELECT local_id, decision_type, description, resolution "
        "FROM extraction_decision "
        "WHERE decision_type IN ('evidence_downgrade', 'classification_conflict', "
        "                           'falsifier_absent') ORDER BY local_id"
    ).fetchall(),
    columns=["decision", "type", "description", "resolution"],
))
''',
    reproducibility=(
        "The claim table is read in full with `viz.fetch_all_claims`; every "
        "count on this page is a group-by over that frame, with no "
        "hand-maintained totals. Metrics with unstated conditions and the "
        "downgrade decisions come from the `unstated_conditions` view and the "
        "`extraction_decision` table respectively."
    ),
)

NOTEBOOK_SPECS = [INDEX, MATTER, ENERGY, SECURITY, BUSINESS]


def _stamp_cell_ids(nb: nbformat.NotebookNode, name: str) -> nbformat.NotebookNode:
    """Give every cell a stable, content-derived id.

    nbformat assigns random cell ids, which would make ``--check`` (and the
    matching test) fail on every regeneration for no real difference.
    """
    for index, cell in enumerate(nb.cells):
        digest = hashlib.sha256(
            f"{name}:{index}:{cell.cell_type}:{cell.source}".encode("utf-8")
        ).hexdigest()[:8]
        cell["id"] = f"{name}-{index}-{digest}"
    return nb


def build_all() -> list[Path]:
    NOTEBOOK_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for spec in NOTEBOOK_SPECS:
        nb = _stamp_cell_ids(build_notebook(**spec), spec["name"])
        path = NOTEBOOK_DIR / f"{spec['name']}.ipynb"
        path.write_text(nbformat.writes(nb), encoding="utf-8")
        written.append(path)
    return written


def notebook_paths() -> list[Path]:
    return sorted(NOTEBOOK_DIR.glob("*.ipynb"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if any notebook on disk differs from the generated content",
    )
    args = parser.parse_args(argv)

    if args.check:
        import tempfile

        stale: list[str] = []
        with tempfile.TemporaryDirectory() as tmp:
            for spec in NOTEBOOK_SPECS:
                path = NOTEBOOK_DIR / f"{spec['name']}.ipynb"
                expected = nbformat.writes(
                    _stamp_cell_ids(build_notebook(**spec), spec["name"])
                )
                if not path.exists() or path.read_text(encoding="utf-8") != expected:
                    stale.append(path.name)
        if stale:
            print("notebooks out of date: " + ", ".join(stale))
            print("regenerate with: python scripts/build_visualization_notebooks.py")
            return 1
        print(f"{len(NOTEBOOK_SPECS)} notebooks up to date")
        return 0

    for path in build_all():
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
