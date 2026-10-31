# Assessor policy

## Purpose

The `assess` CLI is a **post-submit self-check** for evidence you already produced. It helps you compare your work to course completion criteria and to **meets** vs **below** exemplars.

## When to use it

- Run **`assess submit`** only **after** you finish an activity.
- Do **not** use it while you are still coding, debugging, or reading exercises.

## What it is not

- Not a tutor, hint engine, or code generator.
- Not a substitute for the syllabus **independent-work** rule (no AI during activities).
- Not connected to Taskwarrior: it does **not** mark tasks `done`.
- Exemplars show **evidence shape**, not answers to copy.

## Technology

v1 uses **deterministic checks** (Git paths, patterns) and **spaCy** similarity to authored exemplars. It does **not** call generative LLMs.

## Privacy

Reports are written under `.assessor/reports/` in your clone (gitignored by default). Nothing is uploaded.

## Dual-platform scope of this pilot

The existing post-submit assessor pilots (2A and 3A) began with Emery-focused evidence checks. **A passing assessor report is not a certification of Gabbro compilation, circular layout, touch handling or real hardware behavior.** Keep additional Time 2 and Round 2 evidence in the same EVIDENCE.md or attached logs, and check both platforms manually against the [course's dual-platform acceptance guidance](../curriculum/dual-platform/README.md). Do not submit during exercises or allow automated assessment to generate source solutions.
