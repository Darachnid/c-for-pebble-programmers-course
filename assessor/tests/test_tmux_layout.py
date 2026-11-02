from pathlib import Path

from assessor.tmux_layout import layout_commands, wizard_shell_command


def test_layout_commands_cover_session_lesson_shell_and_wizard(tmp_path: Path):
    root = tmp_path / "course"
    lesson = root / "lessons" / "1A" / "README.md"
    work = root / "lessons" / "1A" / "clock"
    commands = layout_commands(
        course_root=root,
        activity_id="1A",
        title="Explore Pebble examples",
        lesson_readme=lesson,
        pebble_workdir=work,
        wizard_cmd=wizard_shell_command(root),
        pebble_notes="Also inspect fonts",
    )
    flat = [" ".join(argv) for argv in commands]
    joined = "\n".join(flat)
    assert "new-session -d -s pebble-course" in joined
    assert "split-window -v" in joined
    assert "split-window -h" in joined
    assert str(lesson) in joined
    assert str(work) in joined
    assert "--inside-tmux" in joined
    assert "attach-session -t pebble-course" in joined
    assert flat[-1].startswith("tmux attach-session")


def test_layout_switches_client_when_already_inside_tmux(tmp_path: Path):
    root = tmp_path / "course"
    commands = layout_commands(
        course_root=root,
        activity_id="2A",
        title="Build",
        lesson_readme=root / "lessons/2A/README.md",
        pebble_workdir=root / "lessons/2A/starter",
        wizard_cmd=wizard_shell_command(root),
        inside_tmux=True,
    )
    assert commands[-1][:4] == ["tmux", "switch-client", "-t", "pebble-course"]
