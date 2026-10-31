# C Programming — source-derived modules

These are the first four proposed modules in competency 4, **C Programming**. They map directly to Chapters 3–6 of Mike Jipping's *Learning C with Pebble* and preserve the source's order and teaching approach, with only the platform changes needed for Pebble Time 2 (Emery) and Pebble SDK 4.33.1.

## A–D progression

| Module | Topic | Source chapter | Main coverage |
|---|---|---:|---|
| [4A — Variables, data types, and operators](4A-variables-data-types-operators.md) | C values and expressions | 3 | Variables, types, literals, conversion, casts, operators, precedence, scope, statements, comments |
| [4B — Conditional execution and decision making](4B-conditionals-decision-making.md) | Branching | 4 | Comparisons, Boolean expressions, short-circuiting, `if`, `else-if`, `switch`, conditional expressions |
| [4C — Loops and iteration](4C-loops-iteration.md) | Repetition | 5 | `while`, `for`, `do/while`, nested loops, `break`, `continue`, infinite loops, structured iteration |
| [4D — Functions and program structure](4D-functions-program-structure.md) | Decomposition and abstraction | 6 | Calls, parameters, signatures, return values, function pointers, scope, recursion, modularity |

## How these relate to the existing course

The original `lessons/4A`, `lessons/4B`, and `lessons/4C` directories are the earlier 21-activity course tasks. They are **not overwritten** here. These files establish the new C-programming content under `curriculum/c-programming/`; the course activity IDs and Taskwarrior structure can be reconciled after the full A–H progression is agreed.

## What was adapted

1. Obsolete hosted-IDE project-import and answer URLs were removed. Exercise descriptions remain, but an exercise is not considered runnable until its complete Emery starter is present locally.
2. The original explanation that Pebble hardware lacked floating-point hardware was replaced for Emery. Pebble Time 2 uses the SiFli SF32LB52 SoC and an Arm STAR-MC1 application core with an FPU.
3. The Pebble Time Round-specific graphics note in Project 6.4 was changed to the Emery 200 × 228 rectangular display.
4. Current build instructions use SDK 4.33.1 and the Pebble CLI. The required `sdkVersion: "3"` manifest value is retained.
5. The text's older description of C Boolean support is accompanied by a short C99 / SDK note. A Pebble-specific note distinguishes `APP_LOG()` diagnostics from user-visible display text.

C-language exposition and examples are otherwise left close to the source. This pass does **not** add the future 4E–4H material, nor does it create the old book's project source code or answer projects.

## Source

Jipping, M. (2016). *Learning C with Pebble*. GitBook. https://pebble.gitbooks.io/learning-c-with-pebble/content/

The book is described as an open-source textbook in the [original Pebble announcement](https://developer.rebble.io/blog/2016/05/11/Learning-C-with-Pebble-The-Book/).

## Current Emery references

- [Pebble SDK installation and version guidance](https://developer.repebble.com/sdk/)
- [Pebble Time 2 (Emery) board information](https://developer.repebble.com/pebbleos/docs/boards/obelix/)
- [Pebble hardware/platform information](https://developer.repebble.com/guides/tools-and-resources/hardware-information/)
- [Pebble C SDK reference](https://developer.repebble.com/docs/c/)
