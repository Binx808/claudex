# Git & Version Control Policy

## Commit Content Policy (MANDATORY — All Projects)

Commits must read as if written by the developer. **NEVER include** any of the following in commit messages, PR titles, PR descriptions, or branch names:
- AI tool names or references (e.g. "Claude", "GPT", "Copilot", "AI-generated", "AI-assisted")
- `Co-Authored-By` lines referencing AI tools
- Internal tooling terms, session IDs, or agent names
- References to prompts, conversations, or AI workflows

**Allowed**: GitHub issue numbers (`#1`, `Closes #5`), ticket IDs, feature names, technical terms.

## Commit Format

Use conventional commits:
```
<type>(<scope>): <description>

[optional body]

[required footer — Closes #N or Refs #N]
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`, `style`

**Every commit MUST reference a GitHub Issue** in the footer:
- `Closes #N` — task fully completes the issue
- `Refs #N` — task partially addresses the issue

## Branch Naming

```
<type>/<description>
```
Types: `feature/`, `fix/`, `refactor/`, `docs/`, `test/`, `chore/`

## GitHub Issue Workflow

Every development task MUST be tracked via a GitHub Issue:

```
OPEN (Backlog) -> /dev start (record GH# in session) -> IN PROGRESS -> Commit (Closes #N) -> PR -> MERGED (auto-closes issue)
```

### Required Actions

| Phase | Action |
|-------|--------|
| Task start | Find or create GH issue (`gh issue list` / `gh issue create`) |
| Branch create | Include task context in branch name |
| Every commit | Reference issue in footer (`Closes #N` or `Refs #N`) |
| PR create | Link issue in PR body (`Closes #N`) |

### Issue Hygiene

- Use labels for sprint/type categorization
- New work discovered during a task -> create a new issue, don't expand scope
- Stale issues -> close with `gh issue close <N> --reason "not planned"`

## Always Commit Together

- Source changes + corresponding test files (CI needs tests)
- No test artifacts (`__pycache__/`, `.coverage`, `htmlcov/`, `.pytest_cache/`)
