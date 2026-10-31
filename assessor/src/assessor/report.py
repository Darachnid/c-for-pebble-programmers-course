from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from assessor.bundle import SubmitBundle
from assessor.checks_deterministic import criterion_deterministic_status, run_deterministic
from assessor.checks_llm import run_llm
from assessor.ollama_client import OllamaConfig
from assessor.rubric import Rubric


@dataclass
class CriterionResult:
    id: str
    text: str
    status: str  # pass | fail | uncertain
    messages: list[str] = field(default_factory=list)
    closest_meets: str | None = None
    closest_below: str | None = None


@dataclass
class AssessmentReport:
    activity_id: str
    timestamp: str
    overall: str  # pass | fail | uncertain
    ollama_model: str | None = None
    criteria: list[CriterionResult] = field(default_factory=list)
    deterministic_checks: list[dict] = field(default_factory=list)
    llm_checks: list[dict] = field(default_factory=list)


def _merge_status(*statuses: str | None) -> str:
    ordered = [s for s in statuses if s]
    if not ordered:
        return "uncertain"
    if any(s == "fail" for s in ordered):
        return "fail"
    if any(s == "uncertain" for s in ordered):
        return "uncertain"
    return "pass"


def assess_rubric(
    rubric: Rubric,
    bundle: SubmitBundle,
    assessor_root: Path,
    ollama: OllamaConfig,
) -> AssessmentReport:
    det_outcomes = run_deterministic(rubric, bundle)
    llm_outcomes = run_llm(rubric, bundle, assessor_root, ollama)

    llm_by_id = {o.criterion_id: o for o in llm_outcomes}
    criteria_results: list[CriterionResult] = []

    for criterion in rubric.criteria:
        det_status = criterion_deterministic_status(criterion.id, det_outcomes)
        llm_o = llm_by_id.get(criterion.id)
        llm_status = llm_o.status if llm_o else None
        if not criterion.llm_assess:
            llm_status = None
        status = _merge_status(det_status, llm_status)

        messages: list[str] = []
        for o in det_outcomes:
            if o.criterion_id == criterion.id:
                messages.append(o.message)
        if llm_o:
            messages.append(f"[LLM] {llm_o.message}")

        criteria_results.append(
            CriterionResult(
                id=criterion.id,
                text=criterion.text,
                status=status,
                messages=messages,
                closest_meets=llm_o.closest_meets if llm_o else None,
                closest_below=llm_o.closest_below if llm_o else None,
            )
        )

    overall = _merge_status(*(c.status for c in criteria_results))

    return AssessmentReport(
        activity_id=rubric.id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        overall=overall,
        ollama_model=ollama.model,
        criteria=criteria_results,
        deterministic_checks=[asdict(o) for o in det_outcomes],
        llm_checks=[asdict(o) for o in llm_outcomes],
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
        "ollama_model": report.ollama_model,
        "criteria": [asdict(c) for c in report.criteria],
        "deterministic_checks": report.deterministic_checks,
        "llm_checks": report.llm_checks,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def format_report_text(report: AssessmentReport) -> str:
    lines = [
        f"Assessment: {report.activity_id} — {report.overall.upper()}",
    ]
    if report.ollama_model:
        lines.append(f"Ollama model: {report.ollama_model}")
    lines.append("")
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
