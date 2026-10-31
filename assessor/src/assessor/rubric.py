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
class Criterion:
    id: str
    text: str
    source: str = "lesson"
    deterministic: list[DeterministicCheck] = field(default_factory=list)
    llm_assess: bool = True


@dataclass
class Rubric:
    id: str
    lesson_readme: str
    paths: list[str]
    evidence_sections: list[str]
    criteria: list[Criterion]
    llm_global: dict[str, Any] = field(default_factory=dict)
    evidence_template: str = "templates/EVIDENCE.md.tpl"

    @property
    def exemplar_meets(self) -> Path | None:
        rel = self.llm_global.get("exemplar_dirs", {}).get("meets")
        return Path(rel) if rel else None

    @property
    def exemplar_below(self) -> Path | None:
        rel = self.llm_global.get("exemplar_dirs", {}).get("below")
        return Path(rel) if rel else None


def _parse_check(raw: dict[str, Any]) -> DeterministicCheck:
    kind = raw.pop("kind")
    return DeterministicCheck(kind=kind, params=raw)


def _parse_llm_global(data: dict[str, Any]) -> dict[str, Any]:
    if "llm" in data:
        return dict(data["llm"])
    if "spacy" in data:
        # Legacy pilot YAML on other branches
        legacy = dict(data["spacy"])
        legacy.pop("meets_min_margin", None)
        legacy.pop("uncertain_band", None)
        return legacy
    return {}


def load_rubric(path: Path) -> Rubric:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    criteria: list[Criterion] = []
    for item in data.get("criteria", []):
        llm_flag = item.get("llm", True)
        if "spacy" in item and "llm" not in item:
            llm_flag = True
        if llm_flag is False or llm_flag == "false":
            assess = False
        else:
            assess = True
        det = [_parse_check(dict(c)) for c in item.get("deterministic", [])]
        criteria.append(
            Criterion(
                id=item["id"],
                text=item["text"],
                source=item.get("source", "lesson"),
                deterministic=det,
                llm_assess=assess,
            )
        )
    return Rubric(
        id=data["id"],
        lesson_readme=data.get("lesson_readme", ""),
        paths=list(data.get("paths", [])),
        evidence_sections=list(data.get("evidence_sections", [])),
        criteria=criteria,
        llm_global=_parse_llm_global(data),
        evidence_template=data.get("evidence_template", "templates/EVIDENCE.md.tpl"),
    )
