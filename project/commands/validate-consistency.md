# Consistency Validator

Validate consistency across layers: Frontend <-> Backend <-> Database.

## Checklist

### 1. Schema Consistency
- [ ] Database columns match ORM models
- [ ] ORM models match domain entities
- [ ] Domain entities match API schemas
- [ ] API schemas match frontend types

### 2. Enum Consistency
- [ ] String values match exactly across all layers
- [ ] API uses snake_case, frontend transforms to camelCase

### 3. Type Consistency
| Python | TypeScript | Database |
|--------|-----------|----------|
| str | string | VARCHAR/TEXT |
| int | number | INTEGER |
| float | number | REAL/FLOAT |
| bool | boolean | BOOLEAN |
| datetime | string (ISO) | TIMESTAMP |
| Optional[T] | T \| null | NULLABLE |

## Output: Schema alignment table, enum alignment, issues found, PASS/FAIL.

**Invocation**: `/validate-consistency [entity-name]`
