"""Shared visualization-core library for the SmartHome analysis notebooks.

Every notebook in ``notebooks/`` reads directly from ``data/smarthome.duckdb``
(read-only) via the helpers in this module, guaranteeing a single source of
truth and a reproducible provenance trail.

Data-model note (important -- see AGENTS.md / .kilo/plans/1790631970347):
    The Stage 2 schema (``schemas/stage2.sql``) deliberately carries **no
    foreign key** linking ``stage2_claim`` to ``metric`` or ``entity``. Claims
    and metrics share a ``section`` and sometimes a ``source_ref``. The helpers
    below therefore derive claim -> metric / entity / source / log provenance
    with documented, conservative heuristics rather than FK joins:

      * metrics for a claim  = same ``section`` (primary) OR ``source_ref``
        tokens overlap the claim's ``source_refs``.
      * entities for a claim = same ``section`` (entities carry no source_ref).
      * sources for a claim  = ``source_refs`` tokens matched to
        ``source_mirror.local_id``.
      * predicates for entities = subject/object type word-overlap with the
        entity ``type`` (predicates carry no entity FK; best-effort).
      * extraction log for a claim = decisions whose ``stage1_source`` /
        ``description`` / ``resolution`` mention the claim's ``section`` or
        ``local_id`` (text match).

All ``fetch_*_for_claim`` helpers accept the human-readable local id used in
``research/raw/Stage 2/Extraction 2/Claims.md`` (e.g. ``"C001"``), which is the
identifier referenced throughout the notebook catalogue.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = os.environ.get(
    "SMARTHOME_DB", str(ROOT / "data" / "smarthome.duckdb")
)

CONFIDENCE_COLORS = {
    "high": "#1a7f37",
    "medium": "#b06000",
    "low": "#b32637",
    None: "#757575",
}

# The corpus stores an explicit placeholder instead of a real falsifier in
# cells that never recorded one; matching on the text catches claims whose
# falsifier_stated flag disagrees with the cell contents.
FALSIFIER_PLACEHOLDER = "[falsifier not stated]"

# Evidence / claim-type markers (plain-text, no emoji) for text and HTML use.
EVIDENCE_MARKERS = {
    "documented fact": "DOC",
    "reported signal": "SIG",
    "inference": "INF",
    "recommendation": "REC",
}

# Domain classification is section-keyword based. NOTE (AGENTS.md / plan
# 1790631970347): the plan assigns claims to domains by C-number range, and
# those ranges OVERLAP on shared sections (e.g. 'Documented developments' and
# 'Limitations' are reused across Matter, AI/Voice, Security, Energy and
# Business). Sections are therefore not domain-pure, so this classifier is a
# best-effort, explainable navigation aid for the index -- not a canonical claim
# assignment. Notebook claim clusters are enumerated explicitly per notebook.
# Order matters: the least-overlap / most specific keywords win first.
_DOMAIN_KEYWORDS: list[tuple[tuple[str, ...], str]] = [
    (("semantic scholar source block", "ieee source block", "arxiv source block",
      "appended market report", "recruiting", "5. study architecture",
      "4. survey instrument", "scoring rubric", "test case design", "test procedure",
      "sample size and allocation", "conjoint", "pricing design", "prioritized recommendations",
      "evidence gaps requiring further testing", "important interpretation warnings",
      "limitations"),
     "Meta"),
    (("the practical gap", "support periods and update mechanisms by device category",
      "where compliance does not demonstrate practical safety",
      "interoperability and lifecycle risk assessment", "priority 2", "priority 3",
      "low risk", "for standards and certification bodies", "for product teams",
      "effectiveness of segmentation, automatic updates, mfa, and secure commissioning"),
     "Security"),
    (("safe autonomy vs. required confirmation", "ambiguity, household identities, guests, "
      "children, and adversarial commands"),
     "AI/Voice"),
    (("what savings are measured rather than claimed?", "device-level flexibility modeling",
      "payback and npv", "6. sensitivity analysis", "5. value distribution",
      "who receives the value?", "1. system boundary and baseline"),
     "Energy"),
    (("1. ai hubs (local ai brains)", "which advantages survive standardization?",
      "2. home routers as smart home controllers"),
     "Emerging"),
    (("subscription fatigue", "dominant barriers", "business model comparison",
      "measurement inconsistency", "product-design implications",
      "product-design and strategy implications", "recruiting",
      "recurring-revenue models that retain without harmful lock-in"),
     "Business"),
    (("core idea", "documented developments", "trade-offs and open questions",
      "device types & feature consistency", "optional features, extensions, and certification gaps",
      "what fails when infrastructure goes offline",
      "matter/thread vs. zigbee, z-wave, and proprietary systems",
      "interoperability risk assessment", "1. interoperability vs. differentiation",
      "comparison table: observed ecosystem behavior", "closing synthesis", "failure modes",
      "scope and inventory", "1. smart homes key technology trends - index"),
     "Matter/Thread"),
]


def connect_db(read_only: bool = True) -> duckdb.DuckDBPyConnection:
    """Return a DuckDB connection to ``data/smarthome.duckdb``.

    Set env ``SMARTHOME_DB`` to override the path. Callers owning the
    connection are responsible for closing it; the ``fetch_*`` helpers manage
    their own short-lived connections.
    """
    return duckdb.connect(DEFAULT_DB_PATH, read_only=read_only)


def _source_tokens(ref_string: str | None) -> list[str]:
    """Split a ``source_refs`` / ``source_ref`` cell into individual source ids.

    Handles both claim cells (``"S10;S34;S36"``) and metric cells (``"S1;S34"``)
    as well as comma separators.
    """
    if not ref_string:
        return []
    tokens: list[str] = []
    for tok in re.split(r"[,;\s]+", str(ref_string)):
        tok = tok.strip()
        if tok:
            tokens.append(tok)
    return tokens


def _rows_to_df(rows: list[tuple], columns: list[str]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=columns)
    return pd.DataFrame(rows, columns=columns)


def _lookup_claim_row(con: duckdb.DuckDBPyConnection, claim_id: str) -> tuple | None:
    columns = ("claim_id", "local_id", "claim_text", "claim_type", "confidence",
               "falsifier", "falsifier_stated", "workflow_stage", "source_refs",
               "stage1_source", "section", "document_id")
    row = con.execute(
        "SELECT claim_id, local_id, claim_text, claim_type, confidence, falsifier, "
        "falsifier_stated, workflow_stage, source_refs, stage1_source, section, "
        "document_id FROM stage2_claim WHERE local_id = ?", (claim_id,)
    ).fetchone()
    if row is None:
        row = con.execute(
            "SELECT claim_id, local_id, claim_text, claim_type, confidence, falsifier, "
            "falsifier_stated, workflow_stage, source_refs, stage1_source, section, "
            "document_id FROM stage2_claim WHERE claim_id = ?", (claim_id,)
        ).fetchone()
    return row


def fetch_claim(claim_id: str) -> dict:
    """Fetch a single claim by local id (e.g. ``"C001"``) as a dict."""
    con = connect_db()
    try:
        row = _lookup_claim_row(con, claim_id)
        if row is None:
            raise KeyError(f"Claim not found: {claim_id}")
        columns = ("claim_id", "local_id", "claim_text", "claim_type", "confidence",
                   "falsifier", "falsifier_stated", "workflow_stage", "source_refs",
                   "stage1_source", "section", "document_id")
        return dict(zip(columns, row))
    finally:
        con.close()


def fetch_metrics_for_claim(claim_id: str) -> pd.DataFrame:
    """Supporting metrics for a claim (section match, then source overlap).

    Linkage is heuristic (no FK): same ``section`` is the primary signal;
    metrics sharing a source with the claim are secondary. A ``linkage``
    column records the reason.
    """
    claim = fetch_claim(claim_id)
    con = connect_db()
    try:
        rows = con.execute(
            "SELECT metric_id, local_id, metric_name, value, unit, scope_conditions, "
            "conditions_stated, claim_type, confidence, source_ref, section, "
            "document_id FROM metric"
        ).fetchall()
    finally:
        con.close()
    columns = ("metric_id", "local_id", "metric_name", "value", "unit",
               "scope_conditions", "conditions_stated", "claim_type", "confidence",
               "source_ref", "section", "document_id")
    df = _rows_to_df(rows, columns)
    if df.empty:
        return df
    claim_tokens = set(_source_tokens(claim["source_refs"]))
    sec_mask = df["section"] == claim["section"]

    def has_overlap(ref: str) -> bool:
        return bool(claim_tokens & set(_source_tokens(ref)))

    src_mask = df["source_ref"].apply(has_overlap)
    df = df.assign(
        linkage="section",
        linkage_reason="shared section " + repr(claim["section"] or "(none)"),
    )
    df.loc[src_mask & ~sec_mask, "linkage"] = "source"
    df.loc[src_mask & ~sec_mask, "linkage_reason"] = "shared source id"
    df = df[sec_mask | src_mask].sort_values("local_id").reset_index(drop=True)
    return df


def fetch_entities_for_claim(claim_id: str) -> pd.DataFrame:
    """Entities sharing the claim's ``section`` (entities carry no source_ref)."""
    claim = fetch_claim(claim_id)
    con = connect_db()
    try:
        rows = con.execute(
            "SELECT entity_id, local_id, canonical_name, type, boundary, "
            "boundary_stated, stage1_source, section, confidence, document_id "
            "FROM entity"
        ).fetchall()
    finally:
        con.close()
    columns = ("entity_id", "local_id", "canonical_name", "type", "boundary",
               "boundary_stated", "stage1_source", "section", "confidence",
               "document_id")
    df = _rows_to_df(rows, columns)
    if df.empty:
        return df
    mask = df["section"] == claim["section"]
    df = df[mask].sort_values("local_id").reset_index(drop=True)
    if "linkage" not in df.columns:
        df["linkage"] = "section"
    return df


