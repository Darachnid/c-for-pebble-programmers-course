# Taskwarrior import — 41 Emery course tasks

Run `python3 taskwarrior/import_course.py` from the repository root and type `CREATE` when prompted.

The importer creates or updates the full course with `estimated` time, `effort` (L/M/H), `priority` (L/M/H), annotations linking exact local lesson folders, and **actual UUID dependency relationships**. Existing task records with the same course ID are reused, including previously imported 3A/8B/9C with older titles.

Completed status and personal annotations are preserved. The importer updates pending task names, metadata and prerequisites according to the new syllabus.

```sh
task project:pebble.course list
task project:pebble.course unblocked
task <ID> info
```

Total estimated focused time: **52h 35m** across 26 activities. All projects target Emery.

The 15 added tasks come from [extension_api_labs.json](extension_api_labs.json), including dependencies and local starter annotations. Run the importer again and confirm with `CREATE`. Existing completions and personal notes are preserved.

## Curriculum alignment

The extension catalog now includes 12A–40N plus 41A. All 41 records carry **primary + supporting competency** annotations (41A integrates all seven), while previous task IDs, completion records and personal annotations remain intact. The updated [mastery rubric](../curriculum/course-design/learning-outcomes-and-assessment.md) is an additional learner self-check; Taskwarrior completion is still explicitly controlled by the learner.

## ID migration (existing Taskwarrior users)

The numeric prefixes now mean **course position**, not skill category; letters retain their original suffixes without an A-before-B requirement. Running `python3 taskwarrior/import_course.py` will offer an in-place UUID migration from the old IDs and make a local gitignored backup before changes. Read [RENUMBERING.md](RENUMBERING.md) and inspect [legacy-id-map.json](legacy-id-map.json).
