# Development Tools and Workflow — read alongside 2A, 7B and 31C

**Goal:** build repeatable, recoverable software work. A working watch app is not sufficient if you cannot reconstruct how it was built, what changed, and how you verified it.

## 2A · Build and observe one known program

[Local time-only watchface](../../lessons/2A/)

**Read first.** A Pebble C project normally includes `package.json` (target/configuration), `wscript` (build instructions), and `src/c/main.c` (entry point and callbacks). The project root is the folder that contains `package.json`; run `pebble build` there rather than one level above or inside `src/c`. For this course the only target is `emery`; SDK version 4.33.1 is assumed.

**Practice:** build with `pebble build`; install with `pebble install --emulator emery`; check live output and `pebble logs --emulator emery`. Check the package target, identify the main C file, and explain the difference between editing source, building an app bundle and running the result. Repeat after a clean change to confirm it is reproducible.

**Evidence:** build command/output, emulator observation, file map, and an explanation of what the build does *not* prove.

## 7B · Keep work reversible with Git

[Local one-layer watchface](../../lessons/7B/)

**Read first.** Git records snapshots, while GitHub hosts and reviews them. A **repository** contains project history; a **branch** is a safe line of development; a **commit** is a labeled snapshot; a **diff** shows changed lines; a **pull request** proposes merging a branch. A commit is local until pushed to GitHub. You need not push to earn the lesson's Git evidence.

**Practice:** follow the full [beginner contribution guide](../../CONTRIBUTING.md) for vocabulary and safety. For your lesson, start in your **own copy**, create a baseline commit, change one visual property, build/test, inspect `git diff`, and commit the verified result. Use `git status` before each commit to avoid including generated bundles or unrelated files. Demonstrate `git log --oneline` and `git show` to recover context; if reverting, make a new branch or use a safe restore operation on disposable work, not `reset --hard` on valuable changes.

**Evidence:** two commits with meaningful messages, a build test, and a comparison of the snapshots.

## 31C · Integrate two separate programs

[Local font selector and persistent counter](../../lessons/31C/)

**Read first.** Combining programs involves more than copying functions. Inventory each program's state, startup, event subscriptions, UI elements and cleanup. The integration must decide which single component owns the selected font index; when it is loaded; what writes it; and how invalid saved data is handled. Work incrementally, with a successful Emery build after each meaningful checkpoint.

**Practice:** make an integration checklist with: baseline font selector works; saved data researched; startup fallback designed; save action added; restart verified; invalid state verified; new code reviewed. Create small commits for each passing checkpoint. Do not start by copying the intentionally defective 32C sample.

**Evidence:** code history, test results for first run and restart, explanation of state ownership, and a short integration retrospective.

## Core command reference

```sh
# Run from an actual Pebble project directory, e.g. lessons/2A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery

# Run Git commands in your own working repository
git status
git diff
git add path/to/changed-file
git commit -m "Describe the change and why"
git log --oneline -5
```

**Common errors:** wrong working directory; editing the starter instead of a copy; accidentally staging `build/`; ignoring compile warnings; assuming tests pass just because Git accepts the commit; forgetting to check first-launch behavior. Use the [syllabus](../../SYLLABUS.md) for assessment and [CONTRIBUTING.md](../../CONTRIBUTING.md) for publishing to GitHub.
