# Workflow Improvement Analyzer

Analyze feedback data and propose improvements to guidelines and workflow.

## Process
1. Read feedback files: VIOLATIONS_LOG.md, LESSONS_LEARNED_INDEX.md, PATTERN_CORRECTIONS.md
2. Identify patterns: repeated violations, missing corrections, stale guidelines
3. Propose improvements tiered by scope:
   - Tier 1 (CLAUDE.md): Universal permanent rules
   - Tier 2 (Guidelines): General patterns
   - Tier 3 (Knowledge): Project-specific
   - Tier 4 (Corrections): Specific fixes
4. Generate improvement report with priority-ordered actions

## Scope Options
- `violations` - Analyze recent violations
- `patterns` - Review pattern corrections
- `guidelines` - Propose guideline updates
- `all` - Full improvement cycle

**Invocation**: `/improve-workflow [violations|patterns|guidelines|all]`
