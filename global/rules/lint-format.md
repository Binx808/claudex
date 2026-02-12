# Lint, Format & Type Checking Policy

## Pre-Commit: Always Run Both Lint and Format

Before every commit, run the project's linter AND formatter. Code must pass both checks before committing.

### Python Projects (ruff)
```bash
ruff check src/ tests/              # Lint
ruff format src/ tests/ --check     # Format (dry-run)
```
If either fails:
```bash
ruff check src/ tests/ --fix        # Auto-fix lint
ruff format src/ tests/             # Auto-format
```

### TypeScript/JavaScript Projects (eslint + prettier)
```bash
npm run lint                        # or npx eslint .
npx prettier --check .             # Format check
```

## Rule Suppressions

When suppressing a lint rule:
1. Add an inline comment or config entry explaining **why**
2. Prefer per-file or per-directory ignores over global ignores
3. Document project-specific suppressions in that project's `.claude/` docs

## Type Checking

Run type checks when available before committing type-sensitive changes:
- Python: `mypy src/`
- TypeScript: `tsc --noEmit`
