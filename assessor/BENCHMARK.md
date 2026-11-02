# SpaCy vs Ollama backend benchmark

Compare semantic scoring on the **same fixture corpus** without merging backends into one binary.

## Prerequisites

- Course clone on branch `assessor/backend-benchmark` (harness) or `main` after merge
- [git worktree](https://git-scm.com/docs/git-worktree)
- [uv](https://docs.astral.sh/uv/)
- **spaCy path:** `uv sync --group dev --group model` in `assessor/` on `main`
- **Ollama path:** [Ollama](https://ollama.com/) running locally, e.g. `ollama pull llama3.2`

## One-command compare

From the **course repository root** (harness checkout):

```bash
bash assessor/scripts/compare_backends.sh
```

Options:

| Flag | Meaning |
|------|---------|
| `--fixtures 7A_meets_01,7A_below_01` | Subset of fixture ids |
| `--skip-ollama` | spaCy worktree only (JSONL to stdout) |
| `--model mistral` | Override `ASSESSOR_OLLAMA_MODEL` |

Worktrees are created under `.assessor/worktrees/spacy` (`main`) and `.assessor/worktrees/ollama` (`assessor/ollama-local`).

Reports: `assessor/benchmark/reports/compare-<timestamp>.json` (gitignored).

## Fixture corpus

Defined in [`benchmark/fixtures.json`](benchmark/fixtures.json):

- 8 shipped exemplars (`7A_meets_01` … `4A_below_02`)
- 3 synthetics (`7A_keyword_stuff`, `7A_missing_emery`, `7A_empty`)

Each fixture can override `diff_text` / `changed_files` so semantic layers are tested without relying on real git state.

## Reading the report

- **Agreement rate** — share of criterion pairs where spaCy and Ollama assign the same `pass` / `fail` / `uncertain`
- **Confusion table** — rows = spaCy status, columns = Ollama status
- **Disagreements** — fixture id, criterion id, both messages (manual review list)
- **Tier pass rates** — for `gold_tier=meets|below|synthetic`, how often each backend semantic-passes

## Calibrations

| File | Backend | Use |
|------|---------|-----|
| [`calibrated_spacy.json`](benchmark/calibrated_spacy.json) | spaCy | Locked by `test_benchmark_fixtures_spacy.py` |
| [`calibrated_ollama.json`](benchmark/calibrated_ollama.json) | Ollama | Optional; model-specific, regenerate after compare |

Regenerate spaCy calibration (spaCy checkout):

```bash
cd assessor
JSONL=$(mktemp)
for fid in $(python3 -c "import json; print(' '.join(f['id'] for f in json.load(open('benchmark/fixtures.json'))['fixtures']))"); do
  uv run python benchmark/run_fixture.py --course-root .. --fixture "$fid" --backend spacy >> "$JSONL"
done
uv run python benchmark/compare_report.py --input "$JSONL" --write-calibration spacy \
  --calibration-path benchmark/calibrated_spacy.json
```

Regenerate Ollama calibration after a full compare with Ollama running:

```bash
bash assessor/scripts/compare_backends.sh
# Then extract ollama statuses from latest report or add --write-calibration ollama to compare_report when both backends present
```

## Sample calibration run

With `llama3.2:3b` (local Ollama), a full 11-fixture compare yielded **~30% criterion agreement** — Ollama tended to **pass** more below-tier fixtures than spaCy (see [`calibrated_ollama.json`](benchmark/calibrated_ollama.json) meta). Treat LLM scores as model-specific; re-run compare after changing model.

## Known divergences (spaCy limits vs LLM)

Documented from spaCy rigorous tests and benchmark compare:

| Case | spaCy typical | Ollama typical |
|------|---------------|----------------|
| 7A vague below | All criteria **fail** (margin + phrases) | Most criteria **fail** (live test) |
| 7A date-layer below | **uncertain** margin; `time_only_face` **fail** (phrases) | May **fail** on criterion text (adds date layer) |
| 4A parrots below | **uncertain** (margin ≈ 0) | Often **fail** (judges parroting) |
| 4A meets/01 | `c_feature_and_diff` **fail** (missing word “variable”) | May **pass** (semantic reading) |
| 4A meets/02 | All **uncertain** (margin &lt; 0.04) | Model-dependent |
| Keyword stuffing | No **pass** on semantic layer | Model-dependent; do not rely on LLM alone |

Deterministic checks (git paths, regex) are identical on both branches.

## Tests

```bash
# spaCy calibration lock (needs en_core_web_md)
cd assessor && uv sync --group dev --group model
uv run pytest tests/test_spacy_boundaries.py tests/test_benchmark_fixtures_spacy.py -v

# Ollama branch (mocked, CI-safe)
uv run pytest tests/test_llm_boundaries.py -m "not ollama_live" -v

# Compare report unit tests (any branch with harness)
uv run pytest tests/test_compare_report.py -v
```
