# C for Pebble Programmers Course

A self-directed, **41-activity**, **Emery-only** C programming course: seven developer competencies and an eight-module C track (4A–4H), with real dependency links and evidence-based completion.

**Estimated focused time:** 52h 35m. No prescribed calendar deadlines.

## Start here

- [Complete syllabus](SYLLABUS.md) ([PDF snapshot](SYLLABUS.pdf); Markdown contains the newest companion-reading links)
- [All 41 lesson folders and local examples](lessons/README.md)
- [Learning materials for all seven competencies and the API labs](curriculum/README.md) (including [C modules](curriculum/c-programming/README.md))
- [Taskwarrior importer](taskwarrior/README.md)
- [Optional post-submit evidence assessor](assessor/README.md) (pilot: **7A**, **4A**; run only after you finish an activity)

## Examples and assignments

Every lesson begins from source included in this repository. The original C textbook exercises in Chapters 3–6 have **eleven working-intended, Emery-targeted starter projects** with TODOs (not finished solutions). For example:

```sh
cd lessons/4A/projects/project-3-2
pebble build
pebble install --emulator emery
```

4E–4H additionally include complete base watchapps under `lessons/<ID>/starter`. The watchapps are deliberately simple so you can investigate and extend them yourself.

The developer skills remain UI Design, Idea Generation, Algorithmic Thinking, C Programming, Resource Literacy, Debugging and Testing, and Development Tools and Workflow.

**No AI-generated solutions during exercises.** Use the included source, SDK docs, compiler messages, emulator and Git; preserve evidence of your own work.

**Build verification:** Source and manifests have been checked for Emery; compilation on the Pebble SDK remains to be performed on a configured development machine.

## New: recurring Pebble API projects

Fourteen new [capability labs](curriculum/pebble-api/README.md) build progressively on **three Emery watchapps**: Clock Workshop (windows/buttons/timers/persistence), Field Instrument (accelerometer/compass/backlight/vibration), and Pocket Field Guide (menus/drawing/paths/bitmaps/resources/phone messages). Consult the [chapter coverage matrix](curriculum/pebble-api/capability-matrix.md). Every activity includes its own local starter project.

**Syllabus editions:** Both files cover the 41 activities. The Markdown now also includes companion-reading links introduced after the latest PDF generation.

## How to contribute

**No Git experience needed.** To suggest a documentation edit: (1) sign in to GitHub; (2) click **Fork** on this repository to make your own copy; (3) open the file in your fork and click the pencil icon; (4) **Commit changes** on a new branch; (5) click **Contribute → Open pull request** and explain the change. A pull request is a proposal: it does not directly overwrite the course. Report testing and preserve the intentional faults in debugging lessons.

For C or larger changes, clone your fork, make a named branch, build and install the local example on `emery`, commit and push the change, then open a pull request. The **[complete beginner guide](CONTRIBUTING.md)** explains every Git term, browser click and terminal command.

## License options (not yet selected)

There is **no root `LICENSE` file** yet, so the repository's original material is **not automatically open-source licensed** just because it is public. Here are possible licenses for **new material owned by the course contributors**:

| Material | Candidate | Tradeoff |
|---|---|---|
| Original C/examples | **MIT (recommended)** | Short, permissive, widely compatible with bundled Pebble MIT source; preserve notices. |
| Original C/examples | **Apache-2.0** | Permissive plus explicit patent-grant terms and notice requirements. |
| Original C/examples | **GPL-3.0-or-later** | Copyleft for redistributed derivative programs; review compatibility/obligations. |
| Original educational writing | **CC BY 4.0 (recommended)** | Allows adaptations with attribution and license conditions. |
| Original educational writing | **CC BY-SA 4.0** | Requires adapted material to remain under a compatible share-alike license. |

**Rights warning:** Bundled Pebble examples have their *own* MIT notices (for example `lessons/1C/starter/LICENSE`). The 4A–4D readings contain substantial source-derived passages from *Learning C with Pebble*. Verify their copyright and redistribution permissions **before** applying a blanket license or claiming that all course material is freely reusable. A new repository license cannot grant rights to third-party text, code or artwork. Creative Commons licenses are for the original instructional text here, **not** for the C code.

This is a **proposal**, not a license grant. See [GitHub's licensing explanation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) and [Choose a License](https://choosealicense.com/).

## Syllabus formats

[SYLLABUS.md](SYLLABUS.md) is the up-to-date authoritative syllabus. [SYLLABUS.pdf](SYLLABUS.pdf) has been regenerated for the 41-activity syllabus, including the recent assessor note. The Markdown version remains the authoritative editable edition, with local links to full companion readings.

## Pedagogical redesign

All **seven competencies** now have explicit outcomes and evidence criteria; 40 preparatory activities assign a primary and supporting competence, with five primary tasks per non-C competence and ten for C. New [41-activity integrated sequence](curriculum/course-design/integrated-sequence.md) interleaves the original programming exercises and three evolving SDK projects. A required [original-app capstone (9A)](lessons/9A/) assesses all seven. [Read the four-level mastery rubric](curriculum/course-design/learning-outcomes-and-assessment.md).

**Source validation:** Emery manifests and paths have been checked; SDK compilation, emulator execution and physical hardware confirmation remain unverified.
