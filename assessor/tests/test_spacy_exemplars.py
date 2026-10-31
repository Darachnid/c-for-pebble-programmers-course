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


@pytest.mark.skipif(not _nlp_available(), reason="en_core_web_md not installed")
def test_meets_exemplar_beats_below_on_margin():
    root = find_course_root()
    rubric = load_rubric(root / "assessor/rubrics/2A.yaml")
    assessor_root = root / "assessor"
    meets_text = (assessor_root / "examples/2A/meets/01-minimal-pass/EVIDENCE.md").read_text(
        encoding="utf-8"
    )
    below_text = (assessor_root / "examples/2A/below/01-vague-no-artifacts/EVIDENCE.md").read_text(
        encoding="utf-8"
    )
    meets_out = run_spacy(rubric, meets_text, assessor_root)
    below_out = run_spacy(rubric, below_text, assessor_root)
    assert meets_out and below_out
    meets_margin = meets_out[0].margin
    below_margin = below_out[0].margin
    assert meets_margin is not None and below_margin is not None
    assert meets_margin > below_margin
