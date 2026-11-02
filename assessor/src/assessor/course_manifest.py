from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml
import re


@dataclass
class UserField:
    key: str
    section: str
    prompt: str


@dataclass
class Activity:
    id: str
    title: str
    depends: list[str]
    lesson_readme: str
    pebble_workdir: str
    assessor_rubric: str | None
    user_fields: list[UserField] = field(default_factory=list)
    pebble_notes: str | None = None


@dataclass
class CourseManifest:
    version: int
    sequence: list[str]
    activities: dict[str, Activity]

    def activity(self, activity_id: str) -> Activity:
        if activity_id not in self.activities:
            raise KeyError(f"Unknown activity {activity_id!r}")
        return self.activities[activity_id]


LESSON_QUESTIONS = {
  "6A": [
    "Compiler diagnostic",
    "Record the original compiler error and source location.",
    "Cause and minimal fix",
    "Explain what caused the error and the single change made.",
    "Successful rebuild",
    "Record the build result after the correction."
  ],
  "7B": [
    "Git baseline",
    "Record the known-good baseline commit.",
    "Modification commit",
    "Identify the changed feature and its commit.",
    "Diff and recovery",
    "Explain the diff and how you could restore the baseline."
  ],
  "8B": [
    "Conditional logic",
    "Identify the branches and predicates used in each assigned project.",
    "Branch outcomes",
    "Record results for each intended branch.",
    "Boundary conditions",
    "Record the limit or fallback case required by the exercise."
  ],
  "9C": [
    "Iteration implementation",
    "Identify the loops completed in each assigned project.",
    "Termination and output",
    "Explain stopping conditions and observed results.",
    "Edge cases",
    "Record empty, first/last, or limiting iteration cases where applicable."
  ],
  "10D": [
    "Functions completed",
    "List the required functions in each local project and their responsibilities.",
    "Inputs and return values",
    "Explain how data is passed and returned.",
    "Verification",
    "Record normal and edge-case results for each project."
  ],
  "11A": [
    "Lifecycle diagram",
    "Provide the diagram location or describe the startup, tick, and cleanup paths.",
    "Callbacks versus direct calls",
    "Identify which transitions the framework invokes and which your code calls."
  ],
  "12A": [
    "Window and layer hierarchy",
    "Describe the two screens and their root/child layers.",
    "Lifecycle evidence",
    "Describe load, unload, and destruction behavior.",
    "Display verification",
    "Record both screens' display observations."
  ],
  "13B": [
    "Time and date display",
    "Describe the two TextLayers and their updating behavior.",
    "Date layer lifecycle",
    "Explain creation, styling, attachment, updates and teardown.",
    "Layout observations",
    "Record legibility on the required screens."
  ],
  "14B": [
    "Source locations",
    "Record the file names and functions that process the input.",
    "Event trace",
    "Trace input to state mutation and display update.",
    "Documentation",
    "Identify the relevant SDK API references."
  ],
  "15B": [
    "Font-cycling pseudocode",
    "Give the pseudocode or its artifact location.",
    "Flowchart",
    "Describe or reference both navigation directions.",
    "Wraparound traces",
    "Show first/last boundary behavior."
  ],
  "16B": [
    "Two source examples",
    "Identify both original examples and the features to combine.",
    "Remix concept",
    "Explain intended use and a minimal working version.",
    "Open technical questions",
    "List the uncertainties identified in the brief."
  ],
  "17E": [
    "Array and string changes",
    "Describe six-message list, item lookup and safe label formatting.",
    "Index boundaries",
    "Record first and last index behavior.",
    "Long-string test",
    "Describe the result for an overlong label."
  ],
  "18F": [
    "Pointer-based helpers",
    "Identify the output-pointer rewrite and second helper.",
    "Ownership and lifetime",
    "Explain what each pointer refers to and who owns the TextLayer.",
    "NULL test",
    "Describe the deliberate NULL test and return to safe code."
  ],
  "19G": [
    "AppState and enums",
    "Describe the PAUSED state and timer count field.",
    "Mode transition table",
    "Provide the state/transition table or location.",
    "Mode tests",
    "Report EDIT, non-EDIT and default/fallback behavior."
  ],
  "20C": [
    "Capability and sources",
    "Name the researched capability and documentation/example links.",
    "APIs and constraints",
    "Identify required functions, limitations and fallbacks.",
    "Implementation outline",
    "Give the proposed implementation steps."
  ],
  "21B": [
    "Reproduction",
    "Give the button sequence and relevant index logs.",
    "Root cause and correction",
    "Explain the original selection defect and repair.",
    "Regression tests",
    "Describe both ends of the font list after correction."
  ],
  "22C": [
    "Three ideas",
    "Summarize or link the three competing app concepts.",
    "Selection rationale",
    "Compare feasibility, usefulness and uncertainties.",
    "Chosen specification",
    "Describe purpose, interaction and smallest working version."
  ],
  "23C": [
    "State diagram",
    "Provide the state diagram or artifact reference.",
    "Transition table",
    "Record triggers, destination states and visible responses.",
    "Unusual transitions",
    "Cover important edge or invalid event cases."
  ],
  "24H": [
    "Lifecycle and callbacks",
    "Identify the event handlers and initialization/cleanup flow.",
    "State integration",
    "Explain how event-driven behavior changes application state.",
    "Execution tests",
    "Record normal and edge-case operation."
  ],
  "25C": [
    "Multi-mode interface",
    "Describe screens, modes and navigation.",
    "Emery and Gabbro layouts",
    "Provide design artifacts or observations for both display shapes.",
    "Design rationale",
    "Explain visual hierarchy, interaction and feedback."
  ],
  "26B": [
    "Menu hierarchy",
    "Describe menu items and scrolling behavior.",
    "Selection interaction",
    "Document the intended result of item selection.",
    "Navigation checks",
    "Record first/last item and back-navigation behavior."
  ],
  "27C": [
    "Button mapping",
    "List button actions and navigation transitions.",
    "Window changes",
    "Describe visible results from input.",
    "Interaction checks",
    "Record normal and relevant boundary button sequences."
  ],
  "28D": [
    "Custom drawing",
    "Identify graphics drawing functions and what they render.",
    "Drawing updates",
    "Describe refresh/invalidation events.",
    "Display fit",
    "Record visible output on both watch shapes."
  ],
  "29E": [
    "Graphics path",
    "Describe the path points, creation and rendering.",
    "Transformations",
    "Explain movement/rotation or other path operations.",
    "Geometry checks",
    "Describe expected versus observed boundary placement."
  ],
  "30G": [
    "Accelerometer readings",
    "Identify the reading method and observed data.",
    "Motion behavior",
    "Explain the interpretation of sensor input.",
    "Sensor testing",
    "Distinguish emulator tests from any physical-watch verification."
  ],
  "31C": [
    "Font browser integration",
    "Describe font navigation and display updates.",
    "Persistent setting",
    "Record how selection is saved and restored.",
    "Restart test",
    "Report results across restart and boundary selections."
  ],
  "32C": [
    "Fault reproduction",
    "Record how the persistent-state bug appears.",
    "Diagnosis and correction",
    "Explain source, hypothesis and minimal fix.",
    "Regression evidence",
    "Report restart and invalid-state behavior after repair."
  ],
  "33F": [
    "Bitmap resources",
    "Identify assets and loading/drawing operations.",
    "Bitmap management",
    "Explain memory ownership and release.",
    "Display tests",
    "Describe observed rendering and dimensions."
  ],
  "34H": [
    "Compass readings",
    "Describe heading data acquisition and interpretation.",
    "Calibration and limits",
    "Record sensor availability and limitations.",
    "Heading tests",
    "Distinguish emulator behavior from physical hardware observations."
  ],
  "35I": [
    "Backlight control",
    "Explain the actual controllable APIs and app behavior.",
    "Ambient-light limitations",
    "Distinguish supported data from unsupported sensor assumptions.",
    "Fallback behavior",
    "Describe how the app behaves without ambient light data."
  ],
  "36J": [
    "Vibration patterns",
    "Identify patterns or triggers used.",
    "User experience",
    "Explain when vibration is appropriate.",
    "Hardware verification",
    "State what was tested on real hardware versus emulator."
  ],
  "37K": [
    "Timer lifecycle",
    "Identify schedule, callback, cancel and reschedule behavior.",
    "State transitions",
    "Explain how timer callbacks affect the UI.",
    "Timing edge cases",
    "Record cancellation or repeated-timer behavior."
  ],
  "38L": [
    "Resource files",
    "List the included assets and resource identifiers.",
    "Resource loading",
    "Explain retrieval and ownership.",
    "Missing/invalid resource handling",
    "Describe the appropriate fallback or error behavior."
  ],
  "39M": [
    "Persisted values",
    "Identify stored data, keys and read/write functions.",
    "Startup defaults",
    "Describe missing or invalid data handling.",
    "Restart verification",
    "Record state restored after relaunch."
  ],
  "40N": [
    "Phone messaging",
    "Describe request/response payloads and handlers.",
    "Disconnected behavior",
    "Explain what happens when the phone is unavailable.",
    "Communication tests",
    "Record messages and failures observed."
  ],
  "41A": [
    "Original app and purpose",
    "Provide project location and intended user interaction.",
    "Implemented features",
    "Describe the working application and its main screens.",
    "Testing evidence",
    "Record Emery/Gabbro checks and relevant boundary/failure cases.",
    "Design and technical decisions",
    "Explain architecture, tradeoffs and remaining limitations.",
    "Demonstration and reflection",
    "Reference the demonstration and assess achievement of the existing capstone criteria."
  ]
}


