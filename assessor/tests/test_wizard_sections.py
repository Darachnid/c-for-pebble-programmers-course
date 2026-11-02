from assessor.evidence import merge_evidence_sections, split_evidence_sections

HEADINGS = [
    "## Artifact paths",
    "## Build and run",
    "## Explain in your own words",
]


def test_split_and_merge_roundtrip():
    text = """# Evidence

## Artifact paths

- lessons/1A/clock

## Build and run

pebble build

## Explain in your own words

five ideas here
"""
    bodies = split_evidence_sections(text, HEADINGS)
    assert "lessons/1A/clock" in bodies["## Artifact paths"]
    bodies["## Explain in your own words"] = "updated ideas"
    merged = merge_evidence_sections(text, HEADINGS, bodies)
    assert "updated ideas" in merged
    assert "pebble build" in merged
