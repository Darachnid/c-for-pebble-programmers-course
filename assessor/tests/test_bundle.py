from pathlib import Path

from assessor.bundle import (
    SubmitBundle,
    count_textlayer_create_in_diff,
    validate_evidence_sections,
)


def test_validate_evidence_sections():
    text = "## Build and run\n\nok\n## Behavior observed\n"
    missing = validate_evidence_sections(
        text,
        ["## Build and run", "## Behavior observed", "## Missing"],
    )
    assert missing == ["## Missing"]


def test_count_textlayer_create_in_diff():
    diff = """
--- a/main.c
+++ b/main.c
+  s_layer = text_layer_create(bounds);
+  // comment text_layer_create fake
+  s_date = text_layer_create(d2);
"""
    assert count_textlayer_create_in_diff(diff) == 2


def test_combined_text_for_spacy():
    b = SubmitBundle(
        activity_id="2A",
        course_root=Path("/tmp"),
        evidence_path=Path("/tmp/e"),
        evidence_text="hello",
        diff_text="",
        log_oneline="",
        build_log_text="BUILD OK",
    )
    assert "BUILD OK" in b.combined_text_for_spacy
