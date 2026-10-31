# Taskwarrior course importer

Imports the [21 Emery course activities](https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md) with real Taskwarrior UUID dependencies, `estimated` duration, `effort` (L/M/H), `priority` (L/M/H), and detailed annotations linking **back to this repository**.

Download or clone this repository and run:

```sh
python3 taskwarrior/import_course.py
```

Type **CREATE** when prompted. The script recognizes tasks by their existing descriptions and updates course-generated annotations, preserving user-written notes. It will not overwrite completed tasks' statuses. This version supersedes earlier conversation downloads.

Inspect your imported tasks:

```sh
task project:pebble.course list
task project:pebble.course unblocked
task <ID> info
```

A course task's **Starting example** and **Supporting resources** annotations point to local files inside this GitHub repository. This script does not install or run Pebble examples for you.

