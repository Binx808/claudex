# Background Queue Manager

Manage the background agent task queue for async development work.

## Sub-commands

Determine which sub-command the user wants from their arguments:

### `/background-queue add <description>`

Add a new task to the background queue:

1. Read `.claude/session/BACKGROUND_QUEUE.md`
2. Generate next ID (BG-NNN format)
3. Append new row to the Queue table:
   - **ID**: BG-NNN
   - **Description**: from user input
   - **Branch**: auto-generate as `bg/<short-description>`
   - **GH Issue**: ask user or leave TBD
   - **Criteria**: ask user for done criteria or infer from description
   - **Status**: QUEUED
   - **Created**: current date
4. Write updated file

### `/background-queue list`

Display all tasks by status:

1. Read `.claude/session/BACKGROUND_QUEUE.md`
2. Show QUEUED tasks first, then KICKED, then BLOCKED
3. Show completed tasks from the Completed table
4. Show summary: "N queued, N kicked, N completed"

### `/background-queue kick <id|all>`

Prepare background agent launch commands:

1. Read the specified task(s) from BACKGROUND_QUEUE.md
2. For each QUEUED task:
   a. Generate worktree command: `git worktree add ../<project>-<id> -b <branch> origin/main`
   b. Generate headless claude command with task-specific prompt
   c. Update status to KICKED
3. Output all commands as a copy-pasteable shell script block
4. Remind user: "Copy and run these commands. Agents will create PRs when done."

### `/background-queue review`

Check status of kicked background agents:

1. Run `git worktree list` to see active worktrees
2. Run `gh pr list --state open` to see open PRs
3. Cross-reference with KICKED tasks in BACKGROUND_QUEUE.md
4. For each:
   - If PR exists and CI passes: mark COMPLETED, move to Completed table, note PR#
   - If PR exists but CI fails: report failures
   - If no PR yet: report "still running or failed"
5. Suggest: "Run `/background-queue clean` to remove completed worktrees"

### `/background-queue clean`

Clean up completed background work:

1. For each COMPLETED task:
   - Remove worktree: `git worktree remove ../<project>-<id>`
   - Confirm PR was merged or close it
2. Archive completed tasks
3. Report cleanup summary

## Project-Specific Rules

- Every background task should reference a GitHub Issue (create one if needed)
- Background PRs target the main branch
- Max 5 concurrent background agents
