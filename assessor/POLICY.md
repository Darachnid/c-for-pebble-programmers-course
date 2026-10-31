# Assessor policy

## Purpose

The `assess` CLI is a **post-submit self-check** for evidence you already produced. It helps you compare your work to course completion criteria and to **meets** vs **below** exemplars.

## When to use it

- Run **`assess submit`** only **after** you finish an activity.
- Do **not** use it while you are still coding, debugging, or reading exercises.

## What it is not

- Not a tutor, hint engine, or code generator during exercises.
- Not a substitute for the syllabus **independent-work** rule (no AI during activities).
- Not connected to Taskwarrior: it does **not** mark tasks `done`.
- Exemplars show **evidence shape**, not answers to copy.

## Technology (Ollama branch)

v1 on this branch uses:

1. **Deterministic checks** (Git paths, regex, light diff heuristics).
2. **Local Ollama** (default model `llama3.2`, override with `--model` or `ASSESSOR_OLLAMA_MODEL`) to map your evidence and diff excerpts to rubric criteria, calibrated by meets/below exemplars in the prompt.

The model runs on **your machine** only; nothing is uploaded to a cloud grader.

## Privacy

Reports are written under `.assessor/reports/` in your clone (gitignored by default).
