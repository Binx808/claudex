# Parallel Development (Git Worktrees)

## Why Worktrees

When running multiple Claude Code sessions in parallel, **NEVER** `git checkout` or `git switch` in a shared working directory. This breaks all other active sessions.

## Rules

1. **One branch per worktree** - each parallel session gets its own worktree
2. **Never checkout in the main directory** if other sessions are active
3. **Create worktrees from the main directory**:
   ```bash
   # From the primary repo directory:
   git worktree add ../project-name-taskname -b <branch-name> origin/main
   ```
4. **List active worktrees** before starting: `git worktree list`
5. **Clean up after merge**: `git worktree remove ../project-name-taskname`
6. **Max 5 concurrent sessions** - beyond this, coordination overhead exceeds benefit

## Direct -> Dissect -> Delegate Framework

### 1. Direct (Frame the feature)
- Define the goal, constraints, and success criteria
- Identify all files that will be touched

### 2. Dissect (Split into parallel threads)
- Group files by ownership - each thread owns distinct files
- Identify dependency order for merge sequence
- Create PARALLEL_SESSIONS.md with the session plan
- Mark conflict zones (files NO session may touch)

### 3. Delegate (Assign to sessions)
- Create worktrees for each session
- Each session reads PARALLEL_SESSIONS.md for coordination
- Sessions update their status in PARALLEL_SESSIONS.md when done

## Coordination

- **PARALLEL_SESSIONS.md** is the primary coordination file
- Session docs (CURRENT_TASK.md, TASK_PROGRESS.md) are per-session
- Split tasks by **file ownership** - no two sessions edit the same files
- Merge in dependency order (base modules first, dependents second)
- If Session B depends on Session A's changes, B rebases after A merges

## Anti-Patterns

- **Shared file edits**: Two sessions touching the same file = guaranteed conflicts
- **No coordination file**: Without PARALLEL_SESSIONS.md, sessions can't see each other
- **Skipping merge order**: Merging dependents before base = broken imports
- **Too many sessions**: >5 sessions creates more coordination overhead than time saved

## Before Any Branch Operation

```bash
# ALWAYS check first
git worktree list

# If other worktrees exist, create a new one instead of checking out
git worktree add ../project-taskname -b fix/my-task origin/main

# NEVER do this if other sessions are active:
# git checkout main        <- BREAKS other sessions
# git switch feature/x     <- BREAKS other sessions
```
