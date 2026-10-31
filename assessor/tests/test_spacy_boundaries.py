"""Rigorous spaCy boundary tests — documents margin limits and phrase-gate behavior.

Calibrated against en_core_web_md on shipped exemplars (regression guard + limit map).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from assessor.checks_spacy import run_spacy
from assessor.paths import find_course_root
from assessor.rubric import load_rubric

pytestmark = pytest.mark.spacy


def _nlp_available() -> bool:
    try:
        import spacy

        spacy.load("en_core_web_md")
        return True
    except OSError:
        return False


def _root() -> Path:
    return find_course_root(Path(__file__).resolve())


def _assessor_root() -> Path:
    return _root() / "assessor"


def _load_exemplar(activity_id: str, tier: str, name: str) -> str:
    path = _assessor_root() / "examples" / activity_id / tier / name / "EVIDENCE.md"
    return path.read_text(encoding="utf-8")


def _run(activity_id: str, text: str):
    rubric = load_rubric(_assessor_root() / "rubrics" / f"{activity_id}.yaml")
    outcomes = run_spacy(rubric, text, _assessor_root())
    by_id = {o.criterion_id: o for o in outcomes}
    margin = outcomes[0].margin if outcomes else None
    return rubric, outcomes, by_id, margin


@pytest.mark.skipif(not _nlp_available(), reason="en_core_web_md not installed")
class TestSpacyMarginSeparation:
    """Global document margin (meets_sim - below_sim) must separate tiers."""

    def test_7a_meets_margins_above_threshold(self):
        rubric, _, _, _ = _run("7A", _load_exemplar("7A", "meets", "01-minimal-pass"))
        min_margin = rubric.meets_min_margin
        for name in ("01-minimal-pass", "02-with-build-log"):
            _, _, by_id, margin = _run("7A", _load_exemplar("7A", "meets", name))
            assert margin is not None
            assert margin >= min_margin, f"7A meets/{name} margin {margin} < {min_margin}"
            for cid, o in by_id.items():
                assert o.status == "pass", f"7A meets/{name} {cid}: {o.message}"

    def test_7a_below_vague_margin_below_negative_threshold(self):
        rubric, _, by_id, margin = _run("7A", _load_exemplar("7A", "below", "01-vague-no-artifacts"))
        assert margin is not None
        assert margin <= -rubric.meets_min_margin
        assert all(o.status == "fail" for o in by_id.values())

    def test_7a_meets_beat_vague_pairwise(self):
        meets_m = _run("7A", _load_exemplar("7A", "meets", "01-minimal-pass"))[3]
        below_m = _run("7A", _load_exemplar("7A", "below", "01-vague-no-artifacts"))[3]
        assert meets_m is not None and below_m is not None
        assert meets_m - below_m >= 0.15, "Expected wide separation for anchor exemplars"

    def test_4a_meets_anchor_above_below_vague(self):
        meets_m = _run("4A", _load_exemplar("4A", "meets", "01-both-projects"))[3]
        below_m = _run("4A", _load_exemplar("4A", "below", "01-one-project-only"))[3]
        assert meets_m is not None and below_m is not None
        assert meets_m > below_m
        assert meets_m - below_m >= 0.15


@pytest.mark.skipif(not _nlp_available(), reason="en_core_web_md not installed")
class TestSpacyKnownLimits:
    """Document brittle zones: threshold band, phrase gates, ambiguous exemplars."""

    def test_7a_date_layer_exemplar_borderline_margin(self):
        """Below exemplar with real build detail sits in uncertain band (not a clean fail)."""
        rubric, _, by_id, margin = _run("7A", _load_exemplar("7A", "below", "02-date-layer-added"))
        assert margin is not None
        assert abs(margin) < rubric.meets_min_margin, (
            f"date-layer margin {margin} expected inside ±{rubric.meets_min_margin} ambiguous band"
        )
        assert by_id["time_only_face"].status == "fail", "missing TextLayer/minute phrases"
        assert by_id["build_and_run"].status in ("uncertain", "fail")

    def test_4a_meets_concrete_features_below_threshold(self):
        """Strong exemplar can still land below meets_min_margin (0.04) — embedding limit."""
        rubric, _, by_id, margin = _run("4A", _load_exemplar("4A", "meets", "02-concrete-features"))
        assert margin is not None
        assert margin < rubric.meets_min_margin
        assert all(o.status == "uncertain" for o in by_id.values())

    def test_4a_parrots_reading_ambiguous_not_clear_fail(self):
        """Syllabus-parroting text is not far enough below threshold for auto-fail."""
        rubric, _, by_id, margin = _run("4A", _load_exemplar("4A", "below", "02-parrots-reading"))
        assert margin is not None
        assert -rubric.meets_min_margin < margin < rubric.meets_min_margin
        assert all(o.status == "uncertain" for o in by_id.values())

    def test_4a_meets_both_projects_phrase_gate_variable(self):
        """Phrase gate can fail a meets exemplar — spaCy pass requires both margin and phrases."""
        _, _, by_id, margin = _run("4A", _load_exemplar("4A", "meets", "01-both-projects"))
        assert margin is not None and margin >= 0.04
        assert by_id["both_projects"].status == "pass"
        assert by_id["c_feature_and_diff"].status == "fail"
        assert "variable" in by_id["c_feature_and_diff"].message.lower()


@pytest.mark.skipif(not _nlp_available(), reason="en_core_web_md not installed")
class TestSpacyPhraseGates:
    """Required phrases are hard fails independent of exemplar margin."""

    def test_missing_emery_fails_despite_positive_margin_text(self):
        text = (
            "## Artifact paths\n\nx\n## Build and run\n\npebble build success in emulator\n"
            "## Behavior observed\n\nTextLayer updates each minute\n## Boundary case tested\n\nboundary\n"
            "## Explain in your own words\n\nok\n## Source diff\n\ngit\n"
        )
        _, _, by_id, margin = _run("7A", text)
        assert margin is not None
        assert by_id["build_and_run"].status == "fail"
        assert "emery" in by_id["build_and_run"].message.lower()

    def test_keyword_stuffing_does_not_reach_meets_margin(self):
        """All required tokens present but no exemplar-like prose — still below meets bar."""
        text = (
            "## Artifact paths\n\nlessons/7A\n## Build and run\n\npebble build emery emulator\n"
            "## Behavior observed\n\nTextLayer minute\n## Boundary case tested\n\nboundary boundary\n"
            "## Explain in your own words\n\nbuild emery emulator TextLayer minute boundary\n"
            "## Source diff\n\ngit diff\n"
        )
        rubric, outcomes, _, margin = _run("7A", text)
        meets_anchor = _run("7A", _load_exemplar("7A", "meets", "01-minimal-pass"))[3]
        assert margin is not None and meets_anchor is not None
        assert margin < meets_anchor
        assert margin < rubric.meets_min_margin, (
            "keyword-stuffed evidence should not clear meets_min_margin"
        )
        assert all(o.status != "pass" for o in outcomes), (
            "phrase gates alone must not yield spaCy pass without exemplar-like margin"
        )

    def test_empty_sections_fail_multiple_phrase_gates(self):
        text = "## Artifact paths\n\n\n## Build and run\n\n\n## Behavior observed\n\n\n"
        _, _, by_id, _ = _run("7A", text)
        assert by_id["build_and_run"].status == "fail"
        assert by_id["time_only_face"].status == "fail"


@pytest.mark.skipif(not _nlp_available(), reason="en_core_web_md not installed")
class TestSpacyInternalConsistency:
    def test_single_margin_per_submit_across_criteria(self):
        _, outcomes, _, _ = _run("7A", _load_exemplar("7A", "meets", "01-minimal-pass"))
        margins = {o.margin for o in outcomes}
        assert len(margins) == 1

    def test_closest_exemplar_points_into_meets_for_meets_text(self):
        _, outcomes, _, _ = _run("7A", _load_exemplar("7A", "meets", "01-minimal-pass"))
        assert outcomes[0].closest_meets in ("01-minimal-pass", "02-with-build-log")
        assert outcomes[0].closest_below in ("01-vague-no-artifacts", "02-date-layer-added")
