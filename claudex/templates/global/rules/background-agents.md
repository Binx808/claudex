# Background Agent Rules

## What Background Agents Are

Background agents are headless Claude Code sessions that run autonomously on well-scoped tasks. Think of them as async junior devs: give clear specs, they deliver PRs.

## Scoping Rules (Non-Negotiable)

1. **Single-PR scope** — one agent = one PR = one concern
2. **Own worktree + branch** — never share working directory with another session
3. **Max 300 lines changed** — if larger, split into multiple agents
4. **Must include tests** — no code-only PRs from background agents
5. **Never touch main directly** — always branch, always PR
6. **No shared interface changes** — don't modify files other agents depend on

## Good Background Tasks

- "Add unit tests for module X targeting 95% coverage"
- "Refactor module Y to extract Z into its own file"
- "Fix all lint warnings in directory D - no logic changes"
- "Add error handling to all API endpoints in routes/foo.py"
- "Write integration test for the evaluation pipeline"

## Bad Background Tasks

- "Implement the entire feature" (too broad)
- "Refactor all modules" (cross-cutting)
- "Fix all bugs" (undefined scope)
- "Update interfaces.py and all dependents" (shared dependency)

## Night Queue Workflow

1. **Accumulate** - during focused work, note tasks in BACKGROUND_QUEUE.md
2. **Kick** - before EOD, run `/night-kick` to prep worktrees + commands
3. **Execute** - copy-paste headless commands (run overnight)
4. **Review** - next morning, `/background-queue review` to check results

## Verification Requirements

- CI must pass (lint + tests + security) before human review
- Human reviews architecture decisions - agents handle implementation
- If agent PR fails CI, fix manually or re-queue with better specs
- Never merge agent PRs without reading the diff

## Coordination with Interactive Sessions

- Background agents update BACKGROUND_QUEUE.md with their status
- Interactive sessions check queue before starting to avoid file conflicts
- If an agent needs a file owned by an interactive session, it waits (BLOCKED status)
