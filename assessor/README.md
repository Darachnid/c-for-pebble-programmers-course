# Course evidence assessor (pilot)

Student-local, post-submit checker for Phase I activities **1A–5A** (spaCy pilot). See [POLICY.md](POLICY.md).

## Install

From the course repository root:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ./assessor
python -m spacy download en_core_web_md
```

With [uv](https://docs.astral.sh/uv/) (recommended on some Linux setups):

```bash
cd assessor && uv sync --group dev --group model
uv run python -m spacy download en_core_web_md   # once, inside assessor/
```

Run **`assess` from the course repository root** (the folder that contains `lessons/` and `assessor/`). `--directory assessor` is relative to your shell cwd — if you are elsewhere, uv fails with `No such file or directory`.

```bash
cd ~/PebbleWatch/c-for-pebble-programmers-course
uv run --directory assessor assess init 2A
# or from anywhere in the clone:
./scripts/assess init 2A
```

If your shell is already in `assessor/`, use:

```bash
uv run python -m assessor.cli init 2A
uv run python -m assessor.cli submit 2A
```

**Do not** use `uv run --active` while the broken course-root `.venv` is activated (Cursor-as-`python`); run `deactivate` and `rm -rf ../.venv` if you created that venv from the IDE terminal.

Avoid bare `uv run assess` if you see `Failed to spawn: assess` — the module form above always works.

## Quick workflow

**Terminal course driver (recommended):** see [COURSE-TERMINAL.md](../COURSE-TERMINAL.md).

```bash
./scripts/course
```

**Manual assess only:**

```bash
assess init 2A
# … complete the lesson, commit changes under lesson paths …
# … fill submit/<ID>/EVIDENCE.md …
assess diff 2A          # preview git capture
assess examples 2A      # meets vs below exemplars
assess submit 2A        # exit 1 if any criterion fails
```

Optional: save `submit/2A/build.log` for stronger build evidence.

## Commands

| Command | Description |
|---------|-------------|
| `assess init <ID>` | Create `submit/<ID>/EVIDENCE.md` from template |
| `assess diff <ID>` | Show paths, commits, truncated diff (no scoring) |
| `assess examples <ID>` | List `examples/<ID>/meets` and `below` folders |
| `assess wizard <ID>` | Deprecated — use `./scripts/course` |
| `assess submit <ID>` | Run rubric; save JSON under `.assessor/reports/` |

`--baseline <git-ref>` on `diff` and `submit` compares against a ref instead of the working tree.

## Maintainer note

[`scripts/check_course.py`](../scripts/check_course.py) still validates a 26-activity Taskwarrior import; syllabus lists 40 activities. Reconciling that metadata is separate from this pilot.

## Tests

**Full smoke** (pytest + exemplar CLI checks):

```bash
bash assessor/scripts/smoke.sh
```

With `uv`, the script runs `uv sync --group dev --group model` inside `assessor/` first.

**Unit tests only:**

```bash
pip install -e "./assessor[dev]"
pytest assessor/tests
```

spaCy tests skip without `en_core_web_md` (`pytest assessor/tests -m "not spacy"` for deterministic-only).

Rigorous spaCy limit tests (margins, phrase gates, known ambiguous exemplars):

```bash
cd assessor && uv sync --group dev --group model && uv run pytest tests/test_spacy_boundaries.py -v
```

## Dual-platform scope of this pilot

The post-submit assessor pilot (Phase I **1A–5A**) began with Emery-focused evidence checks. **A passing assessor report is not a certification of Gabbro compilation, circular layout, touch handling or real hardware behavior.** Keep additional Time 2 and Round 2 evidence in the same EVIDENCE.md or attached logs, and check both platforms manually against the [course's dual-platform acceptance guidance](../curriculum/dual-platform/README.md). Do not submit during exercises or allow automated assessment to generate source solutions.

## Backend comparison (maintainers)

**Compare spaCy vs Ollama** on the shared fixture corpus: see [BENCHMARK.md](BENCHMARK.md) and `bash assessor/scripts/compare_backends.sh` from the repo root.
