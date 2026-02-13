# PyPI Publishing Guide for claudex

## Pre-Publication Checklist

### 1. Verify Package Configuration

- [x] Fix package name references in `pyproject.toml`
- [x] Add PyPI metadata (keywords, authors, URLs)
- [ ] Update email address (currently placeholder)
- [ ] Verify version number (currently `1.0.0`)
- [ ] Ensure README.md is comprehensive
- [ ] Verify LICENSE file exists

### 2. Test Package Locally

```bash
# Clean any previous builds
rm -rf dist/ build/ *.egg-info

# Build the package
python -m build

# Verify contents
tar -tzf dist/claudex-1.0.0.tar.gz | head -20
unzip -l dist/claudex-1.0.0-py3-none-any.whl

# Install locally to test
pip install dist/claudex-1.0.0-py3-none-any.whl

# Test installation
claudex --version
claudex presets

# Uninstall test version
pip uninstall claudex -y
```

### 3. Run All Tests

```bash
# Run test suite
pytest tests/ -v

# Run lint checks
ruff check claudex/ tests/

# Run format check
ruff format claudex/ tests/ --check

# Fix any issues
ruff check claudex/ tests/ --fix
ruff format claudex/ tests/
```

### 4. Verify Template Files are Included

```bash
# After building, check that templates are in the wheel
unzip -l dist/claudex-1.0.0-py3-none-any.whl | grep templates

# You should see:
# - claudex/templates/global/
# - claudex/templates/project/
# - claudex/presets/*.yaml
```

---

## Publishing to TestPyPI (Recommended First)

TestPyPI is a separate instance of PyPI for testing. **Always test here first!**

### 1. Create TestPyPI Account

1. Go to https://test.pypi.org/account/register/
2. Verify email
3. Enable 2FA (required)
4. Create API token:
   - Go to https://test.pypi.org/manage/account/token/
   - Scope: "Entire account" (for first upload)
   - Save the token (starts with `pypi-`)

### 2. Configure PyPI Credentials

```bash
# Create/edit ~/.pypirc
cat > ~/.pypirc <<EOF
[distutils]
index-servers =
    pypi
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-YOUR_PYPI_TOKEN_HERE
EOF

chmod 600 ~/.pypirc
```

### 3. Upload to TestPyPI

```bash
# Install twine if not already installed
pip install twine

# Build fresh
rm -rf dist/
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Expected output:
# Uploading distributions to https://test.pypi.org/legacy/
# Uploading claudex-1.0.0-py3-none-any.whl
# Uploading claudex-1.0.0.tar.gz
```

### 4. Test Installation from TestPyPI

```bash
# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ claudex

# Test it works
claudex --version
claudex info .
claudex presets

# Clean up
pip uninstall claudex -y
```

### 5. Verify TestPyPI Page

Visit: https://test.pypi.org/project/claudex/

Check:
- [ ] README renders correctly
- [ ] Version is correct
- [ ] Links work (GitHub, Issues, Docs)
- [ ] Classifiers are correct
- [ ] Installation command shown is correct

---

## Publishing to PyPI (Production)

**Only proceed if TestPyPI testing was successful!**

### 1. Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Verify email
3. Enable 2FA (required)
4. Create API token:
   - Go to https://pypi.org/manage/account/token/
   - Scope: "Entire account" (for first upload)
   - Save the token

### 2. Final Checks

```bash
# Ensure you're on main branch
git branch

# Ensure working tree is clean
git status

# Tag the release
git tag v1.0.0
git push origin v1.0.0
```

### 3. Upload to PyPI

```bash
# Build fresh (clean first!)
rm -rf dist/
python -m build

# Check the package
twine check dist/*

# Upload to PyPI (PRODUCTION!)
twine upload dist/*

# Enter your PyPI credentials or use API token
```

### 4. Verify PyPI Page

Visit: https://pypi.org/project/claudex/

Check:
- [ ] README renders correctly
- [ ] Installation command: `pip install claudex`
- [ ] Version badge (if any)
- [ ] All metadata correct

### 5. Test Installation from PyPI

```bash
# Create clean virtual environment
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate

# Install from PyPI
pip install claudex

# Verify installation
claudex --version
claudex presets

# Test on a real project
cd /path/to/test/project
claudex init . --dry-run

# Clean up
deactivate
rm -rf test_env
```

---

## Post-Publication Tasks

### 1. Update README.md

```bash
# Remove "Coming soon" notice
# Change:
**Coming soon**: `pip install claudex` (PyPI)

# To:
pip install claudex
```

### 2. Update Roadmap

