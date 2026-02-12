# Development Workflow Guidelines

## Core Principles (Never Violate)

| Principle | Description |
|-----------|-------------|
| **Never Assume** | Validate everything; if unsure, look it up |
| **Step by Step** | Complete each phase before moving on |
| **Review Without Bias** | Critically evaluate even your own code |
| **Clarify First** | Ask questions when context is insufficient |

## Pre-Work Checklist

- [ ] Read and understand the task requirements
- [ ] Identify which workflow type applies
- [ ] Review relevant existing code/patterns
- [ ] Find or create GitHub Issue for this task

## Workflow Phases

### Phase 1: Analysis (Steps 1-3)
1. Analyze the plan — understand deliverables and constraints
2. Analyze current implementation — review existing code, patterns, dependencies
3. Evaluate — score against quality criteria

### Phase 2: Planning (Steps 4-6)
4. Refine plan if analysis revealed new complexity
5. Choose development style (TDD recommended for business logic)
6. Break down into micro-tasks (15-30 min each)

### Phase 3: Implementation (Steps 7-8)
7. Implement — one micro-task at a time, follow layer rules and size limits
8. Test — AAA pattern, edge cases, error conditions

### Phase 4: Quality Assurance (Steps 9-12)
9. Self-audit — architecture, quality, security, documentation
10. Commit — conventional commits, issue reference in footer
11. QA checklist — functional, quality, testing, consistency checks
12. Expert review — for changes spanning 3+ files or new patterns

## Quality Gates

| Gate | Phase | Blocks On |
|------|-------|-----------|
| 1: Init | Pre-Impl | No session, no GH issue |
| 2: Architecture | Pre-Impl | Layer violations |
| 3: Patterns | Pre-Impl | Pattern violations |
| 4: Quality | Impl | Size >500 lines, lint/format fails |
| 5: Testing | Impl | No tests or failing tests |
| 6: Consistency | Post-Impl | Cross-layer mismatches |
| 7: Audit | Post-Impl | Critical audit issues |
| 8: Commit | Commit | Missing GH# ref, policy violation |

## Session Persistence

Session files in `.claude/session/` survive context compaction:
- `/dev start` creates session files
- `/dev checkpoint` saves progress
- `/dev continue` resumes from files
- `/dev complete` archives session
