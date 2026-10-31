# Course evidence assessor (pilot)

Student-local, post-submit checker for **7A** and **4A**. See [POLICY.md](POLICY.md).

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
uv run assess init 7A   # from course root: uv run --directory assessor assess …
```

## Quick workflow

```bash
assess init 7A
# … complete the lesson, commit changes under lessons/7A/ …
# … fill submit/7A/EVIDENCE.md …
assess diff 7A          # preview git capture
assess examples 7A      # meets vs below exemplars
assess submit 7A        # exit 1 if any criterion fails
```

Optional: save `submit/7A/build.log` for stronger build evidence.

## Commands

| Command | Description |
|---------|-------------|
| `assess init <ID>` | Create `submit/<ID>/EVIDENCE.md` from template |
| `assess diff <ID>` | Show paths, commits, truncated diff (no scoring) |
| `assess examples <ID>` | List `examples/<ID>/meets` and `below` folders |
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
