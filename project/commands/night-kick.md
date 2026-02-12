# Night Kick - Launch Background Agents

One-command launcher for the night queue. Reads BACKGROUND_QUEUE.md and generates everything needed to run agents overnight.

## What This Does

1. Read `.claude/session/BACKGROUND_QUEUE.md`
2. Filter tasks with status QUEUED (skip KICKED, BLOCKED, COMPLETED)
3. For each QUEUED task (up to 5):
   a. Generate `git worktree add` command
   b. Generate headless `claude` command with task-specific prompt
   c. Include: task description, done criteria, branch name, GH issue reference
4. Output as a single copy-pasteable shell script block
5. Update each task status from QUEUED to KICKED in BACKGROUND_QUEUE.md

## Output Format

```bash
#!/bin/bash
# Night Kick - Generated <date>
# Tasks: BG-001, BG-002, BG-003

# BG-001: <description>
git worktree add ../<project>-bg-001 -b bg/<short-desc> origin/main
cd ../<project>-bg-001 && claude --headless --prompt "<task prompt>" &

echo "Launched N background agents. Check progress tomorrow with /background-queue review"
```

## Safety

- If no QUEUED tasks exist, report "Nothing to kick" and exit
- If >5 QUEUED tasks, only kick the first 5 and warn about the rest
- Never auto-execute the commands - always output for user to copy-paste
