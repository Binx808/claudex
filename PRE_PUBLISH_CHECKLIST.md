# Pre-Publish Checklist for claudex v1.0.0

## Critical Fixes Applied ✅

- [x] Fixed `pyproject.toml` package references (`claude_scaffold` → `claudex`)
- [x] Added PyPI metadata (URLs, keywords, authors)
- [x] Verified package structure (`claudex/` exists with all modules)

## Pre-Publication Tasks

### 1. Update Contact Information

```toml
# In pyproject.toml, update email (line ~24):
authors = [
    {name = "Binx808", email = "YOUR_REAL_EMAIL@example.com"},
]
maintainers = [
    {name = "Binx808", email = "YOUR_REAL_EMAIL@example.com"},
]
```

### 2. Test Package Build

```bash
# Install build tools
pip install build twine

# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build
python -m build

# Expected output:
# dist/
#   claudex-1.0.0-py3-none-any.whl
#   claudex-1.0.0.tar.gz
```

### 3. Verify Package Contents

```bash
# Check wheel contents
python -m zipfile -l dist/claudex-1.0.0-py3-none-any.whl

# Must include:
# - claudex/__init__.py
# - claudex/cli.py
# - claudex/detectors.py
# - claudex/generator.py
# - claudex/copier.py
# - claudex/validator.py
# - claudex/templates/ (CRITICAL!)
# - claudex/presets/ (CRITICAL!)

# Check source distribution
tar -tzf dist/claudex-1.0.0.tar.gz | grep -E "(templates|presets)"

# Must show template files
```

### 4. Local Installation Test

```bash
# Create test environment
python -m venv test_venv
source test_venv/bin/activate  # Windows: test_venv\Scripts\activate

# Install from wheel
pip install dist/claudex-1.0.0-py3-none-any.whl

# Test commands
claudex --version
# Expected: claudex 1.0.0

claudex presets
# Expected: List of presets (python-fastapi, python-django, nextjs, generic)

# Test dry run
claudex init . --dry-run

# Clean up
deactivate
rm -rf test_venv
```

### 5. Run All Tests

```bash
# Full test suite
pytest tests/ -v

# Lint check
ruff check claudex/ tests/

# Format check
ruff format claudex/ tests/ --check
```

### 6. Verify Git Status

```bash
# Ensure on main branch
git branch
# Should show: * main or * master

# Ensure clean working tree
git status
# Should show: nothing to commit, working tree clean

# If you made changes, commit them:
git add pyproject.toml
git commit -m "fix: update pyproject.toml for PyPI publication

- Fix package name references (claude_scaffold → claudex)
- Add PyPI metadata (URLs, keywords, authors)
- Prepare for v1.0.0 release

Refs #N"

git push origin main
```

---

## Publication Steps

### Option A: TestPyPI First (RECOMMENDED)

```bash
# 1. Upload to TestPyPI
twine upload --repository testpypi dist/*

# 2. Test installation
pip install --index-url https://test.pypi.org/simple/ claudex

# 3. Verify it works
claudex --version
claudex presets

# 4. If successful, proceed to PyPI
```

### Option B: Direct to PyPI

```bash
# 1. Final check
twine check dist/*

# 2. Upload (THIS IS PERMANENT!)
twine upload dist/*

# 3. Verify on PyPI
# Visit: https://pypi.org/project/claudex/
```

---

## Post-Publication Tasks

### 1. Git Tag

```bash
git tag v1.0.0
git push origin v1.0.0
```

### 2. GitHub Release

Create release at: https://github.com/Binx808/claudex/releases/new
- Tag: `v1.0.0`
- Title: `v1.0.0 - Initial PyPI Release`
- Upload: `dist/claudex-1.0.0.tar.gz` and `.whl`

### 3. Update README.md

Remove "Coming soon" and update installation instructions:
```bash
# Change:
**Coming soon**: `pip install claudex` (PyPI)

# To:
pip install claudex
```

### 4. Update Roadmap

```bash
# In README.md, check off:
- [x] Publish to PyPI
```

Commit and push:
```bash
git add README.md
git commit -m "docs: update README for PyPI release"
git push origin main
```

---

## Common Issues

### Templates Not Included

**Symptom**: Package installs but `claudex init` fails with "template not found"

**Fix**: Add to `pyproject.toml`:
```toml
[tool.hatch.build]
include = [
    "claudex/**/*.py",
    "claudex/templates/**/*",
    "claudex/presets/**/*.yaml",
]
```

### Version Already Exists on PyPI

**Symptom**: "File already exists" error during upload

**Fix**: Bump version in `pyproject.toml` and `__init__.py`, rebuild, re-upload

### Windows Build Errors

**Symptom**: Build fails with path errors

**Workaround**:
```bash
# Use WSL if available
wsl
cd /mnt/d/claudex
python -m build

# Or build in cloud (GitHub Actions)
```

---

## Ready to Publish?

- [ ] Email updated in `pyproject.toml`
- [ ] Package builds successfully
- [ ] Templates verified in package
- [ ] Local install test passed
- [ ] All tests pass
- [ ] Git working tree clean
- [ ] PyPI account created with 2FA
- [ ] API token generated

**If all checked, proceed with TestPyPI upload!**

See `PYPI_PUBLISHING_GUIDE.md` for detailed instructions.
