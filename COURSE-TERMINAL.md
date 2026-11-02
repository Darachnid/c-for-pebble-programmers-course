# Terminal course driver (Phase I)

One command is the whole course. It opens a tmux session and stays there through **1A–5A**: progress, the lesson, a Pebble shell, and the evidence wizard. **No Taskwarrior, no file manager, no `status` or `go` subcommands.**

```bash
./scripts/course
```

tmux is required (`pacman -S tmux` on Arch).

## Setup (once)

```bash
cd ~/PebbleWatch/c-for-pebble-programmers-course   # your clone path
cd assessor && uv sync --group dev --group model
uv run python -m spacy download en_core_web_md
```

Optional: `export PEBBLE_COURSE_ROOT=/path/to/course` if auto-discovery fails.

## Panes

| Pane | What it shows |
|------|----------------|
| Top-left | `less` on the current lesson README (`q` quits `less`; the pane stays) |
| Top-right | Shell already in that lesson's project directory, with `pebble build` and `pebble install --emulator emery` printed. The driver does not run them. |
| Bottom | Progress, the evidence prompts, and the spaCy check. On a pass it loads the next activity into the other panes. |

Move between panes with `Ctrl-b` then an arrow key. Detach with `Ctrl-b` then `d`. Running `./scripts/course` again reattaches the same `pebble-course` session.

The tmux status line shows the current activity id and title.

## What the wizard records

1. You type only your own notes (ideas, observations, API write-up).
2. Paths and build hints are filled in automatically.
3. Evidence is written to `submit/<ID>/EVIDENCE.md` (gitignored).
4. A passing check is stored in `.course/progress.json` (gitignored) and the next activity starts in the same session.

## What you still do yourself

- Run the printed Pebble commands in the top-right pane.
- Write original exercise answers (no AI during activities, per syllabus).
- Leave any personal task list alone — the driver does not sync Taskwarrior.

## Maintainers

- `uv run --directory assessor python -m assessor.cli submit 1A` — submit one activity without the session
- [taskwarrior/README.md](taskwarrior/README.md) — optional 41-task import
