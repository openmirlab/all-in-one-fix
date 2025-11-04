# PyPI Publishing Setup

This repository is configured for automated PyPI publishing using **Trusted Publishing** (OIDC-based authentication).

## 🎯 How It Works

When you push a git tag starting with `v` (e.g., `v2.0.0`), the GitHub Actions workflow automatically:
1. Builds the package using `uv build`
2. Publishes to PyPI via Trusted Publishing (no API tokens needed!)

## 🔧 One-Time Setup Required

### Step 1: Configure Trusted Publishing on PyPI

1. **Go to PyPI**: https://pypi.org/manage/account/publishing/
2. **Add a new publisher** with these exact settings:
   - **PyPI Project Name**: `allin1fix`
   - **Owner**: `openmirlab`
   - **Repository**: `all-in-one-fix`
   - **Workflow name**: `publish.yml`
   - **Environment name**: (leave blank)

3. Click **Add**

> **Note**: You can set this up before the package exists on PyPI. The first publish will create it.

### Step 2: (Optional) Test Build Locally

Before creating a release, test the build locally:

```bash
# Install UV if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Build the package
uv build

# Check the dist/ directory
ls -lh dist/
```

You should see:
- `allin1fix-2.0.0.tar.gz` (source distribution)
- `allin1fix-2.0.0-py3-none-any.whl` (wheel)

## 🚀 Publishing a Release

### Method 1: Using Git Tags (Recommended)

```bash
# Tag the release
git tag v2.0.0

# Push the tag
git push origin v2.0.0
```

The GitHub Actions workflow will automatically:
- Build the package
- Publish to PyPI
- Make it available via `pip install allin1fix`

### Method 2: Using GitHub Releases UI

1. Go to: https://github.com/openmirlab/all-in-one-fix/releases/new
2. **Choose a tag**: Create new tag `v2.0.0`
3. **Release title**: `v2.0.0: NATTEN 0.21.0 Support`
4. **Description**: Copy from `docs/RELEASE_SUMMARY.md`
5. Click **Publish release**

The workflow triggers automatically!

## 📋 Version Numbering

The package version is defined in: `src/allin1fix/__about__.py`

```python
__version__ = "2.0.0"
```

**Before tagging a release:**
1. Update `__version__` in `src/allin1fix/__about__.py`
2. Commit the change
3. Then create the git tag

## ✅ Verifying Publication

After the workflow completes:

```bash
# Check on PyPI
open https://pypi.org/project/allin1fix/

# Install and test
pip install allin1fix
allin1fix --help
```

## 🔍 Troubleshooting

### Workflow fails with "Trusted publishing exchange failure"

**Solution**: Make sure you've configured Trusted Publishing on PyPI (Step 1 above) with the exact repository and workflow names.

### Build fails locally

```bash
# Clear cache and rebuild
rm -rf dist/
uv build
```

### Wrong version published

1. Delete the git tag: `git tag -d v2.0.0 && git push origin :refs/tags/v2.0.0`
2. Update `__version__` in `src/allin1fix/__about__.py`
3. Commit and create new tag

## 📚 Resources

- **PyPI Trusted Publishing**: https://docs.pypi.org/trusted-publishers/
- **UV Build**: https://docs.astral.sh/uv/guides/publish/
- **GitHub Actions**: https://github.com/openmirlab/all-in-one-fix/actions

## 🎊 Benefits of This Setup

✅ **No API tokens** - Uses OIDC (more secure)
✅ **Automated** - Just push a tag
✅ **Fast builds** - Uses UV (10-100x faster)
✅ **Consistent** - Same build process every time
✅ **Transparent** - All builds visible in GitHub Actions