def fetch_sources_for_claim(claim_id: str) -> pd.DataFrame:
    """Source mirror rows referenced by the claim's ``source_refs``."""
    claim = fetch_claim(claim_id)
    tokens = _source_tokens(claim["source_refs"])
    columns = ("source_id", "local_id", "title", "url", "publisher",
               "classification", "publication_date", "document_id")
    if not tokens:
        return _rows_to_df([], (*columns, "linkage"))
    con = connect_db()
    try:
        placeholders = ", ".join("?" for _ in tokens)
        rows = con.execute(
            f"SELECT source_id, local_id, title, url, publisher, classification, "
            f"publication_date, document_id FROM source_mirror "
            f"WHERE local_id IN ({placeholders})",
            tokens,
        ).fetchall()
    finally:
        con.close()
    df = _rows_to_df(rows, columns)
    if not df.empty:
        df["linkage"] = "source_ref"
    return df.sort_values("local_id").reset_index(drop=True)


def fetch_predicates_for_entities(entity_ids: list[str]) -> pd.DataFrame:
    """Predicates relating to the given entities.

    ``entity_ids`` may be local ids (``"E001"``) or canonical names. Predicates
    carry no entity FK, so matching is word-overlap on the entity ``type``
    against the predicate ``subject_type`` / ``object_type`` (best-effort,
    documented).
    """
    con = connect_db()
    try:
        rows = con.execute(
            "SELECT predicate_id, predicate, subject_type, object_type, direction, "
            "example, stage1_source, document_id FROM predicate"
        ).fetchall()
        ent_rows = con.execute(
            "SELECT entity_id, local_id, canonical_name, type FROM entity"
        ).fetchall()
    finally:
        con.close()
    ent_id_set = {e.lower() for e in entity_ids}
    ent_names = {row[2] for row in ent_rows
                 if row[1].lower() in ent_id_set or row[2].lower() in ent_id_set}
    ent_type_words = [{w for w in re.split(r"[\s,;()&]+", (row[3] or "").lower()) if w}
                      for row in ent_rows
                      if row[1].lower() in ent_id_set or row[2].lower() in ent_id_set]
    columns = ("predicate_id", "predicate", "subject_type", "object_type", "direction",
               "example", "stage1_source", "document_id", "linkage")
    out: list[list] = []
    for row in rows:
        p_words = {w for w in re.split(r"[\s,;()/]+",
                        f"{(row[2] or '')} {(row[3] or '')}".lower()) if w}
        example_mentions = any(name and name.lower() in (row[5] or "").lower()
                               for name in ent_names)
        type_matches = any(p_words & tw for tw in ent_type_words)
        if type_matches or example_mentions:
            out.append(list(row) + ["type_overlap" if type_matches else "example_mention"])
    return _rows_to_df(out, columns)


