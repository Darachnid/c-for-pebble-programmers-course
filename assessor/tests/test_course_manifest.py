from assessor.course_manifest import load_manifest, validate_manifest
from assessor.paths import find_course_root, assessor_dir


def test_phase1_manifest_loads_and_paths_exist():
    root = find_course_root()
    manifest = load_manifest(assessor_dir(root))
    assert manifest.sequence == ["1A", "2A", "3A", "4A", "5A"]
    validate_manifest(root, manifest)
    for aid in manifest.sequence:
        act = manifest.activity(aid)
        assert act.user_fields
        assert act.assessor_rubric
