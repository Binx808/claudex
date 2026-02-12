# Security Policy

## Never Commit (All Projects)

These files must NEVER be committed to any repo:
- `.claude/` — internal Claude Code config
- `.env`, `.env.*` — environment secrets
- `*.pem`, `*.key`, `*.token` — certificates and keys
- `credentials.json`, `secrets.yaml` — service credentials
- `__pycache__/`, `node_modules/` — generated artifacts

## Never Read in Sessions

The following are denied via global `settings.json` permissions:
- `.env`, `.env.*` — environment variables with secrets
- `*.pem`, `*.key`, `*.token` — private keys and tokens
- `credentials.json`, `secrets.yaml` — service credentials

## Code Security

- Never hardcode secrets, API keys, or passwords in source code
- Use environment variables for all configuration secrets
- Validate all external inputs at system boundaries
- Use parameterized queries (no string interpolation in SQL)
- Set timeouts on all external API calls
- Enforce file size limits on uploads
