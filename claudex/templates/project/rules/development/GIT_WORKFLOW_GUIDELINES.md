# Git Workflow Guidelines

## Branch Naming
```
<type>/<description>
Types: feature/, fix/, refactor/, docs/, test/, chore/
```

## Commit Format (Conventional Commits)
```
<type>(<scope>): <description>

[optional body]

[required footer — Closes #N or Refs #N]
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`, `style`

## Commit Content Policy (MANDATORY)
NEVER include: AI tool names, Co-Authored-By AI lines, internal tooling terms, session IDs.
ALWAYS include: `Closes #N` or `Refs #N` in footer.

## Staging Rules
### Never Stage
- `.claude/` — internal config
- `.env`, `.env.*` — secrets
- `*.pem`, `*.key`, `*.token` — certificates
- `credentials.json`, `secrets.yaml` — credentials

### Pre-Commit Checklist
- [ ] Only related changes staged
- [ ] No debug code
- [ ] No hardcoded secrets
- [ ] Tests pass locally
- [ ] Lint + format passes
- [ ] Commit references GitHub Issue
- [ ] No AI terms in message

## PR Guidelines
- Title: `<type>(<scope>): <description>` (under 70 chars)
- Body: Summary bullets, test plan, `Closes #N`
- Size: <500 lines ideal, split if larger
