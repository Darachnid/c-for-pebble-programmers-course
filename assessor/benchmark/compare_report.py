#!/usr/bin/env python3
"""Merge benchmark JSONL runs and print agreement / disagreement report."""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def _load_jsonl(lines: list[str]) -> list[dict]:
    rows: list[dict] = []
    for line in lines:
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def _semantic_map(row: dict) -> dict[str, str]:
    return {item["id"]: item["status"] for item in row.get("semantic") or []}


def _semantic_detail(row: dict) -> dict[str, dict]:
    return {item["id"]: item for item in row.get("semantic") or []}


def build_report(rows: list[dict]) -> dict:
    by_fixture: dict[str, dict[str, dict]] = defaultdict(dict)
    for row in rows:
        by_fixture[row["fixture_id"]][row["backend"]] = row

    disagreements: list[dict] = []
    agreements = 0
    comparisons = 0
    confusion: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for fixture_id, backends in sorted(by_fixture.items()):
        sp = backends.get("spacy")
        ol = backends.get("ollama")
        if not sp or not ol:
            continue
        sm = _semantic_map(sp)
        om = _semantic_map(ol)
        sd = _semantic_detail(sp)
        od = _semantic_detail(ol)
        for cid in sorted(set(sm) | set(om)):
            s_status = sm.get(cid, "missing")
            o_status = om.get(cid, "missing")
            comparisons += 1
            confusion[s_status][o_status] += 1
            if s_status == o_status:
                agreements += 1
            else:
                disagreements.append(
                    {
                        "fixture_id": fixture_id,
                        "criterion_id": cid,
                        "gold_tier": sp.get("gold_tier"),
                        "spacy": s_status,
                        "ollama": o_status,
                        "spacy_message": (sd.get(cid) or {}).get("message", ""),
                        "ollama_message": (od.get(cid) or {}).get("message", ""),
                    }
                )

    tier_stats: dict[str, dict] = defaultdict(
        lambda: {"spacy_pass": 0, "ollama_pass": 0, "criteria": 0}
    )
    for fixture_id, backends in by_fixture.items():
        tier = backends.get("spacy", {}).get("gold_tier") or "unknown"
        for backend_name in ("spacy", "ollama"):
            row = backends.get(backend_name)
            if not row:
                continue
            for item in row.get("semantic") or []:
                tier_stats[tier]["criteria"] += 1
                if item.get("status") == "pass":
                    tier_stats[tier][f"{backend_name}_pass"] += 1

    agreement_rate = agreements / comparisons if comparisons else 0.0
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fixture_count": len(by_fixture),
        "criterion_comparisons": comparisons,
        "agreement_rate": agreement_rate,
        "confusion_spacy_vs_ollama": {k: dict(v) for k, v in confusion.items()},
        "disagreements": disagreements,
        "tier_pass_rates": dict(tier_stats),
        "raw_backends": by_fixture,
    }


def format_text(report: dict) -> str:
    lines = [
        f"Benchmark report — agreement {report['agreement_rate']:.1%} "
        f"({report['criterion_comparisons']} criterion pairs)",
        "",
    ]
    lines.append("Confusion (rows=spaCy, cols=Ollama):")
    for s_row, cols in sorted(report.get("confusion_spacy_vs_ollama", {}).items()):
        lines.append(f"  spacy={s_row}: {cols}")
    lines.append("")
    lines.append("Tier pass rates (semantic pass / criteria):")
    for tier, stats in sorted(report.get("tier_pass_rates", {}).items()):
        c = stats.get("criteria") or 1
        sp = stats.get("spacy_pass", 0)
        ol = stats.get("ollama_pass", 0)
        lines.append(f"  {tier}: spacy {sp}/{c}, ollama {ol}/{c}")
    lines.append("")
    if report.get("disagreements"):
        lines.append(f"Disagreements ({len(report['disagreements'])}):")
        for d in report["disagreements"][:25]:
            lines.append(
                f"  {d['fixture_id']} / {d['criterion_id']}: "
                f"spacy={d['spacy']} vs ollama={d['ollama']}"
            )
        if len(report["disagreements"]) > 25:
            lines.append(f"  … and {len(report['disagreements']) - 25} more")
    return "\n".join(lines) + "\n"


def write_calibration(report: dict, backend: str, path: Path) -> None:
    """Write semantic statuses from one backend for spacy-only calibration snapshot."""
    snapshot: dict[str, dict[str, str]] = {}
    for fixture_id, backends in report.get("raw_backends", {}).items():
        row = backends.get(backend)
        if not row:
            continue
        snapshot[fixture_id] = _semantic_map(row)
    path.write_text(
        json.dumps(
            {"backend": backend, "generated_from": report.get("timestamp"), "fixtures": snapshot},
            indent=2,
        ),
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="JSONL file (default stdin)")
    parser.add_argument("--output", type=Path, help="Write full JSON report")
    parser.add_argument("--write-calibration", choices=("spacy", "ollama"))
    parser.add_argument(
        "--calibration-path",
        type=Path,
        help="Output path for calibration file",
    )
    args = parser.parse_args(argv)

    if args.input:
        lines = args.input.read_text(encoding="utf-8").splitlines()
    else:
        lines = sys.stdin.read().splitlines()

    rows = _load_jsonl(lines)
    report = build_report(rows)
    print(format_text(report))

    bench_dir = Path(__file__).resolve().parent
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        out_dir = bench_dir / "reports"
        out_dir.mkdir(parents=True, exist_ok=True)
        ts = report["timestamp"].replace(":", "-")
        default_out = out_dir / f"compare-{ts}.json"
        default_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {default_out}", file=sys.stderr)

    if args.write_calibration:
        cal_path = args.calibration_path or (
            bench_dir / f"calibrated_{args.write_calibration}.json"
        )
        write_calibration(report, args.write_calibration, cal_path)
        print(f"Wrote calibration {cal_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
