# Code Auditor

Perform comprehensive code audits against project standards.

## Audit Checklist

### 1. Architecture Compliance
- [ ] Dependencies flow INWARD only
- [ ] No forbidden imports per layer rules
- [ ] No circular dependencies

### 2. File & Method Size Limits
- [ ] Files <=300 lines (ideal), <=500 max
- [ ] Methods <=30 lines (ideal), <=50 max
- [ ] Nesting depth <=3 levels

### 3. SOLID Principles
- [ ] SRP: Each class has ONE responsibility
- [ ] DI: Dependencies injected, not created internally
- [ ] DRY: No code repeated 3+ times

### 4. Naming Conventions
- [ ] Methods: verb + noun pattern
- [ ] Classes: No vague suffixes (Manager, Handler, Util)

### 5. Security
- [ ] All external inputs validated
- [ ] No hardcoded secrets
- [ ] Timeouts on external calls

### 6. Testing
- [ ] Tests exist for business logic
- [ ] Edge cases covered
- [ ] >=80% coverage target

## Output Format

For each file: Status (PASS/FAIL), issues with file:line references, recommendations.

**Invocation**: `/audit [files-or-directory]`
