# Architecture Validator

Validate that code follows architectural principles.

## Validation Checklist

### 1. Layer Placement
For each file, verify it's in the correct directory per project CLAUDE.md.

### 2. Dependency Direction
Dependencies flow INWARD only. Verify imports don't go from inner to outer layers.

### 3. Interface Compliance
Interfaces defined in application/core layer, implementations in infrastructure/outer layer.

### 4. Size Limits
- Files <=500 lines (blocking), <=300 ideal
- Methods <=50 lines (blocking), <=30 ideal

## Output Format

```
## Architecture Validation Report
### Layer Placement: [OK/VIOLATION]
### Dependency Analysis: [OK/VIOLATION]
### Size Analysis: [OK/WARNING]
### Result: PASS / FAIL
```

**Invocation**: `/validate-architecture [file-or-directory]`
