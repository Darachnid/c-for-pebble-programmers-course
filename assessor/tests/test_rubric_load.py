from assessor.paths import find_course_root
from assessor.rubric import load_rubric


def test_load_pilot_rubrics():
    root = find_course_root()
    for aid in ("1A", "2A", "3A", "4A", "5A"):
        rubric = load_rubric(root / "assessor/rubrics" / f"{aid}.yaml")
        assert rubric.id == aid
        assert rubric.criteria
        assert rubric.exemplar_meets
