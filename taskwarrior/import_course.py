#!/usr/bin/env python3
"""Emery-only resume-safe importer for the 26-task Pebble C course.

Platform: Pebble Time 2, Emery, 200x228 rectangular display.
Every starting example is Emery-targeted: verified emery platform in its
manifest, an Emery-capable contemporary project, or the current C tutorial.
No legacy Aplite/Basalt/Chalk-only starting examples are assigned.

Uses real Taskwarrior UUID dependencies and estimates, priority, difficulty,
and detailed annotation content. Updates existing imported course annotations
without duplicating tasks and without deleting personal notes.
"""

import json
import re
import shutil
import subprocess
import sys

PROJECT = "pebble.course"
TAGS = ("+pebble", "+course", "+emery")

TASKS = [{'key': '2A',
  'description': '2A Explore Pebble examples',
  'skill': 'Idea Generation',
  'difficulty': 'L',
  'estimated': '20m',
  'priority': 'H',
  'depends': [],
  'instructions': 'Inspect the three linked emery-capable C examples only. For one example, brainstorm '
                  'five original ways to change or extend its behavior. Note the UI, API, or other '
                  'capability each idea might need. Do not write code or choose a permanent project '
                  'yet.',
  'done': 'Five distinct ideas are recorded, each describes a possible change, and one idea is marked '
          'as the most interesting to investigate.',
  'resources': 'Browse three Emery-compatible C apps: https://github.com/a-type/nimbus-watchface ; '
               'https://github.com/awwaiid/pebble-watchface-basic-big-digital ; '
               'https://github.com/pebble-examples/app-font-browser. The Font Browser declares emery '
               'in appinfo.json but uses an older project format. Browse them as inspiration; do not '
               'code.',
  'prereq_note': 'None. This is an entry-point activity.',
  'starting_example_title': 'Emery-compatible C examples for exploration',
  'starting_example_url': 'https://github.com/a-type/nimbus-watchface',
  'starting_example_note': 'Choose ONLY from the three linked emery-capable C projects; do not browse '
                           'the unfiltered legacy examples organization.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '7A',
  'description': '7A Build and run a time-only C watchface',
  'skill': 'Development Tools and Workflow',
  'difficulty': 'L',
  'estimated': '30m',
  'priority': 'H',
  'depends': [],
  'instructions': 'Create a new C project with the CURRENT watchface tutorial for SDK 4. Set '
                  'package.json targetPlatforms to ["emery"]. Follow the tutorial through Displaying '
                  'the Time and STOP before Adding the Date. Run pebble build then pebble install '
                  '--emulator emery; confirm time updates and only one TextLayer exists. Identify '
                  'project structure and build output.',
  'done': 'The project builds and runs in the emulator, displays the current time, updates by minute, '
          'and has no date TextLayer.',
  'resources': 'Current Emery C tutorial: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/ ; current C source '
               'repository for reference: https://github.com/coredevices/c-watchface-tutorial. Start '
               'from new SDK project, not the completed repo.',
  'prereq_note': 'None. This is the first build-and-run exercise.',
  'starting_example_title': 'Current C watchface tutorial: time-only checkpoint',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Create a C project with package.json targetPlatforms containing emery, and '
                           'stop exactly before Adding the Date. Build/install with --emulator emery.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '4A',
  'description': '4A Annotate the time-only watchface code',
  'skill': 'C Programming',
  'difficulty': 'L',
  'estimated': '45m',
  'priority': 'H',
  'depends': ['7A'],
  'instructions': 'Use your time-only watchface source. In your own notes, annotate the variable '
                  'declarations, data types, pointers, function calls, arguments, and callback '
                  'registrations. For each function, state its responsibility. Mark which calls happen '
                  'directly and which functions Pebble calls as callbacks. Do not use AI to explain or '
                  'write the annotations.',
  'done': "Your notes explain the key declarations and each function's role, and distinguish direct "
          'calls from callbacks.',
  'resources': 'Follow source from your OWN time-only checkpoint: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/ ; full C source '
               'reference https://github.com/coredevices/c-watchface-tutorial.',
  'prereq_note': 'Requires 7A: a working project and source files.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Work from your already-built emery watchface; do not copy a finished '
                           'example.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '5A',
  'description': '5A Find and document a Pebble API function',
  'skill': 'Resource Literacy',
  'difficulty': 'L',
  'estimated': '20m',
  'priority': 'H',
  'depends': ['4A'],
  'instructions': 'Find the SDK documentation for text_layer_set_font() or another function used by '
                  'your watchface. Record what it does, its full function signature, the type and '
                  'purpose of each argument, its return type, and one example of where it is used. '
                  'Write the explanation in your own words.',
  'done': 'A concise API note contains purpose, signature, argument meanings, return type, and a usage '
          'example.',
  'resources': 'C SDK reference: https://developer.repebble.com/docs/c/ ; time-only example: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 4A: familiarity with the source code and function calls.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Look up an API used in the current emery C tutorial, not a legacy '
                           'unsupported sample.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '3A',
  'description': '3A Trace the watchface lifecycle',
  'skill': 'Algorithmic Thinking',
  'difficulty': 'L',
  'estimated': '30m',
  'priority': 'H',
  'depends': ['4A', '7A'],
  'instructions': 'Draw the execution flow for the time-only watchface. Include main(), init(), '
                  'window_stack_push(), main_window_load(), update_time(), tick_handler(), '
                  'app_event_loop(), main_window_unload(), and deinit() where applicable. Show which '
                  'functions call other functions and which are callbacks. Show the separate path for '
                  'a minute tick after startup.',
  'done': 'A flow diagram shows startup, initial display, minute updates, and cleanup, with direct '
          'calls distinguished from callbacks.',
  'resources': 'Time-only C tutorial: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 4A and 7A.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Use the emery watchface lifecycle you built in 7A.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '1A',
  'description': '1A Change one visual property of a time-only watchface',
  'skill': 'UI Design',
  'difficulty': 'L',
  'estimated': '30m',
  'priority': 'H',
  'depends': ['4A', '5A', '7A'],
  'instructions': 'Start from the time-only checkpoint of the C watchface tutorial: the code after '
                  "'Displaying the Time' and before 'Adding the Date'. Choose exactly one visual "
                  'property to change: font, position, alignment, text color, or background color. '
                  'Make the change, build, and inspect it in the emulator. Keep the time working and '
                  'do not add the date or other functionality.',
  'done': 'The app builds and runs, the time still updates, and one intentional visual change is '
          'visible. The watchface still has no date layer.',
  'resources': 'Time-only Emery C example: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/ ; current C source '
               'https://github.com/coredevices/c-watchface-tutorial. STOP before the date step.',
  'prereq_note': 'Requires 4A, 5A, and 7A.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Use your own time-only emery checkpoint; never start from the completed '
                           'time+date example.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '6A',
  'description': '6A Diagnose a simple compiler error',
  'skill': 'Debugging and Testing',
  'difficulty': 'L',
  'estimated': '20m',
  'priority': 'H',
  'depends': ['4A', '7A'],
  'instructions': 'Make a separate copy or Git branch of the time-only watchface. Introduce one simple '
                  'compile-time error, such as a missing semicolon or a misspelled identifier. Build '
                  'the project, read the compiler message, locate the cause, fix it, and build again. '
                  'Change only one thing while diagnosing.',
  'done': 'You can show the original error, identify its cause, fix it, and produce a successful '
          'build.',
  'resources': 'Current C tutorial: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 4A and 7A.',
  'starting_example_title': 'Your time-only Emery C watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Use a copy or Git branch of the Emery-only project made in 7A.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '7B',
  'description': '7B Create a Git-based modification workflow',
  'skill': 'Development Tools and Workflow',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'H',
  'depends': ['7A', '1A', '6A'],
  'instructions': 'Create your own working copy of the example; do not edit the reference repository '
                  'in place. Initialize or use a Git repository, commit the known-good starting point, '
                  'make one small visual modification, build and test it, then commit the working '
                  'change with a meaningful message. Confirm you can inspect the diff and return to '
                  'the earlier version.',
  'done': 'The repository has a baseline commit and a modification commit, the app builds, and you '
          'have inspected the diff or demonstrated how to restore the baseline.',
  'resources': 'Current C source repository: https://github.com/coredevices/c-watchface-tutorial ; '
               'tutorial: https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 7A, 1A, and 6A.',
  'starting_example_title': 'Your time-only Emery C watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Keep a Git baseline for the time-only emery watchface before '
                           'modifications.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '5B',
  'description': '5B Trace an existing feature through source code',
  'skill': 'Resource Literacy',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'M',
  'depends': ['3A', '4A', '5A'],
  'instructions': 'Open the Font Browser example. Find where button input is registered or handled, '
                  'identify the state that changes, and follow the code until the display is updated. '
                  'Use the README and SDK docs to look up unfamiliar APIs. Write down the '
                  'file/function names and draw the input -> state change -> display update path.',
  'done': 'Your notes identify the input handling, changed state, display update, and the relevant '
          'source locations and documentation.',
  'resources': 'Emery is explicitly listed under targetPlatforms in '
               'https://github.com/pebble-examples/app-font-browser/blob/master/appinfo.json ; SDK C '
               'reference: https://developer.repebble.com/docs/c/. Legacy SDK 3 layout: read as source '
               'even if it requires migrating to a modern project.',
  'prereq_note': 'Requires 3A, 4A, and 5A.',
  'starting_example_title': 'Pebble Font Browser (explicit emery target)',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Trace its button-to-font flow. Be aware that the older repository uses '
                           'appinfo.json, even though emery is in its target list.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '1B',
  'description': '1B Add and style a date TextLayer',
  'skill': 'UI Design',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'M',
  'depends': ['1A', '4A', '5A'],
  'instructions': 'From YOUR time-only emery code, follow the Adding the Date section of the current C '
                  'tutorial to create, style, position, update, and unload a second TextLayer. Arrange '
                  'time and date for the Emery 200x228 screen. Build and install on emery. Do not '
                  'switch to a completed repository.',
  'done': 'The watchface displays both time and date, both update correctly, and you can explain how '
          'the date layer is created, styled, attached, updated, and destroyed.',
  'resources': 'Use the Adding the Date section of '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/, from your '
               'time-only emery checkpoint.',
  'prereq_note': 'Requires 1A, 4A, and 5A.',
  'starting_example_title': 'Current C tutorial: Adding the Date',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Do not start from a completed date watchface. Add the date yourself, '
                           'testing exclusively on emery.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '3B',
  'description': '3B Design a font-cycling algorithm',
  'skill': 'Algorithmic Thinking',
  'difficulty': 'M',
  'estimated': '30m',
  'priority': 'M',
  'depends': ['3A', '5B'],
  'instructions': 'Before editing code, write pseudocode for cycling through a list of fonts in both '
                  'directions. Define how the selected font is represented, what Up and Down do, '
                  'whether the list wraps at either end, and how the screen is refreshed. Work through '
                  'the first item, last item, and a one-item list. Keep this as an algorithm-design '
                  'exercise; do not implement it yet.',
  'done': 'Pseudocode and a small flowchart cover both directions, normal selection, and boundary '
          'cases.',
  'resources': 'Emery-compatible source for review: '
               'https://github.com/pebble-examples/app-font-browser ; emulator command reference: '
               'https://developer.repebble.com/faqs/.',
  'prereq_note': 'Requires 3A and 5B.',
  'starting_example_title': 'Pebble Font Browser (explicit emery target)',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Plan the algorithm yourself. Font Browser is a watchapp with buttons, not '
                           'a watchface.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '2B',
  'description': '2B Write a two-example remix brief',
  'skill': 'Idea Generation',
  'difficulty': 'M',
  'estimated': '30m',
  'priority': 'M',
  'depends': ['2A', '5B'],
  'instructions': 'Study the emery-compatible Font Browser watchapp and Nimbus C watchface. Describe '
                  'an original idea combining one observable behavior or display idea from each; '
                  'identify the minimum version and any uncertainty. This is a design brief, not a '
                  'build.',
  'done': 'A one-page brief explains the purpose, source features, minimal version, and one or more '
          'technical questions to investigate.',
  'resources': 'Font Browser (emery in appinfo.json): '
               'https://github.com/pebble-examples/app-font-browser ; Nimbus C watchface (emery): '
               'https://github.com/a-type/nimbus-watchface ; C SDK: '
               'https://developer.repebble.com/docs/c/.',
  'prereq_note': 'Requires 2A and 5B.',
  'starting_example_title': 'Emery examples: Font Browser + Nimbus',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Use these two emery-capable examples for the remix brief; code is NOT '
                           'required.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '4B',
  'description': '4B Modify the Font Browser',
  'skill': 'C Programming',
  'difficulty': 'M',
  'estimated': '120m',
  'priority': 'M',
  'depends': ['3B', '5B', '7B'],
  'instructions': 'Study Font Browser, an older C watchapp whose manifest explicitly declares emery. '
                  'Rebuild its font browsing behavior or adapt it into an emery-only modern C watchapp '
                  'if legacy project metadata prevents building with your SDK. Add ONE original '
                  'extension, such as a selected-font label. Test on emery and preserve the original '
                  'navigation. Do not copy a completed custom app.',
  'done': 'Your modified app builds and runs, the original font browsing still works, and your added '
          'feature is visible and tested.',
  'resources': 'Font Browser legacy C watchapp with emery target: '
               'https://github.com/pebble-examples/app-font-browser ; current SDK documentation: '
               'https://developer.repebble.com/docs/c/.',
  'prereq_note': 'Requires 3B, 5B, and 7B.',
  'starting_example_title': 'Pebble Font Browser (explicit emery target)',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'If this legacy SDK 3 project does not build under your SDK, transfer the '
                           'relevant C functions into a freshly created emery-only SDK 4 watchapp. Do '
                           'not switch target platforms.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '6B',
  'description': '6B Diagnose a font-selection boundary bug',
  'skill': 'Debugging and Testing',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'M',
  'depends': ['4B', '6A'],
  'instructions': 'In a separate copy or branch of your modified Font Browser, introduce or reproduce '
                  'a boundary bug in the selection logic (for example, an index moving outside the '
                  'valid range). Write down the expected behavior at the first and last entries, '
                  'reproduce the failure, inspect the state change, fix it, and test both directions '
                  'at both boundaries.',
  'done': 'The bug is reproducible, the cause is explained, and tests show that cycling works '
          'correctly at both ends of the list.',
  'resources': 'Font Browser source (lists emery): https://github.com/pebble-examples/app-font-browser '
               '; SDK docs: https://developer.repebble.com/docs/c/.',
  'prereq_note': 'Requires 4B and 6A.',
  'starting_example_title': 'Your Emery Font Browser modification',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Reproduce and test the bug on emery, using the watchapp built in 4B.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '5C',
  'description': '5C Research an unfamiliar Pebble capability',
  'skill': 'Resource Literacy',
  'difficulty': 'H',
  'estimated': '60m',
  'priority': 'M',
  'depends': ['5B'],
  'instructions': 'Study persistence as demonstrated in the CURRENT C watchface tutorial Part 6 '
                  '(Emery-supported), and the official C storage API. Record persist_exists, '
                  'persist_read_int, persist_write_int, relevant default/error handling, and a minimal '
                  'plan for remembering a selected font. This is research and note-taking only; do not '
                  'code.',
  'done': 'A technical note names the capability, links the documentation and example, lists relevant '
          'APIs and constraints, and proposes implementation steps.',
  'resources': 'Emery-supported C example including persisted settings: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part6/ ; C persistence '
               'guide: https://developer.repebble.com/guides/events-and-services/persistent-storage/ ; '
               'alternative emery C source: https://github.com/a-type/nimbus-watchface.',
  'prereq_note': 'Requires 5B.',
  'starting_example_title': 'Current C tutorial with persistent settings',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part6/',
  'starting_example_note': 'Investigate C persistence as the target capability (or another capability '
                           'clearly supported by an emery example). Do not use the old Persist Counter '
                           'or Menu Layer demo.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '2C',
  'description': '2C Develop an original Pebble app concept',
  'skill': 'Idea Generation',
  'difficulty': 'H',
  'estimated': '60m',
  'priority': 'M',
  'depends': ['2B', '5C'],
  'instructions': 'Use the linked Emery-compatible examples as inspiration. Generate three original '
                  'ideas, compare them for usefulness and feasibility on a Pebble Time 2, and develop '
                  'a small specification for one idea. This is not a commitment to implement it. Cite '
                  'the example code you inspected.',
  'done': 'Three ideas are compared and one has a concise specification for purpose, interaction, '
          'minimum version, and technical uncertainty.',
  'resources': 'Emery-native C sources: https://github.com/a-type/nimbus-watchface ; '
               'https://github.com/awwaiid/pebble-watchface-basic-big-digital ; '
               'https://github.com/sheppoor/touch-tone ; '
               'https://github.com/pebble-examples/app-font-browser ; current C tutorial '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 2B and 5C.',
  'starting_example_title': 'Emery C example collection for inspiration',
  'starting_example_url': 'https://github.com/a-type/nimbus-watchface',
  'starting_example_note': 'Base feasibility research only on the linked emery-capable examples and '
                           'current C SDK.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '3C',
  'description': '3C Design a state machine for an app',
  'skill': 'Algorithmic Thinking',
  'difficulty': 'H',
  'estimated': '60m',
  'priority': 'M',
  'depends': ['2C', '3B', '4B'],
  'instructions': 'Use your original emery app concept or the Emery Touch Tone watchapp as an '
                  'input-pattern reference. Enumerate states, transitions, button press behavior, '
                  'screen changes, and edge cases. Create a state diagram and table. Plan for Emery '
                  'input and display only.',
  'done': 'A state diagram and transition table describe all main states, triggers, resulting states, '
          'and visible responses, including important edge cases.',
  'resources': 'Emery-specific button/touch interaction example: '
               'https://github.com/sheppoor/touch-tone ; emery C watchface with mode switching: '
               'https://github.com/a-type/nimbus-watchface.',
  'prereq_note': 'Requires 2C, 3B, and 4B.',
  'starting_example_title': 'Pebble Time 2 Touch Tone watchapp',
  'starting_example_url': 'https://github.com/sheppoor/touch-tone',
  'starting_example_note': 'Use these as references for states and transitions, not legacy UI pattern '
                           'examples.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '1C',
  'description': '1C Design a multi-mode Pebble interface',
  'skill': 'UI Design',
  'difficulty': 'H',
  'estimated': '90m',
  'priority': 'M',
  'depends': ['1B', '2C', '3C', '4B'],
  'instructions': 'Sketch every mode of your application on a 200 x 228 rectangular Pebble Time 2 '
                  '(Emery) display. Label positioning, fonts, actions, and screen transitions. '
                  'Reference the Emery-compatible Nimbus watchface layout if useful. Verify the '
                  'mockups cover the behavior from 3C. No round-screen design.',
  'done': 'A set of labeled sketches covers every main state, navigation between states, button '
          'outcomes, and screen-size considerations.',
  'resources': 'Emery C watchface with more than one display mode: '
               'https://github.com/a-type/nimbus-watchface ; emery font/layout example: '
               'https://github.com/awwaiid/pebble-watchface-basic-big-digital.',
  'prereq_note': 'Requires 1B, 2C, 3C, and 4B.',
  'starting_example_title': 'Pebble Time 2 Nimbus C watchface',
  'starting_example_url': 'https://github.com/a-type/nimbus-watchface',
  'starting_example_note': 'Sketch for 200 x 228 rectangular Emery only; do not require round or other '
                           'platform layouts.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '4C',
  'description': '4C Refactor font selection into a reusable component',
  'skill': 'C Programming',
  'difficulty': 'H',
  'estimated': '90m',
  'priority': 'M',
  'depends': ['3B', '4B', '5C'],
  'instructions': 'Using your emery-compatible Font Browser implementation, refactor selected font '
                  'state and update logic into reusable functions without duplicating cases. Use '
                  'current C watchface custom font tutorial Part 2 if you add font resources. Confirm '
                  'correct loading/unloading. Build, install, and test on emery exclusively.',
  'done': 'Font selection uses a reusable function and organized data, both navigation directions '
          'work, and any allocated font resources are cleaned up correctly.',
  'resources': 'Font Browser (emery declared): https://github.com/pebble-examples/app-font-browser ; '
               'current C custom font instructions compatible with emery: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part2/ ; C SDK '
               'https://developer.repebble.com/docs/c/.',
  'prereq_note': 'Requires 3B, 4B, and 5C.',
  'starting_example_title': 'Font Browser + current C font tutorial',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Refactor your emery watchapp. Use the modern C tutorial for custom font '
                           'resource lifecycle; do not use unsupported old feature-custom-font.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '7C',
  'description': '7C Integrate font browsing with persistent selection',
  'skill': 'Development Tools and Workflow',
  'difficulty': 'H',
  'estimated': '150m',
  'priority': 'M',
  'depends': ['2C', '4C', '5B', '7B'],
  'instructions': 'Combine your functioning emery-only Font Browser watchapp with persistence code '
                  'patterned on the CURRENT Emery C watchface tutorial Part 6. Save the chosen font '
                  'index; load it at startup; choose a safe default if absent or invalid. Test by '
                  'selecting a font, exiting, and reopening the app. Keep Git commits and use emery '
                  'only.',
  'done': 'The combined app builds, font navigation works, the selected font survives a restart, '
          'invalid or absent stored values are handled safely, and Git records the work.',
  'resources': 'Font browsing (explicit emery target): '
               'https://github.com/pebble-examples/app-font-browser ; emery C persistent settings '
               'example: https://developer.repebble.com/tutorials/watchface-tutorial/part6/ ; C '
               'storage API: '
               'https://developer.repebble.com/guides/events-and-services/persistent-storage/.',
  'prereq_note': 'Requires 2C, 4C, 5B, and 7B.',
  'starting_example_title': 'Font Browser + current Emery C persistence tutorial',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Combine the Font Browser emery watchapp with the persistent-state pattern '
                           'from the CURRENT Emery C tutorial, not the unsupported legacy Persist '
                           'Counter project.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '6C',
  'description': '6C Diagnose a persistent-state integration bug',
  'skill': 'Debugging and Testing',
  'difficulty': 'H',
  'estimated': '90m',
  'priority': 'L',
  'depends': ['4C', '6B', '7C'],
  'instructions': 'Use your emery-only font/persistence app from 7C. Introduce or find one '
                  'reproducible storage bug (invalid saved index, wrong saved value, or a startup '
                  'mismatch). Record expected and actual behavior, isolate and fix it, then test fresh '
                  'install, selections, restart, and invalid data handling on emery.',
  'done': 'A reproducible bug report records expected and actual behavior, the cause is explained, and '
          'the fix passes fresh-start, selection, and restart tests.',
  'resources': 'Your combined emery watchapp; C persistence example '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part6/ ; Font Browser '
               'https://github.com/pebble-examples/app-font-browser ; C Storage guide '
               'https://developer.repebble.com/guides/events-and-services/persistent-storage/.',
  'prereq_note': 'Requires 4C, 6B, and 7C.',
  'starting_example_title': 'Your integrated Emery font-persistence watchapp',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Test on emery, including fresh install and closing/reopening. Do not load '
                           'builds for other platforms.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'}]


