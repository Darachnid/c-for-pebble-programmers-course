#!/usr/bin/env bash
# Compare spaCy (main) vs Ollama (assessor/ollama-local) on shared benchmark fixtures.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
BENCHMARK_DIR="${ROOT}/assessor/benchmark"
RUNNER="${BENCHMARK_DIR}/run_fixture.py"
COMPARE="${BENCHMARK_DIR}/compare_report.py"
WORKTREE_BASE="${ROOT}/.assessor/worktrees"
SPACY_WT="${WORKTREE_BASE}/spacy"
OLLAMA_WT="${WORKTREE_BASE}/ollama"
SPACY_REF="${SPACY_REF:-main}"
OLLAMA_REF="${OLLAMA_REF:-assessor/ollama-local}"
FIXTURE_FILTER=""
SKIP_OLLAMA=0
MODEL="${ASSESSOR_OLLAMA_MODEL:-}"

usage() {
  echo "Usage: $0 [--fixtures id1,id2] [--skip-ollama] [--model NAME]" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --fixtures) FIXTURE_FILTER="$2"; shift 2 ;;
    --skip-ollama) SKIP_OLLAMA=1; shift ;;
    --model) MODEL="$2"; shift 2 ;;
    -h|--help) usage ;;
    *) echo "Unknown arg: $1" >&2; usage ;;
  esac
done

if ! git -C "${ROOT}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "error: not a git repository: ${ROOT}" >&2
  exit 1
fi

if [[ ! -f "${RUNNER}" ]]; then
  echo "error: missing ${RUNNER} — checkout assessor/backend-benchmark" >&2
  exit 1
fi

mkdir -p "${WORKTREE_BASE}"

ensure_worktree() {
  local path="$1"
  local ref="$2"
  if [[ -d "${path}/.git" || -f "${path}/.git" ]]; then
    git -C "${path}" fetch origin 2>/dev/null || true
    git -C "${path}" checkout "${ref}" 2>/dev/null || git -C "${path}" pull --ff-only 2>/dev/null || true
  else
    git -C "${ROOT}" worktree add -f "${path}" "${ref}"
  fi
}

ensure_worktree "${SPACY_WT}" "${SPACY_REF}"
if [[ "${SKIP_OLLAMA}" -eq 0 ]]; then
  ensure_worktree "${OLLAMA_WT}" "${OLLAMA_REF}"
fi

sync_spacy() {
  if command -v uv >/dev/null 2>&1; then
    (cd "${SPACY_WT}/assessor" && uv sync --group dev --group model -q)
  else
    echo "warning: uv not found; ensure spacy assessor installed in ${SPACY_WT}" >&2
  fi
}

sync_ollama() {
  if command -v uv >/dev/null 2>&1; then
    (cd "${OLLAMA_WT}/assessor" && uv sync --group dev -q)
  fi
}

sync_spacy
if [[ "${SKIP_OLLAMA}" -eq 0 ]]; then
  sync_ollama
fi

fixture_ids() {
  python3 - <<PY
import json
from pathlib import Path
data = json.loads(Path("${BENCHMARK_DIR}/fixtures.json").read_text())
ids = [f["id"] for f in data["fixtures"]]
filt = "${FIXTURE_FILTER}".strip()
if filt:
    want = set(filt.split(","))
    ids = [i for i in ids if i in want]
for i in ids:
    print(i)
PY
}

run_one() {
  local wt="$1"
  local backend="$2"
  local fixture="$3"
  local -a extra=()
  if [[ "${backend}" == "ollama" && -n "${MODEL}" ]]; then
    extra+=(--model "${MODEL}")
  fi
  if command -v uv >/dev/null 2>&1; then
    (cd "${wt}/assessor" && uv run python "${RUNNER}" \
      --course-root "${wt}" \
      --fixture "${fixture}" \
      --backend "${backend}" \
      "${extra[@]}")
  else
    python3 "${RUNNER}" \
      --course-root "${wt}" \
      --fixture "${fixture}" \
      --backend "${backend}" \
      "${extra[@]}"
  fi
}

JSONL="$(mktemp)"
trap 'rm -f "${JSONL}"' EXIT

while IFS= read -r fid; do
  echo "==> fixture ${fid} (spacy)" >&2
  run_one "${SPACY_WT}" spacy "${fid}" >> "${JSONL}"
  if [[ "${SKIP_OLLAMA}" -eq 0 ]]; then
    echo "==> fixture ${fid} (ollama)" >&2
    run_one "${OLLAMA_WT}" ollama "${fid}" >> "${JSONL}"
  fi
done < <(fixture_ids)

if [[ "${SKIP_OLLAMA}" -eq 1 ]]; then
  echo "Ollama skipped; run compare_report manually on JSONL for spacy-only." >&2
  cat "${JSONL}"
  exit 0
fi

if command -v uv >/dev/null 2>&1; then
  (cd "${ROOT}/assessor" && uv run python "${COMPARE}" --input "${JSONL}")
else
  python3 "${COMPARE}" --input "${JSONL}"
fi
