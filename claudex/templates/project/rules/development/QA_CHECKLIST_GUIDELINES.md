# QA Checklist Guidelines

## New Feature
- [ ] All acceptance criteria met
- [ ] Edge cases handled
- [ ] Error scenarios handled
- [ ] File/method sizes within limits
- [ ] Naming conventions followed
- [ ] Unit tests written (TDD)
- [ ] Integration tests (if cross-layer)
- [ ] All tests passing
- [ ] Cross-layer consistency verified (if applicable)

## Bug Fix
- [ ] Root cause identified
- [ ] Fix addresses root cause (not symptom)
- [ ] Regression test added
- [ ] No new issues introduced
- [ ] All existing tests pass

## Refactoring
- [ ] All existing tests pass unchanged
- [ ] External API unchanged (or documented)
- [ ] No functional changes introduced
- [ ] Code is more readable
- [ ] Performance not degraded
