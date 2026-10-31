from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class DeterministicCheck:
    kind: str
    params: dict[str, Any] = field(default_factory=dict)


@dataclass
class SpacyCriterion:
    required_phrases: list[str] = field(default_factory=list)
    exemplar_tag: str | None = None


@dataclass
class Criterion:
    id: str
    text: str
    source: str = "lesson"
    deterministic: list[DeterministicCheck] = field(default_factory=list)
    spacy: SpacyCriterion | None = None


@dataclass
class Rubric:
    id: str
    lesson_readme: str
    paths: list[str]
    evidence_sections: list[str]
    criteria: list[Criterion]
    spacy_global: dict[str, Any] = field(default_factory=dict)
    evidence_template: str = "templates/EVIDENCE.md.tpl"

    @property
    def exemplar_meets(self) -> Path | None:
        rel = self.spacy_global.get("exemplar_dirs", {}).get("meets")
        return Path(rel) if rel else None

    @property
    def exemplar_below(self) -> Path | None:
        rel = self.spacy_global.get("exemplar_dirs", {}).get("below")
        return Path(rel) if rel else None

    @property
    def meets_min_margin(self) -> float:
        return float(self.spacy_global.get("meets_min_margin", 0.05))

    @property
    def uncertain_band(self) -> float:
        return float(self.spacy_global.get("uncertain_band", 0.02))


def _parse_check(raw: dict[str, Any]) -> DeterministicCheck:
    kind = raw.pop("kind")
    return DeterministicCheck(kind=kind, params=raw)


def load_rubric(path: Path) -> Rubric:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    criteria: list[Criterion] = []
    for item in data.get("criteria", []):
        spacy_raw = item.get("spacy")
        spacy = None
        if spacy_raw:
            spacy = SpacyCriterion(
                required_phrases=list(spacy_raw.get("required_phrases", [])),
                exemplar_tag=spacy_raw.get("exemplar_tag"),
            )
        det = [_parse_check(dict(c)) for c in item.get("deterministic", [])]
        criteria.append(
            Criterion(
                id=item["id"],
                text=item["text"],
                source=item.get("source", "lesson"),
                deterministic=det,
                spacy=spacy,
            )
        )
    return Rubric(
        id=data["id"],
        lesson_readme=data.get("lesson_readme", ""),
        paths=list(data.get("paths", [])),
        evidence_sections=list(data.get("evidence_sections", [])),
        criteria=criteria,
        spacy_global=dict(data.get("spacy", {})),
        evidence_template=data.get("evidence_template", "templates/EVIDENCE.md.tpl"),
    )
