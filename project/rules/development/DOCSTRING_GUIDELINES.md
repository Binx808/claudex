# Minimal Docstring Guidelines

**Philosophy**: Code should be self-documenting. Type hints document parameters. Docstrings explain "why", not "what".

## Required
- **Class docstrings**: One-line summary of responsibility
- **Complex business logic**: Explain WHY this logic exists
- **Non-obvious algorithms**: Explain algorithmic choices or edge cases

## Omit
- Simple methods obvious from name + signature
- Getters/setters
- Private helpers (unless complex)
- Redundant Args/Returns sections when type hints are present

## Examples
```python
# GOOD - minimal for class
class TranslationAdapter:
    """Adapts generic LLM client for translation workflows."""

# GOOD - explain WHY for complex logic
def calculate_risk(tier: str, volatility: float) -> float:
    """Apply asymmetric risk scaling.
    Higher volatility tiers get less risk allowance
    to protect against tail events.
    """

# BAD - redundant
def get_user(self, id: str) -> User:
    """Get a user by ID.
    Args:
        id: The user ID
    Returns:
        User object
    """
```

**Golden Rule**: If deleting the docstring leaves the code perfectly clear, delete it.
