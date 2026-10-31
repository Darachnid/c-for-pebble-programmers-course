#!/usr/bin/env bash
# Full assessor test: pytest + CLI exemplar smoke (run from anywhere in the course clone).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSESSOR_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ROOT="$(cd "${ASSESSOR_DIR}/.." && pwd)"

if ! git -C "${ROOT}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "error: ${ROOT} is not a git repository" >&2
  exit 1
fi

cd "${ASSESSOR_DIR}"

if command -v uv >/dev/null 2>&1; then
  uv sync --group dev --group model
  PYTEST=(uv run pytest)
  SMOKE=(uv run python scripts/run_smoke.py)
else
  python3 -m pip install -q -e ".[dev]" 2>/dev/null || python3 -m pip install -q -e .
  if ! python3 -c "import spacy; spacy.load('en_core_web_md')" 2>/dev/null; then
    python3 -m spacy download en_core_web_md
  fi
  PYTEST=(python3 -m pytest)
  SMOKE=(python3 scripts/run_smoke.py)
fi

echo "==> pytest (assessor/tests)"
"${PYTEST[@]}" tests -v

echo "==> CLI smoke (exemplar meets / below)"
"${SMOKE[@]}"

echo "==> assessor smoke: OK"
