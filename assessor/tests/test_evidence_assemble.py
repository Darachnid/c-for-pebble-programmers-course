from assessor.course_manifest import load_manifest
from assessor.evidence import assemble_evidence, split_evidence_sections
from assessor.paths import assessor_dir, find_course_root
from assessor.paths import rubric_path
from assessor.rubric import load_rubric


def test_assemble_writes_user_sections(tmp_path, monkeypatch):
    root = find_course_root()
    monkeypatch.chdir(root)
    manifest = load_manifest(assessor_dir(root))
    activity = manifest.activity("1A")
    rubric = load_rubric(rubric_path(root, "1A"))
    user = {
        "behavior": "Saw clock and fonts examples.",
        "boundary": "Compared one-layer vs two-layer ideas as boundary.",
        "explain": "Five ideas with API. Most interesting to investigate first: idea 1. "
        "Example variation feasibility noted.",
    }
    path = assemble_evidence(root, activity, rubric, user)
    text = path.read_text(encoding="utf-8")
    bodies = split_evidence_sections(text, rubric.evidence_sections)
    assert "Five ideas" in bodies["## Explain in your own words"]
    assert "lessons/1A/clock" in bodies["## Artifact paths"]
    assert "pebble build" in bodies["## Build and run"]
