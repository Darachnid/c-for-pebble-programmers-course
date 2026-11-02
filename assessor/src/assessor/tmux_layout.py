"""tmux session layout for the single-command course driver."""
from __future__ import annotations

import os
import shlex
import shutil
import subprocess
from pathlib import Path

SESSION = "pebble-course"
WINDOW = "course"
# Window index 0 stays valid after rename-window changes the visible tab name.
LESSON_PANE = f"{SESSION}:0.0"
WIZARD_PANE = f"{SESSION}:0.1"
SHELL_PANE = f"{SESSION}:0.2"


def tmux_available() -> bool:
    return shutil.which("tmux") is not None


def session_exists(session: str = SESSION) -> bool:
    result = subprocess.run(
        ["tmux", "has-session", "-t", session],
        capture_output=True,
        check=False,
    )
    return result.returncode == 0


def wizard_shell_command(course_root: Path) -> str:
    root = shlex.quote(str(course_root))
    assessor = shlex.quote(str(course_root / "assessor"))
    return (
        f"cd {root} && PEBBLE_COURSE_ROOT={root} exec uv run --directory {assessor} "
        "python -m assessor.course_flow --inside-tmux"
    )


def shell_banner(pebble_workdir: Path, notes: str | None) -> str:
    lines = [
        f"cd {shlex.quote(str(pebble_workdir))}",
        "printf '%s\\n' 'pebble build' 'pebble install --emulator emery'",
    ]
    if notes:
        lines.append(f"printf '%s\\n' {shlex.quote(notes)}")
    return " && ".join(lines)


def layout_commands(
    *,
    course_root: Path,
    activity_id: str,
    title: str,
    lesson_readme: Path,
    pebble_workdir: Path,
    wizard_cmd: str,
    pebble_notes: str | None = None,
    inside_tmux: bool = False,
) -> list[list[str]]:
    """tmux invocations that create the three-pane course window.

    Pane 0 is the lesson (top-left), pane 1 is the wizard (bottom), pane 2 is
    the Pebble shell (top-right).
    """
    target = f"{SESSION}:0"
    status_right = f"{activity_id} {title}"
    lesson_cmd = f"less -R {shlex.quote(str(lesson_readme))}"
    banner = shell_banner(pebble_workdir, pebble_notes)
    cmds: list[list[str]] = [
        [
            "tmux",
            "new-session",
            "-d",
            "-s",
            SESSION,
            "-n",
            WINDOW,
            "-c",
            str(course_root),
        ],
        [
            "tmux",
            "split-window",
            "-v",
            "-t",
            f"{target}.0",
            "-p",
            "40",
            "-c",
            str(course_root),
        ],
        [
            "tmux",
            "split-window",
            "-h",
            "-t",
            f"{target}.0",
            "-p",
            "40",
            "-c",
            str(pebble_workdir),
        ],
        ["tmux", "select-pane", "-t", LESSON_PANE, "-T", "lesson"],
        ["tmux", "select-pane", "-t", WIZARD_PANE, "-T", "wizard"],
        ["tmux", "select-pane", "-t", SHELL_PANE, "-T", "shell"],
        ["tmux", "send-keys", "-t", LESSON_PANE, lesson_cmd, "Enter"],
        ["tmux", "send-keys", "-t", SHELL_PANE, banner, "Enter"],
        ["tmux", "send-keys", "-t", WIZARD_PANE, wizard_cmd, "Enter"],
        ["tmux", "select-pane", "-t", WIZARD_PANE],
        ["tmux", "rename-window", "-t", target, activity_id],
        [
            "tmux",
            "set-option",
            "-t",
            SESSION,
            "status-right",
            status_right,
        ],
    ]
    if inside_tmux:
        cmds.append(["tmux", "switch-client", "-t", SESSION])
    else:
        cmds.append(["tmux", "attach-session", "-t", SESSION])
    return cmds


def refresh_activity_panes(
    *,
    activity_id: str,
    title: str,
    lesson_readme: Path,
    pebble_workdir: Path,
    pebble_notes: str | None = None,
) -> None:
    """Point the lesson and shell panes at the next activity. Leave the wizard pane."""
    target = f"{SESSION}:0"
    lesson_cmd = f"less -R {shlex.quote(str(lesson_readme))}"
    banner = shell_banner(pebble_workdir, pebble_notes)
    subprocess.run(
        ["tmux", "respawn-pane", "-k", "-t", LESSON_PANE, lesson_cmd],
        check=False,
    )
    subprocess.run(
        ["tmux", "send-keys", "-t", SHELL_PANE, "C-u", banner, "Enter"],
        check=False,
    )
    subprocess.run(["tmux", "rename-window", "-t", target, activity_id], check=False)
    subprocess.run(
        ["tmux", "set-option", "-t", SESSION, "status-right", f"{activity_id} {title}"],
        check=False,
    )


def launch_session(commands: list[list[str]]) -> None:
    """Run every tmux command except the last, then replace this process with it.

    The last command is attach-session or switch-client.
    """
    if not commands:
        raise SystemExit("No tmux commands to run.")
    for argv in commands[:-1]:
        subprocess.run(argv, check=True)
    attach = commands[-1]
    os.execvp(attach[0], attach)
