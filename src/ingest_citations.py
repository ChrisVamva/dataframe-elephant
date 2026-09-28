"""Build the local citation intelligence database from research Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import duckdb


PARSER_VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[1]
URL_PATTERN = re.compile(
    r"(?:https?://|www\.)[^\s<>\[\]|,;]+|"
    r"(?<![@\w])(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?:/[^\s<>\[\]|,;]*)?",
    re.IGNORECASE,
)
TRACKING_PARAMETERS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
CLAIM_TYPES = {
    "documented fact": "documented fact",
    "reported signal": "reported signal",
    "inference": "inference",
    "recommendation": "recommendation",
}


@dataclass(frozen=True)
class MarkdownTable:
    headers: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    header_line: int
    row_lines: tuple[int, ...]
    heading: str


def stable_id(kind: str, value: str) -> str:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return f"{kind}_{digest[:24]}"


def normalize_url(raw_url: str) -> str | None:
    value = raw_url.strip().strip("<>").rstrip(".,;:)]}")
    if not value:
        return None
    if value.lower().startswith("www."):
        value = f"https://{value}"
    elif not re.match(r"^https?://", value, re.IGNORECASE):
        value = f"https://{value}"

    try:
        parts = urlsplit(value)
    except ValueError:
        return None
    host = (parts.hostname or "").lower()
    if not host or "." not in host:
        return None
    if host.startswith("www."):
        host = host[4:]
    try:
        port = parts.port
    except ValueError:
        return None
    netloc = host if port is None or port == 443 else f"{host}:{port}"
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if path != "/":
        path = path.rstrip("/")
    query = [
        (key, item)
        for key, item in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_PARAMETERS
    ]
    query.sort()
    return urlunsplit(("https", netloc, path, urlencode(query), ""))


def _url_candidates(raw_text: str) -> list[str]:
    candidates: list[str] = []
    for match in URL_PATTERN.finditer(raw_text):
        normalized = normalize_url(match.group(0))
        if normalized and normalized not in candidates:
            candidates.append(normalized)
    return candidates


def _is_direct_url(url: str) -> bool:
    return urlsplit(url).path not in ("", "/")


def _source_identity(title: str, canonical_url: str) -> str:
    if _is_direct_url(canonical_url):
        return f"url:{canonical_url}"
    return f"publisher:{canonical_url}|title:{_normalized_text(title)}"


def _normalized_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def _split_markdown_row(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    cells: list[str] = []
    cell: list[str] = []
    escaped = False
    for character in value:
        if character == "|" and not escaped:
            cells.append("".join(cell).strip().replace("\\|", "|"))
            cell = []
        else:
            cell.append(character)
        escaped = character == "\\" and not escaped
        if character != "\\":
            escaped = False
    cells.append("".join(cell).strip().replace("\\|", "|"))
    return cells


def _is_separator(line: str) -> bool:
    cells = _split_markdown_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def parse_markdown_tables(markdown: str) -> list[MarkdownTable]:
    lines = markdown.splitlines()
    headings: list[tuple[int, str]] = []
    for line_number, line in enumerate(lines):
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading:
            headings.append((line_number, heading.group(1).strip()))

    tables: list[MarkdownTable] = []
    index = 0
    while index + 1 < len(lines):
        if "|" not in lines[index] or not _is_separator(lines[index + 1]):
            index += 1
            continue
        headers = _split_markdown_row(lines[index])
        row_values: list[tuple[str, ...]] = []
        row_lines: list[int] = []
        end = index + 2
        while end < len(lines) and "|" in lines[end] and lines[end].strip():
            cells = _split_markdown_row(lines[end])
            if len(cells) == len(headers):
                row_values.append(tuple(cells))
                row_lines.append(end + 1)
            end += 1
        heading_text = next(
            (text for line_number, text in reversed(headings) if line_number < index),
            "",
        )
        tables.append(
            MarkdownTable(
                headers=tuple(headers),
                rows=tuple(row_values),
                header_line=index + 1,
                row_lines=tuple(row_lines),
                heading=heading_text,
            )
        )
        index = end
    return tables


def classify_evidence(raw_classification: str) -> str | None:
    value = raw_classification.strip().casefold()
    if re.search(r"\binternal\b", value):
        return "internal"
    match = re.match(r"^(primary|secondary)\b", value)
    return match.group(1) if match else None


def _parse_date(value: str) -> date | None:
    value = value.strip()
    if not value:
        return None
    iso_match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", value)
    if iso_match:
        try:
            return date.fromisoformat(iso_match.group(1))
        except ValueError:
            return None
    for pattern in ("%B %d, %Y", "%b %d, %Y", "%B %Y", "%b %Y"):
        match = re.search(r"[A-Za-z]+ \d{1,2},? \d{4}|[A-Za-z]+ \d{4}", value)
        if not match:
            break
        try:
            return datetime.strptime(match.group(0).replace(",", ""), pattern.replace(",", "")).date()
        except ValueError:
            continue
    return None


def _header_index(headers: tuple[str, ...], predicate: Any) -> int | None:
    return next((index for index, value in enumerate(headers) if predicate(value)), None)


def _header_name(value: str) -> str:
    return re.sub(r"[`*_]", "", value).strip().casefold()


def _source_columns(table: MarkdownTable) -> dict[str, int | None]:
    headers = tuple(_header_name(header) for header in table.headers)
    title_index = _header_index(
        headers,
        lambda value: value in {"citation", "source", "reference", "source title", "reference title"}
        or re.match(r"^(?:source|citation|reference)\s*[(:-]", value) is not None,
    )
    publisher_index = _header_index(headers, lambda value: "publisher" in value or value == "author")
    if publisher_index == title_index:
        publisher_index = None
    date_index = _header_index(
        headers,
        lambda value: value in {"publication date", "published", "date", "publisher / date"},
    )
    if date_index == title_index:
        date_index = None
    return {
        "title": title_index,
        "label": _header_index(
            headers,
            lambda value: value in {"#", "id", "source id", "citation id", "reference id", "ref"},
        ),
        "url": _header_index(headers, lambda value: "url" in value or value in {"website", "link"}),
        "publisher": publisher_index,
        "classification": _header_index(
            headers,
            lambda value: "classification" in value or "evidence class" in value,
        ),
        "date": date_index,
    }


def _is_source_table(table: MarkdownTable) -> bool:
    columns = _source_columns(table)
    return columns["title"] is not None and any(
        columns[name] is not None for name in ("url", "publisher", "classification")
    )


def _column(row: tuple[str, ...], index: int | None) -> str:
    return row[index].strip() if index is not None and index < len(row) else ""


def _document_metadata(path: Path, relative_path: str, markdown: str) -> dict[str, Any]:
    frontmatter = ""
    frontmatter_match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", markdown, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
    title_match = re.search(r"(?m)^title:\s*[\"']?(.+?)[\"']?\s*$", frontmatter)
    if not title_match:
        title_match = re.search(r"(?m)^#\s+(.+?)\s*$", markdown)
    title = title_match.group(1).strip() if title_match else path.stem
    lower_path = relative_path.casefold()
    if path.name.casefold() == "first-ratings.md":
        document_type = "internal_evaluation"
    elif path.name.casefold() == "citation.md":
        document_type = "citation_registry"
    elif path.name.casefold() == "report.md" and "citations/" in lower_path:
        document_type = "source_quality_report"
    elif "structured research" in title.casefold() or "research brief" in title.casefold():
        document_type = "research_brief"
    else:
        document_type = "research_note"

    evaluation_date = _parse_date(
        _metadata_value(frontmatter + "\n" + markdown, ("evaluation date", "evaluated"))
    )
    evaluation_decision = _metadata_value(markdown, ("decision", "outcome")) or None
    if evaluation_decision is not None:
        evaluation_decision = evaluation_decision.strip().rstrip(".!")
        evaluation_decision = evaluation_decision.strip().casefold()
        if evaluation_decision not in {"accept", "accept with limitations", "revise", "reject"}:
            evaluation_decision = None
    quality_rating = _metadata_value(markdown, ("quality rating", "overall rating")) or None
    return {
        "title": title,
        "document_type": document_type,
        "evaluation_date": evaluation_date,
        "evaluation_decision": evaluation_decision,
        "quality_rating": quality_rating,
        "is_internal": document_type == "internal_evaluation",
    }


def _metadata_value(text: str, keys: tuple[str, ...]) -> str:
    keys_pattern = "|".join(re.escape(key) for key in keys)
    normalized = text.replace("**", "").replace("__", "")
    match = re.search(rf"(?im)^\s*(?:[-*]\s*)?(?:{keys_pattern})\s*:\s*(.+?)\s*$", normalized)
    if not match:
        return ""
    return match.group(1).strip(" `*_\"'\n\r").strip(".!,;:?")


EVIDENCE_TIERS = frozenset({
    "tier_1_primary",
    "tier_2_secondary",
    "tier_3_tertiary",
    "unclassified",
})


def _classify_evidence_tier(recorded_classification: str | None) -> str:
    """Return an evidence tier label for a citation occurrence.

    Performs a case-insensitive substring match against ``recorded_classification``.
    The return value is always a member of ``EVIDENCE_TIERS``.
    """
    if not recorded_classification:
        return "unclassified"
    value = recorded_classification.casefold()
    if "primary" in value:
        return "tier_1_primary"
    if "secondary" in value:
        return "tier_2_secondary"
    if "internal" in value:
        return "tier_3_tertiary"
    return "unclassified"


def _classify_source_type(title: str, url: str | None) -> str:
    value = (title + " " + (url or "")).casefold()
    host = urlsplit(url).hostname if url else ""
    if any(token in value for token in ("job posting", "job board", "career")):
        return "job_posting"
    if host and (host.endswith(".gov") or host.endswith(".gov.uk")):
        return "government"
    if host and ("w3.org" in host or "nist.gov" in host):
        return "standard"
    if host and any(token in host for token in ("doi.org", "acm.org", "springer.com", "arxiv.org")):
        return "academic"
    if "/docs" in value or "documentation" in value:
        return "documentation"
    if any(token in value for token in ("blog", "newsletter", "medium.com")):
        return "blog"
    return "web_source"


DOMAIN_CATEGORIES = frozenset({
    "compliance_regulation",
    "ai_ml_technology",
    "workflow_process",
    "market_research",
    "technical_standard",
    "academic_research",
    "organizational",
    "uncategorised",
})

# Keyword rules applied to each field in turn; first matching rule wins.
# Each entry is (token_or_tokens, category). A string is a single token;
# a tuple means *any* of the tokens triggers the category.
_DOMAIN_KEYWORD_RULES: tuple[tuple[str | tuple[str, ...], str], ...] = (
    # Checked against the hostname only
    # (host rules are handled separately in _classify_domain; listed here for documentation)
    # Checked against the full lowercased field value
    (("gdpr", "accessibility", "wcag", "legal", "regulation", "compliance"), "compliance_regulation"),
    (("llm", "machine learning", "artificial intelligence", "nlp"), "ai_ml_technology"),
    (("procurement", "onboarding", "workflow", "operations", "process"), "workflow_process"),
    (("market research", "industry report", "analyst", "gartner", "forrester"), "market_research"),
    (("job posting", "job board", "career"), "organizational"),
)


def _classify_domain(
    canonical_url: str | None,
    title: str,
    publisher: str | None,
) -> str:
    """Return a domain_category from DOMAIN_CATEGORIES for the given source fields.

    Field precedence: canonical_url → publisher → title.
    First-matching rule wins within each field.
    """

    def _category_for_value(value: str, host: str) -> str | None:
        # Host-level rules (applied first within this field)
        if host in ("w3.org", "nist.gov", "iso.org") or any(
            host.endswith(f".{apex}") for apex in ("w3.org", "nist.gov", "iso.org")
        ):
            return "technical_standard"
        if host in ("doi.org", "arxiv.org", "acm.org", "springer.com") or any(
            host.endswith(f".{apex}") for apex in ("doi.org", "arxiv.org", "acm.org", "springer.com")
        ):
            return "academic_research"
        if host and (host.endswith(".gov") or host.endswith(".gov.uk")):
            return "compliance_regulation"
        if host == "linkedin.com" or host.endswith(".linkedin.com"):
            return "organizational"
        # Keyword rules applied to the lowercased field value.
        # URL paths use hyphens/underscores as word separators; normalise them to spaces
        # so that "machine-learning" matches the "machine learning" keyword.
        lower = re.sub(r"[-_]", " ", value)
        for tokens, category in _DOMAIN_KEYWORD_RULES:
            token_list = (tokens,) if isinstance(tokens, str) else tokens
            for token in token_list:
                if token == "ai":
                    # Only match " ai " as a standalone word to avoid spurious hits
                    if " ai " in f" {lower} " or lower.startswith("ai "):
                        return category
                elif token == "ml":
                    if " ml " in f" {lower} " or lower.startswith("ml "):
                        return category
                elif token in lower:
                    return category
        return None

    # Evaluate each field in precedence order
    for raw_field in (canonical_url, publisher, title):
        if not raw_field:
            continue
        lower_field = raw_field.casefold()
        parsed = urlsplit(raw_field) if raw_field.startswith(("http://", "https://")) else None
        host = (parsed.hostname or "").casefold() if parsed else ""
        result = _category_for_value(lower_field, host)
        if result is not None:
            return result

    return "uncategorised"


def _make_warning(
    run_id: str,
    input_path: str,
    warning_type: str,
    message: str,
    raw_value: str = "",
) -> dict[str, str]:
    warning_id = stable_id(
        "warn",
        "\0".join((run_id, input_path, warning_type, message, raw_value)),
    )
    return {
        "warning_id": warning_id,
        "run_id": run_id,
        "input_path": input_path,
        "warning_type": warning_type,
        "message": message,
        "raw_value": raw_value,
    }


def _date_from_access_text(markdown: str) -> date | None:
    value = _metadata_value(markdown, ("accessed", "access date", "sources access date"))
    return _parse_date(value)


def _source_row_data(
    table: MarkdownTable,
    row: tuple[str, ...],
    row_index: int,
    document_id: str,
    relative_path: str,
    run_id: str,
    access_date: date | None,
    warnings: list[dict[str, str]],
) -> tuple[dict[str, Any] | None, dict[str, Any], dict[str, Any]]:
    columns = _source_columns(table)
    raw_title = _column(row, columns["title"])
    title = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1", raw_title).strip()
    publisher_from_title = None
    quoted_title = re.match(r'^["“](.+?)["”]\s*,\s*(.+)$', title)
    if quoted_title:
        title = quoted_title.group(1).strip()
        publisher_from_title = quoted_title.group(2).strip()
    raw_url = _column(row, columns["url"])
    publisher = _column(row, columns["publisher"]) or publisher_from_title
    classification = _column(row, columns["classification"])
    label = _column(row, columns["label"]) or None
    raw_row = " | ".join(row)
    locator = f"{table.heading or 'table'} :: line {row_index}"
    candidates = _url_candidates(f"{raw_url} {raw_title}")
    source: dict[str, Any] | None = None
    source_id: str | None = None
    resolution_status = "unresolved"

    if not title:
        warnings.append(
            _make_warning(run_id, relative_path, "missing_title", f"Source row at {locator} has no title.", raw_row)
        )
    elif len(candidates) > 1:
        resolution_status = "ambiguous"
        warnings.append(
            _make_warning(
                run_id,
                relative_path,
                "duplicate_candidate",
                f"Source row at {locator} groups multiple URL candidates; no source was assigned.",
                raw_url,
            )
        )
    elif len(candidates) == 1:
        canonical_url = candidates[0]
        source_id = stable_id("src", _source_identity(title, canonical_url))
        resolution_status = "resolved"
        source = {
            "source_id": source_id,
            "canonical_url": canonical_url,
            "title": title,
            "publisher": publisher,
            "author": None,
            "source_type": _classify_source_type(title, canonical_url),
            "evidence_class": classify_evidence(classification),
            "directness": None,
            "publication_date": _parse_date(_column(row, columns["date"]) or raw_title),
            "access_date": access_date,
            "status": None,
            "bias_notes": None,
            "metadata_notes": (
                "Publisher-level URL only; source identity keyed by title and host."
                if not _is_direct_url(canonical_url)
                else None
            ),
            "domain_category": _classify_domain(canonical_url, title, publisher),
        }
        if not _is_direct_url(canonical_url):
            warnings.append(
                _make_warning(
                    run_id,
                    relative_path,
                    "source_rows_lacking_direct_urls",
                    f"Source row at {locator} identifies a publisher domain, not a page URL.",
                    raw_url,
                )
            )
    else:
        if re.search(r"\b(truncated|incomplete|cut off)\b", raw_url, re.IGNORECASE):
            warnings.append(
                _make_warning(
                    run_id,
                    relative_path,
                    "truncated_url",
                    f"Source row at {locator} contains a truncated or incomplete URL.",
                    raw_url,
                )
            )
        else:
            warnings.append(
                _make_warning(
                    run_id,
                    relative_path,
                    "source_rows_lacking_direct_urls",
                    f"Source row at {locator} has no resolvable URL.",
                    raw_url or title,
                )
            )

    if classification and classify_evidence(classification) is None:
        warnings.append(
            _make_warning(
                run_id,
                relative_path,
                "weak_source_classification",
                f"Source row at {locator} has an unmapped classification.",
                classification,
            )
        )

    if source_id is None and label:
        warnings.append(
            _make_warning(
                run_id,
                relative_path,
                "unresolved_alias",
                f"Local label {label!r} at {locator} has no unambiguous source mapping.",
                label,
            )
        )
    occurrence_id = stable_id("occ", f"{document_id}\0{row_index}\0{raw_row}")
    occurrence = {
        "occurrence_id": occurrence_id,
        "local_label": label,
        "raw_citation_text": raw_row,
        "source_id": source_id,
        "document_id": document_id,
        "locator": locator,
        "recorded_classification": classification or None,
        "extraction_method": "markdown_source_table",
        "resolution_status": resolution_status,
        "evidence_tier": _classify_evidence_tier(classification),
    }
    alias_value = label or title
    alias = {
        "alias_id": stable_id("alias", f"{document_id}\0{row_index}\0{alias_value}"),
        "alias": alias_value,
        "source_id": source_id,
        "document_id": document_id,
        "normalization_notes": "Raw alias retained; no fuzzy matching performed.",
        "match_method": "canonical_url" if source_id else "unresolved",
    }
    return source, occurrence, alias


def _claim_columns(table: MarkdownTable) -> dict[str, int | None]:
    headers = tuple(_header_name(header) for header in table.headers)
    return {
        "claim": _header_index(headers, lambda value: value in {"claim", "claim text", "assertion"}),
        "type": _header_index(headers, lambda value: value in {"claim type", "type", "status"}),
        "confidence": _header_index(headers, lambda value: "confidence" in value),
        "source": _header_index(headers, lambda value: value in {"source", "sources", "evidence source", "source ids"}),
        "relation": _header_index(headers, lambda value: "relationship" in value or "relation" == value),
        "stage": _header_index(headers, lambda value: value in {"workflow stage", "stage"}),
        "falsifier": _header_index(headers, lambda value: "falsifier" in value),
        "valid_from": _header_index(headers, lambda value: value in {"valid from", "validity start"}),
        "valid_to": _header_index(headers, lambda value: value in {"valid to", "valid until", "validity end"}),
        "limitations": _header_index(headers, lambda value: "limitation" in value),
        "locator": _header_index(headers, lambda value: "locator" in value or "span" in value),
        "quote": _header_index(headers, lambda value: "quote" in value or "evidence text" in value),
        "independence": _header_index(headers, lambda value: "independence group" in value),
    }


def _parse_claim_row(
    table: MarkdownTable,
    row: tuple[str, ...],
    row_index: int,
    document_id: str,
    relative_path: str,
    run_id: str,
    local_aliases: dict[str, list[str]],
    warnings: list[dict[str, str]],
) -> tuple[dict[str, Any], list[dict[str, Any]]] | None:
    columns = _claim_columns(table)
    claim_text = _column(row, columns["claim"])
    raw_type = _column(row, columns["type"]).strip().casefold()
    claim_type = CLAIM_TYPES.get(raw_type)
    raw_confidence = _column(row, columns["confidence"]).strip().casefold()
    confidence = next(
        (level for level in ("high", "medium", "low") if re.match(rf"^{level}\b", raw_confidence)),
        None,
    )
    if not claim_text or not claim_type or not confidence:
        warnings.append(
            _make_warning(
                run_id,
                relative_path,
                "unsupported_table_shape",
                f"Claim-like table row at line {row_index} lacks an explicit claim type or confidence.",
                " | ".join(row),
            )
        )
        return None

    claim_id = stable_id(
        "clm",
        f"{document_id}\0{claim_type}\0{confidence}\0{_normalized_text(claim_text)}",
    )
    claim = {
        "claim_id": claim_id,
        "document_id": document_id,
        "claim_text": claim_text,
        "claim_type": claim_type,
        "confidence": confidence,
        "workflow_stage": _column(row, columns["stage"]) or None,
        "falsifier": _column(row, columns["falsifier"]) or None,
        "valid_from": _parse_date(_column(row, columns["valid_from"])),
        "valid_to": _parse_date(_column(row, columns["valid_to"])),
        "limitations": _column(row, columns["limitations"]) or None,
        "extraction_method": "markdown_claim_table",
    }
    relationships = {
        "supports": "supports",
        "conflicts": "conflicts",
        "contextualizes": "contextualizes",
    }
    raw_relationship = _column(row, columns["relation"]).casefold()
    relationship = relationships.get(raw_relationship, "supports")
    claim_sources: list[dict[str, Any]] = []
    source_refs = _column(row, columns["source"])
    labels = re.findall(r"\bS\d+[A-Za-z]?\b", source_refs, re.IGNORECASE)
    for label in labels:
        matching_ids = sorted(set(local_aliases.get(label.casefold(), [])))
        if len(matching_ids) != 1:
            warnings.append(
                _make_warning(
                    run_id,
                    relative_path,
                    "unresolved_alias",
                    f"Claim {claim_id} references {label!r}, which does not resolve to exactly one local source.",
                    label,
                )
            )
            continue
        source_id = matching_ids[0]
        claim_sources.append(
            {
                "claim_source_id": stable_id(
                    "cs",
                    f"{claim_id}\0{source_id}\0{relationship}\0{_column(row, columns['locator'])}",
                ),
                "claim_id": claim_id,
                "source_id": source_id,
                "relationship": relationship,
                "evidence_locator": _column(row, columns["locator"]) or None,
                "evidence_quote": _column(row, columns["quote"]) or None,
                "independence_group": _column(row, columns["independence"]) or None,
            }
        )
    return claim, claim_sources


def _merge_source_metadata(
    sources: dict[str, dict[str, Any]],
    source: dict[str, Any],
    relative_path: str,
    run_id: str,
    warnings: list[dict[str, str]],
) -> None:
    existing = sources.get(source["source_id"])
    if existing is None:
        sources[source["source_id"]] = source
        return
    left_class = existing["evidence_class"]
    right_class = source["evidence_class"]
    if left_class and right_class and left_class != right_class:
        existing["evidence_class"] = None
        warnings.append(
            _make_warning(
                run_id,
                relative_path,
                "classification_conflict",
                f"Exact-URL source {source['source_id']} has conflicting classifications; canonical class left unset.",
                f"{left_class} / {right_class}",
            )
        )
    else:
        existing["evidence_class"] = left_class or right_class
    for key in ("publisher", "author", "publication_date", "access_date", "bias_notes", "metadata_notes"):
        existing[key] = existing[key] or source[key]


def _load_file_cache(database_path: Path) -> dict[str, str]:
    """Return {path: sha256} from the most recent ingestion_run in database_path.

    Returns an empty dict if the database does not exist, cannot be opened,
    or contains no ingestion_run rows.
    """
    if not database_path.exists():
        return {}
    connection: duckdb.DuckDBPyConnection | None = None
    try:
        connection = duckdb.connect(str(database_path), read_only=True)
        results = connection.execute(
            """
            SELECT ii.path, ii.sha256
            FROM ingestion_input ii
            JOIN ingestion_run ir ON ir.run_id = ii.run_id
            WHERE ir.built_at = (SELECT MAX(built_at) FROM ingestion_run)
            """
        ).fetchall()
        return {row[0]: row[1] for row in results}
    except Exception:
        return {}
    finally:
        if connection is not None:
            connection.close()


def _copy_unchanged_rows(
    old_db_path: Path,
    unchanged_paths: set[str],
    run_id: str,
    source_records: dict[str, dict[str, Any]],
    warnings: list[dict[str, str]],
) -> tuple[
    list[dict[str, Any]],  # document_rows
    list[dict[str, Any]],  # occurrence_rows
    list[dict[str, Any]],  # alias_rows
    list[dict[str, Any]],  # claim_rows
    list[dict[str, Any]],  # claim_source_rows
]:
    """Carry forward rows for unchanged files from the previous database.

    ATTACHes ``old_db_path`` read-only, SELECTs all rows belonging to
    ``unchanged_paths`` from each content table, and returns them as Python
    lists so that the caller can merge and insert them.  Source rows are fed
    through ``_merge_source_metadata`` into ``source_records`` directly rather
    than returned in a list.  ``ingestion_warning`` rows are appended directly
    to ``warnings``.

    If ``unchanged_paths`` is empty, returns five empty lists immediately.
    If any exception occurs, catches it and returns five empty lists so that
    ``build_database`` falls back to a full rebuild for those files.
    """
    if not unchanged_paths:
        return [], [], [], [], []

    connection: duckdb.DuckDBPyConnection | None = None
    try:
        connection = duckdb.connect(str(old_db_path), read_only=True)
        placeholders = ", ".join("?" for _ in unchanged_paths)
        path_list = list(unchanged_paths)

        def _fetch(sql: str, params: list[Any]) -> list[dict[str, Any]]:
            cursor = connection.execute(sql, params)
            col_names = [desc[0] for desc in cursor.description]
            return [dict(zip(col_names, row)) for row in cursor.fetchall()]

        # 1. research_document
        document_rows = _fetch(
            f"SELECT * FROM research_document WHERE path IN ({placeholders})",
            path_list,
        )

        # 2. source — feed through merge, do not collect into a return list
        source_rows = _fetch(
            f"""
            SELECT * FROM source
            WHERE source_id IN (
                SELECT DISTINCT source_id
                FROM citation_occurrence
                WHERE document_id IN (
                    SELECT document_id FROM research_document
                    WHERE path IN ({placeholders})
                )
                AND source_id IS NOT NULL
            )
            """,
            path_list,
        )
        for source_row in source_rows:
            _merge_source_metadata(source_records, source_row, "cache", run_id, warnings)

        # 3. citation_occurrence (includes evidence_tier)
        occurrence_rows = _fetch(
            f"""
            SELECT * FROM citation_occurrence
            WHERE document_id IN (
                SELECT document_id FROM research_document
                WHERE path IN ({placeholders})
            )
            """,
            path_list,
        )

        # 4. source_alias
        alias_rows = _fetch(
            f"""
            SELECT * FROM source_alias
            WHERE document_id IN (
                SELECT document_id FROM research_document
                WHERE path IN ({placeholders})
            )
            """,
            path_list,
        )

        # 5. claim
        claim_rows = _fetch(
            f"""
            SELECT * FROM claim
            WHERE document_id IN (
                SELECT document_id FROM research_document
                WHERE path IN ({placeholders})
            )
            """,
            path_list,
        )

        # 6. claim_source
        claim_source_rows = _fetch(
            f"""
            SELECT * FROM claim_source
            WHERE claim_id IN (
                SELECT claim_id FROM claim
                WHERE document_id IN (
                    SELECT document_id FROM research_document
                    WHERE path IN ({placeholders})
                )
            )
            """,
            path_list,
        )

        # 7. ingestion_warning — re-stamp carried-forward rows to the new run_id
        # (warning_id is content-derived from the OLD run_id, so regenerate both
        # to satisfy the ingestion_warning.run_id -> ingestion_run FK).
        warning_rows = _fetch(
            f"SELECT * FROM ingestion_warning WHERE input_path IN ({placeholders})",
            path_list,
        )
        for carried in warning_rows:
            warnings.append(
                _make_warning(
                    run_id,
                    carried["input_path"],
                    carried["warning_type"],
                    carried["message"],
                    carried.get("raw_value", "") or "",
                )
            )

        return document_rows, occurrence_rows, alias_rows, claim_rows, claim_source_rows

    except Exception:
        return [], [], [], [], []
    finally:
        if connection is not None:
            connection.close()


def _insert_rows(connection: duckdb.DuckDBPyConnection, table: str, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    columns = tuple(rows[0])
    sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join('?' for _ in columns)})"
    connection.executemany(sql, [tuple(row[column] for column in columns) for row in rows])


def build_database(
    raw_dir: Path,
    database_path: Path,
    warnings_path: Path,
    schema_path: Path | None = None,
) -> dict[str, Any]:
    raw_dir = raw_dir.resolve()
    database_path = database_path.resolve()
    warnings_path = warnings_path.resolve()
    schema_path = (schema_path or ROOT / "schemas" / "citations.sql").resolve()
    database_path.parent.mkdir(parents=True, exist_ok=True)
    warnings_path.parent.mkdir(parents=True, exist_ok=True)
    temp_database_path = database_path.with_name(f"{database_path.stem}.tmp{database_path.suffix}")
    candidate_roots = [raw_dir]
    if raw_dir.is_relative_to(ROOT):
        analysis_root = ROOT / "analysis"
        if analysis_root.exists():
            candidate_roots.append(analysis_root)
    documents = sorted(
        {path for root in candidate_roots for path in root.rglob("*.md")},
        key=lambda path: path.relative_to(ROOT).as_posix().casefold() if path.is_relative_to(ROOT) else path.as_posix().casefold(),
    )
    snapshots = [
        {
            "path": path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.relative_to(raw_dir).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "modified_at": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).replace(tzinfo=None),
            "absolute_path": path,
        }
        for path in documents
    ]
    run_fingerprint = "\n".join(
        f"{item['path']}\0{item['sha256']}" for item in snapshots
    ) + f"\n{PARSER_VERSION}"
    run_id = stable_id("run", run_fingerprint)
    input_root = raw_dir.relative_to(ROOT).as_posix() if raw_dir.is_relative_to(ROOT) else raw_dir.as_posix()
    built_at = datetime.now(timezone.utc).replace(tzinfo=None)

    temp_database_path = temp_database_path.with_name(f"{temp_database_path.stem}_{hashlib.sha256(str(database_path).encode('utf-8')).hexdigest()[:12]}{temp_database_path.suffix}")
    connection = duckdb.connect(str(temp_database_path))
    connection.execute(schema_path.read_text(encoding="utf-8"))
    warnings: list[dict[str, str]] = []
    source_records: dict[str, dict[str, Any]] = {}
    document_rows: list[dict[str, Any]] = []
    occurrence_rows: list[dict[str, Any]] = []
    alias_rows: list[dict[str, Any]] = []
    claim_rows: list[dict[str, Any]] = []
    claim_source_rows: list[dict[str, Any]] = []

    # --- Incremental cache ---
    # Load the hash cache from the previous database (returns {} if none exists or fails)
    file_cache = _load_file_cache(database_path)

    # Classify each snapshot as unchanged or changed
    unchanged_paths: set[str] = {
        snap["path"]
        for snap in snapshots
        if file_cache.get(snap["path"]) == snap["sha256"]
    }
    changed_snapshots = [snap for snap in snapshots if snap["path"] not in unchanged_paths]

    # Carry forward rows for unchanged files (mutates source_records and warnings in place)
    cached_doc_rows, cached_occ_rows, cached_alias_rows, cached_claim_rows, cached_cs_rows = (
        _copy_unchanged_rows(database_path, unchanged_paths, run_id, source_records, warnings)
    )
    document_rows.extend(cached_doc_rows)
    occurrence_rows.extend(cached_occ_rows)
    alias_rows.extend(cached_alias_rows)
    claim_rows.extend(cached_claim_rows)
    claim_source_rows.extend(cached_cs_rows)

    parsed_documents: list[dict[str, Any]] = []
    for snapshot in changed_snapshots:
        path = snapshot["absolute_path"]
        relative_path = snapshot["path"]
        markdown = path.read_text(encoding="utf-8", errors="replace")
        metadata = _document_metadata(path, relative_path, markdown)
        document_id = stable_id("doc", relative_path.casefold())
        document_rows.append(
            {
                "document_id": document_id,
                "path": relative_path,
                "title": metadata["title"],
                "document_type": metadata["document_type"],
                "evaluation_date": metadata["evaluation_date"],
                "evaluation_decision": metadata["evaluation_decision"],
                "quality_rating": metadata["quality_rating"],
                "is_internal": metadata["is_internal"],
                "content_sha256": snapshot["sha256"],
                "modified_at": snapshot["modified_at"],
            }
        )
        parsed_documents.append(
            {
                "document_id": document_id,
                "path": relative_path,
                "markdown": markdown,
                "tables": parse_markdown_tables(markdown),
                "access_date": _date_from_access_text(markdown),
                "is_internal": metadata["is_internal"],
            }
        )

    local_aliases_by_document: dict[str, dict[str, list[str]]] = {}
    for document in parsed_documents:
        relative_path = document["path"]
        document_id = document["document_id"]
        local_aliases: dict[str, list[str]] = {}
        for table in document["tables"]:
            if _is_source_table(table):
                for row, row_index in zip(table.rows, table.row_lines):
                    source, occurrence, alias = _source_row_data(
                        table,
                        row,
                        row_index,
                        document_id,
                        relative_path,
                        run_id,
                        document["access_date"],
                        warnings,
                    )
                    if source:
                        _merge_source_metadata(source_records, source, relative_path, run_id, warnings)
                    occurrence_rows.append(occurrence)
                    alias_rows.append(alias)
                    if alias["source_id"] and re.fullmatch(r"S\d+[A-Za-z]?", alias["alias"], re.IGNORECASE):
                        local_aliases.setdefault(alias["alias"].casefold(), []).append(alias["source_id"])
            headers = {_header_name(header) for header in table.headers}
            if any(header in {"claim", "claim text", "assertion"} for header in headers):
                claim_columns = _claim_columns(table)
                full_claim_contract = all(
                    claim_columns[key] is not None for key in ("claim", "type", "confidence")
                )
                if not full_claim_contract and table.rows:
                    warnings.append(
                        _make_warning(
                            run_id,
                            relative_path,
                            "unsupported_table_shape",
                            f"Claim-like table at line {table.header_line} lacks required type/confidence columns.",
                            " | ".join(table.headers),
                        )
                    )
        local_aliases_by_document[document_id] = local_aliases

    for document in parsed_documents:
        if document["is_internal"]:
            continue
        relative_path = document["path"]
        document_id = document["document_id"]
        local_aliases = local_aliases_by_document[document_id]
        for table in document["tables"]:
            headers = {_header_name(header) for header in table.headers}
            if not any(header in {"claim", "claim text", "assertion"} for header in headers):
                continue
            columns = _claim_columns(table)
            if not all(columns[key] is not None for key in ("claim", "type", "confidence")):
                continue
            for row, row_index in zip(table.rows, table.row_lines):
                parsed = _parse_claim_row(
                    table,
                    row,
                    row_index,
                    document_id,
                    relative_path,
                    run_id,
                    local_aliases,
                    warnings,
                )
                if parsed:
                    claim, claim_sources = parsed
                    claim_rows.append(claim)
                    claim_source_rows.extend(claim_sources)

    merged_claim_rows: dict[str, dict[str, Any]] = {}
    for claim in claim_rows:
        claim_id = claim["claim_id"]
        existing = merged_claim_rows.get(claim_id)
        if existing is None:
            merged_claim_rows[claim_id] = claim
            continue
        warnings.append(
            _make_warning(
                run_id,
                claim["document_id"],
                "duplicate_claim",
                f"Merged duplicate claim row for {claim['claim_text']!r}; identical normalized text, claim type, and confidence were kept once.",
                claim_id,
            )
        )

    deduplicated_claim_rows = list(merged_claim_rows.values())
    deduplicated_claim_sources: dict[tuple[str, str, str, str | None], dict[str, Any]] = {}
    for claim_source in claim_source_rows:
        key = (
            claim_source["claim_id"],
            claim_source["source_id"],
            claim_source["relationship"],
            claim_source["evidence_locator"],
        )
        deduplicated_claim_sources.setdefault(key, claim_source)
    merged_claim_source_rows = list(deduplicated_claim_sources.values())

    try:
        connection.execute("BEGIN TRANSACTION")
        _insert_rows(
            connection,
            "ingestion_run",
            [{"run_id": run_id, "built_at": built_at, "parser_version": PARSER_VERSION, "input_root": input_root}],
        )
        _insert_rows(
            connection,
            "ingestion_input",
            [
                {"run_id": run_id, "path": item["path"], "sha256": item["sha256"], "modified_at": item["modified_at"]}
                for item in snapshots
            ],
        )
        _insert_rows(connection, "research_document", document_rows)
        _insert_rows(connection, "source", list(source_records.values()))
        _insert_rows(connection, "citation_occurrence", occurrence_rows)
        _insert_rows(connection, "source_alias", alias_rows)
        _insert_rows(connection, "claim", deduplicated_claim_rows)
        _insert_rows(connection, "claim_source", merged_claim_source_rows)
        # Deduplicate warnings by warning_id before inserting (carried-forward + new may overlap)
        deduplicated_warnings: dict[str, dict[str, str]] = {}
        for w in warnings:
            deduplicated_warnings.setdefault(w["warning_id"], w)
        warnings = list(deduplicated_warnings.values())
        _insert_rows(connection, "ingestion_warning", warnings)
        connection.execute("COMMIT")
    except Exception:
        connection.execute("ROLLBACK")
        raise
    finally:
        connection.close()

    temp_database_path.replace(database_path)

    with warnings_path.open("w", encoding="utf-8", newline="\n") as warning_file:
        for warning in sorted(warnings, key=lambda item: (item["input_path"], item["warning_id"])):
            warning_file.write(json.dumps(warning, ensure_ascii=True, sort_keys=True) + "\n")

    return {
        "run_id": run_id,
        "database_path": str(database_path),
        "warnings_path": str(warnings_path),
        "documents": len(document_rows),
        "sources": len(source_records),
        "occurrences": len(occurrence_rows),
        "claims": len(deduplicated_claim_rows),
        "claim_source_mappings": len(merged_claim_source_rows),
        "warnings": len(warnings),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-dir", type=Path, default=ROOT / "research" / "raw")
    parser.add_argument("--database", type=Path, default=ROOT / "data" / "citations.duckdb")
    parser.add_argument("--warnings", type=Path, default=ROOT / "data" / "citation_ingestion_warnings.jsonl")
    parser.add_argument("--schema", type=Path, default=ROOT / "schemas" / "citations.sql")
    arguments = parser.parse_args()
    print(json.dumps(build_database(arguments.raw_dir, arguments.database, arguments.warnings, arguments.schema), indent=2))


if __name__ == "__main__":
    main()