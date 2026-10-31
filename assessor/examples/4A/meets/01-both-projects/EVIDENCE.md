# Evidence — 4A

## Artifact paths

- lessons/4A/projects/project-3-1/src/c/main.c
- lessons/4A/projects/project-3-2/src/c/main.c

## Build and run

Built each project with `pebble build` and installed on `--emulator emery`. Both run without errors.

## Behavior observed

Project 3-1: integer sizes print as expected in the debug window.
Project 3-2: arithmetic matches hand-checked values on device.

## Boundary case tested

Project 3-1 boundary: tested largest `int` constant used in the exercise.
Project 3-2 boundary: division by one and by zero guard path if present in my edits.

## Explain in your own words

I used `%d` formatting and fixed-width types in 3-1, and practiced operator precedence and compound assignment in 3-2.

## Source diff

Git diff covers both project directories; committed after each exercise.
