# Documentation Update Assistant

Update documentation based on code changes. Keep API contracts, architecture docs, and guidelines in sync.

## When to Use
- After adding new API endpoints
- After architectural changes
- After schema changes
- After adding new patterns

## Process
1. Identify what documentation needs updating based on code changes
2. Generate documentation content following existing format
3. Apply updates to existing files (NEVER create duplicate docs)
4. Verify: no duplicates, format consistent, examples accurate

## Single Source of Truth Rules
- Update existing files (default action)
- NEVER create ACTUAL_, FINAL_, UPDATED_ files
- One authoritative file per topic

**Invocation**: `/update-docs`
