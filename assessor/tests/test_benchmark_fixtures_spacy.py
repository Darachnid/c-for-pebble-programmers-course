"""Lock spaCy semantic statuses to calibrated_spacy.json (regression on fixture corpus)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from assessor.paths import find_course_root


def _run_fixture_mod():
    path = Path(__file__).resolve().parents[1] / "benchmark" / "run_fixture.py"
    spec = importlib.util.spec_from_file_location("run_fixture", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


_run_fixture = _run_fixture_mod()
load_fixtures = _run_fixture.load_fixtures
run_fixture_main = _run_fixture.main

pytestmark = pytest.mark.spacy


def _nlp_available() -> bool:
    try:
        import spacy

        spacy.load("en_core_web_md")
        return True
    except OSError:
        return False


def _calibrated() -> dict[str, dict[str, str]]:
    path = Path(__file__).resolve().parents[1] / "benchmark" / "calibrated_spacy.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["fixtures"]


@pytest.mark.skipif(not _nlp_available(), reason="en_core_web_md not installed")
@pytest.mark.parametrize("fixture_id", list(load_fixtures().keys()))
def test_fixture_matches_spacy_calibration(fixture_id: str, capsys):
    root = find_course_root(Path(__file__).resolve())
    expected = _calibrated().get(fixture_id)
    assert expected, f"Add {fixture_id} to calibrated_spacy.json"

    run_fixture_main(
        [
            "--course-root",
            str(root),
            "--fixture",
            fixture_id,
            "--backend",
            "spacy",
        ]
    )
    out = capsys.readouterr().out.strip()
    row = json.loads(out)
    actual = {item["id"]: item["status"] for item in row["semantic"]}
    assert actual == expected, (
        f"{fixture_id}: semantic status drift; re-run compare_report --write-calibration spacy"
    )
