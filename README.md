# C for Pebble Programmers

Learn C by completing guided Pebble exercises on **Pebble Time 2 (Emery)** and **Pebble Round 2 (Gabbro)**.

## Start the exercise wizard

From your local copy of the repository, install the wizard requirements once:

```bash
# On Manjaro/Arch, install tmux and uv if needed.
sudo pacman -S tmux uv
cd assessor
uv sync --group dev --group model
uv run python -m spacy download en_core_web_md
cd ..
```

Then launch the course:

```bash
./scripts/course
```

The wizard opens a three-pane terminal session:

- **Top left — Lesson:** read the current exercise and its completion requirements.
- **Top right — Workspace:** edit the included project, run `pebble build`, and test on the emulator. The wizard does **not** build or write your solution for you.
- **Bottom — Guide:** follow the prompts, describe what you did and tested, and submit evidence. The wizard checks your work and moves to the next eligible exercise after it passes.

Use **Ctrl-b**, then an arrow key, to switch panes. Use **Ctrl-b**, then **d**, to detach. Run `./scripts/course` again to resume.

Your evidence is saved in `submit/<ID>/EVIDENCE.md`; completed exercises are tracked in `.course/progress.json`. Both are local and gitignored. You can correct an unsuccessful submission and try again.

**Wizard coverage:** all **41 activities (1A–41A)**. Lessons 1A–5A have automated assessment; lessons 6A–41A guide evidence collection and require learner-confirmed completion rather than automated grading. [Lesson directory](lessons/README.md).

For setup details or troubleshooting, see the [wizard guide](COURSE-TERMINAL.md). For the complete curriculum, see the [syllabus](SYLLABUS.md).
