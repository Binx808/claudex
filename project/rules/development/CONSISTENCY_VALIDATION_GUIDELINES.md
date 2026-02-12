# Consistency Validation Guidelines

## Cross-Layer Field Mapping
```
Database Column -> ORM Model -> Domain Entity -> API Schema -> Frontend Type
snake_case      -> snake_case -> snake_case   -> snake_case -> camelCase
```

## Type Mapping
| Python | TypeScript | Database |
|--------|-----------|----------|
| str | string | VARCHAR/TEXT |
| int | number | INTEGER |
| float | number | REAL/FLOAT |
| bool | boolean | BOOLEAN |
| datetime | string (ISO) | TIMESTAMP |
| Optional[T] | T \| null | NULLABLE |

## Enum Values
String values MUST match exactly (snake_case in API).

## Validation Rules
If backend validates `0 < value <= 100`, frontend MUST enforce same.

## Checklist
- [ ] Database columns match ORM models
- [ ] ORM models match domain entities
- [ ] Domain entities match API schemas
- [ ] API schemas match frontend types
- [ ] Enum values match across layers
- [ ] Nullable fields handled in all layers
