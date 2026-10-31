# 21B — Instrumented logic challenge (MEDIUM)

**This project deliberately compiles and runs, but has one incorrect interaction.**

Task: Build and install on Emery. Write down the expected behavior of Up and Down, observe four successive presses in each direction, and compare to what happens. Use `pebble logs --emulator emery` to inspect the provided **old/new selection-index diagnostic lines**. Locate the defective state transition and change only what is necessary.

Evidence: your reproduction sequence, expected versus actual font selection, relevant log entries, and proof that forward/backward cycling visits every font.

Compiler messages will not reveal this bug; the included runtime logging is intended to make the faulty transition tractable. Avoid opening the clean font-selector source until after you diagnose it.
