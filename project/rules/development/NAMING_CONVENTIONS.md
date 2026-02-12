# Naming Conventions

## Python

### Files & Classes
| Type | Convention | Example |
|------|-----------|---------|
| Module | snake_case | `user_repository.py` |
| Class | PascalCase | `UserRepository` |
| Interface | I + PascalCase | `IUserRepository` |
| Use Case | Action + UseCase | `CreateUserUseCase` |
| Exception | PascalCase + Error | `UserNotFoundError` |

### Functions & Variables
| Type | Convention | Example |
|------|-----------|---------|
| Function | verb_noun | `create_user()` |
| Boolean | is/has/can | `is_active` |
| Converter | to_target | `to_domain()` |
| Constant | UPPER_SNAKE | `MAX_RETRIES` |

## TypeScript
| Type | Convention | Example |
|------|-----------|---------|
| Component | PascalCase.tsx | `UserCard.tsx` |
| Hook | use-kebab.ts | `use-user-data.ts` |
| Variable | camelCase | `userName` |

## Database
| Type | Convention | Example |
|------|-----------|---------|
| Table | snake_case plural | `users` |
| Column | snake_case | `created_at` |
| Foreign key | entity_id | `user_id` |

## API
| Layer | Convention |
|-------|-----------|
| API JSON | snake_case |
| Frontend | camelCase |

## Anti-Patterns (NEVER USE)
- Generic names: `data`, `info`, `item`, `obj`, `temp`
- Vague verbs: `handle()`, `do()`, `process()`, `manage()`
- Vague suffixes: `Manager`, `Handler`, `Helper`, `Util`
