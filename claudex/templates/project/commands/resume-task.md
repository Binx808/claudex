# Task Resume Assistant

Recover task context from session files after conversation compacting.

## Process

1. **Read session files** in order: CURRENT_TASK.md, TASK_PROGRESS.md, VALIDATION_STATE.md, CONTEXT_SUMMARY.md
2. **Reconstruct context**: identify task, understand progress, review decisions
3. **Identify next action**: determine where we left off, find next micro task
4. **Present summary**: task name, progress, key decisions, validation state, next step

## When to Use

- At start of new conversation
- After context compaction
- When unsure of current task state

**Invocation**: `/resume-task`
