# Integrated learning sequence — 41 activities

**Purpose:** this is the recommended learning order, NOT five isolated topic blocks. The 14 Pebble API labs are interleaved with foundational programming, UI, debugging, research, and workflow tasks. Follow Taskwarrior's **actual prerequisites** if working out of order. Work across the three recurring projects as each becomes available.

| Phase | Learning emphasis | IDs in recommended order |
|---|---|---|
| I | Orientation, C basics, diagnostics and Git | 1A → 2A → 3A → 4A → 5A → 6A → 7B |
| II | Control flow, design, and first reusable Windows | 8B → 9C → 10D → 11A → 12A → 13B → 14B → 15B → 16B |
| III | Memory, state, creativity, and interactive foundations | 17E → 18F → 19G → 20C → 21B → 22C → 23C → 24H → 25C → 26B → 27C → 28D → 29E → 30G |
| IV | Hardware/graphics integration, validation and persistence | 31C → 32C → 33F → 34H → 35I → 36J → 37K → 38L → 39M → 40N |
| V | Independent synthesis and competency demonstration | 41A |

## Cross-competency map

Each task has one **primary** and one **supporting** assessment lens; this is not a limitation on what the task may teach. Levels and evidence criteria are defined in [Learning outcomes and assessment](learning-outcomes-and-assessment.md).

| Phase | ID | Primary competency | Supporting competency | Dependencies (added labs) |
|---|---|---|---|---|
| I | [1A](../../lessons/1A/) | Idea Generation | Resource Literacy | See existing syllabus |
| I | [2A](../../lessons/2A/) | Development Tools and Workflow | C Programming | See existing syllabus |
| I | [3A](../../lessons/3A/) | C Programming | Debugging and Testing | See existing syllabus |
| I | [4A](../../lessons/4A/) | Resource Literacy | C Programming | See existing syllabus |
| I | [5A](../../lessons/5A/) | UI Design | Resource Literacy | See existing syllabus |
| I | [6A](../../lessons/6A/) | Debugging and Testing | Development Tools and Workflow | See existing syllabus |
| I | [7B](../../lessons/7B/) | Development Tools and Workflow | Debugging and Testing | See existing syllabus |
| II | [8B](../../lessons/8B/) | C Programming | Algorithmic Thinking | See existing syllabus |
| II | [9C](../../lessons/9C/) | C Programming | Algorithmic Thinking | See existing syllabus |
| II | [10D](../../lessons/10D/) | C Programming | Algorithmic Thinking | See existing syllabus |
| II | [11A](../../lessons/11A/) | Algorithmic Thinking | C Programming | See existing syllabus |
| II | [12A](../../lessons/12A/) | UI Design | Development Tools and Workflow | 2A, 11A |
| II | [13B](../../lessons/13B/) | UI Design | C Programming | See existing syllabus |
| II | [14B](../../lessons/14B/) | Resource Literacy | Algorithmic Thinking | See existing syllabus |
| II | [15B](../../lessons/15B/) | Algorithmic Thinking | UI Design | See existing syllabus |
| II | [16B](../../lessons/16B/) | Idea Generation | UI Design | See existing syllabus |
| III | [17E](../../lessons/17E/) | C Programming | Debugging and Testing | See existing syllabus |
| III | [18F](../../lessons/18F/) | C Programming | Debugging and Testing | See existing syllabus |
| III | [19G](../../lessons/19G/) | C Programming | Algorithmic Thinking | See existing syllabus |
| III | [20C](../../lessons/20C/) | Resource Literacy | C Programming | See existing syllabus |
| III | [21B](../../lessons/21B/) | Debugging and Testing | C Programming | See existing syllabus |
| III | [22C](../../lessons/22C/) | Idea Generation | Resource Literacy | See existing syllabus |
| III | [23C](../../lessons/23C/) | Algorithmic Thinking | UI Design | See existing syllabus |
| III | [24H](../../lessons/24H/) | C Programming | Development Tools and Workflow | See existing syllabus |
| III | [25C](../../lessons/25C/) | UI Design | Idea Generation | See existing syllabus |
| III | [26B](../../lessons/26B/) | UI Design | Algorithmic Thinking | 17E, 24H |
| III | [27C](../../lessons/27C/) | Algorithmic Thinking | C Programming | 12A, 24H |
| III | [28D](../../lessons/28D/) | Idea Generation | UI Design | 26B, 10D |
| III | [29E](../../lessons/29E/) | Algorithmic Thinking | UI Design | 28D, 18F |
| III | [30G](../../lessons/30G/) | C Programming | Resource Literacy | 24H, 20C |
| IV | [31C](../../lessons/31C/) | Development Tools and Workflow | Debugging and Testing | See existing syllabus |
| IV | [32C](../../lessons/32C/) | Debugging and Testing | Development Tools and Workflow | See existing syllabus |
| IV | [33F](../../lessons/33F/) | C Programming | Debugging and Testing | 29E, 18F |
| IV | [34H](../../lessons/34H/) | Resource Literacy | C Programming | 30G |
| IV | [35I](../../lessons/35I/) | Resource Literacy | UI Design | 30G, 20C |
| IV | [36J](../../lessons/36J/) | Debugging and Testing | UI Design | 30G, 24H |
| IV | [37K](../../lessons/37K/) | Debugging and Testing | Algorithmic Thinking | 27C, 24H |
| IV | [38L](../../lessons/38L/) | Idea Generation | Resource Literacy | 33F, 20C |
| IV | [39M](../../lessons/39M/) | Development Tools and Workflow | Debugging and Testing | 37K, 24H |
| IV | [40N](../../lessons/40N/) | Development Tools and Workflow | C Programming | 38L, 24H, 7B |
| V | [41A](../../lessons/41A/) | Integrated: all seven | All seven | 22C, 25C, 32C, 36J, 39M, 40N |

## Conceptual introduction versus advanced application

- **25C** sketches interfaces; **12A** implements window and layer lifecycles. A drawing/design activity can precede the detailed API lab without requiring API mastery.
- **24H** introduces basic tick/button callbacks and a single persistence pattern; **27C** builds multi-window navigation; **39M** hardens persistence with missing/corrupt data and restart testing.
- **31C** performs introductory font-selection persistence before **39M** generalizes persistent settings and validation; the later activity does not retroactively become a prerequisite for the earlier one.
- **26B** begins its own Field Guide project after C data structures and the event-driven C introduction; it has no artificial dependency on the Clock Workshop project 12A.
- **30G** begins a separate Field Instrument strand and needs callbacks/research skills, not completion of the other project's buttons lab.

**Progress checkpoints:** At the end of each phase, use the readiness gate and reflection rubric. The capstone is an original working app, not only the 22C concept or the 25C drawings.
