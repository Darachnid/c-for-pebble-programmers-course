# C for Pebble Programmers Course

A self-directed, **41-activity**, **Emery + Gabbro** C programming course: seven developer competencies and an eight-module C track (3A–24H), with real dependency links and evidence-based completion.

**Estimated focused time:** 52h 35m. No prescribed calendar deadlines.

## Start here

- [Complete syllabus](SYLLABUS.md) ([up-to-date PDF syllabus](SYLLABUS.pdf))
- [All 41 lesson folders and local examples](lessons/README.md)
- [Learning materials for all seven competencies and the API labs](curriculum/README.md) (including [C modules](curriculum/c-programming/README.md))
- [Taskwarrior importer](taskwarrior/README.md)
- [Optional post-submit evidence assessor](assessor/README.md) (pilot: **2A**, **3A**; run only after you finish an activity)

## Examples and assignments

Every lesson begins from source included in this repository. All local C projects target **both** `emery` and `gabbro`. The original C textbook exercises in Chapters 3–6 have **eleven working-intended, Emery/Gabbro-targeted starter projects** with TODOs (not finished solutions). For example:

```sh
cd lessons/3A/projects/project-3-2
pebble build
pebble install --emulator emery
pebble install --emulator gabbro
```

17E–24H additionally include complete base watchapps under `lessons/<ID>/starter`. The watchapps are deliberately simple so you can investigate and extend them yourself.

The developer skills remain UI Design, Idea Generation, Algorithmic Thinking, C Programming, Resource Literacy, Debugging and Testing, and Development Tools and Workflow.

**No AI-generated solutions during exercises.** Use the included source, SDK docs, compiler messages, emulator and Git; preserve evidence of your own work.

**Build verification:** Manifests target both Emery and Gabbro and key starters include shape-aware layouts. Actual SDK compilation, emulator runs and physical hardware tests remain to be performed on a configured machine.

## New: recurring Pebble API projects

Fourteen new [capability labs](curriculum/pebble-api/README.md) build progressively on **three Emery/Gabbro watchapps**: Clock Workshop (windows/buttons/timers/persistence), Field Instrument (accelerometer/compass/backlight/vibration), and Pocket Field Guide (menus/drawing/paths/bitmaps/resources/phone messages). Consult the [chapter coverage matrix](curriculum/pebble-api/capability-matrix.md). Every activity includes its own local starter project.

**Syllabus editions:** Both Markdown and PDF have been updated for the dual-platform 41-activity course; Markdown remains the editable source of truth.

## How to contribute

**No Git experience needed.** To suggest a documentation edit: (1) sign in to GitHub; (2) click **Fork** on this repository to make your own copy; (3) open the file in your fork and click the pencil icon; (4) **Commit changes** on a new branch; (5) click **Contribute → Open pull request** and explain the change. A pull request is a proposal: it does not directly overwrite the course. Report testing and preserve the intentional faults in debugging lessons.

For C or larger changes, clone your fork, make a named branch, build and install the local example on both `emery` and `gabbro`, commit and push the change, then open a pull request. The **[complete beginner guide](CONTRIBUTING.md)** explains every Git term, browser click and terminal command.

## License options (not yet selected)

There is **no root `LICENSE` file** yet, so the repository's original material is **not automatically open-source licensed** just because it is public. Here are possible licenses for **new material owned by the course contributors**:

| Material | Candidate | Tradeoff |
|---|---|---|
| Original C/examples | **MIT (recommended)** | Short, permissive, widely compatible with bundled Pebble MIT source; preserve notices. |
| Original C/examples | **Apache-2.0** | Permissive plus explicit patent-grant terms and notice requirements. |
| Original C/examples | **GPL-3.0-or-later** | Copyleft for redistributed derivative programs; review compatibility/obligations. |
| Original educational writing | **CC BY 4.0 (recommended)** | Allows adaptations with attribution and license conditions. |
| Original educational writing | **CC BY-SA 4.0** | Requires adapted material to remain under a compatible share-alike license. |

**Rights warning:** Bundled Pebble examples have their *own* MIT notices (for example `lessons/25C/starter/LICENSE`). The 3A–10D readings contain substantial source-derived passages from *Learning C with Pebble*. Verify their copyright and redistribution permissions **before** applying a blanket license or claiming that all course material is freely reusable. A new repository license cannot grant rights to third-party text, code or artwork. Creative Commons licenses are for the original instructional text here, **not** for the C code.

This is a **proposal**, not a license grant. See [GitHub's licensing explanation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) and [Choose a License](https://choosealicense.com/).

## Syllabus formats

[SYLLABUS.md](SYLLABUS.md) is the up-to-date authoritative syllabus. [SYLLABUS.pdf](SYLLABUS.pdf) has been regenerated for the 41-activity syllabus, including the recent assessor note. The Markdown version remains the authoritative editable edition, with local links to full companion readings.

## Pedagogical redesign

All **seven competencies** now have explicit outcomes and evidence criteria; 40 preparatory activities assign a primary and supporting competence, with five primary tasks per non-C competence and ten for C. New [41-activity integrated sequence](curriculum/course-design/integrated-sequence.md) interleaves the original programming exercises and three evolving SDK projects. A required [original-app capstone (41A)](lessons/41A/) assesses all seven. [Read the four-level mastery rubric](curriculum/course-design/learning-outcomes-and-assessment.md).

**Source validation:** Emery manifests and paths have been checked; SDK compilation, emulator execution and physical hardware confirmation remain unverified.

## Ordered lesson IDs (1–41)

The numeric part now gives the **recommended position** of every lesson, while its original letter suffix remains unchanged. For example, **10D precedes 11A**, and **30G precedes 31C**. This is not an alphabetical A-before-B ordering. [Browse the numbered lesson index](lessons/README.md) and [old-to-new migration map](taskwarrior/legacy-id-map.json).

Existing Taskwarrior records are migrated by UUID when you rerun the importer, with a local JSON backup and no loss of completed status or personal notes. Review [migration instructions](taskwarrior/RENUMBERING.md) before importing.

## Pebble Round 2 / Gabbro support

The same 41-lesson curriculum now covers **Pebble Time 2 (Emery, 200×228 rectangle) and Pebble Round 2 (Gabbro, 260×260 circle)**. All included project manifests advertise both platforms, and the recurring starter applications use circular-safe content areas. The three projects and seven competencies remain unchanged. Study [two-platform layout, testing, touch and sensor differences](curriculum/dual-platform/README.md) before running C exercises on Gabbro. Check **both** emulators; Round 2's 260×260 resolution is not a full rectangular content area. [Static audit](scripts/check_dual_platform.py) · [one-project build/install smoke test](scripts/test_dual_platform.sh).
