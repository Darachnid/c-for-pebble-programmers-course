# Sequential lesson IDs and Taskwarrior migration

The course now has **one unique numeric prefix for each position 1–41**, with its **original suffix letter unchanged**. Suffix letters have *no ordering significance*. For example, `10D` precedes `11A`, and `30G` precedes `31C`.

This mapping is available in [legacy-id-map.json](legacy-id-map.json). Full source-path migration details are in [course-renumber-manifest.json](../course-renumber-manifest.json).

## Existing Taskwarrior tasks

Run `python3 taskwarrior/import_course.py` from the repository root and review the preview before typing `CREATE`. The importer identifies tasks by their legacy course annotations and descriptions, not just their possibly colliding numeric prefix. It **updates the existing UUIDs in place** and retains completion dates, status, user notes and any personal tags. It creates a pre-migration JSON backup in `taskwarrior/backups/` (gitignored).

If the importer detects conflicting or ambiguous task identities, it stops instead of manufacturing duplicate tasks. Do not manually rename IDs in Taskwarrior first; the script handles the mapping in one pass.

For an installation with no existing course tasks, it simply creates the current 41 activities.
