# C for Pebble Programmers Course

A 21-activity, self-directed **Pebble Time 2 (Emery-only)** C programming course organized by seven core skills and real prerequisites.

## Start here

- [Full syllabus — all 21 activities](SYLLABUS.md) ([PDF edition](SYLLABUS.pdf))
- [All 21 individual lesson folders](lessons/README.md) — three clean starters plus three deliberately flawed debugging projects
- [Taskwarrior importer](taskwarrior/README.md) — 21 tasks with estimates, effort, priorities, dependencies, and detailed repository-linked annotations

## Build any included project

```sh
cd examples/time-only
pebble build
pebble install --emulator emery
```

The debug-6a source is **intentionally unbuildable** until you locate the syntax error. Debug-6b and debug-6c compile but contain deliberate defects; their READMEs explain how to collect the provided diagnostic evidence without giving away a solution.

**No AI during the learning exercises.** The source and challenges are scaffolding, not solutions to student deliverables. Keep your experiments in a separate copy or branch. All course starting examples are locally authored and targeted at `emery`.

The course has no calendar deadline; estimated workload is **19 h 15 m** of focused work.

## Per-lesson source folders

Every lesson has a local complete starter under [lessons/](lessons/), including official MIT-licensed SDK source excerpts where redistribution is authorized. For example, see [7A](lessons/7A/), [1B](lessons/1B/), [6B](lessons/6B/) or [7C](lessons/7C/). No external example clone is required while completing an exercise.

## C programming reading modules

The new proposed **4A–4D** C-language progression is being developed separately from the original 21-activity task IDs, so existing lessons are preserved for now.

- [C Programming module index](curriculum/c-programming/README.md)
- [4A — Variables, data types, and operators](curriculum/c-programming/4A-variables-data-types-operators.md)
- [4B — Conditional execution and decision making](curriculum/c-programming/4B-conditionals-decision-making.md)
- [4C — Loops and iteration](curriculum/c-programming/4C-loops-iteration.md)
- [4D — Functions and program structure](curriculum/c-programming/4D-functions-program-structure.md)

These are adapted from Mike Jipping's *Learning C with Pebble*, with the minimum SDK 4.33.1 / Emery changes documented in the module index. Legacy hosted-IDE project links are removed; the associated project starters still need to be made local before those exercises are assigned.
