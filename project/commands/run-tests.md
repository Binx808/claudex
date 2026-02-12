# Test Runner

Run tests with appropriate scope and provide clear feedback.

## Test Scopes

| Context | Default Scope | Command |
|---------|---------------|---------|
| During implementation | Unit tests | `pytest tests/unit/ -v --tb=short` |
| Before commit | Unit + Integration | `pytest tests/ -v --tb=short` |
| Specific feature | Pattern match | `pytest -k "test_feature" -v` |
| With coverage | Full + coverage | `pytest --cov=src --cov-report=term-missing` |

## Process

1. Determine test scope from context
2. Run appropriate test command
3. Parse results (passed/failed/errors/skipped)
4. For failures: show file:line, error, likely cause, suggested fix
5. Report summary with pass/fail status

## Coverage Targets

| Layer | Minimum | Target |
|-------|---------|--------|
| Core/Domain | 90% | 95% |
| Application | 85% | 90% |
| Infrastructure | 75% | 80% |
| **Overall** | **80%** | **85%** |

**Invocation**: `/run-tests [scope]`
