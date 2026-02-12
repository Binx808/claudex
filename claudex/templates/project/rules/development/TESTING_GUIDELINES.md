# Testing Guidelines

## TDD Workflow (MANDATORY for business logic)
```
1. RED    - Write failing test first
2. GREEN  - Write minimal code to pass
3. REFACTOR - Improve code, keep tests green
```

## Test Structure (AAA Pattern)
```python
def test_creates_user_with_valid_email():
    # Arrange
    email = "test@example.com"

    # Act
    user = create_user(email=email)

    # Assert
    assert user.email == email
```

## Test Naming
```python
# Pattern: test_<action>_<condition>_<expected>
def test_create_user_with_invalid_email_raises_value_error(): ...
def test_find_user_when_not_exists_returns_none(): ...
```

## When to Mock
- External APIs, LLM calls, third-party services
- Database (for unit tests only)
- File system, time-dependent code

## When NOT to Mock
- Domain/business logic (test directly)
- Simple utilities
- Database (in integration tests)

## Edge Cases to ALWAYS Test
1. Empty inputs: `""`, `[]`, `{}`
2. None/null values
3. Boundary values: min, max, 0, -1
4. Invalid inputs: wrong types, out of range
5. Error conditions: exceptions, timeouts

## Coverage Targets
| Layer | Target |
|-------|--------|
| Core/Domain | 95% |
| Application | 90% |
| Infrastructure | 80% |
| Overall | 85% |