# Repository-first reference mapping. The original lesson data remains intact, but
# every course task now points to its version-controlled in-repository starter.
COURSE_REPO = "https://github.com/Darachnid/c-for-pebble-programmers-course"
COURSE_EXAMPLES = {
  "2A": "lessons/2A/README.md",
  "7A": "lessons/7A/README.md",
  "4A": "lessons/4A/README.md",
  "5A": "lessons/5A/README.md",
  "3A": "lessons/3A/README.md",
  "1A": "lessons/1A/README.md",
  "6A": "lessons/6A/README.md",
  "7B": "lessons/7B/README.md",
  "5B": "lessons/5B/README.md",
  "1B": "lessons/1B/README.md",
  "3B": "lessons/3B/README.md",
  "2B": "lessons/2B/README.md",
  "4B": "lessons/4B/README.md",
  "6B": "lessons/6B/README.md",
  "5C": "lessons/5C/README.md",
  "2C": "lessons/2C/README.md",
  "3C": "lessons/3C/README.md",
  "1C": "lessons/1C/README.md",
  "4C": "lessons/4C/README.md",
  "7C": "lessons/7C/README.md",
  "6C": "lessons/6C/README.md"
}
COURSE_OVERRIDES = {"2A":"Browse only the included Emery-targeted projects under examples/, initially time-only, font-selector, and persist-counter. Choose one and brainstorm five creative variations; describe what changes and what new API each might require. Do not browse or solve the debugging challenges yet.","6A":"Start from the deliberately flawed examples/debug-6a project. Run pebble build; capture the first compiler diagnostic; identify and correct the single syntax fault; rebuild and run on emery. The original clean time-only example is for comparison AFTER the diagnosis.","2B":"Select two examples from the included examples/ folder (such as time-only and persist-counter). Describe a possible new application using an element from each. State its purpose, the elements to borrow, the smallest working version and a technical uncertainty. Do not implement yet.","4B":"Start from the working local Emery font-selector watchapp. Trace its input handler, index state, and apply_font function; add one extension you design yourself (e.g., index indicator or extra preview), committing and testing after each change. This is a watchapp, so Up/Down are available.","6B":"Use the provided deliberately flawed examples/debug-6b project. It compiles but navigation behaves incorrectly. Reproduce four successive Up and Down presses, collect the included APP_LOG index traces with pebble logs --emulator emery, locate the wrong transition, apply a minimal fix and verify both boundaries. Compare with the clean example only after debugging.","5C":"Study the local Emery persist-counter app. Identify how it checks for saved data, reads it at startup, and writes changes. Research the SDK's persistence functions using official documentation, and write an implementation plan to reuse the pattern in another app; no copy-and-paste integration yet.","2C":"Use the included examples/ collection as inspiration. Propose three original Pebble Time 2 applications based on your interests. Compare feasibility and learning value; write a minimal specification for one without committing to build it.","1C":"Using your concept from 2C and the state diagram from 3C, draw each interface mode for the Emery 200x228 rectangular screen. Use layouts from the included simple examples as starting references, but develop your own visual hierarchy and navigation.","7C":"Start with the local clean font-selector project and the local persist-counter reference. Add persistent selection to your own font app, saving its font index and restoring it on startup, with a safe default for missing/out-of-range values. Build and test on Emery; do not simply copy the integrated debugging sample.","6C":"Use the deliberately flawed examples/debug-6c project. Select a nondefault font, exit, reopen; document the discrepancy. Inspect the provided startup and selection logs; trace storage write/read behavior; fix the single persistence defect and test fresh install plus repeated restarts. Do not consult a clean integrated implementation before diagnosing."}
for lesson in TASKS:
    key = lesson["key"]
    local_path = COURSE_EXAMPLES[key]
    lesson["starting_example_title"] = "Local Emery course starter: " + local_path
    lesson["starting_example_url"] = COURSE_REPO + "/blob/main/" + local_path
    lesson["starting_example_note"] = (
        "Use the included source at " + COURSE_REPO +
        "/tree/main/" + local_path.split("/README.md")[0] +
        "; read its README before modifying it."
    )
    lesson["resources"] = (
        "Included course examples: " + COURSE_REPO + "/tree/main/examples ; "
        "Activity specification: " + COURSE_REPO + "/blob/main/SYLLABUS.md ; "
        "Local starting material: " + lesson["starting_example_url"]
    )
    if key in COURSE_OVERRIDES:
        lesson["instructions"] = COURSE_OVERRIDES[key]

