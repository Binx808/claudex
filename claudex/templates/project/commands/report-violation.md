# Violation Reporter

Capture violations when they occur and trigger improvement workflow.

## Process
1. **Gather details**: file path, line, what happened vs what should have happened
2. **Classify**: Architecture, Naming, Consistency, Testing, Security, Quality, Documentation
3. **Severity**: CRITICAL (architecture/security), HIGH (consistency/tests), MEDIUM (quality/naming), LOW (docs/style)
4. **Log**: Append to `.claude/feedback/VIOLATIONS_LOG.md` with unique ID
5. **Trigger improvement**: Update relevant guidelines or pattern corrections

## Auto-Triggered When
- `/dev validate` finds violations
- `/audit` finds CRITICAL or HIGH issues
- `/complete-task` finds blocking issues

**Invocation**: `/report-violation <description>`
