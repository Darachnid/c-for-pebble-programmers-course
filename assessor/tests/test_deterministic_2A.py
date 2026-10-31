from pathlib import Path

from assessor.bundle import SubmitBundle
from assessor.checks_deterministic import run_deterministic
from assessor.paths import find_course_root
from assessor.rubric import load_rubric


def _bundle(diff: str, evidence: str) -> SubmitBundle:
    root = find_course_root(Path(__file__).resolve())
    return SubmitBundle(
        activity_id="2A",
        course_root=root,
        evidence_path=root / "submit/2A/EVIDENCE.md",
        evidence_text=evidence,
        diff_text=diff,
        log_oneline="abc123 init",
        changed_files=["lessons/2A/starter/src/c/main.c"],
    )


def test_two_textlayer_creates_fail():
    root = find_course_root(Path(__file__).resolve())
    rubric = load_rubric(root / "assessor/rubrics/2A.yaml")
    diff = "+  a = text_layer_create(b1);\n+  b = text_layer_create(b2);\n"
    evidence = (
        "## Artifact paths\n\nx\n## Build and run\n\npebble build emery\n"
        "## Behavior observed\n\nTextLayer time\n## Boundary case tested\n\nboundary minute\n"
        "## Explain in your own words\n\nok\n## Source diff\n\ngit\n"
    )
    outcomes = run_deterministic(rubric, _bundle(diff, evidence))
    kinds = [(o.check_kind, o.status) for o in outcomes]
    assert ("max_textlayer_create_in_diff", "fail") in kinds


def test_single_textlayer_passes_heuristic():
    root = find_course_root(Path(__file__).resolve())
    rubric = load_rubric(root / "assessor/rubrics/2A.yaml")
    diff = "+  s_layer = text_layer_create(bounds);\n"
    evidence = (
        "## Artifact paths\n\nx\n## Build and run\n\npebble build success emery\n"
        "## Behavior observed\n\nTextLayer minute\n## Boundary case tested\n\nboundary rollover\n"
        "## Explain in your own words\n\nok\n## Source diff\n\ngit diff\n"
    )
    outcomes = run_deterministic(rubric, _bundle(diff, evidence))
    layer_checks = [o for o in outcomes if o.check_kind == "max_textlayer_create_in_diff"]
    assert layer_checks and layer_checks[0].status == "pass"
