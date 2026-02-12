# Workflow Enforcement

## 8 Mandatory Gates

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

## NO BYPASS Allowed
- Architecture violations
- Security issues
- File size >500 lines
- Failing tests
