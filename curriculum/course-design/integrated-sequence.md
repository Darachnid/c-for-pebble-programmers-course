# Integrated learning sequence — 41 activities

**Purpose:** this is the recommended learning order, NOT five isolated topic blocks. The 14 Pebble API labs are interleaved with foundational programming, UI, debugging, research, and workflow tasks. Follow Taskwarrior's **actual prerequisites** if working out of order. Work across the three recurring projects as each becomes available.

| Phase | Learning emphasis | IDs in recommended order |
|---|---|---|
| I | Orientation, C basics, diagnostics and Git | 2A → 7A → 4A → 5A → 1A → 6A → 7B |
| II | Control flow, design, and first reusable Windows | 4B → 4C → 4D → 3A → 8A → 1B → 5B → 3B → 2B |
| III | Memory, state, creativity, and interactive foundations | 4E → 4F → 4G → 5C → 6B → 2C → 3C → 4H → 1C → 8B → 8C → 8D → 8E → 8G |
| IV | Hardware/graphics integration, validation and persistence | 7C → 6C → 8F → 8H → 8I → 8J → 8K → 8L → 8M → 8N |
| V | Independent synthesis and competency demonstration | 9A |

## Cross-competency map

Each task has one **primary** and one **supporting** assessment lens; this is not a limitation on what the task may teach. Levels and evidence criteria are defined in [Learning outcomes and assessment](learning-outcomes-and-assessment.md).

| Phase | ID | Primary competency | Supporting competency | Dependencies (added labs) |
|---|---|---|---|---|
| I | [2A](../../lessons/2A/) | Idea Generation | Resource Literacy | See existing syllabus |
| I | [7A](../../lessons/7A/) | Development Tools and Workflow | C Programming | See existing syllabus |
| I | [4A](../../lessons/4A/) | C Programming | Debugging and Testing | See existing syllabus |
| I | [5A](../../lessons/5A/) | Resource Literacy | C Programming | See existing syllabus |
| I | [1A](../../lessons/1A/) | UI Design | Resource Literacy | See existing syllabus |
| I | [6A](../../lessons/6A/) | Debugging and Testing | Development Tools and Workflow | See existing syllabus |
| I | [7B](../../lessons/7B/) | Development Tools and Workflow | Debugging and Testing | See existing syllabus |
| II | [4B](../../lessons/4B/) | C Programming | Algorithmic Thinking | See existing syllabus |
| II | [4C](../../lessons/4C/) | C Programming | Algorithmic Thinking | See existing syllabus |
| II | [4D](../../lessons/4D/) | C Programming | Algorithmic Thinking | See existing syllabus |
| II | [3A](../../lessons/3A/) | Algorithmic Thinking | C Programming | See existing syllabus |
| II | [8A](../../lessons/8A/) | UI Design | Development Tools and Workflow | 7A, 3A |
| II | [1B](../../lessons/1B/) | UI Design | C Programming | See existing syllabus |
| II | [5B](../../lessons/5B/) | Resource Literacy | Algorithmic Thinking | See existing syllabus |
| II | [3B](../../lessons/3B/) | Algorithmic Thinking | UI Design | See existing syllabus |
| II | [2B](../../lessons/2B/) | Idea Generation | UI Design | See existing syllabus |
| III | [4E](../../lessons/4E/) | C Programming | Debugging and Testing | See existing syllabus |
| III | [4F](../../lessons/4F/) | C Programming | Debugging and Testing | See existing syllabus |
| III | [4G](../../lessons/4G/) | C Programming | Algorithmic Thinking | See existing syllabus |
| III | [5C](../../lessons/5C/) | Resource Literacy | C Programming | See existing syllabus |
| III | [6B](../../lessons/6B/) | Debugging and Testing | C Programming | See existing syllabus |
| III | [2C](../../lessons/2C/) | Idea Generation | Resource Literacy | See existing syllabus |
| III | [3C](../../lessons/3C/) | Algorithmic Thinking | UI Design | See existing syllabus |
| III | [4H](../../lessons/4H/) | C Programming | Development Tools and Workflow | See existing syllabus |
| III | [1C](../../lessons/1C/) | UI Design | Idea Generation | See existing syllabus |
| III | [8B](../../lessons/8B/) | UI Design | Algorithmic Thinking | 4E, 4H |
| III | [8C](../../lessons/8C/) | Algorithmic Thinking | C Programming | 8A, 4H |
| III | [8D](../../lessons/8D/) | Idea Generation | UI Design | 8B, 4D |
| III | [8E](../../lessons/8E/) | Algorithmic Thinking | UI Design | 8D, 4F |
| III | [8G](../../lessons/8G/) | C Programming | Resource Literacy | 4H, 5C |
| IV | [7C](../../lessons/7C/) | Development Tools and Workflow | Debugging and Testing | See existing syllabus |
| IV | [6C](../../lessons/6C/) | Debugging and Testing | Development Tools and Workflow | See existing syllabus |
| IV | [8F](../../lessons/8F/) | C Programming | Debugging and Testing | 8E, 4F |
| IV | [8H](../../lessons/8H/) | Resource Literacy | C Programming | 8G |
| IV | [8I](../../lessons/8I/) | Resource Literacy | UI Design | 8G, 5C |
| IV | [8J](../../lessons/8J/) | Debugging and Testing | UI Design | 8G, 4H |
| IV | [8K](../../lessons/8K/) | Debugging and Testing | Algorithmic Thinking | 8C, 4H |
| IV | [8L](../../lessons/8L/) | Idea Generation | Resource Literacy | 8F, 5C |
| IV | [8M](../../lessons/8M/) | Development Tools and Workflow | Debugging and Testing | 8K, 4H |
| IV | [8N](../../lessons/8N/) | Development Tools and Workflow | C Programming | 8L, 4H, 7B |
| V | [9A](../../lessons/9A/) | Integrated: all seven | All seven | 2C, 1C, 6C, 8J, 8M, 8N |

## Conceptual introduction versus advanced application

- **1C** sketches interfaces; **8A** implements window and layer lifecycles. A drawing/design activity can precede the detailed API lab without requiring API mastery.
- **4H** introduces basic tick/button callbacks and a single persistence pattern; **8C** builds multi-window navigation; **8M** hardens persistence with missing/corrupt data and restart testing.
- **7C** performs introductory font-selection persistence before **8M** generalizes persistent settings and validation; the later activity does not retroactively become a prerequisite for the earlier one.
- **8B** begins its own Field Guide project after C data structures and the event-driven C introduction; it has no artificial dependency on the Clock Workshop project 8A.
- **8G** begins a separate Field Instrument strand and needs callbacks/research skills, not completion of the other project's buttons lab.

**Progress checkpoints:** At the end of each phase, use the readiness gate and reflection rubric. The capstone is an original working app, not only the 2C concept or the 1C drawings.
