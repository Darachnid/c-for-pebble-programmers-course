#!/usr/bin/env python3
"""Run deterministic + semantic assessor layers for one benchmark fixture (stdout JSON)."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from assessor.bundle import SubmitBundle
from assessor.checks_deterministic import run_deterministic
from assessor.paths import assessor_dir
from assessor.rubric import load_rubric


def _benchmark_dir() -> Path:
    return Path(__file__).resolve().parent


def load_fixtures() -> dict:
    data = json.loads((_benchmark_dir() / "fixtures.json").read_text(encoding="utf-8"))
    return {f["id"]: f for f in data["fixtures"]}


def _build_bundle(course_root: Path, fixture: dict) -> SubmitBundle:
    assess_root = assessor_dir(course_root)
    if fixture.get("evidence_inline"):
        evidence_text = fixture["evidence_inline"]
    else:
        rel = fixture["evidence_path"]
        path = assess_root / rel
        if not path.is_file():
            raise SystemExit(f"Missing evidence file: {path}")
        evidence_text = path.read_text(encoding="utf-8")

    overrides = fixture.get("bundle_overrides") or {}
    activity_id = fixture["activity_id"]
    return SubmitBundle(
        activity_id=activity_id,
        course_root=course_root,
        evidence_path=course_root / "submit" / activity_id / "EVIDENCE.md",
        evidence_text=evidence_text,
        diff_text=overrides.get("diff_text", ""),
        log_oneline=overrides.get("log_oneline", "benchmark fixture"),
        changed_files=list(overrides.get("changed_files") or []),
        build_log_text=overrides.get("build_log_text"),
    )


def _semantic_spacy(rubric, bundle, assessor_root):
    from assessor.checks_spacy import run_spacy

    text = getattr(bundle, "combined_text_for_spacy", None) or bundle.combined_text_for_assessment
    outcomes = run_spacy(rubric, text, assessor_root)
    return [
        {
            "id": o.criterion_id,
            "status": o.status,
            "message": o.message,
            "margin": o.margin,
            "closest_meets": o.closest_meets,
            "closest_below": o.closest_below,
        }
        for o in outcomes
    ]


def _semantic_ollama(rubric, bundle, assessor_root, model: str | None):
    try:
        from assessor.checks_llm import run_llm
        from assessor.ollama_client import OllamaConfig
    except ImportError as exc:
        raise SystemExit(
            "Ollama backend not available in this checkout (need assessor/ollama-local branch)."
        ) from exc

    config = OllamaConfig.from_env()
    if model:
        config = OllamaConfig(
            base_url=config.base_url, model=model, timeout_s=config.timeout_s
        )
    outcomes = run_llm(rubric, bundle, assessor_root, config)
    return [
        {
            "id": o.criterion_id,
            "status": o.status,
            "message": o.message,
            "closest_meets": o.closest_meets,
            "closest_below": o.closest_below,
        }
        for o in outcomes
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Benchmark one fixture")
    parser.add_argument("--course-root", type=Path, default=Path.cwd())
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--backend", choices=("spacy", "ollama"), required=True)
    parser.add_argument("--model", default=None, help="Ollama model override")
    args = parser.parse_args(argv)

    course_root = args.course_root.resolve()
    fixtures = load_fixtures()
    if args.fixture not in fixtures:
        raise SystemExit(f"Unknown fixture {args.fixture!r}")
    fixture = fixtures[args.fixture]
    assessor_root = assessor_dir(course_root)
    rubric = load_rubric(assessor_root / "rubrics" / f"{fixture['activity_id']}.yaml")
    bundle = _build_bundle(course_root, fixture)

    det = [asdict(o) for o in run_deterministic(rubric, bundle)]
    if args.backend == "spacy":
        semantic = _semantic_spacy(rubric, bundle, assessor_root)
    else:
        semantic = _semantic_ollama(rubric, bundle, assessor_root, args.model)

    payload = {
        "fixture_id": args.fixture,
        "activity_id": fixture["activity_id"],
        "gold_tier": fixture.get("gold_tier"),
        "backend": args.backend,
        "deterministic": det,
        "semantic": semantic,
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
