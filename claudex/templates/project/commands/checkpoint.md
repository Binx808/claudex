# Checkpoint Manager

Save current task progress to session files to survive conversation compacting.

## Process

1. **Update CURRENT_TASK.md**: task description, criteria status, decisions, blockers
2. **Update TASK_PROGRESS.md**: mark completed items, note current focus, list next steps
3. **Update VALIDATION_STATE.md**: record checkpoints passed, issues found
4. **Update CONTEXT_SUMMARY.md**: recent decisions, files modified, critical context

## When to Run

- Before ending a session
- After completing a major milestone
- When asked to pause work
- Every 30 minutes during long tasks

**Invocation**: `/checkpoint`
