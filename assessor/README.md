# Course evidence assessor (pilot, Ollama)

Student-local, post-submit checker for **7A** and **4A**. See [POLICY.md](POLICY.md).

## Prerequisites

- [Ollama](https://ollama.com/) running locally
- A pulled model (default **`llama3.2`**):

```bash
ollama serve   # if not already running
ollama pull llama3.2
```

Environment (optional):

| Variable | Default |
|----------|---------|
| `OLLAMA_HOST` | `http://127.0.0.1:11434` |
| `ASSESSOR_OLLAMA_MODEL` | `llama3.2` |
| `ASSESSOR_OLLAMA_TIMEOUT` | `120` (seconds) |

## Install

From the course repository root:

```bash
pip install -e ./assessor
```

With [uv](https://docs.astral.sh/uv/):

```bash
cd assessor && uv sync --group dev
uv run assess init 7A   # from course root: uv run --directory assessor assess …
```

## Quick workflow

```bash
assess init 7A
# … complete the lesson, commit changes under lessons/7A/ …
# … fill submit/7A/EVIDENCE.md …
assess diff 7A
assess examples 7A
assess submit 7A
# or: assess submit 7A --model mistral
```

Optional: `submit/7A/build.log` for build excerpts in the LLM prompt.

## Commands

| Command | Description |
|---------|-------------|
| `assess init <ID>` | Create `submit/<ID>/EVIDENCE.md` from template |
| `assess diff <ID>` | Preview git capture (no scoring) |
| `assess examples <ID>` | List meets vs below exemplar folders |
| `assess submit <ID>` | Deterministic gates + **Ollama** rubric pass |

`--baseline <git-ref>`, `--model`, `--ollama-url`, `--json` on submit.

## Tests

```bash
bash assessor/scripts/smoke.sh
```

- **pytest** always (includes mocked Ollama unit test).
- **CLI exemplar submit** runs only if Ollama responds at `OLLAMA_HOST`.

```bash
cd assessor && uv sync --group dev && uv run pytest tests -v
```

## Maintainer note

[`scripts/check_course.py`](../scripts/check_course.py) Taskwarrior activity count may differ from the syllabus; unrelated to this pilot.
