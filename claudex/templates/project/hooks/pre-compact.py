#!/usr/bin/env python3
"""PreCompact Hook — State extraction + auto-checkpoint before context compaction.

Runs before Claude compresses the conversation context:
- Extracts full structured session state into PRE_COMPACT_SNAPSHOT.md
- Marks TASK_PROGRESS.md with checkpoint timestamp
- Snapshot survives compaction and provides re-injection context
"""

import json
import re
from datetime import UTC, datetime
from pathlib import Path


def get_project_root() -> Path:
    current = Path.cwd()
    while current != current.parent:
        if (current / ".claude").exists():
            return current
        current = current.parent
    return Path.cwd()


def read_section(text: str, heading: str) -> str:
    """Extract a section from markdown content by heading."""
    if heading not in text:
        return ""
    parts = text.split(heading)[1]
    # Stop at next ## heading
    next_heading = re.search(r"\n##\s", parts)
    if next_heading:
        parts = parts[: next_heading.start()]
    return parts.strip()[:500]  # Cap at 500 chars per section


def extract_state(session_dir: Path) -> dict:
    """Extract structured state from all session files."""
    state = {
        "task": None,
        "phase": None,
        "completed_steps": [],
        "active_decisions": [],
        "modified_files": [],
        "current_phase_detail": None,
        "next_actions": [],
        "validation_gates": [],
    }

    # From CURRENT_TASK.md
    current_task = session_dir / "CURRENT_TASK.md"
    if current_task.exists():
        try:
            text = current_task.read_text(encoding="utf-8")
            desc = read_section(text, "## Task Description")
            if desc:
                state["task"] = desc.split("\n")[0].strip()[:120]
            phase_section = read_section(text, "## Current Phase")
            if phase_section:
                state["phase"] = phase_section.split("\n")[0].strip()
        except Exception:
            pass

    # From TASK_PROGRESS.md
    progress_file = session_dir / "TASK_PROGRESS.md"
    if progress_file.exists():
        try:
            text = progress_file.read_text(encoding="utf-8")
            for line in text.split("\n"):
                line = line.strip()
                is_done = re.match(r"^[-\u2705]\s*\[x\]", line, re.IGNORECASE) or line.startswith(
                    "\u2705"
                )
                if is_done:
                    step = re.sub(r"^[-\u2705\s\[x\]]+", "", line, flags=re.IGNORECASE).strip()
                    if step:
                        state["completed_steps"].append(step)
                elif re.match(r"^-\s*\[\s\]", line):
                    action = re.sub(r"^-\s*\[\s\]\s*", "", line).strip()
                    if action:
                        state["next_actions"].append(action)
            state["completed_steps"] = state["completed_steps"][-8:]
            state["next_actions"] = state["next_actions"][:5]
        except Exception:
            pass

    # From CONTEXT_SUMMARY.md
    context_file = session_dir / "CONTEXT_SUMMARY.md"
    if context_file.exists():
        try:
            text = context_file.read_text(encoding="utf-8")
            decisions_section = read_section(text, "## Decisions")
            if not decisions_section:
                decisions_section = read_section(text, "## Architectural Decisions")
            for line in decisions_section.split("\n"):
                line = line.strip().lstrip("- ").strip()
                if line and len(line) > 10:
                    state["active_decisions"].append(line[:120])
            state["active_decisions"] = state["active_decisions"][:5]

            files_section = read_section(text, "## Files Modified")
            if not files_section:
                files_section = read_section(text, "## Files Modified This Session")
            for line in files_section.split("\n"):
                line = line.strip()
                if line.startswith("-"):
                    state["modified_files"].append(line.lstrip("- ").strip()[:80])
            state["modified_files"] = state["modified_files"][:10]
        except Exception:
            pass

    # From VALIDATION_STATE.md
    validation_file = session_dir / "VALIDATION_STATE.md"
    if validation_file.exists():
        try:
            text = validation_file.read_text(encoding="utf-8")
            for line in text.split("\n"):
                if "\u2705" in line or "\u274c" in line or "[x]" in line.lower():
                    gate = line.strip()[:80]
                    if gate:
                        state["validation_gates"].append(gate)
            state["validation_gates"] = state["validation_gates"][:6]
        except Exception:
            pass

    return state


def write_snapshot(session_dir: Path, state: dict, timestamp: str):
    """Write PRE_COMPACT_SNAPSHOT.md with extracted state."""
    snapshot_file = session_dir / "PRE_COMPACT_SNAPSHOT.md"

    lines = [
        "# Pre-Compact Snapshot",
        f"_Saved: {timestamp}_",
        "_Re-inject this context after compaction to restore session state._",
        "",
    ]

    if state["task"]:
        lines += ["## Active Task", state["task"], ""]

    if state["phase"]:
        lines += ["## Current Phase", state["phase"], ""]

    if state["completed_steps"]:
        lines += ["## Completed Steps"]
        for s in state["completed_steps"]:
            lines.append(f"- \u2705 {s}")
        lines.append("")

    if state["next_actions"]:
        lines += ["## Next Actions"]
        for a in state["next_actions"]:
            lines.append(f"- [ ] {a}")
        lines.append("")

    if state["active_decisions"]:
        lines += ["## Architectural Decisions Made"]
        for d in state["active_decisions"]:
            lines.append(f"- {d}")
        lines.append("")

    if state["modified_files"]:
        lines += ["## Files Modified This Session"]
        for f in state["modified_files"]:
            lines.append(f"- {f}")
        lines.append("")

    if state["validation_gates"]:
        lines += ["## Validation Gate Status"]
        for g in state["validation_gates"]:
            lines.append(f"  {g}")
        lines.append("")

    lines += [
        "---",
        "_To resume: read this file and continue from Current Phase / Next Actions above._",
    ]

    try:
        snapshot_file.write_text("\n".join(lines), encoding="utf-8")
    except Exception:
        pass


def auto_checkpoint(project_root: Path, timestamp: str) -> dict:
    """Mark TASK_PROGRESS.md and create PRE_COMPACT_SNAPSHOT.md."""
    session_dir = project_root / ".claude" / "session"

    if not session_dir.exists():
        return {"status": "skip"}

    current_task = session_dir / "CURRENT_TASK.md"
    if not current_task.exists():
        return {"status": "skip"}

    # Mark progress file
    progress_file = session_dir / "TASK_PROGRESS.md"
    if progress_file.exists():
        try:
            content = progress_file.read_text(encoding="utf-8")
            marker = f"\n\n---\n_Auto-checkpoint before compaction: {timestamp}_\n"
            progress_file.write_text(content + marker, encoding="utf-8")
        except Exception:
            pass

    # Extract and write snapshot
    state = extract_state(session_dir)
    write_snapshot(session_dir, state, timestamp)

    return {"status": "ok", "checkpointed_at": timestamp}


def main():
    project_root = get_project_root()
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    result = auto_checkpoint(project_root, now)
    output = {"status": result.get("status", "ok")}
    if result.get("checkpointed_at"):
        ts = result["checkpointed_at"]
        output["user_message"] = (
            f"Pre-compact snapshot saved ({ts}) \u2014 state preserved in PRE_COMPACT_SNAPSHOT.md"
        )
    print(json.dumps(output))


if __name__ == "__main__":
    main()
