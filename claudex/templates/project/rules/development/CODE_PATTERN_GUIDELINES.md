# Code Pattern Guidelines

## Domain Entity (Immutable)
```python
@dataclass(frozen=True)
class User:
    """Immutable domain entity."""
    id: str
    email: str

    def __post_init__(self) -> None:
        if not self.email:
            raise ValueError("Email is required")
```

## Use Case with Dependency Injection
```python
class CreateUserUseCase:
    def __init__(self, user_repo: IUserRepository) -> None:
        self._user_repo = user_repo

    async def execute(self, email: str) -> User:
        user = User(id=generate_id(), email=email)
        await self._user_repo.save(user)
        return user
```

## Repository Interface + Implementation
```python
# Interface (in core/application layer)
class IUserRepository(Protocol):
    async def find_by_id(self, id: str) -> User | None: ...
    async def save(self, user: User) -> None: ...

# Implementation (in infrastructure/db layer)
class UserRepositoryImpl(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
    # ... implement methods
```

## Error Handling
```python
class DomainError(Exception):
    """Base domain exception."""

class UserNotFoundError(DomainError):
    def __init__(self, user_id: str) -> None:
        super().__init__(f"User {user_id} not found")
```

## Anti-Patterns (AVOID)
- God classes that do everything
- Hard-coded dependencies (`self.repo = UserRepo()`)
- Domain knowing about database (`db_session` in entity)
- Generic catch-all error handling