def fetch_extraction_log_for_claim(claim_id: str) -> pd.DataFrame:
    """Extraction-decision entries whose text references the claim's section/id.

    The schema has no claim->decision FK, so this is a conservative text match
    against ``stage1_source``, ``description`` and ``resolution``.
    """
    claim = fetch_claim(claim_id)
    con = connect_db()
    try:
        rows = con.execute(
            "SELECT decision_id, local_id, step, stage1_source, decision_type, "
            "description, resolution, document_id FROM extraction_decision"
        ).fetchall()
    finally:
        con.close()
    columns = ("decision_id", "local_id", "step", "stage1_source", "decision_type",
               "description", "resolution", "document_id")
    df = _rows_to_df(rows, columns)
    if df.empty:
        return df
    needles = [str(claim["section"]) if claim["section"] else None,
               claim["local_id"]]
    def hit(row: pd.Series) -> bool:
        blob = " ".join(filter(None, [str(row.get("stage1_source")),
                                      str(row.get("description")),
                                      str(row.get("resolution"))])).lower()
        return any(n is not None and n.lower() in blob for n in needles)
    df = df[df.apply(hit, axis=1)].sort_values("local_id").reset_index(drop=True)
    df["linkage"] = "text_match"
    return df


def fetch_all_claims() -> pd.DataFrame:
    """Full claim catalog with computed ``domain`` for the index notebook."""
    con = connect_db()
    try:
        rows = con.execute(
            "SELECT local_id, claim_text, claim_type, confidence, falsifier, "
            "falsifier_stated, workflow_stage, source_refs, section "
            "FROM stage2_claim ORDER BY local_id"
        ).fetchall()
    finally:
        con.close()
    columns = ("local_id", "claim_text", "claim_type", "confidence", "falsifier",
               "falsifier_stated", "workflow_stage", "source_refs", "section")
    df = _rows_to_df(rows, list(columns))
    df["domain"] = df["section"].apply(claim_domain)
    df["evidence_marker"] = df["claim_type"].apply(evidence_class_marker)
    df["falsifier_missing"] = [
        (not stated) or FALSIFIER_PLACEHOLDER in str(text or "").lower()
        for stated, text in zip(df["falsifier_stated"], df["falsifier"])
    ]
    return df


