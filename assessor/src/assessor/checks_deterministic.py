from __future__ import annotations

import re
from dataclasses import dataclass

from assessor.bundle import SubmitBundle, count_textlayer_create_in_diff
from assessor.rubric import Criterion, DeterministicCheck, Rubric


@dataclass
class CheckOutcome:
    criterion_id: str
    check_kind: str
    status: str  # pass | fail | skip
    message: str


def _apply_check(check: DeterministicCheck, criterion: Criterion, bundle: SubmitBundle, rubric: Rubric) -> CheckOutcome:
    kind = check.kind
    p = check.params
    cid = criterion.id

    if kind == "require_section":
        section = p.get("section", "")
        if section in bundle.evidence_text:
            return CheckOutcome(cid, kind, "pass", f"Found section {section!r}.")
        return CheckOutcome(cid, kind, "fail", f"Missing section heading {section!r} in EVIDENCE.md.")

    if kind == "regex_in_evidence":
        pattern = p["pattern"]
        if re.search(pattern, bundle.evidence_text, re.MULTILINE):
            return CheckOutcome(cid, kind, "pass", f"Evidence matches /{pattern}/.")
        return CheckOutcome(cid, kind, "fail", f"Evidence does not match required pattern /{pattern}/.")

    if kind == "forbid_regex_in_evidence":
        pattern = p["pattern"]
        if re.search(pattern, bundle.evidence_text, re.MULTILINE | re.I):
            return CheckOutcome(cid, kind, "fail", f"Evidence matches forbidden pattern /{pattern}/.")
        return CheckOutcome(cid, kind, "pass", "No forbidden phrasing detected.")

    if kind == "regex_in_diff":
        pattern = p["pattern"]
        if re.search(pattern, bundle.diff_text, re.MULTILINE):
            return CheckOutcome(cid, kind, "pass", f"Diff matches /{pattern}/.")
        return CheckOutcome(cid, kind, "fail", f"Diff does not match /{pattern}/.")

    if kind == "require_paths_changed":
        min_files = int(p.get("min_files", 1))
        n = len(bundle.changed_files)
        if n >= min_files:
            return CheckOutcome(cid, kind, "pass", f"{n} file(s) changed under lesson paths.")
        return CheckOutcome(
            cid,
            kind,
            "fail",
            f"Expected at least {min_files} changed file(s) under lesson paths; found {n}. "
            "Commit your work or widen paths in EVIDENCE.md if your project lives elsewhere.",
        )

    if kind == "max_textlayer_create_in_diff":
        maximum = int(p.get("max", 1))
        count = count_textlayer_create_in_diff(bundle.diff_text)
        if count <= maximum:
            return CheckOutcome(
                cid,
                kind,
                "pass",
                f"At most {maximum} TextLayer create in diff (+ lines); counted {count}.",
            )
        return CheckOutcome(
            cid,
            kind,
            "fail",
            f"Too many TextLayer create calls in diff ({count} > {maximum}). "
            "2A requires a time-only face with no date layer.",
        )

    if kind == "require_phrase_count":
        phrase = p["phrase"]
        minimum = int(p.get("min", 1))
        count = len(re.findall(re.escape(phrase), bundle.evidence_text, re.I))
        if count >= minimum:
            return CheckOutcome(cid, kind, "pass", f"Found {count} mention(s) of {phrase!r}.")
        return CheckOutcome(
            cid,
            kind,
            "fail",
            f"Expected at least {minimum} mention(s) of {phrase!r}; found {count}.",
        )

    if kind == "require_build_log_or_evidence":
        if bundle.build_log_text and re.search(p.get("log_pattern", "."), bundle.build_log_text):
            return CheckOutcome(cid, kind, "pass", "build.log present with expected content.")
        pattern = p.get("evidence_pattern", "(?i)build")
        if re.search(pattern, bundle.evidence_text):
            return CheckOutcome(cid, kind, "pass", "Build described in EVIDENCE.md (optional build.log absent).")
        return CheckOutcome(
            cid,
            kind,
            "fail",
            "Add submit/<ID>/build.log or describe a successful pebble build in EVIDENCE.md.",
        )

    return CheckOutcome(cid, kind, "fail", f"Unknown deterministic check kind: {kind!r}")


def run_deterministic(rubric: Rubric, bundle: SubmitBundle) -> list[CheckOutcome]:
    outcomes: list[CheckOutcome] = []
    for criterion in rubric.criteria:
        if not criterion.deterministic:
            continue
        for check in criterion.deterministic:
            outcomes.append(_apply_check(check, criterion, bundle, rubric))
    return outcomes


def criterion_deterministic_status(criterion_id: str, outcomes: list[CheckOutcome]) -> str | None:
    relevant = [o for o in outcomes if o.criterion_id == criterion_id]
    if not relevant:
        return None
    if any(o.status == "fail" for o in relevant):
        return "fail"
    return "pass"
