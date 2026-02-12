# Task Initialization Assistant

Initialize a new development task with session files, guideline loading, and task breakdown.

## Process

1. **Archive previous session** (if exists) to `.claude/session/archive/`
2. **Analyze task**: identify type (Build/Fix/Refactor), affected layers, workflow type
3. **Create session files**: CURRENT_TASK.md, TASK_PROGRESS.md, VALIDATION_STATE.md, CONTEXT_SUMMARY.md
4. **Find/create GitHub Issue**: record GH# in CURRENT_TASK.md
5. **Select development style**: TDD (default for business logic) or Implementation-First
6. **Create micro-task breakdown**: 15-30 min chunks, ordered by dependency
7. **Present summary** with task details, affected layers, and first action

## Session File Templates

### CURRENT_TASK.md
```markdown
# Current Task
**Started**: [timestamp]
**Status**: in_progress
**GitHub Issue**: #N — title

## Task Description
[description]

## Acceptance Criteria
- [ ] [criteria]
```

### TASK_PROGRESS.md
```markdown
# Task Progress
## Micro Tasks
### Phase 1: Analysis
- [ ] Analyze requirements
### Phase 2: Implementation
[populated after planning]
### Phase 3: QA
- [ ] Self-audit
- [ ] Tests passing
```

**Invocation**: `/start-task <description>` or via `/dev start`
