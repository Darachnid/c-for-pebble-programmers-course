# Taskwarrior course importer

This imports all 21 activities, with priorities, effort, estimated time and real UUID dependency links. Course-generated annotations now point directly to **`lessons/<ID>/`** inside this repository, not to upstream GitHub examples.

```sh
python3 taskwarrior/import_course.py
task project:pebble.course list
task project:pebble.course unblocked
task <ID> info
```

Type `CREATE` when prompted. The importer is designed to reuse matching tasks and refresh course-generated annotations, preserving personal notes. The entire starter code for each activity is inside that lesson's folder.
