# Background Agent Queue

> Max 5 concurrent agents. Max 300 lines per PR. Must include tests.

## Queue

| ID | Description | Branch | GH Issue | Criteria | Status | Created |
|----|-------------|--------|----------|----------|--------|---------|
| -- | No tasks queued | -- | -- | -- | -- | -- |

## Completed

| ID | Description | PR | Result | Completed |
|----|-------------|----|--------|-----------|
| -- | No completed tasks | -- | -- | -- |

## Rules

- **QUEUED**: Ready to be kicked off
- **KICKED**: Worktree created, agent running
- **BLOCKED**: Waiting on another task or interactive session
- **COMPLETED**: PR created and CI passed
- **FAILED**: Agent errored or CI failed - needs manual intervention
