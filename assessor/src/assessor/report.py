from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from assessor.bundle import SubmitBundle
from assessor.checks_deterministic import CheckOutcome, criterion_deterministic_status, run_deterministic
from assessor.checks_spacy import SpacyOutcome, run_spacy
from assessor.rubric import Rubric


@dataclass
class CriterionResult:
    id: str
    text: str
    status: str  # pass | fail | uncertain
    messages: list[str] = field(default_factory=list)
    closest_meets: str | None = None
    closest_below: str | None = None
    margin: float | None = None


@dataclass
class AssessmentReport:
    activity_id: str
    timestamp: str
    overall: str  # pass | fail | uncertain
    criteria: list[CriterionResult] = field(default_factory=list)
    deterministic_checks: list[dict] = field(default_factory=list)
    spacy_checks: list[dict] = field(default_factory=list)


def _merge_status(*statuses: str | None) -> str:
    ordered = [s for s in statuses if s]
    if not ordered:
        return "uncertain"
    if any(s == "fail" for s in ordered):
        return "fail"
    if any(s == "uncertain" for s in ordered):
        return "uncertain"
    return "pass"


def assess_rubric(rubric: Rubric, bundle: SubmitBundle, assessor_root: Path) -> AssessmentReport:
    det_outcomes = run_deterministic(rubric, bundle)
    spacy_outcomes = run_spacy(rubric, bundle.combined_text_for_spacy, assessor_root)

    spacy_by_id = {o.criterion_id: o for o in spacy_outcomes}
    criteria_results: list[CriterionResult] = []

    for criterion in rubric.criteria:
        det_status = criterion_deterministic_status(criterion.id, det_outcomes)
        spacy_o = spacy_by_id.get(criterion.id)
        spacy_status = spacy_o.status if spacy_o else None
        status = _merge_status(det_status, spacy_status)

        messages: list[str] = []
        for o in det_outcomes:
            if o.criterion_id == criterion.id:
                messages.append(o.message)
        if spacy_o:
            messages.append(spacy_o.message)

        criteria_results.append(
            CriterionResult(
                id=criterion.id,
                text=criterion.text,
                status=status,
                messages=messages,
                closest_meets=spacy_o.closest_meets if spacy_o else None,
                closest_below=spacy_o.closest_below if spacy_o else None,
                margin=spacy_o.margin if spacy_o else None,
            )
        )

    overall = _merge_status(*(c.status for c in criteria_results))

    return AssessmentReport(
        activity_id=rubric.id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        overall=overall,
        criteria=criteria_results,
        deterministic_checks=[asdict(o) for o in det_outcomes],
        spacy_checks=[asdict(o) for o in spacy_outcomes],
    )


def save_report(course_root: Path, report: AssessmentReport) -> Path:
    out_dir = course_root / ".assessor" / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    safe_ts = report.timestamp.replace(":", "-")
    path = out_dir / f"{report.activity_id}-{safe_ts}.json"
    payload = {
        "activity_id": report.activity_id,
        "timestamp": report.timestamp,
        "overall": report.overall,
        "criteria": [asdict(c) for c in report.criteria],
        "deterministic_checks": report.deterministic_checks,
        "spacy_checks": report.spacy_checks,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def format_report_text(report: AssessmentReport) -> str:
    lines = [
        f"Assessment: {report.activity_id} — {report.overall.upper()}",
        "",
    ]
    for c in report.criteria:
        lines.append(f"[{c.status.upper()}] {c.id}: {c.text}")
        for msg in c.messages:
            lines.append(f"    • {msg}")
        if c.closest_below and c.status == "fail":
            lines.append(f"    ↳ Compare with exemplar below/{c.closest_below}")
        if c.closest_meets and c.status == "pass":
            lines.append(f"    ↳ Similar to exemplar meets/{c.closest_meets}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
