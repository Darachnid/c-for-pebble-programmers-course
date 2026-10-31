#!/usr/bin/env bash
# Assessor test: pytest (always) + CLI smoke when Ollama is reachable.
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
  uv sync --group dev
  PYTEST=(uv run pytest)
  SMOKE=(uv run python scripts/run_smoke.py)
else
  python3 -m pip install -q -e ".[dev]"
  PYTEST=(python3 -m pytest)
  SMOKE=(python3 scripts/run_smoke.py)
fi

echo "==> pytest (assessor/tests, no live Ollama required)"
"${PYTEST[@]}" tests -v -m "not ollama"

echo "==> CLI smoke"
OLLAMA_BASE="${OLLAMA_HOST:-http://127.0.0.1:11434}"
MODEL="${ASSESSOR_OLLAMA_MODEL:-llama3.2}"
TAGS="$(curl -sf "${OLLAMA_BASE}/api/tags" 2>/dev/null || true)"
if [ -n "${TAGS}" ] && echo "${TAGS}" | grep -q "\"name\":\"${MODEL}\""; then
  "${SMOKE[@]}"
else
  echo "    Skipping exemplar submit checks (need Ollama at ${OLLAMA_BASE} with model ${MODEL}; ollama pull ${MODEL})"
  "${SMOKE[@]}" --skip-submit
fi

echo "==> assessor smoke: OK"
