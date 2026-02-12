# Task Completion Assistant

Complete the current task with full validation, QA checklist, and commit preparation.

## Process

### Step 1: Run All Validations (STRICT)

#### 1.1 Architecture Validation
- [ ] All files in correct layers
- [ ] Dependencies flow inward only

#### 1.2 Code Quality
- [ ] All files <=500 lines (BLOCK if exceeded)
- [ ] All methods <=50 lines (BLOCK if exceeded)

#### 1.3 Test Execution
```bash
pytest tests/ -v --tb=short
```
- [ ] All tests passing

#### 1.4 Lint & Format Check
```bash
ruff check src/ tests/
ruff format src/ tests/ --check
```
- [ ] No lint or format errors

### Step 2: Generate QA Checklist
Based on task type (feature/fix/refactor), generate appropriate checklist.

### Step 3: Prepare for Commit

#### Pre-Commit Checklist
- [ ] Only related changes staged
- [ ] No debug code
- [ ] No hardcoded secrets
- [ ] Tests pass locally
- [ ] Lint + format passes
- [ ] Commit message follows convention
- [ ] Commit footer has `Closes #N` or `Refs #N`
- [ ] No AI tool names in commit message
- [ ] No `.claude/` or credential files staged

### Step 4: Archive Session
Move session files to `.claude/session/archive/[MILESTONE]/`

## Blocking Conditions
- Architecture violations exist
- Tests failing
- File size exceeds 500 lines
- Lint or format errors present

**Invocation**: `/complete-task` or via `/dev complete`
