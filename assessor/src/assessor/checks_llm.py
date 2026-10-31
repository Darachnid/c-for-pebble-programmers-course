from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from assessor.bundle import SubmitBundle
from assessor.ollama_client import OllamaConfig, chat_json, ollama_available
from assessor.rubric import Rubric

SYSTEM_PROMPT = """You are a post-submit evidence assessor for a Pebble C programming course.
You ONLY evaluate submitted evidence against fixed rubric criteria. You do NOT tutor, debug code,
suggest implementations, or rewrite the student's work.

Use the meets-threshold and below-threshold exemplars to calibrate what adequate evidence looks like.
Exemplars show evidence shape, not solutions to copy.

Respond with JSON only, matching this schema:
{
  "criteria": [
    {
      "id": "<criterion id>",
      "status": "pass" | "fail" | "uncertain",
      "message": "<one or two sentences citing the student's evidence>",
      "closest_meets": "<exemplar folder name or null>",
      "closest_below": "<exemplar folder name or null>"
    }
  ]
}

Rules:
- pass: evidence clearly meets the criterion text
- fail: evidence missing, vague, contradicts the criterion, or matches below-exemplar patterns
- uncertain: partial or ambiguous evidence; say what is missing
- Do not mark pass without concrete artifacts described when the criterion requires them
"""


@dataclass
class LlmOutcome:
    criterion_id: str
    status: str
    message: str
    closest_meets: str | None = None
    closest_below: str | None = None


def _load_exemplars(base: Path | None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if not base or not base.is_dir():
        return items
    for child in sorted(base.iterdir()):
        if not child.is_dir():
            continue
        ev = child / "EVIDENCE.md"
        notes = child / "NOTES.md"
        if not ev.is_file():
            continue
        items.append(
            {
                "name": child.name,
                "evidence": ev.read_text(encoding="utf-8")[:4000],
                "notes": notes.read_text(encoding="utf-8").strip()[:500] if notes.is_file() else "",
            }
        )
    return items


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 20] + "\n… (truncated)"


def _build_user_prompt(
    rubric: Rubric,
    bundle: SubmitBundle,
    meets: list[dict[str, str]],
    below: list[dict[str, str]],
) -> str:
    criteria_block = [
        {"id": c.id, "text": c.text, "source": c.source} for c in rubric.criteria if c.llm_assess
    ]
    payload = {
        "activity_id": rubric.id,
        "criteria": criteria_block,
        "student_evidence_md": bundle.evidence_text,
        "build_log_excerpt": _truncate(bundle.build_log_text or "", 3000),
        "git_changed_files": bundle.changed_files[:40],
        "git_diff_excerpt": _truncate(bundle.diff_text, 8000),
        "meets_threshold_exemplars": meets,
        "below_threshold_exemplars": below,
    }
    import json

    return json.dumps(payload, indent=2)


def run_llm(
    rubric: Rubric,
    bundle: SubmitBundle,
    assessor_root: Path,
    config: OllamaConfig,
) -> list[LlmOutcome]:
    needs = any(c.llm_assess for c in rubric.criteria) or rubric.llm_global
    if not needs:
        return []

    if not ollama_available(config):
        raise SystemExit(
            f"Ollama is not reachable at {config.base_url}.\n"
            "Install and start Ollama, then: ollama pull "
            f"{config.model}"
        )

    meets_dir = assessor_root / rubric.exemplar_meets if rubric.exemplar_meets else None
    below_dir = assessor_root / rubric.exemplar_below if rubric.exemplar_below else None
    meets = _load_exemplars(meets_dir)
    below = _load_exemplars(below_dir)

    user_prompt = _build_user_prompt(rubric, bundle, meets, below)
    parsed = chat_json(config, SYSTEM_PROMPT, user_prompt)

    raw_list = parsed.get("criteria") or []
    by_id = {str(item.get("id", "")): item for item in raw_list if item.get("id")}

    outcomes: list[LlmOutcome] = []
    for criterion in rubric.criteria:
        if not criterion.llm_assess:
            continue
        item = by_id.get(criterion.id)
        if not item:
            outcomes.append(
                LlmOutcome(
                    criterion_id=criterion.id,
                    status="uncertain",
                    message="LLM did not return this criterion; retry submit or check model JSON compliance.",
                )
            )
            continue
        status = str(item.get("status", "uncertain")).lower()
        if status not in ("pass", "fail", "uncertain"):
            status = "uncertain"
        outcomes.append(
            LlmOutcome(
                criterion_id=criterion.id,
                status=status,
                message=str(item.get("message", "")).strip() or "No message from LLM.",
                closest_meets=item.get("closest_meets") or None,
                closest_below=item.get("closest_below") or None,
            )
        )
    return outcomes