def claim_domain(section: str | None) -> str | None:
    """Classify a claim section into a notebook domain (keyword based)."""
    if not section:
        return None
    s = section.strip().lower()
    for keywords, domain in _DOMAIN_KEYWORDS:
        if any(kw in s for kw in keywords):
            return domain
    return "Unclassified"


def confidence_color(confidence: str | None) -> str:
    """Map a confidence level to a CSS hex color."""
    return CONFIDENCE_COLORS.get(confidence, CONFIDENCE_COLORS[None])


def evidence_class_marker(claim_type: str | None) -> str:
    """Short plain-text evidence-class marker for a claim type."""
    return EVIDENCE_MARKERS.get(claim_type, "??")


def render_provenance_panel(claim_id: str) -> "object":  # ipywidgets.HTML
    """Render an evidence-grounded, collapsible provenance panel for a claim.

    Returns an ``ipywidgets.HTML`` object; ipywidgets is imported lazily so the
    module stays importable in non-interactive/test contexts.
    """
    import ipywidgets  # lazy: only needed for interactive rendering

    claim = fetch_claim(claim_id)
    sources = fetch_sources_for_claim(claim_id)
    log = fetch_extraction_log_for_claim(claim_id)
    color = confidence_color(claim["confidence"])
    marker = evidence_class_marker(claim["claim_type"])
    conf_label = (claim["confidence"] or "unknown").capitalize()
    falsifier_text = _escape(claim["falsifier"] or FALSIFIER_PLACEHOLDER)
    falsifier_missing = (not claim["falsifier_stated"]) or (
        FALSIFIER_PLACEHOLDER in str(claim["falsifier"] or "").lower())
    if falsifier_missing:
        falsifier_text += " <span style='color:#b06000'>[falsifier not stated]</span>"

    def _li(text: str) -> str:
        return f"<li style='margin:2px 0'>{text}</li>"

    def _source_li(row) -> str:
        title = _escape(row.title)
        url = str(row.url or "").strip()
        label = (f"<a href='{_escape(url)}'>{title}</a>" if url
                 else f"{title} <span style='color:#b06000'>[no URL recorded]</span>")
        return _li(f"<b>{_escape(row.local_id)}</b> &mdash; {label} "
                   f"<i>({_escape(row.publisher) or 'n.d.'})</i>")

    source_items = "".join(_source_li(r) for r in sources.itertuples(index=False)) \
        or _li("No source ids mapped")
    log_items = "".join(
        _li(f"<b>{_escape(r.local_id)}</b> [{_escape(r.decision_type)}] &mdash; "
            f"{_escape(r.description or '')}")
        for r in log.itertuples(index=False)
    ) or _li("No extraction-log references matched")

    body = (
        f"<style> .prov-badge {{ background:#f0f0f0; border-radius:4px; "
        f"padding:2px 6px; font-size:0.85em; font-weight:600; }} "
        f".prov-conf {{ color:{color}; font-weight:600; }} </style>"
        f"<div style='font-family:monospace; font-size:0.9em'>"
        f"<b>{_escape(claim_domain(claim['section']) or 'unclassified domain')}</b>"
        f" &mdash; <i>{_escape(claim['section'] or 'no section')}</i>  "
        f"<span class='prov-badge'>{marker}</span> "
        f"<span class='prov-conf'>confidence: {conf_label}</span> "
        f"<span class='prov-badge'>{_escape(claim['workflow_stage'])}</span></div>"
        f"<p style='margin:4px 0 2px'><b>{_escape(claim['local_id'])}</b> &mdash; "
        f"{_escape(claim['claim_text'])}</p>"
        f"<p style='margin:2px 0'><b>Falsifier:</b> {falsifier_text}</p>"
        f"<ul style='margin:4px 0; padding-left:18px'><b>Sources</b>{source_items}</ul>"
        f"<ul style='margin:4px 0; padding-left:18px'><b>Extraction log</b>{log_items}</ul>"
        f"<p style='font-size:0.8em; color:#757575'>Source of truth: "
        f"data/smarthome.duckdb (read-only)</p>"
    )
    return ipywidgets.HTML(value=body)


