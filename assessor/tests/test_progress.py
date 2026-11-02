from assessor.course_manifest import load_manifest
from assessor.paths import assessor_dir, find_course_root
from assessor.progress import Progress, next_unblocked, resolve_current


def test_next_unblocked_respects_deps():
    root = find_course_root()
    manifest = load_manifest(assessor_dir(root))
    progress = Progress(completed=["1A", "2A", "3A", "4A"], current=None)
    assert next_unblocked(manifest, progress) == "5A"
    progress2 = Progress(completed=[], current=None)
    assert next_unblocked(manifest, progress2) == "1A"
