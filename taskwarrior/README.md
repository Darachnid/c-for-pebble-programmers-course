# Taskwarrior import — 26 Emery course tasks

Run `python3 taskwarrior/import_course.py` from the repository root and type `CREATE` when prompted.

The importer creates or updates the full course with `estimated` time, `effort` (L/M/H), `priority` (L/M/H), annotations linking exact local lesson folders, and **actual UUID dependency relationships**. Existing task records with the same course ID are reused, including previously imported 4A/4B/4C with older titles.

Completed status and personal annotations are preserved. The importer updates pending task names, metadata and prerequisites according to the new syllabus.

```sh
task project:pebble.course list
task project:pebble.course unblocked
task <ID> info
```

Total estimated focused time: **31h 15m** across 26 activities. All projects target Emery.