def _escape(text: str | None) -> str:
    import html
    return html.escape(str(text or ""))


def claim_metrics_lookup(claim_ids: list[str]) -> pd.DataFrame:
    """Union of supporting metrics across several claims (cluster helper)."""
    frames = [fetch_metrics_for_claim(c) for c in claim_ids]
    frames = [f for f in frames if not f.empty]
    if not frames:
        return pd.DataFrame(columns=["metric_id", "local_id", "metric_name"])
    return pd.concat(frames, ignore_index=True).drop_duplicates("local_id")


def fetch_claims(claim_ids: list[str]) -> pd.DataFrame:
    """Fetch several claims at once, preserving the requested order.

    Notebooks present claim *clusters*, so a cluster-scoped accessor is needed
    alongside the single-claim helpers. Missing ids raise ``KeyError`` so a
    typo in a notebook's cluster list fails loudly rather than silently
    dropping a claim from the evidence panel.
    """
    columns = ("claim_id", "local_id", "claim_text", "claim_type", "confidence",
               "falsifier", "falsifier_stated", "workflow_stage", "source_refs",
               "stage1_source", "section", "document_id")
    rows = [fetch_claim(cid) for cid in claim_ids]
    df = pd.DataFrame(rows, columns=list(columns))
    df["domain"] = df["section"].apply(claim_domain)
    df["evidence_marker"] = df["claim_type"].apply(evidence_class_marker)
    df["falsifier_missing"] = [
        (not stated) or FALSIFIER_PLACEHOLDER in str(text or "").lower()
        for stated, text in zip(df["falsifier_stated"], df["falsifier"])
    ]
    return df


