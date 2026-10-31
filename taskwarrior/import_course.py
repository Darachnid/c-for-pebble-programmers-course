#!/usr/bin/env python3
"""Emery-only resume-safe importer for the 41-task Pebble C course.

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

TASKS = [{'key': '1A',
  'description': '1A Explore Pebble examples',
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
 {'key': '2A',
  'description': '2A Build and run a time-only C watchface',
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
 {'key': '3A',
  'description': '3A Annotate the time-only watchface code',
  'skill': 'C Programming',
  'difficulty': 'L',
  'estimated': '45m',
  'priority': 'H',
  'depends': ['2A'],
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
  'prereq_note': 'Requires 2A: a working project and source files.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Work from your already-built emery watchface; do not copy a finished '
                           'example.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '4A',
  'description': '4A Find and document a Pebble API function',
  'skill': 'Resource Literacy',
  'difficulty': 'L',
  'estimated': '20m',
  'priority': 'H',
  'depends': ['3A'],
  'instructions': 'Find the SDK documentation for text_layer_set_font() or another function used by '
                  'your watchface. Record what it does, its full function signature, the type and '
                  'purpose of each argument, its return type, and one example of where it is used. '
                  'Write the explanation in your own words.',
  'done': 'A concise API note contains purpose, signature, argument meanings, return type, and a usage '
          'example.',
  'resources': 'C SDK reference: https://developer.repebble.com/docs/c/ ; time-only example: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 3A: familiarity with the source code and function calls.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Look up an API used in the current emery C tutorial, not a legacy '
                           'unsupported sample.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '11A',
  'description': '11A Trace the watchface lifecycle',
  'skill': 'Algorithmic Thinking',
  'difficulty': 'L',
  'estimated': '30m',
  'priority': 'H',
  'depends': ['3A', '2A'],
  'instructions': 'Draw the execution flow for the time-only watchface. Include main(), init(), '
                  'window_stack_push(), main_window_load(), update_time(), tick_handler(), '
                  'app_event_loop(), main_window_unload(), and deinit() where applicable. Show which '
                  'functions call other functions and which are callbacks. Show the separate path for '
                  'a minute tick after startup.',
  'done': 'A flow diagram shows startup, initial display, minute updates, and cleanup, with direct '
          'calls distinguished from callbacks.',
  'resources': 'Time-only C tutorial: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 3A and 2A.',
  'starting_example_title': 'Current C tutorial: time-only watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Use the emery watchface lifecycle you built in 2A.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '5A',
  'description': '5A Change one visual property of a time-only watchface',
  'skill': 'UI Design',
  'difficulty': 'L',
  'estimated': '30m',
  'priority': 'H',
  'depends': ['3A', '4A', '2A'],
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
  'prereq_note': 'Requires 3A, 4A, and 2A.',
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
  'depends': ['3A', '2A'],
  'instructions': 'Make a separate copy or Git branch of the time-only watchface. Introduce one simple '
                  'compile-time error, such as a missing semicolon or a misspelled identifier. Build '
                  'the project, read the compiler message, locate the cause, fix it, and build again. '
                  'Change only one thing while diagnosing.',
  'done': 'You can show the original error, identify its cause, fix it, and produce a successful '
          'build.',
  'resources': 'Current C tutorial: '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 3A and 2A.',
  'starting_example_title': 'Your time-only Emery C watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Use a copy or Git branch of the Emery-only project made in 2A.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '7B',
  'description': '7B Create a Git-based modification workflow',
  'skill': 'Development Tools and Workflow',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'H',
  'depends': ['2A', '5A', '6A'],
  'instructions': 'Create your own working copy of the example; do not edit the reference repository '
                  'in place. Initialize or use a Git repository, commit the known-good starting point, '
                  'make one small visual modification, build and test it, then commit the working '
                  'change with a meaningful message. Confirm you can inspect the diff and return to '
                  'the earlier version.',
  'done': 'The repository has a baseline commit and a modification commit, the app builds, and you '
          'have inspected the diff or demonstrated how to restore the baseline.',
  'resources': 'Current C source repository: https://github.com/coredevices/c-watchface-tutorial ; '
               'tutorial: https://developer.repebble.com/tutorials/watchface-tutorial/part1/.',
  'prereq_note': 'Requires 2A, 5A, and 6A.',
  'starting_example_title': 'Your time-only Emery C watchface',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Keep a Git baseline for the time-only emery watchface before '
                           'modifications.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '14B',
  'description': '14B Trace an existing feature through source code',
  'skill': 'Resource Literacy',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'M',
  'depends': ['11A', '3A', '4A'],
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
  'prereq_note': 'Requires 11A, 3A, and 4A.',
  'starting_example_title': 'Pebble Font Browser (explicit emery target)',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Trace its button-to-font flow. Be aware that the older repository uses '
                           'appinfo.json, even though emery is in its target list.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '13B',
  'description': '13B Add and style a date TextLayer',
  'skill': 'UI Design',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'M',
  'depends': ['5A', '3A', '4A'],
  'instructions': 'From YOUR time-only emery code, follow the Adding the Date section of the current C '
                  'tutorial to create, style, position, update, and unload a second TextLayer. Arrange '
                  'time and date for the Emery 200x228 screen. Build and install on emery. Do not '
                  'switch to a completed repository.',
  'done': 'The watchface displays both time and date, both update correctly, and you can explain how '
          'the date layer is created, styled, attached, updated, and destroyed.',
  'resources': 'Use the Adding the Date section of '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part1/, from your '
               'time-only emery checkpoint.',
  'prereq_note': 'Requires 5A, 3A, and 4A.',
  'starting_example_title': 'Current C tutorial: Adding the Date',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part1/',
  'starting_example_note': 'Do not start from a completed date watchface. Add the date yourself, '
                           'testing exclusively on emery.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '15B',
  'description': '15B Design a font-cycling algorithm',
  'skill': 'Algorithmic Thinking',
  'difficulty': 'M',
  'estimated': '30m',
  'priority': 'M',
  'depends': ['11A', '14B'],
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
  'prereq_note': 'Requires 11A and 14B.',
  'starting_example_title': 'Pebble Font Browser (explicit emery target)',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Plan the algorithm yourself. Font Browser is a watchapp with buttons, not '
                           'a watchface.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '16B',
  'description': '16B Write a two-example remix brief',
  'skill': 'Idea Generation',
  'difficulty': 'M',
  'estimated': '30m',
  'priority': 'M',
  'depends': ['1A', '14B'],
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
  'prereq_note': 'Requires 1A and 14B.',
  'starting_example_title': 'Emery examples: Font Browser + Nimbus',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Use these two emery-capable examples for the remix brief; code is NOT '
                           'required.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '8B',
  'description': '8B Modify the Font Browser',
  'skill': 'C Programming',
  'difficulty': 'M',
  'estimated': '120m',
  'priority': 'M',
  'depends': ['15B', '14B', '7B'],
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
  'prereq_note': 'Requires 15B, 14B, and 7B.',
  'starting_example_title': 'Pebble Font Browser (explicit emery target)',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'If this legacy SDK 3 project does not build under your SDK, transfer the '
                           'relevant C functions into a freshly created emery-only SDK 4 watchapp. Do '
                           'not switch target platforms.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '21B',
  'description': '21B Diagnose a font-selection boundary bug',
  'skill': 'Debugging and Testing',
  'difficulty': 'M',
  'estimated': '45m',
  'priority': 'M',
  'depends': ['8B', '6A'],
  'instructions': 'In a separate copy or branch of your modified Font Browser, introduce or reproduce '
                  'a boundary bug in the selection logic (for example, an index moving outside the '
                  'valid range). Write down the expected behavior at the first and last entries, '
                  'reproduce the failure, inspect the state change, fix it, and test both directions '
                  'at both boundaries.',
  'done': 'The bug is reproducible, the cause is explained, and tests show that cycling works '
          'correctly at both ends of the list.',
  'resources': 'Font Browser source (lists emery): https://github.com/pebble-examples/app-font-browser '
               '; SDK docs: https://developer.repebble.com/docs/c/.',
  'prereq_note': 'Requires 8B and 6A.',
  'starting_example_title': 'Your Emery Font Browser modification',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Reproduce and test the bug on emery, using the watchapp built in 8B.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '20C',
  'description': '20C Research an unfamiliar Pebble capability',
  'skill': 'Resource Literacy',
  'difficulty': 'H',
  'estimated': '60m',
  'priority': 'M',
  'depends': ['14B'],
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
  'prereq_note': 'Requires 14B.',
  'starting_example_title': 'Current C tutorial with persistent settings',
  'starting_example_url': 'https://developer.repebble.com/tutorials/watchface-tutorial/part6/',
  'starting_example_note': 'Investigate C persistence as the target capability (or another capability '
                           'clearly supported by an emery example). Do not use the old Persist Counter '
                           'or Menu Layer demo.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '22C',
  'description': '22C Develop an original Pebble app concept',
  'skill': 'Idea Generation',
  'difficulty': 'H',
  'estimated': '60m',
  'priority': 'M',
  'depends': ['16B', '20C'],
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
  'prereq_note': 'Requires 16B and 20C.',
  'starting_example_title': 'Emery C example collection for inspiration',
  'starting_example_url': 'https://github.com/a-type/nimbus-watchface',
  'starting_example_note': 'Base feasibility research only on the linked emery-capable examples and '
                           'current C SDK.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '23C',
  'description': '23C Design a state machine for an app',
  'skill': 'Algorithmic Thinking',
  'difficulty': 'H',
  'estimated': '60m',
  'priority': 'M',
  'depends': ['22C', '15B', '8B'],
  'instructions': 'Use your original emery app concept or the Emery Touch Tone watchapp as an '
                  'input-pattern reference. Enumerate states, transitions, button press behavior, '
                  'screen changes, and edge cases. Create a state diagram and table. Plan for Emery '
                  'input and display only.',
  'done': 'A state diagram and transition table describe all main states, triggers, resulting states, '
          'and visible responses, including important edge cases.',
  'resources': 'Emery-specific button/touch interaction example: '
               'https://github.com/sheppoor/touch-tone ; emery C watchface with mode switching: '
               'https://github.com/a-type/nimbus-watchface.',
  'prereq_note': 'Requires 22C, 15B, and 8B.',
  'starting_example_title': 'Pebble Time 2 Touch Tone watchapp',
  'starting_example_url': 'https://github.com/sheppoor/touch-tone',
  'starting_example_note': 'Use these as references for states and transitions, not legacy UI pattern '
                           'examples.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '25C',
  'description': '25C Design a multi-mode Pebble interface',
  'skill': 'UI Design',
  'difficulty': 'H',
  'estimated': '90m',
  'priority': 'M',
  'depends': ['13B', '22C', '23C', '8B'],
  'instructions': 'Sketch every mode of your application on a 200 x 228 rectangular Pebble Time 2 '
                  '(Emery) display. Label positioning, fonts, actions, and screen transitions. '
                  'Reference the Emery-compatible Nimbus watchface layout if useful. Verify the '
                  'mockups cover the behavior from 23C. No round-screen design.',
  'done': 'A set of labeled sketches covers every main state, navigation between states, button '
          'outcomes, and screen-size considerations.',
  'resources': 'Emery C watchface with more than one display mode: '
               'https://github.com/a-type/nimbus-watchface ; emery font/layout example: '
               'https://github.com/awwaiid/pebble-watchface-basic-big-digital.',
  'prereq_note': 'Requires 13B, 22C, 23C, and 8B.',
  'starting_example_title': 'Pebble Time 2 Nimbus C watchface',
  'starting_example_url': 'https://github.com/a-type/nimbus-watchface',
  'starting_example_note': 'Sketch for 200 x 228 rectangular Emery only; do not require round or other '
                           'platform layouts.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '9C',
  'description': '9C Refactor font selection into a reusable component',
  'skill': 'C Programming',
  'difficulty': 'H',
  'estimated': '90m',
  'priority': 'M',
  'depends': ['15B', '8B', '20C'],
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
  'prereq_note': 'Requires 15B, 8B, and 20C.',
  'starting_example_title': 'Font Browser + current C font tutorial',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Refactor your emery watchapp. Use the modern C tutorial for custom font '
                           'resource lifecycle; do not use unsupported old feature-custom-font.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '31C',
  'description': '31C Integrate font browsing with persistent selection',
  'skill': 'Development Tools and Workflow',
  'difficulty': 'H',
  'estimated': '150m',
  'priority': 'M',
  'depends': ['22C', '9C', '14B', '7B'],
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
  'prereq_note': 'Requires 22C, 9C, 14B, and 7B.',
  'starting_example_title': 'Font Browser + current Emery C persistence tutorial',
  'starting_example_url': 'https://github.com/pebble-examples/app-font-browser',
  'starting_example_note': 'Combine the Font Browser emery watchapp with the persistent-state pattern '
                           'from the CURRENT Emery C tutorial, not the unsupported legacy Persist '
                           'Counter project.',
  'emery_rule': 'Emery only (Pebble Time 2; rectangular 200x228, 64 colors). If building code, '
                'package.json targetPlatforms must include emery and run pebble build then pebble '
                'install --emulator emery. No round/older-platform testing required.'},
 {'key': '32C',
  'description': '32C Diagnose a persistent-state integration bug',
  'skill': 'Debugging and Testing',
  'difficulty': 'H',
  'estimated': '90m',
  'priority': 'L',
  'depends': ['9C', '21B', '31C'],
  'instructions': 'Use your emery-only font/persistence app from 31C. Introduce or find one '
                  'reproducible storage bug (invalid saved index, wrong saved value, or a startup '
                  'mismatch). Record expected and actual behavior, isolate and fix it, then test fresh '
                  'install, selections, restart, and invalid data handling on emery.',
  'done': 'A reproducible bug report records expected and actual behavior, the cause is explained, and '
          'the fix passes fresh-start, selection, and restart tests.',
  'resources': 'Your combined emery watchapp; C persistence example '
               'https://developer.repebble.com/tutorials/watchface-tutorial/part6/ ; Font Browser '
               'https://github.com/pebble-examples/app-font-browser ; C Storage guide '
               'https://developer.repebble.com/guides/events-and-services/persistent-storage/.',
  'prereq_note': 'Requires 9C, 21B, and 31C.',
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
  "1A": "lessons/1A/README.md",
  "2A": "lessons/2A/README.md",
  "3A": "lessons/3A/README.md",
  "4A": "lessons/4A/README.md",
  "11A": "lessons/11A/README.md",
  "5A": "lessons/5A/README.md",
  "6A": "lessons/6A/README.md",
  "7B": "lessons/7B/README.md",
  "14B": "lessons/14B/README.md",
  "13B": "lessons/13B/README.md",
  "15B": "lessons/15B/README.md",
  "16B": "lessons/16B/README.md",
  "8B": "lessons/8B/README.md",
  "21B": "lessons/21B/README.md",
  "20C": "lessons/20C/README.md",
  "22C": "lessons/22C/README.md",
  "23C": "lessons/23C/README.md",
  "25C": "lessons/25C/README.md",
  "9C": "lessons/9C/README.md",
  "31C": "lessons/31C/README.md",
  "32C": "lessons/32C/README.md"
}
COURSE_OVERRIDES = {"1A":"Browse only the included Emery-targeted projects under examples/, initially time-only, font-selector, and persist-counter. Choose one and brainstorm five creative variations; describe what changes and what new API each might require. Do not browse or solve the debugging challenges yet.","6A":"Start from the deliberately flawed examples/debug-6a project. Run pebble build; capture the first compiler diagnostic; identify and correct the single syntax fault; rebuild and run on emery. The original clean time-only example is for comparison AFTER the diagnosis.","16B":"Select two examples from the included examples/ folder (such as time-only and persist-counter). Describe a possible new application using an element from each. State its purpose, the elements to borrow, the smallest working version and a technical uncertainty. Do not implement yet.","8B":"Start from the working local Emery font-selector watchapp. Trace its input handler, index state, and apply_font function; add one extension you design yourself (e.g., index indicator or extra preview), committing and testing after each change. This is a watchapp, so Up/Down are available.","21B":"Use the provided deliberately flawed examples/debug-6b project. It compiles but navigation behaves incorrectly. Reproduce four successive Up and Down presses, collect the included APP_LOG index traces with pebble logs --emulator emery, locate the wrong transition, apply a minimal fix and verify both boundaries. Compare with the clean example only after debugging.","20C":"Study the local Emery persist-counter app. Identify how it checks for saved data, reads it at startup, and writes changes. Research the SDK's persistence functions using official documentation, and write an implementation plan to reuse the pattern in another app; no copy-and-paste integration yet.","22C":"Use the included examples/ collection as inspiration. Propose three original Pebble Time 2 applications based on your interests. Compare feasibility and learning value; write a minimal specification for one without committing to build it.","25C":"Using your concept from 22C and the state diagram from 23C, draw each interface mode for the Emery 200x228 rectangular screen. Use layouts from the included simple examples as starting references, but develop your own visual hierarchy and navigation.","31C":"Start with the local clean font-selector project and the local persist-counter reference. Add persistent selection to your own font app, saving its font index and restoring it on startup, with a safe default for missing/out-of-range values. Build and test on Emery; do not simply copy the integrated debugging sample.","32C":"Use the deliberately flawed examples/debug-6c project. Select a nondefault font, exit, reopen; document the discrepancy. Inspect the provided startup and selection logs; trace storage write/read behavior; fix the single persistence defect and test fresh install plus repeated restarts. Do not consult a clean integrated implementation before diagnosing."}
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
  "1A": {
    "key": "1A",
    "description": "1A Explore Pebble examples",
    "skill": "Idea Generation",
    "difficulty": "L",
    "estimated": "20m",
    "priority": "H",
    "depends": [],
    "instructions": "Inspect the three included Emery-only projects under lessons/1A. Brainstorm five modifications and note what SDK feature each might require. No coding or debugging-project spoilers.",
    "done": "Five distinct ideas are recorded, each describes a possible change, and one idea is marked as the most interesting to investigate.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "None",
    "starting_example_title": "Lesson 1A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/1A",
    "starting_example_note": "Open lessons/1A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "2A": {
    "key": "2A",
    "description": "2A Build and run a time-only C watchface",
    "skill": "Development Tools and Workflow",
    "difficulty": "L",
    "estimated": "30m",
    "priority": "H",
    "depends": [],
    "instructions": "Create a new C project with the CURRENT watchface tutorial for SDK 4. Set package.json targetPlatforms to [\"emery\"]. Follow the tutorial through Displaying the Time and STOP before Adding the Date. Run pebble build then pebble install --emulator emery; confirm time updates and only one TextLayer exists. Identify project structure and build output.",
    "done": "The project builds and runs in the emulator, displays the current time, updates by minute, and has no date TextLayer.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "None",
    "starting_example_title": "Lesson 2A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/2A",
    "starting_example_note": "Open lessons/2A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "3A": {
    "key": "3A",
    "description": "3A Variables, Data Types, and Operators",
    "skill": "C Programming",
    "difficulty": "L",
    "estimated": "120m",
    "priority": "H",
    "depends": [
      "2A"
    ],
    "instructions": "Read variables, types, operators and casts. Complete the bouncing ball and orbiting-letter projects, modifying expressions and interpreting their behavior.",
    "done": "Demonstrate both Emery apps, explain types and arithmetic, and supply code diffs plus boundary tests.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/3A-variables-data-types-operators.md",
    "prereq_note": "2A",
    "starting_example_title": "Lesson 3A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/3A",
    "starting_example_note": "Open lessons/3A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "4A": {
    "key": "4A",
    "description": "4A Find and document a Pebble API function",
    "skill": "Resource Literacy",
    "difficulty": "L",
    "estimated": "20m",
    "priority": "H",
    "depends": [
      "3A"
    ],
    "instructions": "Find the SDK documentation for text_layer_set_font() or another function used by your watchface. Record what it does, its full function signature, the type and purpose of each argument, its return type, and one example of where it is used. Write the explanation in your own words.",
    "done": "A concise API note contains purpose, signature, argument meanings, return type, and a usage example.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "3A",
    "starting_example_title": "Lesson 4A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/4A",
    "starting_example_note": "Open lessons/4A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "5A": {
    "key": "5A",
    "description": "5A Change one visual property of a time-only watchface",
    "skill": "UI Design",
    "difficulty": "L",
    "estimated": "30m",
    "priority": "H",
    "depends": [
      "3A",
      "4A",
      "2A"
    ],
    "instructions": "Use lessons/5A/starter with only one time TextLayer. Change exactly one of font, color, alignment or position; verify that the clock still updates.",
    "done": "The app builds and runs, the time still updates, and one intentional visual change is visible. The watchface still has no date layer.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "3A, 4A, 2A",
    "starting_example_title": "Lesson 5A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/5A",
    "starting_example_note": "Open lessons/5A/README.md. The complete source and instructions are in this repository; no external example download.",
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
      "3A",
      "2A"
    ],
    "instructions": "Use the deliberately flawed local lessons/6A/starter project. Capture the first compiler diagnostic, make the minimal syntax correction, then build and run on Emery.",
    "done": "You can show the original error, identify its cause, fix it, and produce a successful build.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/6A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "3A, 2A",
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
      "2A",
      "5A",
      "6A"
    ],
    "instructions": "Make a personal Git branch or working copy of lessons/7B/starter, commit a baseline, change one visual property, build/test and commit the improvement.",
    "done": "The repository has a baseline commit and a modification commit, the app builds, and you have inspected the diff or demonstrated how to restore the baseline.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "2A, 5A, 6A",
    "starting_example_title": "Lesson 7B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/7B",
    "starting_example_note": "Open lessons/7B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "8B": {
    "key": "8B",
    "description": "8B Conditional Execution and Decision Making",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "120m",
    "priority": "H",
    "depends": [
      "3A"
    ],
    "instructions": "Read if/else, switch, logical operators and short-circuiting. Complete the sweeping-seconds and digital-clock decision exercises.",
    "done": "Two modified Emery builds plus an explanation of each branch and tests at decision boundaries.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/8B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/8B-conditionals-decision-making.md",
    "prereq_note": "3A",
    "starting_example_title": "Lesson 8B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/8B",
    "starting_example_note": "Open lessons/8B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "9C": {
    "key": "9C",
    "description": "9C Loops and Iteration",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "135m",
    "priority": "H",
    "depends": [
      "8B"
    ],
    "instructions": "Study for, while, do/while and nested loops. Complete decimal-to-binary, color-grid replacement and screen-filling text exercises.",
    "done": "All three exercises run on Emery; the loop bounds and termination conditions are explained and verified.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/9C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/9C-loops-iteration.md",
    "prereq_note": "8B",
    "starting_example_title": "Lesson 9C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/9C",
    "starting_example_note": "Open lessons/9C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "10D": {
    "key": "10D",
    "description": "10D Functions and Program Structure",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "150m",
    "priority": "H",
    "depends": [
      "9C"
    ],
    "instructions": "Study signatures, parameters, return values, callbacks and recursion. Complete the clock-helper, bit-pattern, rectangle and concentric-circle projects.",
    "done": "Four project artifacts show correct function contracts, a terminating recursive function and a working build.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/10D ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/10D-functions-program-structure.md",
    "prereq_note": "9C",
    "starting_example_title": "Lesson 10D: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/10D",
    "starting_example_note": "Open lessons/10D/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "11A": {
    "key": "11A",
    "description": "11A Trace the watchface lifecycle",
    "skill": "Algorithmic Thinking",
    "difficulty": "L",
    "estimated": "30m",
    "priority": "H",
    "depends": [
      "10D",
      "2A"
    ],
    "instructions": "Draw the execution flow for the time-only watchface. Include main(), init(), window_stack_push(), main_window_load(), update_time(), tick_handler(), app_event_loop(), main_window_unload(), and deinit() where applicable. Show which functions call other functions and which are callbacks. Show the separate path for a minute tick after startup.",
    "done": "A flow diagram shows startup, initial display, minute updates, and cleanup, with direct calls distinguished from callbacks.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/11A ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "10D, 2A",
    "starting_example_title": "Lesson 11A: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/11A",
    "starting_example_note": "Open lessons/11A/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "13B": {
    "key": "13B",
    "description": "13B Add and style a date TextLayer",
    "skill": "UI Design",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "M",
    "depends": [
      "5A",
      "10D",
      "4A"
    ],
    "instructions": "Start from the time-only watchface in lessons/13B/starter and add a separate date TextLayer, observing creation, layout, minute updates and cleanup on Emery.",
    "done": "The watchface displays both time and date, both update correctly, and you can explain how the date layer is created, styled, attached, updated, and destroyed.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/13B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "5A, 10D, 4A",
    "starting_example_title": "Lesson 13B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/13B",
    "starting_example_note": "Open lessons/13B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "14B": {
    "key": "14B",
    "description": "14B Trace an existing feature through source code",
    "skill": "Resource Literacy",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "M",
    "depends": [
      "11A",
      "10D",
      "4A"
    ],
    "instructions": "Inspect the local lessons/14B/starter font selector. Trace the Up/Down event from callback through index update to apply_font; document API signatures and state updates.",
    "done": "Your notes identify the input handling, changed state, display update, and the relevant source locations and documentation.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/14B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "11A, 10D, 4A",
    "starting_example_title": "Lesson 14B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/14B",
    "starting_example_note": "Open lessons/14B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "15B": {
    "key": "15B",
    "description": "15B Design a font-cycling algorithm",
    "skill": "Algorithmic Thinking",
    "difficulty": "M",
    "estimated": "30m",
    "priority": "M",
    "depends": [
      "11A",
      "14B"
    ],
    "instructions": "Using the local lessons/15B/starter font selector, write original pseudocode for moving through fonts in both directions, including first/last and a one-item edge case.",
    "done": "Pseudocode and a small flowchart cover both directions, normal selection, and boundary cases.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/15B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "11A, 14B",
    "starting_example_title": "Lesson 15B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/15B",
    "starting_example_note": "Open lessons/15B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "16B": {
    "key": "16B",
    "description": "16B Write a two-example remix brief",
    "skill": "Idea Generation",
    "difficulty": "M",
    "estimated": "30m",
    "priority": "M",
    "depends": [
      "1A",
      "14B"
    ],
    "instructions": "Choose components from the two complete local projects in lessons/16B, write a remix brief with core behavior, sources, minimal implementation and technical unknowns.",
    "done": "A one-page brief explains the purpose, source features, minimal version, and one or more technical questions to investigate.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/16B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "1A, 14B",
    "starting_example_title": "Lesson 16B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/16B",
    "starting_example_note": "Open lessons/16B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "17E": {
    "key": "17E",
    "description": "17E Arrays, Strings, and Bounds",
    "skill": "C Programming",
    "difficulty": "M",
    "estimated": "90m",
    "priority": "H",
    "depends": [
      "10D"
    ],
    "instructions": "Read arrays, indices, strings and bounded buffers. Extend the Emery word-selector starter to six choices and test wraparound and long labels.",
    "done": "Build works; selections wrap correctly, strings remain terminated and storage is valid throughout display lifetime.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/17E ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/17E-arrays-strings.md",
    "prereq_note": "10D",
    "starting_example_title": "Lesson 17E: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/17E",
    "starting_example_note": "Open lessons/17E/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "18F": {
    "key": "18F",
    "description": "18F Pointers, Indirection, and Memory Lifetime",
    "skill": "C Programming",
    "difficulty": "H",
    "estimated": "105m",
    "priority": "H",
    "depends": [
      "17E"
    ],
    "instructions": "Read pointer parameters, indirection, ownership and lifetime. Extend the coordinate-pointer app with a safe helper, and document Pebble resource cleanup.",
    "done": "Working application, pointer trace, NULL handling and ownership/lifetime explanation.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/18F ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/18F-pointers-memory.md",
    "prereq_note": "17E",
    "starting_example_title": "Lesson 18F: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/18F",
    "starting_example_note": "Open lessons/18F/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "19G": {
    "key": "19G",
    "description": "19G Structures, Enums, and Program State",
    "skill": "C Programming",
    "difficulty": "H",
    "estimated": "105m",
    "priority": "M",
    "depends": [
      "18F"
    ],
    "instructions": "Read structs, enums, static scope and state transitions. Extend the local mode app with PAUSED and mode-specific behavior.",
    "done": "Mode transition table plus running app demonstrating valid transitions, protected operations and fallback handling.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/19G ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/19G-structs-enums-state.md",
    "prereq_note": "18F",
    "starting_example_title": "Lesson 19G: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/19G",
    "starting_example_note": "Open lessons/19G/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "20C": {
    "key": "20C",
    "description": "20C Research an unfamiliar Pebble capability",
    "skill": "Resource Literacy",
    "difficulty": "H",
    "estimated": "60m",
    "priority": "M",
    "depends": [
      "17E",
      "14B"
    ],
    "instructions": "Research persistence from lessons/20C/starter, trace persist_exists/read/write and write an implementation plan using the current SDK documentation.",
    "done": "A technical note names the capability, links the documentation and example, lists relevant APIs and constraints, and proposes implementation steps.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/20C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "17E, 14B",
    "starting_example_title": "Lesson 20C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/20C",
    "starting_example_note": "Open lessons/20C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "21B": {
    "key": "21B",
    "description": "21B Diagnose a font-selection boundary bug",
    "skill": "Debugging and Testing",
    "difficulty": "M",
    "estimated": "45m",
    "priority": "M",
    "depends": [
      "17E",
      "6A",
      "15B"
    ],
    "instructions": "Use lessons/21B/starter with its deliberate index bug. Reproduce Up/Down behavior, inspect APP_LOG index traces, fix the faulty transition and retest every boundary.",
    "done": "The bug is reproducible, the cause is explained, and tests show that cycling works correctly at both ends of the list.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/21B ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "17E, 6A, 15B",
    "starting_example_title": "Lesson 21B: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/21B",
    "starting_example_note": "Open lessons/21B/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "22C": {
    "key": "22C",
    "description": "22C Develop an original Pebble app concept",
    "skill": "Idea Generation",
    "difficulty": "H",
    "estimated": "60m",
    "priority": "M",
    "depends": [
      "16B",
      "20C"
    ],
    "instructions": "Inspect the three complete local Emery examples in lessons/22C and develop three original ideas; compare feasibility, select one and write a minimal specification.",
    "done": "Three ideas are compared and one has a concise specification for purpose, interaction, minimum version, and technical uncertainty.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/22C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "16B, 20C",
    "starting_example_title": "Lesson 22C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/22C",
    "starting_example_note": "Open lessons/22C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "23C": {
    "key": "23C",
    "description": "23C Design a state machine for an app",
    "skill": "Algorithmic Thinking",
    "difficulty": "H",
    "estimated": "60m",
    "priority": "M",
    "depends": [
      "22C",
      "15B",
      "19G"
    ],
    "instructions": "Use lessons/23C/starter and your 22C app concept to specify a state machine: states, inputs, transitions, visible outputs, default cases and invalid events.",
    "done": "A state diagram and transition table describe all main states, triggers, resulting states, and visible responses, including important edge cases.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/23C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "22C, 15B, 19G",
    "starting_example_title": "Lesson 23C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/23C",
    "starting_example_note": "Open lessons/23C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "24H": {
    "key": "24H",
    "description": "24H Event-Driven Integration and Application Lifecycle",
    "skill": "C Programming",
    "difficulty": "H",
    "estimated": "150m",
    "priority": "M",
    "depends": [
      "19G",
      "23C"
    ],
    "instructions": "Read callback lifecycle, event subscriptions and persistence. Extend the local app with a second mode and show event-driven updates and correct cleanup.",
    "done": "Emery program demonstrates button/tick callbacks, persisted state, mode-dependent actions and safe teardown.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/24H ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md ; C reading: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/curriculum/c-programming/24H-events-lifecycle.md",
    "prereq_note": "19G, 23C",
    "starting_example_title": "Lesson 24H: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/24H",
    "starting_example_note": "Open lessons/24H/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "25C": {
    "key": "25C",
    "description": "25C Design a multi-mode Pebble interface",
    "skill": "UI Design",
    "difficulty": "H",
    "estimated": "90m",
    "priority": "M",
    "depends": [
      "13B",
      "22C",
      "23C",
      "24H"
    ],
    "instructions": "Use lessons/25C/starter (the licensed Simplicity C layout) to sketch multiple Emery screens/modes, navigation and button outcomes for your own concept.",
    "done": "A set of labeled sketches covers every main state, navigation between states, button outcomes, and screen-size considerations.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/25C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "13B, 22C, 23C, 24H",
    "starting_example_title": "Lesson 25C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/25C",
    "starting_example_note": "Open lessons/25C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "31C": {
    "key": "31C",
    "description": "31C Integrate font browsing with persistent selection",
    "skill": "Development Tools and Workflow",
    "difficulty": "H",
    "estimated": "150m",
    "priority": "M",
    "depends": [
      "25C",
      "24H",
      "14B",
      "7B"
    ],
    "instructions": "Combine the two complete but separate projects in lessons/31C (font selector and persistent counter). Implement saved font selection yourself, validate indices and verify restart behavior.",
    "done": "The combined app builds, font navigation works, the selected font survives a restart, invalid or absent stored values are handled safely, and Git records the work.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/31C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "25C, 24H, 14B, 7B",
    "starting_example_title": "Lesson 31C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/31C",
    "starting_example_note": "Open lessons/31C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  },
  "32C": {
    "key": "32C",
    "description": "32C Diagnose a persistent-state integration bug",
    "skill": "Debugging and Testing",
    "difficulty": "H",
    "estimated": "90m",
    "priority": "L",
    "depends": [
      "24H",
      "21B",
      "31C"
    ],
    "instructions": "Use lessons/32C/starter with its deliberate persistence fault. Select a nondefault font, restart, trace save/restore logs, correct the mismatch and retest.",
    "done": "A reproducible bug report records expected and actual behavior, the cause is explained, and the fix passes fresh-start, selection, and restart tests.",
    "resources": "Local complete lesson: https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/32C ; curriculum: https://github.com/Darachnid/c-for-pebble-programmers-course/blob/main/SYLLABUS.md",
    "prereq_note": "24H, 21B, 31C",
    "starting_example_title": "Lesson 32C: exact local Emery starter(s)",
    "starting_example_url": "https://github.com/Darachnid/c-for-pebble-programmers-course/tree/main/lessons/32C",
    "starting_example_note": "Open lessons/32C/README.md. The complete source and instructions are in this repository; no external example download.",
    "emery_rule": "Only emery (Pebble Time 2), 200x228 rectangular, Pebble SDK 4.33.1."
  }
}
COURSE_SEQUENCE = ["1A","2A","3A","4A","5A","6A","7B","8B","9C","10D","11A","13B","14B","15B","16B","17E","18F","19G","20C","21B","22C","23C","24H","25C","31C","32C"]
for item in TASKS:
    item.update(COURSE_V2[item["key"]])
for key in ("10D", "17E", "18F", "19G", "24H"):
    TASKS.append(dict(COURSE_V2[key]))
TASKS.sort(key=lambda item: COURSE_SEQUENCE.index(item["key"]))

# Supplement the legacy course with new numbered capability labs.
# Preserve the original 26 IDs and every user's recorded completion state.
from pathlib import Path
with (Path(__file__).parent / "extension_api_labs.json").open(encoding="utf-8") as extension_file:
    TASKS.extend(json.load(extension_file))

# The initial 41 activity IDs (before sequential renumbering) map to the same
# underlying tasks. This allows in-place UUID migration without loss of progress.
LEGACY_MAP = json.loads((Path(__file__).parent / "legacy-id-map.json").read_text(encoding="utf-8"))
LEGACY_TO_CURRENT = LEGACY_MAP["old_to_new"]
LEGACY_TITLES = LEGACY_MAP["old_titles"]
TASKS.sort(key=lambda task: int(re.match(r"^\d+", task["key"]).group()))

# Core activities also explicitly develop a second competency.
FOUNDATION_SUPPORTING = {"5A":"Resource Literacy","13B":"C Programming","25C":"Idea Generation","1A":"Resource Literacy","16B":"UI Design","22C":"Resource Literacy","11A":"C Programming","15B":"UI Design","23C":"UI Design","3A":"Debugging and Testing","8B":"Algorithmic Thinking","9C":"Algorithmic Thinking","10D":"Algorithmic Thinking","17E":"Debugging and Testing","18F":"Debugging and Testing","19G":"Algorithmic Thinking","24H":"Development Tools and Workflow","4A":"C Programming","14B":"Algorithmic Thinking","20C":"C Programming","6A":"Development Tools and Workflow","21B":"C Programming","32C":"Development Tools and Workflow","2A":"C Programming","7B":"Debugging and Testing","31C":"Debugging and Testing"}
for _task in TASKS:
    if _task["key"] in FOUNDATION_SUPPORTING:
        _task["supporting_competency"] = FOUNDATION_SUPPORTING[_task["key"]]

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
        f"Supporting competency: {t.get('supporting_competency', 'See course map')}",
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
        "Course ID:", "Supporting competency:", "Starting example:", "Starting example guidance:",
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


def legacy_migration_plan(records):
    """Identify course tasks by identity, never by the numeric prefix alone.

    An old 2A and a new 2A describe DIFFERENT lessons, so matching just the
    first word of the task description would corrupt completion history.
    """
    by_current = {item["key"]: item for item in TASKS}
    planned = {}
    for record in records:
        if record.get("status") == "deleted":
            continue
        uuid = record.get("uuid")
        desc = record.get("description", "")
        annotation = annotation_texts(record)
        old_id = None
        for note in annotation:
            if note.startswith("Legacy lesson ID: "):
                candidate = note.removeprefix("Legacy lesson ID: ").strip()
                if candidate in LEGACY_TO_CURRENT:
                    old_id = candidate
                    break
        if old_id is None:
            for note in annotation:
                match = re.match(r"^Course ID: (\d+[A-Z])\s*\|", note)
                if match:
                    candidate = match.group(1)
                    if candidate not in LEGACY_TO_CURRENT:
                        continue
                    canonical = by_current.get(candidate)
                    if canonical and desc == canonical["description"]:
                        # This record already belongs to the NEW numbered course.
                        continue
                    old_id = candidate
                    break
        if old_id is None:
            match = re.match(r"^(\d+[A-Z])\s+(.*)$", desc)
            if match:
                candidate, title = match.groups()
                if candidate in LEGACY_TITLES and title == LEGACY_TITLES[candidate]:
                    canonical = by_current.get(candidate)
                    if not canonical or desc != canonical["description"]:
                        old_id = candidate
        if old_id is None:
            continue
        new_id = LEGACY_TO_CURRENT[old_id]
        wanted = by_current[new_id]["description"]
        if desc == wanted and (old_id == new_id or f"Legacy lesson ID: {old_id}" in annotation):
            continue
        if not uuid:
            raise RuntimeError(f"Legacy course record {old_id} is missing UUID")
        if old_id in planned:
            raise RuntimeError(f"Multiple Taskwarrior records claim legacy lesson {old_id}; resolve duplicates before continuing")
        planned[old_id] = {"uuid": uuid, "old": old_id, "new": new_id,
                           "description": desc, "desired": wanted,
                           "status": record.get("status"),
                           "end": record.get("end"),
                           "has_marker": f"Legacy lesson ID: {old_id}" in annotation}
    # A fresh task with a new ID may already exist after a partial import.
    for entry in planned.values():
        for record in records:
            if record.get("uuid") == entry["uuid"] or record.get("status") == "deleted":
                continue
            current = by_current[entry["new"]]["description"]
            if record.get("description") == current:
                raise RuntimeError(f"Conflicting existing record for {entry['new']}; cannot safely merge two UUIDs")
    return list(planned.values())


def apply_legacy_id_migration(before, plan):
    """Rename existing UUIDs in-place; never create replacements.

    The snapshot is stored locally outside the Git history so a user can
    recover even if Taskwarrior is interrupted halfway through this step.
    """
    if not plan:
        return
    from datetime import datetime, timezone
    directory = Path(__file__).parent / "backups"
    directory.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    destination = directory / f"before-id-renumber-{stamp}.json"
    suffix = 1
    while destination.exists():
        destination = directory / f"before-id-renumber-{stamp}-{suffix}.json"
        suffix += 1
    destination.write_text(json.dumps(before, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Backup: {destination}")
    for row in plan:
        uuid = row["uuid"]
        if not row["has_marker"]:
            task_cmd(uuid, "annotate", f"Legacy lesson ID: {row['old']}")
        if row["description"] != row["desired"]:
            task_cmd(uuid, "modify", "description:" + row["desired"])
        print(f"Migrated {row['old']} -> {row['new']} (preserved UUID {uuid})")
    refreshed = {r.get("uuid"): r for r in course_export()}
    for row in plan:
        record = refreshed.get(row["uuid"])
        if not record or record.get("description") != row["desired"]:
            raise RuntimeError(f"Could not verify migrated UUID {row['uuid']}")
        if record.get("status") != row["status"] or record.get("end") != row["end"]:
            raise RuntimeError(f"Completion status/end date changed unexpectedly for {row['uuid']}")


def main():
    if not shutil.which("task"):
        print("Taskwarrior command `task` was not found on PATH.", file=sys.stderr)
        return 1

    try:
        before = course_export()
        renumber_plan = legacy_migration_plan(before)
        existing = {t["description"]: t for t in before
                    if t.get("status") != "deleted"}
        known_ids = {name.split(" ", 1)[0] for name in existing}
        matched = sum(1 for t in TASKS if t["key"] in known_ids)
        estimated_type = get_config("uda.estimated.type")
        effort_type = get_config("uda.effort.type")
        print(f"Project: {PROJECT} | Activities: {len(TASKS)} | Target: emery (Pebble Time 2) only")
        print(f"Detected existing legacy lessons requiring safe UUID migration: {len(renumber_plan)}")
        print(f"Existing matching tasks: {matched} | New tasks needed: {len(TASKS)-matched}")
        print(f"Estimated UDA: {estimated_type or 'missing (will configure)'}")
        print(f"Effort UDA: {effort_type or 'missing (will configure)'}")
        print("Will replace only course-generated annotations, preserve personal notes, update metadata, and set dependency links.")
        print("Existing completed tasks will be preserved; matching tasks will not be duplicated.")
        confirm = input("Type CREATE to proceed: ").strip()
        if confirm != "CREATE":
            print("Cancelled; no changes made.")
            return 0

        apply_legacy_id_migration(before, renumber_plan)
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
