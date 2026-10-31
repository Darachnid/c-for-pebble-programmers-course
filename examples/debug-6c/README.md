# 6C — Persisted-state challenge (HIGH)

**This project deliberately compiles and runs, but loses a choice across restarts.**

Task: Build and install on Emery, select a nondefault font, close the app, then reopen. Record the expected selection and the selection restored after startup. Capture the supplied startup and button logs with `pebble logs --emulator emery`. Inspect the storage lifecycle and determine why the persisted choice is not restored correctly. Fix the defect, then repeat three scenarios: clean install/no saved choice, saved nondefault selection, and multiple close/reopen cycles.

Evidence: reproduction steps, before/after logs, cause, minimal fix, and restart test matrix. Logs expose symptoms rather than the answer. Do not consult a clean integrated solution before debugging.

This is an exercise in tracing state across distinct app runs; the code contains **one intentionally introduced persistence fault**.