def section_metrics(section: str) -> pd.DataFrame:
    """All metrics recorded under an exact ``section`` (cluster helper)."""
    con = connect_db()
    try:
        rows = con.execute(
            "SELECT metric_id, local_id, metric_name, value, unit, scope_conditions, "
            "conditions_stated, claim_type, confidence, source_ref, section, "
            "document_id FROM metric WHERE section = ? ORDER BY local_id", (section,)
        ).fetchall()
    finally:
        con.close()
    columns = ("metric_id", "local_id", "metric_name", "value", "unit",
               "scope_conditions", "conditions_stated", "claim_type", "confidence",
               "source_ref", "section", "document_id")
    return _rows_to_df(rows, list(columns))


def metrics_by_id(metric_ids: list[str]) -> pd.DataFrame:
    """Fetch metrics by explicit local id, preserving the requested order.

    Notebooks that chart a named set of metrics (``M089``, ``M094``, ...)
    need id-addressed access: section matching is the wrong tool when the
    cluster spans sections, and every other option would re-introduce the
    ad-hoc SQL blocks the notebooks are trying to avoid.
    """
    columns = ["metric_id", "local_id", "metric_name", "value", "unit",
               "scope_conditions", "conditions_stated", "claim_type",
               "confidence", "source_ref", "section", "document_id"]
    if not metric_ids:
        return pd.DataFrame(columns=columns)
    con = connect_db()
    try:
        placeholders = ", ".join("?" for _ in metric_ids)
        rows = con.execute(
            f"SELECT {', '.join(columns)} FROM metric "
            f"WHERE local_id IN ({placeholders})", metric_ids
        ).fetchall()
    finally:
        con.close()
    df = _rows_to_df(rows, columns)
    order = {mid: index for index, mid in enumerate(metric_ids)}
    df = df[df["local_id"].isin(order)]
    df["_order"] = df["local_id"].map(order)
    return df.sort_values("_order").drop(columns="_order").reset_index(drop=True)


def range_frame(metric_ids: list[str], *, name_col: str = "metric_name") -> pd.DataFrame:
    """Metrics as ``(low, high)`` numeric bounds, ready to plot.

    Value cells are authored strings ("3-5", "760 (45%)"), so the bounds come
    from :func:`range_value` and the raw cell is preserved in ``value`` for
    the hover text. Metrics with no parsable number are dropped, and the
    caller can detect that by comparing lengths.
    """
    df = metrics_by_id(metric_ids)
    rows: list[dict] = []
    for record in df.to_dict("records"):
        low, high = range_value(record["value"])
        if low is None:
            continue
        rows.append({
            "metric": record["local_id"],
            "name": record[name_col],
            "value": record["value"],
            "low": low,
            "high": high,
            "unit": record["unit"],
            "confidence": record["confidence"],
            "source": record["source_ref"],
            "conditions_stated": record["conditions_stated"],
            "scope_conditions": record["scope_conditions"],
        })
    return pd.DataFrame(rows)


