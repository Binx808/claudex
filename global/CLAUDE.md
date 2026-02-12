# Global Development Preferences

- Always update the original file when fixing errors or adding features — never create duplicate files
- Always check related files when refactoring so dependencies aren't broken
- Keep root folders clean — only necessary files at root level, everything else in appropriate subdirectories
- Understand dependencies of the whole system before refactoring. Maintain modularity and relationships.

> **Policies**: Git, security, lint/format, and parallel dev rules are in `~/.claude/rules/`. Secrets are denied in `~/.claude/settings.json`.

---

# {{DEVELOPER_NAME}} - Personal Operating Manual

## Developer Brain Type
- {{DEVELOPER_TYPE}}

## Focus & Startup
- Strongest focus: {{FOCUS_TIME}}
- Preferred warm-up: check yesterday's implementation, verify feature works, recall context and rebuild momentum

## Stuck-Handling Rules
1. Logical investigation (15 minutes)
2. Experiment mode (15 minutes): add logs, isolate variables, reduce scope, create minimal reproduction
3. If still unclear: prepare clean question + evidence and ask

## Definition of Done
Strict Done conditions required:
- Expected behavior verified
- Edge cases handled (basic)
- Errors handled
- Tests added (when reasonable)

## Communication Style
- Default: concise + actionable
- Always provide: next action, acceptance criteria (Done), smallest viable scope
- Avoid long text by default
- Exception: Research or root-cause debugging tasks — provide full reasoning steps and evidence-based approach

## Hard Constraints
- NEVER change architecture without explicit approval - propose options, explain trade-offs, ask for confirmation
- Priority support order: task breakdown > unblocking/debugging > spec clarification > code review

---

# AI Orchestration Principles (100x Framework)

- **Stack**: IDE (inner loop) + Terminal Agent (main) + Background Agents (async) + AI Review + CI
- **Core Loop**: Direct (frame the task) -> Dissect (split into 1-PR threads) -> Delegate (assign to agents)
- **Parallel**: max 5 sessions, distinct file ownership, coordination via PARALLEL_SESSIONS.md
- **Background**: single-PR scope, own worktree+branch, include tests, never touch main directly
- **Night queue**: accumulate tasks during deep work, kick off before EOD, review next morning
- **MCP**: wire agents to GitHub/tools via .mcp.json - always prefer MCP over manual CLI for agent tasks
- **Verification**: tests + lint + security on every commit; AI review -> human review -> merge
- **Persistent context**: session files + MEMORY.md compound knowledge across sessions - always update them

---

# Task Management Rules

## Core Principle
Jira-style ticket execution: small scoped tickets, strict Done definition, continuous flow into review.

## Workflow
Backlog -> Ready -> In Progress -> Review -> Done

## WIP Limits
- In Progress: 1 ticket (max 2)
- Review: can accumulate; if blocked, propose a fallback support task

## Ticket Types
- **Build**: new implementation
- **Fix**: bug fixing
- **Research**: investigation / exploration
- **Refactor**: cleanup / structure improvement
- **Docs**: documentation / notes

## Ticket Size
- Ideal: 1-3 hours. If bigger, split immediately.

## Ticket Template (Mandatory)
- **Title**: Verb + Object (e.g. "Implement JWT login endpoint")
- **Goal**: what success means
- **Done**: acceptance criteria (strict)
- **Notes**: context, links, constraints (optional)

## Task Breakdown Rules
Prefer flow-based breakdown (end-to-end path) over component-only breakdown.

## Handling Ambiguity
If spec is ambiguous:
1. Create a Research ticket immediately (time-box 30-60 min)
2. Output: chosen approach, rejected options (short), next executable Build tickets

## Debugging Playbook
1. Isolate scope -> reproduce reliably -> inspect logs/inputs/outputs -> minimal reproduction -> apply fix -> verify with strict Done
2. If stuck > 30 min: create "Need help" note with what was tried, evidence, suspected root cause, clear question

## Daily Planning
- Start: pick up to 3 Ready tickets (1 main, 1 secondary, 1 quick warm-up)
- End: prepare next Ready ticket, write 1-line progress summary
