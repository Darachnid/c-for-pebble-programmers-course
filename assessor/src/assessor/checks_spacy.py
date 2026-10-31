from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from assessor.rubric import Criterion, Rubric


@dataclass
class SpacyOutcome:
    criterion_id: str
    status: str  # pass | fail | uncertain | skip
    margin: float | None
    closest_meets: str | None
    closest_below: str | None
    message: str


def _load_nlp():
    import spacy

    try:
        return spacy.load("en_core_web_md")
    except OSError as exc:
        raise SystemExit(
            "spaCy model en_core_web_md is not installed. Run:\n"
            "  python -m spacy download en_core_web_md"
        ) from exc


def _cosine(a, b) -> float:
    va = np.asarray(a, dtype=float).ravel()
    vb = np.asarray(b, dtype=float).ravel()
    if va.size != vb.size or va.size == 0:
        return 0.0
    na = float(np.linalg.norm(va))
    nb = float(np.linalg.norm(vb))
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(va, vb) / (na * nb))


def _embed_dir(nlp, base: Path) -> list[tuple[str, list[float]]]:
    items: list[tuple[str, list[float]]] = []
    if not base.is_dir():
        return items
    for child in sorted(base.iterdir()):
        if not child.is_dir():
            continue
        ev = child / "EVIDENCE.md"
        if not ev.is_file():
            continue
        text = ev.read_text(encoding="utf-8")
        doc = nlp(text)
        if doc.has_vector and doc.vector.size > 0:
            items.append((child.name, np.asarray(doc.vector, dtype=float)))
    return items


def _best_match(vec: list[float], pool: list[tuple[str, list[float]]]) -> tuple[str | None, float]:
    if not pool:
        return None, 0.0
    best_name = pool[0][0]
    best_sim = _cosine(vec, pool[0][1])
    for name, other in pool[1:]:
        sim = _cosine(vec, other[1])
        if sim > best_sim:
            best_sim = sim
            best_name = name
    return best_name, best_sim


def _phrase_hits(nlp, text: str, phrases: list[str]) -> list[str]:
    doc = nlp(text.lower())
    lemmas = {t.lemma_.lower() for t in doc if not t.is_space}
    text_lower = text.lower()
    missing: list[str] = []
    for phrase in phrases:
        parts = phrase.lower().split()
        if len(parts) == 1:
            if parts[0] not in lemmas and parts[0] not in text_lower:
                missing.append(phrase)
        else:
            if phrase.lower() not in text_lower:
                missing.append(phrase)
    return missing


def run_spacy(
    rubric: Rubric,
    student_text: str,
    assessor_root: Path,
) -> list[SpacyOutcome]:
    needs_spacy = any(c.spacy for c in rubric.criteria) or rubric.spacy_global
    if not needs_spacy:
        return []

    nlp = _load_nlp()
    meets_dir = assessor_root / rubric.exemplar_meets if rubric.exemplar_meets else None
    below_dir = assessor_root / rubric.exemplar_below if rubric.exemplar_below else None
    meets_pool = _embed_dir(nlp, meets_dir) if meets_dir else []
    below_pool = _embed_dir(nlp, below_dir) if below_dir else []

    student_doc = nlp(student_text)
    if not student_doc.has_vector:
        return [
            SpacyOutcome(
                criterion_id=c.id,
                status="uncertain",
                margin=None,
                closest_meets=None,
                closest_below=None,
                message="Could not vectorize evidence text.",
            )
            for c in rubric.criteria
            if c.spacy
        ]
    student_vec = np.asarray(student_doc.vector, dtype=float)

    meets_sim = _best_match(student_vec, meets_pool)[1] if meets_pool else 0.0
    below_sim = _best_match(student_vec, below_pool)[1] if below_pool else 0.0
    margin = meets_sim - below_sim
    closest_meets, _ = _best_match(student_vec, meets_pool)
    closest_below, _ = _best_match(student_vec, below_pool)

    outcomes: list[SpacyOutcome] = []
    min_margin = rubric.meets_min_margin
    uncertain_band = rubric.uncertain_band

    for criterion in rubric.criteria:
        if not criterion.spacy:
            continue
        missing = _phrase_hits(nlp, student_text, criterion.spacy.required_phrases)
        if missing:
            outcomes.append(
                SpacyOutcome(
                    criterion_id=criterion.id,
                    status="fail",
                    margin=margin,
                    closest_meets=closest_meets,
                    closest_below=closest_below,
                    message=f"Missing expected concepts in evidence: {', '.join(missing)}.",
                )
            )
            continue

        if margin >= min_margin:
            status = "pass"
            msg = (
                f"Evidence aligns more with meets exemplars (margin {margin:.3f} >= {min_margin}). "
                f"Closest meets: {closest_meets or 'n/a'}."
            )
        elif margin <= -min_margin:
            status = "fail"
            msg = (
                f"Evidence aligns more with below-threshold exemplars (margin {margin:.3f}). "
                f"Compare assessor/examples/{rubric.id}/meets vs below; closest below: {closest_below or 'n/a'}."
            )
        elif abs(margin) < uncertain_band:
            status = "uncertain"
            msg = (
                f"Exemplar contrast is ambiguous (margin {margin:.3f}). "
                f"Review assessor/examples/{rubric.id}/ meets vs below and strengthen EVIDENCE.md."
            )
        else:
            status = "uncertain"
            msg = (
                f"Borderline exemplar contrast (margin {margin:.3f}). "
                "Add concrete build, behavior, and boundary details."
            )

        outcomes.append(
            SpacyOutcome(
                criterion_id=criterion.id,
                status=status,
                margin=margin,
                closest_meets=closest_meets,
                closest_below=closest_below,
                message=msg,
            )
        )

    return outcomes
