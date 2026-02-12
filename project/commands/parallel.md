# Parallel Session Orchestrator

Plan and manage parallel Claude Code sessions for maximum throughput.

## Sub-commands

Determine which sub-command the user wants from their arguments:

### `/parallel plan <feature>`

Analyze a feature and produce a parallel session plan:

1. **Direct**: Frame the feature
   - Read the feature description/requirements
   - Identify all files that will need changes
   - Map dependencies between changes

2. **Dissect**: Split into sessions
   - Group changes by file ownership (no overlap)
   - Determine dependency order (which sessions must merge first)
   - Identify conflict zones (files NO session should touch)

3. **Output**: Create PARALLEL_SESSIONS.md
   - Write session plan to `.claude/session/PARALLEL_SESSIONS.md`
   - Include: session table, merge order, conflict zones
   - Generate worktree creation commands

4. **Present**: Show the plan to user for approval

### `/parallel status`

Check current parallel session status:

1. Run `git worktree list` to see active worktrees
2. Read `.claude/session/PARALLEL_SESSIONS.md` for planned sessions
3. Cross-reference: which sessions are active, which are done
4. Report status of each session

### `/parallel merge-order`

Determine correct merge sequence:

1. Read PARALLEL_SESSIONS.md
2. Analyze file dependencies between sessions
3. Output ordered merge list with commands

### `/parallel cleanup`

Remove completed parallel worktrees:

1. Read PARALLEL_SESSIONS.md
2. For each DONE session:
   - Verify PR was merged
   - Run `git worktree remove ../<project>-<session>`
   - Update PARALLEL_SESSIONS.md
3. If all sessions done, archive PARALLEL_SESSIONS.md