def sources_for_claims(claim_ids: list[str]) -> pd.DataFrame:
    """Union of the source mirror rows cited by a claim cluster."""
    frames = [fetch_sources_for_claim(cid) for cid in claim_ids]
    frames = [f for f in frames if not f.empty]
    if not frames:
        return pd.DataFrame(columns=["source_id", "local_id", "title", "url",
                                     "publisher", "classification",
                                     "publication_date", "document_id", "linkage"])
    return pd.concat(frames, ignore_index=True).drop_duplicates("local_id")


# A thousands separator is a comma between a digit and exactly three digits.
# "3,750" is one number; "3, 4, 5" is a list of three; "1.4, 1.4.2" is a list of
# version strings. Matching the digit-group shape keeps all three distinct.
_THOUSANDS_RE = re.compile(r"(?<=\d),(?=\d{3}(?!\d))")

# A leading minus is a sign only when it starts a token (string start, space, or
# punctuation). "CTA-2045" is a model number, not a negative number, so the
# lookbehind rejects a sign that follows a letter, digit, dot or underscore.
_NUM_RE = re.compile(r"(?<![A-Za-z0-9_.])-?\d+(?:\.\d+)?")

# A range needs the same guard on its left group, so "2045 200-400" cannot pair
# a trailing digit of one identifier with the dash of a real range.
_RANGE_RE = re.compile(
    r"(?<![A-Za-z0-9_.])(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)(?![\d.])"
)


def parse_numbers(value: str | None) -> list[float]:
    """Every number appearing in a metric value cell, in order.

    Metric values in this corpus are stored as authored strings ("3-5",
    "1.4, 1.4.2, 1.5, 1.6", "760 (45%)", "3,750 USD"). Notebooks need the
    numbers to draw axes, so this pulls them out without pretending the cell is
    machine data.

    Two distinctions the corpus forces:

    * thousands separators are stripped before scanning, so "3,750" is one
      number while "3, 4, 5" stays a list of three;
    * a hyphen between two numbers is a range ("3-5" -> 3.0 then 5.0), but a
      hyphen that follows a letter is part of an identifier, so "CTA-2045"
      yields 2045.0 and never a negative.
    """
    if value is None:
        return []
    text = _THOUSANDS_RE.sub("", str(value))
    numbers: list[float] = []
    cursor = 0
    for match in _RANGE_RE.finditer(text):
        numbers.extend(float(n) for n in _NUM_RE.findall(text[cursor:match.start()]))
        numbers.extend([float(match.group(1)), float(match.group(2))])
        cursor = match.end()
    numbers.extend(float(n) for n in _NUM_RE.findall(text[cursor:]))
    return numbers


def numeric_value(value: str | None) -> float | None:
    """First number in a metric value cell, or ``None`` when there is none."""
    nums = parse_numbers(value)
    return nums[0] if nums else None


def range_value(value: str | None) -> tuple[float | None, float | None]:
    """``(low, high)`` when the cell states one range, ``(v, v)`` for one number.

    Returns ``(None, None)`` for anything it cannot honestly call a range. That
    includes a single number (not a range) *and* a list of unrelated numbers:
    "48 TB; 26 TOPS" and "760 (45%)" are two quantities, not a span, and
    pairing them as endpoints would invent a low above the high. Callers that
    genuinely want a set of numbers should use :func:`parse_numbers` and decide
    for themselves, as the support-period notebook does for "3, 4, 5".
    """
    text = _THOUSANDS_RE.sub("", str(value or ""))
    ranges = list(_RANGE_RE.finditer(text))
    if ranges:
        # Exactly one range, and no other number anywhere in the cell.
        if len(ranges) > 1:
            return (None, None)
        match = ranges[0]
        outside = text[:match.start()] + text[match.end():]
        if _NUM_RE.search(outside):
            return (None, None)
        return (float(match.group(1)), float(match.group(2)))
    numbers = _NUM_RE.findall(text)
    if len(numbers) == 1:
        return (float(numbers[0]), float(numbers[0]))
    return (None, None)
