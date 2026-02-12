# Audit & Code Review Guidelines

## When to Perform Audits

| Trigger | Depth |
|---------|-------|
| Before PR | Files changed only |
| Before merge to main | All affected files |
| Sprint completion | Entire feature area |
| Architecture changes | Cross-layer analysis |

## Review Steps (Priority Order)

### Step 1: Architecture (FIRST — Blocking)
- [ ] Files in correct layers
- [ ] Dependencies flow inward
- [ ] No circular dependencies

### Step 2: Correctness
- [ ] Code does what it should
- [ ] Edge cases handled
- [ ] Error handling appropriate

### Step 3: Quality
- [ ] Files <=300 lines ideal, <=500 max
- [ ] Methods <=30 lines ideal, <=50 max
- [ ] SRP, DRY, DI principles followed

### Step 4: Testing
- [ ] Tests exist and pass
- [ ] Tests cover the changes meaningfully

### Step 5: Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Timeouts on external calls

## Scoring
| Score | Action |
|-------|--------|
| 8-10 | Merge after minor fixes |
| 6-7 | Address before merge |
| 4-5 | Major rework needed |
| 0-3 | Cannot merge |