def lesson_worksheet(activity_id: str) -> list[UserField]:
    questions = LESSON_QUESTIONS[activity_id]
    return [UserField(f"answer_{i+1}", f"## {questions[i]}", questions[i+1]) for i in range(0, len(questions), 2)]


def manifest_path(assessor_root: Path) -> Path:
    return assessor_root / "course" / "manifest.yaml"


def load_manifest(assessor_root: Path) -> CourseManifest:
    path = manifest_path(assessor_root)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    activities: dict[str, Activity] = {}
    for aid, raw in data.get("activities", {}).items():
        fields = [
            UserField(
                key=f["key"],
                section=f["section"],
                prompt=str(f["prompt"]).strip(),
            )
            for f in raw.get("user_fields", [])
        ]
        activities[aid] = Activity(
            id=aid,
            title=raw["title"],
            depends=list(raw.get("depends", [])),
            lesson_readme=raw["lesson_readme"],
            pebble_workdir=raw["pebble_workdir"],
            assessor_rubric=raw.get("assessor_rubric"),
            user_fields=fields,
            pebble_notes=raw.get("pebble_notes"),
        )
    # Discover the 41 activities in the authoritative lesson index.
    course_root = assessor_root.parent
    index = (course_root / "lessons" / "README.md").read_text(encoding="utf-8")
    pattern = r"^\| \[(\d+[A-Z])\]\([^)]+\) \| ([^|]+) \|[^|]+\| ([^|]+) \|"
    for match in re.finditer(pattern, index, re.MULTILINE):
        aid, title, depends = match.groups()
        if aid in activities:
            continue
        folder = course_root / "lessons" / f"{int(aid[:-1]):02d}{aid[-1]}"
        if not folder.is_dir():
            raise FileNotFoundError(f"Missing lesson directory: {folder}")
        projects = sorted(folder.glob("*/package.json"))
        workdir = projects[0].parent if projects else folder
        activities[aid] = Activity(
            id=aid, title=title.strip(),
            depends=re.findall(r"\d+[A-Z]", depends),
            lesson_readme=str((folder / "README.md").relative_to(course_root)),
            pebble_workdir=str(workdir.relative_to(course_root)),
            assessor_rubric=None,
            user_fields=lesson_worksheet(aid),
        )
    sequence = list(data["sequence"]) + [aid for aid in activities if aid not in data["sequence"]]
    return CourseManifest(
        version=int(data.get("version", 1)),
        sequence=sequence,
        activities=activities,
    )


def validate_manifest(course_root: Path, manifest: CourseManifest) -> None:
    for aid in manifest.sequence:
        if aid not in manifest.activities:
            raise ValueError(f"sequence lists {aid} but activities missing")
    for aid, act in manifest.activities.items():
        readme = course_root / act.lesson_readme
        if not readme.is_file():
            raise FileNotFoundError(f"{aid}: missing {act.lesson_readme}")
        workdir = course_root / act.pebble_workdir
        if not workdir.is_dir():
            raise FileNotFoundError(f"{aid}: missing pebble_workdir {act.pebble_workdir}")
        if act.assessor_rubric:
            rubric = course_root / "assessor" / act.assessor_rubric
            if not rubric.is_file():
                raise FileNotFoundError(f"{aid}: missing rubric {act.assessor_rubric}")
