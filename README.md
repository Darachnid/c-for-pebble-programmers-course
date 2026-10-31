# C for Pebble Programmers Course

A self-directed, **26-activity**, **Emery-only** C programming course: seven developer competencies and an eight-module C track (4A–4H), with real dependency links and evidence-based completion.

**Estimated focused time:** 31h 15m. No prescribed calendar deadlines.

## Start here

- [Complete syllabus](SYLLABUS.md) ([PDF edition](SYLLABUS.pdf))
- [All 26 lesson folders and local examples](lessons/README.md)
- [Eight C programming reading modules](curriculum/c-programming/README.md)
- [Taskwarrior importer](taskwarrior/README.md)

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
