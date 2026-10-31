from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SubmitBundle:
    activity_id: str
    course_root: Path
    evidence_path: Path
    evidence_text: str
    diff_text: str
    log_oneline: str
    changed_files: list[str] = field(default_factory=list)
    build_log_text: str | None = None

    @property
    def combined_text_for_spacy(self) -> str:
        parts = [self.evidence_text]
        if self.build_log_text:
            parts.append(self.build_log_text)
        return "\n\n".join(parts)


def _run_git(course_root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(course_root), *args],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout


def _pathspecs(paths: list[str]) -> list[str]:
    """Convert glob patterns to git pathspec magic if needed."""
    specs: list[str] = []
    for p in paths:
        if p.endswith("/**"):
            specs.append(p[:-3])
        else:
            specs.append(p)
    return specs


def collect_git_diff(course_root: Path, paths: list[str], baseline: str | None) -> tuple[str, list[str]]:
    specs = _pathspecs(paths)
    if baseline:
        diff = _run_git(course_root, "diff", baseline, "--", *specs)
        name_out = _run_git(course_root, "diff", "--name-only", baseline, "--", *specs)
    else:
        diff = _run_git(course_root, "diff", "HEAD", "--", *specs)
        name_out = _run_git(course_root, "diff", "--name-only", "HEAD", "--", *specs)
        if not diff.strip():
            diff = _run_git(course_root, "diff", "--", *specs)
            name_out = _run_git(course_root, "diff", "--name-only", "--", *specs)
    changed = [line.strip() for line in name_out.splitlines() if line.strip()]
    return diff, changed


def collect_git_log(course_root: Path, paths: list[str], max_count: int = 20) -> str:
    specs = _pathspecs(paths)
    return _run_git(
        course_root,
        "log",
        f"-{max_count}",
        "--oneline",
        "--",
        *specs,
    )


def validate_evidence_sections(text: str, sections: list[str]) -> list[str]:
    missing: list[str] = []
    for section in sections:
        if section not in text:
            missing.append(section)
    return missing


def evidence_path_for(course_root: Path, activity_id: str) -> Path:
    return course_root / "submit" / activity_id / "EVIDENCE.md"


def optional_build_log(course_root: Path, activity_id: str) -> str | None:
    path = course_root / "submit" / activity_id / "build.log"
    if path.is_file():
        return path.read_text(encoding="utf-8", errors="replace")
    return None


def build_bundle(
    course_root: Path,
    activity_id: str,
    paths: list[str],
    evidence_sections: list[str],
    baseline: str | None = None,
) -> SubmitBundle:
    evidence_path = evidence_path_for(course_root, activity_id)
    if not evidence_path.is_file():
        raise SystemExit(
            f"Missing {evidence_path.relative_to(course_root)} — run: assess init {activity_id}"
        )
    evidence_text = evidence_path.read_text(encoding="utf-8")
    missing = validate_evidence_sections(evidence_text, evidence_sections)
    if missing:
        raise SystemExit(
            "EVIDENCE.md is missing required section headings:\n  "
            + "\n  ".join(missing)
            + f"\nRun assess init {activity_id} to regenerate the template."
        )

    try:
        diff_text, changed_files = collect_git_diff(course_root, paths, baseline)
        log_oneline = collect_git_log(course_root, paths)
    except SystemExit as exc:
        if "not a git repository" in str(exc).lower():
            raise SystemExit("Course directory is not a git repository.") from exc
        raise

    return SubmitBundle(
        activity_id=activity_id,
        course_root=course_root,
        evidence_path=evidence_path,
        evidence_text=evidence_text,
        diff_text=diff_text,
        log_oneline=log_oneline,
        changed_files=changed_files,
        build_log_text=optional_build_log(course_root, activity_id),
    )


def render_bundle_preview(bundle: SubmitBundle) -> str:
    lines = [
        f"Activity: {bundle.activity_id}",
        f"Evidence: {bundle.evidence_path.relative_to(bundle.course_root)}",
        f"Changed files ({len(bundle.changed_files)}):",
    ]
    for f in bundle.changed_files[:30]:
        lines.append(f"  {f}")
    if len(bundle.changed_files) > 30:
        lines.append(f"  ... and {len(bundle.changed_files) - 30} more")
    lines.append("")
    lines.append("Recent commits on lesson paths:")
    lines.append(bundle.log_oneline.strip() or "  (none)")
    lines.append("")
    diff_lines = bundle.diff_text.splitlines()
    lines.append(f"Diff ({len(diff_lines)} lines, truncated to 80):")
    lines.extend(diff_lines[:80])
    if len(diff_lines) > 80:
        lines.append("...")
    return "\n".join(lines)


def count_textlayer_create_in_diff(diff_text: str) -> int:
    """Heuristic: count TextLayer create calls added in diff (+ lines)."""
    count = 0
    for line in diff_text.splitlines():
        if not line.startswith("+"):
            continue
        if line.startswith("+++"):
            continue
        if re.search(r"text_layer_create\s*\(", line, re.I):
            count += 1
    return count