```markdown
# In README.md, check off:
- [x] Publish to PyPI
```

### 3. Create GitHub Release

1. Go to https://github.com/Binx808/claudex/releases/new
2. Tag: `v1.0.0`
3. Title: `v1.0.0 - Initial PyPI Release`
4. Description:
   ```markdown
   ## 🎉 First PyPI Release!

   claudex is now available on PyPI:
   ```bash
   pip install claudex
   ```

   ### Features
   - Smart project detection (Python, TypeScript, JavaScript)
   - Auto-preset selection (FastAPI, Django, Next.js, generic)
   - Generated CLAUDE.md with actual project structure
   - 17 slash commands for development workflow
   - 6 Python hooks for session lifecycle
   - Complete development guidelines

   See [README](https://github.com/Binx808/claudex#readme) for full documentation.
   ```
5. Attach files: Upload `dist/claudex-1.0.0.tar.gz` and `.whl`

### 4. Announce on Social Media / Discord / Forums

Example announcement:
```
🎉 claudex v1.0.0 is now on PyPI!

Set up Claude Code for any project in one command:
pip install claudex && claudex init .

Features:
✅ Auto-detects your stack (FastAPI/Django/Next.js)
✅ Generates project-specific CLAUDE.md
✅ 17 ready-to-use slash commands
✅ Complete development workflow

GitHub: https://github.com/Binx808/claudex
PyPI: https://pypi.org/project/claudex/
```

---

## Troubleshooting

### Issue: "File already exists"

**Cause**: You uploaded the same version twice.

**Fix**:
```bash
# Increment version in pyproject.toml
version = "1.0.1"

# Rebuild and re-upload
rm -rf dist/
python -m build
twine upload dist/*
```

**Note**: PyPI does NOT allow overwriting versions. Each upload must be a new version.

### Issue: Templates not included in package

**Cause**: `hatchling` not including `claudex/templates/` directory.

**Fix**: Check `pyproject.toml`:
```toml
[tool.hatch.build.targets.wheel]
packages = ["claudex"]
include = ["claudex/templates/**/*", "claudex/presets/**/*"]
```

### Issue: "The user 'username' isn't allowed to upload"

**Cause**: Using username instead of API token.

**Fix**: Use `__token__` as username and your API token as password:
```bash
twine upload --username __token__ --password pypi-YOUR_TOKEN dist/*
```

### Issue: README not rendering on PyPI

**Cause**: Markdown syntax not supported by PyPI.

**Fix**: PyPI supports a subset of Markdown. Avoid:
- HTML tags (except allowed ones)
- Complex nested structures
- Relative links (use absolute URLs)

Test locally:
```bash
pip install readme-renderer
python -m readme_renderer README.md
```

---

## Version Management Strategy

### Semantic Versioning

Use `MAJOR.MINOR.PATCH`:
- `MAJOR`: Breaking changes (e.g., 1.0.0 → 2.0.0)
- `MINOR`: New features, backward compatible (e.g., 1.0.0 → 1.1.0)
- `PATCH`: Bug fixes (e.g., 1.0.0 → 1.0.1)

### Pre-releases

For beta/alpha releases:
- `1.0.0a1` - Alpha 1
- `1.0.0b1` - Beta 1
- `1.0.0rc1` - Release candidate 1

### Version Bumping Workflow

```bash
# 1. Update version in pyproject.toml
[project]
version = "1.1.0"

# 2. Update __version__ in claudex/__init__.py
__version__ = "1.1.0"

# 3. Commit
git add pyproject.toml claudex/__init__.py
git commit -m "chore: bump version to 1.1.0"

# 4. Tag
git tag v1.1.0
git push origin main --tags

# 5. Build and upload
rm -rf dist/
python -m build
twine upload dist/*
```

---

## Automated Publishing with GitHub Actions (Optional)

Create `.github/workflows/publish-pypi.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build package
        run: python -m build

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

Then add `PYPI_API_TOKEN` to GitHub repository secrets.

---

## Next Steps After Publishing

1. Monitor PyPI download stats: https://pypistats.org/packages/claudex
2. Set up PyPI trusted publishing (OIDC) for automated releases
3. Add PyPI badge to README:
   ```markdown
   [![PyPI version](https://badge.fury.io/py/claudex.svg)](https://badge.fury.io/py/claudex)
   [![Downloads](https://pepy.tech/badge/claudex)](https://pepy.tech/project/claudex)
   ```
4. Monitor issues/feedback from users
5. Plan next release based on user feedback

---

Good luck with your first PyPI release! 🚀
