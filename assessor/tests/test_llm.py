from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from assessor.bundle import SubmitBundle
from assessor.checks_llm import run_llm
from assessor.ollama_client import OllamaConfig
from assessor.paths import find_course_root
from assessor.rubric import load_rubric


def _bundle(evidence: str) -> SubmitBundle:
    root = find_course_root(Path(__file__).resolve())
    return SubmitBundle(
        activity_id="7A",
        course_root=root,
        evidence_path=root / "submit/7A/EVIDENCE.md",
        evidence_text=evidence,
        diff_text="+ text_layer_create();\n",
        log_oneline="abc init",
        changed_files=["lessons/7A/starter/src/c/main.c"],
    )


@patch("assessor.checks_llm.ollama_available", return_value=True)
@patch("assessor.checks_llm.chat_json")
def test_llm_maps_criteria(mock_chat, _mock_up):
    root = find_course_root(Path(__file__).resolve())
    rubric = load_rubric(root / "assessor/rubrics/7A.yaml")
    mock_chat.return_value = {
        "criteria": [
            {
                "id": "build_and_run",
                "status": "pass",
                "message": "Build and emery install described.",
                "closest_meets": "01-minimal-pass",
                "closest_below": None,
            },
            {
                "id": "time_only_face",
                "status": "fail",
                "message": "Missing minute rollover detail.",
                "closest_meets": None,
                "closest_below": "01-vague-no-artifacts",
            },
            {
                "id": "workflow_artifacts",
                "status": "pass",
                "message": "Boundary and paths listed.",
                "closest_meets": "01-minimal-pass",
                "closest_below": None,
            },
        ]
    }
    evidence = (
        "## Artifact paths\n\nlessons/7A\n## Build and run\n\npebble build emery\n"
        "## Behavior observed\n\nTextLayer\n## Boundary case tested\n\nboundary\n"
        "## Explain in your own words\n\nok\n## Source diff\n\ngit\n"
    )
    outcomes = run_llm(
        rubric,
        _bundle(evidence),
        root / "assessor",
        OllamaConfig(model="test-model"),
    )
    by_id = {o.criterion_id: o for o in outcomes}
    assert by_id["build_and_run"].status == "pass"
    assert by_id["time_only_face"].status == "fail"
    assert by_id["time_only_face"].closest_below == "01-vague-no-artifacts"
