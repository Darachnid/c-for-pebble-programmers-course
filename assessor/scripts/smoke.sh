#!/usr/bin/env bash
# Full assessor test: pytest + optional CLI exemplar smoke (Ollama).
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
  uv sync --group dev -q
  PYTEST=(uv run pytest)
  SMOKE=(uv run python scripts/run_smoke.py)
else
  python3 -m pip install -q -e ".[dev]" 2>/dev/null || python3 -m pip install -q -e .
  PYTEST=(python3 -m pytest)
  SMOKE=(python3 scripts/run_smoke.py)
fi

echo "==> pytest (assessor/tests, excluding live Ollama)"
"${PYTEST[@]}" tests -m "not ollama_live" -v

echo "==> CLI smoke"
if "${SMOKE[@]}" --skip-submit; then
  :
else
  echo "examples smoke failed" >&2
  exit 1
fi

if command -v ollama >/dev/null 2>&1; then
  if curl -sf http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
    echo "==> CLI smoke (Ollama submit checks)"
    "${SMOKE[@]}"
  else
    echo "==> Ollama not running; submit checks skipped"
  fi
else
  echo "==> ollama CLI not installed; submit checks skipped"
fi

echo "==> assessor smoke: OK"