# Lesson-specific repo links supersede the old shared example links.
for lesson in TASKS:
    key = lesson["key"]
    lesson["starting_example_title"] = "Exact local starter for lesson " + key
    lesson["starting_example_url"] = COURSE_REPO + "/tree/main/lessons/" + key
    lesson["starting_example_note"] = (
        "Read lessons/" + key + "/README.md. All required example code is "
        "included in this lesson folder, including both source apps when needed."
    )
    lesson["resources"] = (
        "Exact in-repository example: " + lesson["starting_example_url"] +
        " ; instructions: " + COURSE_REPO + "/blob/main/lessons/" + key +
        "/README.md ; syllabus: " + COURSE_REPO + "/blob/main/SYLLABUS.md"
    )
    lesson["instructions"] = (
        "Open lessons/" + key + "/README.md and use its local source. " +
        lesson["instructions"]
    )

# --- Course version 2: eight C modules, exact lesson folders, 26 tasks. ---
COURSE_V2 = {
  "2A": {
    "key": "2A",
    "description": "2A Explore Pebble examples",
    "skill": "Idea Generation",
    "difficulty": "L",
    "estimated": "20m",
    "priority": "H",
    "depends": [],
    "instructions": "Inspect the three included Emery-only projects under lessons/2A. Brainstorm five modifications and note what SDK feature each might require. No coding or debugging-project spoilers.",
    "done": "Five distinct ideas are recorded, each describes a possible change, and one idea is marked as the most interesting to investigate.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "None",
    "starting_example_title": "Lesson 2A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2A",
    "starting_example_note": "Open lessons/2A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "7A": {
    "key": "7A",
    "description": "7A Build and run a time-only C watchface",
    "skill": "Development Tools and Workflow",
    "difficulty": "L",
    "estimated": "30m",
    "priority": "H",
    "depends": [],
    "instructions": "Create a new C project with the CURRENT watchface tutorial for SDK 4. Set package.json targetPlatforms to [\"emery\"]. Follow the tutorial through Displaying the Time and STOP before Adding the Date. Run pebble build then pebble install --emulator emery; confirm time updates and only one TextLayer exists. Identify project structure and build output.",
    "done": "The project builds and runs in the emulator, displays the current time, updates by minute, and has no date TextLayer.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "None",
    "starting_example_title": "Lesson 7A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7A",
    "starting_example_note": "Open lessons/7A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4A": {
    "key": "4A",
    "description": "4A Variables, Data Types, and Operators",
    "skill": "C Programming",
    "difficulty": "L",
    "estimated": "120m",
    "priority": "H",
    "depends": [
      "7A"
    ],
    "instructions": "Read variables, types, operators and casts. Complete the bouncing ball and orbiting-letter projects, modifying expressions and interpreting their behavior.",
    "done": "Demonstrate both Emery apps, explain types and arithmetic, and supply code diffs plus boundary tests.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4A-variables-data-types-operators.md",
    "prereq_note": "7A",
    "starting_example_title": "Lesson 4A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4A",
    "starting_example_note": "Open lessons/4A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "5A": {
    "key": "5A",
    "description": "5A Find and document a Pebble API function",
    "skill": "Resource Literacy",
    "difficulty": "L",
    "estimated": "20m",
    "priority": "H",
    "depends": [
      "4A"
    ],
    "instructions": "Find the SDK documentation for text_layer_set_font() or another function used by your watchface. Record what it does, its full function signature, the type and purpose of each argument, its return type, and one example of where it is used. Write the explanation in your own words.",
    "done": "A concise API note contains purpose, signature, argument meanings, return type, and a usage example.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4A",
    "starting_example_title": "Lesson 5A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5A",
    "starting_example_note": "Open lessons/5A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "1A": {
    "key": "1A",
    "description": "1A Change one visual property of a time-only watchface",
    "skill": "UI Design",
    "difficulty": "L",
    "estimated": "30m",
    "priority": "H",
    "depends": [
      "4A",
      "5A",
      "7A"
    ],
    "instructions": "Use lessons/1A/starter with only one time TextLayer. Change exactly one of font, color, alignment or position; verify that the clock still updates.",
    "done": "The app builds and runs, the time still updates, and one intentional visual change is visible. The watchface still has no date layer.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4A, 5A, 7A",
    "starting_example_title": "Lesson 1A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1A",
    "starting_example_note": "Open lessons/1A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "6A": {
    "key": "6A",
    "description": "6A Diagnose a simple compiler error",
    "skill": "Debugging and Testing",
    "difficulty": "L",
    "estimated": "20m",
    "priority": "H",
    "depends": [
      "4A",
      "7A"
    ],
    "instructions": "Use the deliberately flawed local lessons/6A/starter project. Capture the first compiler diagnostic, make the minimal syntax correction, then build and run on Emery.",
    "done": "You can show the original error, identify its cause, fix it, and produce a successful build.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4A, 7A",
    "starting_example_title": "Lesson 6A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6A",
    "starting_example_note": "Open lessons/6A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "7B": {
    "key": "7B",
    "description": "7B Create a Git-based modification workflow",
    "skill": "Development Tools and Workflow",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "H",
    "depends": [
      "7A",
      "1A",
      "6A"
    ],
    "instructions": "Make a personal Git branch or working copy of lessons/7B/starter, commit a baseline, change one visual property, build/test and commit the improvement.",
    "done": "The repository has a baseline commit and a modification commit, the app builds, and you have inspected the diff or demonstrated how to restore the baseline.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "7A, 1A, 6A",
    "starting_example_title": "Lesson 7B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7B",
    "starting_example_note": "Open lessons/7B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4B": {
    "key": "4B",
    "description": "4B Conditional Execution and Decision Making",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "120m",
    "priority": "H",
    "depends": [
      "4A"
    ],
    "instructions": "Read if/else, switch, logical operators and short-circuiting. Complete the sweeping-seconds and digital-clock decision exercises.",
    "done": "Two modified Emery builds plus an explanation of each branch and tests at decision boundaries.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4B-conditionals-decision-making.md",
    "prereq_note": "4A",
    "starting_example_title": "Lesson 4B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4B",
    "starting_example_note": "Open lessons/4B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4C": {
    "key": "4C",
    "description": "4C Loops and Iteration",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "135m",
    "priority": "H",
    "depends": [
      "4B"
    ],
    "instructions": "Study for, while, do/while and nested loops. Complete decimal-to-binary, color-grid replacement and screen-filling text exercises.",
    "done": "All three exercises run on Emery; the loop bounds and termination conditions are explained and verified.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4C-loops-iteration.md",
    "prereq_note": "4B",
    "starting_example_title": "Lesson 4C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4C",
    "starting_example_note": "Open lessons/4C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4D": {
    "key": "4D",
    "description": "4D Functions and Program Structure",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "150m",
    "priority": "H",
    "depends": [
      "4C"
    ],
    "instructions": "Study signatures, parameters, return values, callbacks and recursion. Complete the clock-helper, bit-pattern, rectangle and concentric-circle projects.",
    "done": "Four project artifacts show correct function contracts, a terminating recursive function and a working build.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4D ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4D-functions-program-structure.md",
    "prereq_note": "4C",
    "starting_example_title": "Lesson 4D: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4D",
    "starting_example_note": "Open lessons/4D/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "3A": {
    "key": "3A",
    "description": "3A Trace the watchface lifecycle",
    "skill": "Algorithmic Thinking",
    "difficulty": "L",
    "estimated": "30m",
    "priority": "H",
    "depends": [
      "4D",
      "7A"
    ],
    "instructions": "Draw the execution flow for the time-only watchface. Include main(), init(), window_stack_push(), main_window_load(), update_time(), tick_handler(), app_event_loop(), main_window_unload(), and deinit() where applicable. Show which functions call other functions and which are callbacks. Show the separate path for a minute tick after startup.",
    "done": "A flow diagram shows startup, initial display, minute updates, and cleanup, with direct calls distinguished from callbacks.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4D, 7A",
    "starting_example_title": "Lesson 3A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3A",
    "starting_example_note": "Open lessons/3A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "1B": {
    "key": "1B",
    "description": "1B Add and style a date TextLayer",
    "skill": "UI Design",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "M",
    "depends": [
      "1A",
      "4D",
      "5A"
    ],
    "instructions": "Start from the time-only watchface in lessons/1B/starter and add a separate date TextLayer, observing creation, layout, minute updates and cleanup on Emery.",
    "done": "The watchface displays both time and date, both update correctly, and you can explain how the date layer is created, styled, attached, updated, and destroyed.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "1A, 4D, 5A",
    "starting_example_title": "Lesson 1B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1B",
    "starting_example_note": "Open lessons/1B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "5B": {
    "key": "5B",
    "description": "5B Trace an existing feature through source code",
    "skill": "Resource Literacy",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "M",
    "depends": [
      "3A",
      "4D",
      "5A"
    ],
    "instructions": "Inspect the local lessons/5B/starter font selector. Trace the Up/Down event from callback through index update to apply_font; document API signatures and state updates.",
    "done": "Your notes identify the input handling, changed state, display update, and the relevant source locations and documentation.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "3A, 4D, 5A",
    "starting_example_title": "Lesson 5B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5B",
    "starting_example_note": "Open lessons/5B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "3B": {
    "key": "3B",
    "description": "3B Design a font-cycling algorithm",
    "skill": "Algorithmic Thinking",
    "difficulty": "M",
    "estimated": "30m",
    "priority": "M",
    "depends": [
      "3A",
      "5B"
    ],
    "instructions": "Using the local lessons/3B/starter font selector, write original pseudocode for moving through fonts in both directions, including first/last and a one-item edge case.",
    "done": "Pseudocode and a small flowchart cover both directions, normal selection, and boundary cases.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "3A, 5B",
    "starting_example_title": "Lesson 3B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3B",
    "starting_example_note": "Open lessons/3B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "2B": {
    "key": "2B",
    "description": "2B Write a two-example remix brief",
    "skill": "Idea Generation",
    "difficulty": "M",
    "estimated": "30m",
    "priority": "M",
    "depends": [
      "2A",
      "5B"
    ],
    "instructions": "Choose components from the two complete local projects in lessons/2B, write a remix brief with core behavior, sources, minimal implementation and technical unknowns.",
    "done": "A one-page brief explains the purpose, source features, minimal version, and one or more technical questions to investigate.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "2A, 5B",
    "starting_example_title": "Lesson 2B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2B",
    "starting_example_note": "Open lessons/2B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4E": {
    "key": "4E",
    "description": "4E Arrays, Strings, and Bounds",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "90m",
    "priority": "H",
    "depends": [
      "4D"
    ],
    "instructions": "Read arrays, indices, strings and bounded buffers. Extend the Emery word-selector starter to six choices and test wraparound and long labels.",
    "done": "Build works; selections wrap correctly, strings remain terminated and storage is valid throughout display lifetime.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4E ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4E-arrays-strings.md",
    "prereq_note": "4D",
    "starting_example_title": "Lesson 4E: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4E",
    "starting_example_note": "Open lessons/4E/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4F": {
    "key": "4F",
    "description": "4F Pointers, Indirection, and Memory Lifetime",
    "skill": "C Programming",
    "difficulty": "H",
    "estimated": "105m",
    "priority": "H",
    "depends": [
      "4E"
    ],
    "instructions": "Read pointer parameters, indirection, ownership and lifetime. Extend the coordinate-pointer app with a safe helper, and document Pebble resource cleanup.",
    "done": "Working application, pointer trace, NULL handling and ownership/lifetime explanation.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4F ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4F-pointers-memory.md",
    "prereq_note": "4E",
    "starting_example_title": "Lesson 4F: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4F",
    "starting_example_note": "Open lessons/4F/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4G": {
    "key": "4G",
    "description": "4G Structures, Enums, and Program State",
    "skill": "C Programming",
    "difficulty": "H",
    "estimated": "105m",
    "priority": "M",
    "depends": [
      "4F"
    ],
    "instructions": "Read structs, enums, static scope and state transitions. Extend the local mode app with PAUSED and mode-specific behavior.",
    "done": "Mode transition table plus running app demonstrating valid transitions, protected operations and fallback handling.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4G ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4G-structs-enums-state.md",
    "prereq_note": "4F",
    "starting_example_title": "Lesson 4G: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4G",
    "starting_example_note": "Open lessons/4G/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "5C": {
    "key": "5C",
    "description": "5C Research an unfamiliar Pebble capability",
    "skill": "Resource Literacy",
    "difficulty": "H",
    "estimated": "60m",
    "priority": "M",
    "depends": [
      "4E",
      "5B"
    ],
    "instructions": "Research persistence from lessons/5C/starter, trace persist_exists/read/write and write an implementation plan using the current SDK documentation.",
    "done": "A technical note names the capability, links the documentation and example, lists relevant APIs and constraints, and proposes implementation steps.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4E, 5B",
    "starting_example_title": "Lesson 5C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5C",
    "starting_example_note": "Open lessons/5C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "6B": {
    "key": "6B",
    "description": "6B Diagnose a font-selection boundary bug",
    "skill": "Debugging and Testing",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "M",
    "depends": [
      "4E",
      "6A",
      "3B"
    ],
    "instructions": "Use lessons/6B/starter with its deliberate index bug. Reproduce Up/Down behavior, inspect APP_LOG index traces, fix the faulty transition and retest every boundary.",
    "done": "The bug is reproducible, the cause is explained, and tests show that cycling works correctly at both ends of the list.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4E, 6A, 3B",
    "starting_example_title": "Lesson 6B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6B",
    "starting_example_note": "Open lessons/6B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "2C": {
    "key": "2C",
    "description": "2C Develop an original Pebble app concept",
    "skill": "Idea Generation",
    "difficulty": "H",
    "estimated": "60m",
    "priority": "M",
    "depends": [
      "2B",
      "5C"
    ],
    "instructions": "Inspect the three complete local Emery examples in lessons/2C and develop three original ideas; compare feasibility, select one and write a minimal specification.",
    "done": "Three ideas are compared and one has a concise specification for purpose, interaction, minimum version, and technical uncertainty.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "2B, 5C",
    "starting_example_title": "Lesson 2C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2C",
    "starting_example_note": "Open lessons/2C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "3C": {
    "key": "3C",
    "description": "3C Design a state machine for an app",
    "skill": "Algorithmic Thinking",
    "difficulty": "H",
    "estimated": "60m",
    "priority": "M",
    "depends": [
      "2C",
      "3B",
      "4G"
    ],
    "instructions": "Use lessons/3C/starter and your 2C app concept to specify a state machine: states, inputs, transitions, visible outputs, default cases and invalid events.",
    "done": "A state diagram and transition table describe all main states, triggers, resulting states, and visible responses, including important edge cases.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "2C, 3B, 4G",
    "starting_example_title": "Lesson 3C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3C",
    "starting_example_note": "Open lessons/3C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4H": {
    "key": "4H",
    "description": "4H Event-Driven Integration and Application Lifecycle",
    "skill": "C Programming",
    "difficulty": "H",
    "estimated": "150m",
    "priority": "M",
    "depends": [
      "4G",
      "3C"
    ],
    "instructions": "Read callback lifecycle, event subscriptions and persistence. Extend the local app with a second mode and show event-driven updates and correct cleanup.",
    "done": "Emery program demonstrates button/tick callbacks, persisted state, mode-dependent actions and safe teardown.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4H ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/4H-events-lifecycle.md",
    "prereq_note": "4G, 3C",
    "starting_example_title": "Lesson 4H: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4H",
    "starting_example_note": "Open lessons/4H/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "1C": {
    "key": "1C",
    "description": "1C Design a multi-mode Pebble interface",
    "skill": "UI Design",
    "difficulty": "H",
    "estimated": "90m",
    "priority": "M",
    "depends": [
      "1B",
      "2C",
      "3C",
      "4H"
    ],
    "instructions": "Use lessons/1C/starter (the licensed Simplicity C layout) to sketch multiple Emery screens/modes, navigation and button outcomes for your own concept.",
    "done": "A set of labeled sketches covers every main state, navigation between states, button outcomes, and screen-size considerations.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "1B, 2C, 3C, 4H",
    "starting_example_title": "Lesson 1C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1C",
    "starting_example_note": "Open lessons/1C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "7C": {
    "key": "7C",
    "description": "7C Integrate font browsing with persistent selection",
    "skill": "Development Tools and Workflow",
    "difficulty": "H",
    "estimated": "150m",
    "priority": "M",
    "depends": [
      "1C",
      "4H",
      "5B",
      "7B"
    ],
    "instructions": "Combine the two complete but separate projects in lessons/7C (font selector and persistent counter). Implement saved font selection yourself, validate indices and verify restart behavior.",
    "done": "The combined app builds, font navigation works, the selected font survives a restart, invalid or absent stored values are handled safely, and Git records the work.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "1C, 4H, 5B, 7B",
    "starting_example_title": "Lesson 7C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7C",
    "starting_example_note": "Open lessons/7C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "6C": {
    "key": "6C",
    "description": "6C Diagnose a persistent-state integration bug",
    "skill": "Debugging and Testing",
    "difficulty": "H",
    "estimated": "90m",
    "priority": "L",
    "depends": [
      "4H",
      "6B",
      "7C"
    ],
    "instructions": "Use lessons/6C/starter with its deliberate persistence fault. Select a nondefault font, restart, trace save/restore logs, correct the mismatch and retest.",
    "done": "A reproducible bug report records expected and actual behavior, the cause is explained, and the fix passes fresh-start, selection, and restart tests.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "4H, 6B, 7C",
    "starting_example_title": "Lesson 6C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6C",
    "starting_example_note": "Open lessons/6C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  }
}
COURSE_SEQUENCE = ["2A","7A","4A","5A","1A","6A","7B","4B","4C","4D","3A","1B","5B","3B","2B","4E","4F","4G","5C","6B","2C","3C","4H","1C","7C","6C"]
for item in TASKS:
    item.update(COURSE_V2[item["key"]])
for key in ("4D", "4E", "4F", "4G", "4H"):
    TASKS.append(dict(COURSE_V2[key]))
TASKS.sort(key=lambda item: COURSE_SEQUENCE.index(item["key"]))

SHORT = {"H": "High", "M": "Medium", "L": "Low"}


def task_cmd(*args, allow_empty=False):
    """Run Taskwarrior in its own process, without context or commentary text."""
    cmd = ["task", "rc.color=off", "rc.verbose=nothing", "rc.context=", *args]
    result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode != 0:
        if allow_empty and not result.stdout.strip() and not result.stderr.strip():
            return ""
        raise RuntimeError(
            f"Taskwarrior failed (exit {result.returncode}): {cmd!r}\n"
            f"stdout: {result.stdout.strip()}\nstderr: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def get_config(name):
    return task_cmd("_get", f"rc.{name}").strip()


def ensure_udas():
    """Configure only missing UDAs; do not overwrite existing user settings."""
    estimated_type = get_config("uda.estimated.type")
    effort_type = get_config("uda.effort.type")
    if estimated_type and estimated_type not in ("duration", "string"):
        raise RuntimeError(
            "Your uda.estimated.type is " + estimated_type + ". "
            "This course requires duration or string; please inspect Taskwarrior settings."
        )
    if effort_type and effort_type != "string":
        raise RuntimeError(
            "Your uda.effort.type is " + effort_type + ". "
            "This course requires a string UDA to hold H/M/L."
        )
    if not estimated_type:
        task_cmd("rc.confirmation=off", "config", "uda.estimated.type", "duration")
        task_cmd("rc.confirmation=off", "config", "uda.estimated.label", "Estimated Time")
        print("Configured missing estimated UDA (duration).")
    if not effort_type:
        task_cmd("rc.confirmation=off", "config", "uda.effort.type", "string")
        task_cmd("rc.confirmation=off", "config", "uda.effort.label", "Difficulty")
        print("Configured missing effort UDA (string).")


def course_export():
    """Return matching tasks, including existing partial imports and completed tasks."""
    output = task_cmd("rc.json.array=on", f"project:{PROJECT}", "export")
    if not output:
        return []
    try:
        result = json.loads(output)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Taskwarrior export did not return valid JSON. Check your Taskwarrior "
            "version/configuration. First 500 characters:\n" + output[:500]
        ) from exc
    if isinstance(result, dict):
        result = [result]
    if not isinstance(result, list):
        raise RuntimeError("Unexpected Taskwarrior JSON export format")
    return result


def annotation_texts(record):
    return {
        row.get("description", "")
        for row in record.get("annotations", [])
        if isinstance(row, dict)
    }


def annotations_for(t):
    return [
        f"Course ID: {t['key']} | Skill: {t['skill']} | "
        f"Difficulty: {SHORT[t['difficulty']]} | Estimated: {t['estimated']} | "
        f"Priority: {SHORT[t['priority']]}",
        f"Starting example: {t['starting_example_title']} — {t['starting_example_url']}",
        f"Starting example guidance: {t['starting_example_note']}",
        f"Instructions: {t['instructions']}",
        f"Done when: {t['done']}",
        f"Supporting resources: {t['resources']}",
        f"Prerequisites: {t['prereq_note']}",
        f"Target platform: {t['emery_rule']}",
        ("Course rule: Work independently without AI assistance. Use the Pebble "
         "examples, SDK docs, compiler output, emulator, Git, and your own notes."),
    ]


def get_record_by_description(description):
    key = description.split(" ", 1)[0]
    matches = [r for r in course_export()
               if r.get("description", "").split(" ", 1)[0] == key
               and r.get("status") != "deleted"]
    if len(matches) > 1:
        raise RuntimeError(
            f"Found {len(matches)} duplicate tasks with description {description!r}. "
            "Please resolve duplicates manually before retrying."
        )
    return matches[0] if matches else None


def ensure_annotations(uuid, item, existing):
    """Replace course-generated annotations, preserving user's other notes."""
    old = annotation_texts(existing)
    wanted = annotations_for(item)
    prefixes = (
        "Course ID:", "Starting example:", "Starting example guidance:",
        "Instructions:", "Done when:", "Supporting resources:", "Resources:",
        "Prerequisites:", "Target platform:", "Course rule:",
    )
    desired = set(wanted)
    for msg in sorted(old):
        if msg.startswith(prefixes) and msg not in desired:
            task_cmd(uuid, "denotate", msg)
    for msg in wanted:
        if msg not in old:
            task_cmd(uuid, "annotate", msg)


def ensure_fields(uuid, item, existing):
    required = {
        "estimated": item["estimated"],
        "effort": item["difficulty"],
        "priority": item["priority"],
    }
    changes = []
    for k, v in required.items():
        # Taskwarrior may export duration UDAs as seconds rather than '30m'.
        if k == "estimated":
            # The revised curriculum has new time estimates: update pending tasks.
            changes.append(f"{k}:{v}")
        elif existing.get(k) != v:
            changes.append(f"{k}:{v}")
    if changes and existing.get("status") == "pending":
        task_cmd(uuid, "modify", *changes)


def normalize_depends(deps):
    if deps is None:
        return []
    if isinstance(deps, str):
        return [x for x in deps.split(",") if x]
    return list(deps)


def main():
    if not shutil.which("task"):
        print("Taskwarrior command `task` was not found on PATH.", file=sys.stderr)
        return 1

    try:
        before = course_export()
        existing = {t["description"]: t for t in before
                    if t.get("status") != "deleted"}
        known_ids = {name.split(" ", 1)[0] for name in existing}
        matched = sum(1 for t in TASKS if t["key"] in known_ids)
        estimated_type = get_config("uda.estimated.type")
        effort_type = get_config("uda.effort.type")
        print(f"Project: {PROJECT} | Activities: {len(TASKS)} | Target: emery (Pebble Time 2) only")
        print(f"Existing matching tasks: {matched} | New tasks needed: {len(TASKS)-matched}")
        print(f"Estimated UDA: {estimated_type or 'missing (will configure)'}")
        print(f"Effort UDA: {effort_type or 'missing (will configure)'}")
        print("Will replace only course-generated annotations, preserve personal notes, update metadata, and set dependency links.")
        print("Existing completed tasks will be preserved; matching tasks will not be duplicated.")
        confirm = input("Type CREATE to proceed: ").strip()
        if confirm != "CREATE":
            print("Cancelled; no changes made.")
            return 0

        ensure_udas()
        uuids = {}
        for item in TASKS:
            old = get_record_by_description(item["description"])
            if old is None:
                # Taskwarrior's verbosity settings can suppress 'Created task N'.
                # Re-query JSON export after adding instead of parsing human output.
                task_cmd("add", item["description"], f"project:{PROJECT}",
                         f"estimated:{item['estimated']}",
                         f"effort:{item['difficulty']}",
                         f"priority:{item['priority']}", *TAGS)
                old = get_record_by_description(item["description"])
                if old is None:
                    raise RuntimeError(
                        f"Taskwarrior accepted ADD for {item['key']}, but the task "
                        "is missing from project export. Run `task all` and "
                        f"`task project:{PROJECT} export` to inspect it. "
                        "No further tasks were created."
                    )
                action = "Created"
            else:
                action = "Reused"
            uuid = old.get("uuid")
            if not uuid:
                raise RuntimeError(f"Export for {item['key']} has no UUID: {old!r}")
            uuids[item["key"]] = uuid
            if old.get("description") != item["description"] and old.get("status") == "pending":
                task_cmd(uuid, "modify", "description:" + item["description"])
            ensure_fields(uuid, item, old)
            ensure_annotations(uuid, item, old)
            print(f"{action}: {item['key']} — {item['description']}")

        for item in TASKS:
            expected = [uuids[k] for k in item["depends"]]
            old = get_record_by_description(item["description"])
            current = normalize_depends(old.get("depends"))
            if set(expected) != set(current):
                if old.get("status") == "pending":
                    # Replace stale old-course dependencies; do not merely append them.
                    task_cmd(uuids[item["key"]], "modify", "depends:" + ",".join(expected))
                    print(f"Linked: {item['key']} depends on {', '.join(item['depends']) or 'none'}")
                else:
                    print(f"Skipped dependency change for completed task {item['key']}.")

        total = sum(int(t["estimated"][:-1]) for t in TASKS)
        print(f"\nComplete: {len(TASKS)} course tasks, estimated {total // 60}h {total % 60}m.")
        print(f"View: task project:{PROJECT} list")
        print(f"Ready: task project:{PROJECT} unblocked")
        print(f"Details: task <ID> info")
        return 0
    except Exception as exc:
        print("\nImport stopped: " + str(exc), file=sys.stderr)
        print("The script is resume-safe. Resolve the issue, then rerun it.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
