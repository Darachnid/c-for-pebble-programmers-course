"""Unit tests for benchmark compare_report (CI-safe, no Ollama)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _compare_module():
    path = Path(__file__).resolve().parents[1] / "benchmark" / "compare_report.py"
    spec = importlib.util.spec_from_file_location("compare_report", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


_compare = _compare_module()
build_report = _compare.build_report
format_text = _compare.format_text


def test_agreement_and_disagreement():
    rows = [
        {
            "fixture_id": "7A_meets_01",
            "backend": "spacy",
            "gold_tier": "meets",
            "semantic": [
                {"id": "build_and_run", "status": "pass", "message": "a"},
                {"id": "time_only_face", "status": "pass", "message": "b"},
            ],
        },
        {
            "fixture_id": "7A_meets_01",
            "backend": "ollama",
            "gold_tier": "meets",
            "semantic": [
                {"id": "build_and_run", "status": "pass", "message": "c"},
                {"id": "time_only_face", "status": "fail", "message": "d"},
            ],
        },
    ]
    report = build_report(rows)
    assert report["criterion_comparisons"] == 2
    assert report["agreement_rate"] == 0.5
    assert len(report["disagreements"]) == 1
    assert report["disagreements"][0]["criterion_id"] == "time_only_face"
    text = format_text(report)
    assert "50.0%" in text or "50%" in text


def test_fixtures_json_loads():
    from pathlib import Path

    path = Path(__file__).resolve().parents[1] / "benchmark" / "fixtures.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert len(data["fixtures"]) >= 11
