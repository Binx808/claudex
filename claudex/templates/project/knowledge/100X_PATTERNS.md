# 100x Developer Patterns

## Layer Stack

| Layer | Role | Always On? |
|-------|------|-----------|
| IDE + Extensions | Inner loop: autocomplete, inline edits | Yes |
| Terminal Agent (Claude Code) | Main orchestrator: plan, implement, review | Yes |
| Background Agents | Async workers: single-PR scope, own worktree | On demand |
| AI Code Review | PR gatekeeper: architecture + quality checks | Every PR |
| CI Pipeline | Automated verification: tests + lint + security | Every push |

## Core Loop: Direct -> Dissect -> Delegate

### 1. Direct (Frame)
- Define the goal in 1-2 sentences
- Identify constraints and non-negotiables
- Set success criteria

### 2. Dissect (Split)
- Break into independent 1-PR threads
- Each thread owns distinct files (no overlap)
- Identify dependency order for merge sequence

### 3. Delegate (Assign)
- Interactive session: complex architecture, multi-file coordination
- Background agent: well-scoped implementation, test writing, refactoring
- Night queue: accumulated tasks, kicked before EOD

## Background Agent Scoping

### Good Tasks (single-PR, well-defined)
- "Add unit tests for module X targeting 95% coverage"
- "Refactor module Y to extract Z into its own file"
- "Fix lint warnings in directory D - no logic changes"

### Bad Tasks (too broad, cross-cutting)
- "Implement the entire feature"
- "Refactor all modules"
- "Fix all bugs"

### Rules
- Max 300 lines changed per PR
- Must include tests
- Own worktree + branch
- Never modify shared interfaces without coordination
- CI must pass before human review

## Night Queue Protocol

1. **Accumulate**: During deep work, add tasks to BACKGROUND_QUEUE.md
2. **Kick**: Before EOD, run `/night-kick` to generate worktree+agent commands
3. **Execute**: Copy-paste generated commands (agents run headless overnight)
4. **Review**: Next morning, run `/background-queue review` to check PR status

## Persistent Context Compounding

- **Session files**: CURRENT_TASK.md, TASK_PROGRESS.md, CONTEXT_SUMMARY.md survive compaction
- **MEMORY.md**: Cross-session knowledge - lessons, patterns, gotchas
- **Knowledge files**: Domain rules, patterns, templates - always in context
- **Feedback loop**: Violations -> lessons -> workflow improvements -> better defaults

## Verification Non-Negotiables

- Every commit: lint + format pass
- Every PR: unit tests + coverage gate
- Every PR: security scan (SAST + dependency audit)
- Every PR: AI code review (architecture + quality)
- Merge: human review of AI review + CI green
