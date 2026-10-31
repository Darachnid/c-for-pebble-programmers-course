# Evidence — 2A

## Artifact paths

- lessons/2A/starter/

## Build and run

```
pebble build
# ... Waf: Entering directory ...
# 'build' finished successfully
pebble install --emulator emery
```

Build log attached as submit/2A/build.log showing successful app_bundle output.

## Behavior observed

Time displays in HH:MM on Emery rectangular layout. Logs show tick events each minute.
Verified struct field s_time_layer is the only TextLayer pointer used for display text.

## Boundary case tested

Set emulator clock near 09:59 and watched rollover to 10:00.

## Explain in your own words

This exercise practiced the Pebble build/install loop and reading where wscript and src/c/main.c fit in the project.

## Source diff

Diff includes tutorial edits only through Displaying the Time; no date layer code added.
