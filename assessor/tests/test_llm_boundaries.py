"""Rigorous LLM assessor tests (mocked + optional live Ollama)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from assessor.bundle import SubmitBundle
from assessor.checks_llm import run_llm
from assessor.ollama_client import OllamaConfig, ollama_available
from assessor.paths import find_course_root
from assessor.rubric import load_rubric

pytestmark = pytest.mark.ollama


def _run_fixture_mod():
    path = Path(__file__).resolve().parents[1] / "benchmark" / "run_fixture.py"
    spec = importlib.util.spec_from_file_location("run_fixture", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def _load_exemplar(activity_id: str, tier: str, name: str) -> str:
    root = find_course_root(Path(__file__).resolve())
    path = root / "assessor" / "examples" / activity_id / tier / name / "EVIDENCE.md"
    return path.read_text(encoding="utf-8")


def _bundle(activity_id: str, evidence: str, **overrides) -> SubmitBundle:
    root = find_course_root(Path(__file__).resolve())
    return SubmitBundle(
        activity_id=activity_id,
        course_root=root,
        evidence_path=root / "submit" / activity_id / "EVIDENCE.md",
        evidence_text=evidence,
        diff_text=overrides.get("diff_text", "+ x();\n"),
        log_oneline="bench",
        changed_files=overrides.get("changed_files", [f"lessons/{activity_id}/starter/src/c/main.c"]),
    )


def _mock_response(status_map: dict[str, str]) -> dict:
    return {
        "criteria": [
            {
                "id": cid,
                "status": status,
                "message": f"mock {status}",
                "closest_meets": "01-minimal-pass" if status == "pass" else None,
                "closest_below": "01-vague-no-artifacts" if status == "fail" else None,
            }
            for cid, status in status_map.items()
        ]
    }


@patch("assessor.checks_llm.ollama_available", return_value=True)
@patch("assessor.checks_llm.chat_json")
class TestLlmMockedBoundaries:
    def test_missing_criterion_returns_uncertain(self, mock_chat, _up):
        root = find_course_root(Path(__file__).resolve())
        rubric = load_rubric(root / "assessor/rubrics/7A.yaml")
        mock_chat.return_value = {
            "criteria": [{"id": "build_and_run", "status": "pass", "message": "ok"}]
        }
        evidence = _load_exemplar("7A", "meets", "01-minimal-pass")
        outcomes = run_llm(
            rubric, _bundle("7A", evidence), root / "assessor", OllamaConfig(model="test")
        )
        by_id = {o.criterion_id: o for o in outcomes}
        assert by_id["build_and_run"].status == "pass"
        assert by_id["time_only_face"].status == "uncertain"

    def test_invalid_status_coerced_to_uncertain(self, mock_chat, _up):
        root = find_course_root(Path(__file__).resolve())
        rubric = load_rubric(root / "assessor/rubrics/7A.yaml")
        mock_chat.return_value = {
            "criteria": [
                {"id": "build_and_run", "status": "maybe", "message": "hmm"},
            ]
        }
        evidence = _load_exemplar("7A", "meets", "01-minimal-pass")
        outcomes = run_llm(
            rubric, _bundle("7A", evidence), root / "assessor", OllamaConfig(model="test")
        )
        assert outcomes[0].status == "uncertain"

    def test_tier_ordering_meets_vs_vague_mock(self, mock_chat, _up):
        root = find_course_root(Path(__file__).resolve())
        rubric = load_rubric(root / "assessor/rubrics/7A.yaml")
        meets = _load_exemplar("7A", "meets", "01-minimal-pass")
        vague = _load_exemplar("7A", "below", "01-vague-no-artifacts")

        mock_chat.return_value = _mock_response(
            {
                "build_and_run": "pass",
                "time_only_face": "pass",
                "workflow_artifacts": "pass",
            }
        )
        meets_out = run_llm(
            rubric, _bundle("7A", meets), root / "assessor", OllamaConfig(model="test")
        )
        mock_chat.return_value = _mock_response(
            {
                "build_and_run": "fail",
                "time_only_face": "fail",
                "workflow_artifacts": "fail",
            }
        )
        vague_out = run_llm(
            rubric, _bundle("7A", vague), root / "assessor", OllamaConfig(model="test")
        )
        meets_pass = sum(1 for o in meets_out if o.status == "pass")
        vague_pass = sum(1 for o in vague_out if o.status == "pass")
        assert meets_pass > vague_pass


@patch("assessor.checks_llm.ollama_available", return_value=True)
@patch("assessor.checks_llm.chat_json")
def test_4a_one_project_mock_fails_both_projects(mock_chat, _up):
    root = find_course_root(Path(__file__).resolve())
    rubric = load_rubric(root / "assessor/rubrics/4A.yaml")
    text = _load_exemplar("4A", "below", "01-one-project-only")
    mock_chat.return_value = _mock_response(
        {
            "both_projects": "fail",
            "c_feature_and_diff": "fail",
            "boundary_cases": "fail",
        }
    )
    outcomes = run_llm(
        rubric, _bundle("4A", text), root / "assessor", OllamaConfig(model="test")
    )
    assert outcomes[0].status == "fail"


@pytest.mark.ollama_live
@pytest.mark.skipif(not ollama_available(OllamaConfig.from_env()), reason="Ollama not running")
def test_live_7a_vague_majority_fail():
    root = find_course_root(Path(__file__).resolve())
    rubric = load_rubric(root / "assessor/rubrics/7A.yaml")
    text = _load_exemplar("7A", "below", "01-vague-no-artifacts")
    outcomes = run_llm(
        rubric,
        _bundle("7A", text, diff_text="", changed_files=[]),
        root / "assessor",
        OllamaConfig.from_env(),
    )
    fails = sum(1 for o in outcomes if o.status == "fail")
    assert fails >= 2, "Live Ollama should fail most criteria on vague 7A evidence"


@pytest.mark.ollama_live
@pytest.mark.skipif(not ollama_available(OllamaConfig.from_env()), reason="Ollama not running")
def test_live_fixture_runner_7a_meets():
    mod = _run_fixture_mod()
    root = find_course_root(Path(__file__).resolve())
    import io
    import contextlib

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod.main(
            [
                "--course-root",
                str(root),
                "--fixture",
                "7A_meets_01",
                "--backend",
                "ollama",
            ]
        )
    row = json.loads(buf.getvalue())
    assert row["backend"] == "ollama"
    assert len(row["semantic"]) >= 3
