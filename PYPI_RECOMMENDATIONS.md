# PyPI Publishing Recommendations for allin1fix

## Summary

This document provides recommendations for publishing `allin1fix` to PyPI, addressing the `natten` build requirement challenge.

## Key Recommendations

### ✅ 1. Package Configuration (DONE)

- **Dependency Order**: `torch>=2.0.0` is listed **before** `natten==0.17.5` in `pyproject.toml`
- **Build System**: `torch>=2.0.0` is included in `build-system.requires`
- **Python Version**: Set to `>=3.9` (required for `scipy>=1.13` and `madmom`)

### ✅ 2. Documentation Updates (DONE)

- **README.md**: Added clear "Installation from PyPI" section with:
  - Multiple installation methods
  - Explanation of `--no-build-isolation` requirement
  - Troubleshooting tips
- **PYPI_PUBLISHING.md**: Created comprehensive publishing guide

### ✅ 3. GitHub Workflow (DONE)

- Updated `.github/workflows/publish.yml` to:
  - Install `torch>=2.0.0` before building
  - Use standard Python build tools
  - Include package checking with `twine check`

## Before Publishing Checklist

### Pre-Publishing Steps

1. **Test Build Locally**
   ```bash
   python -m pip install --upgrade pip build hatchling torch>=2.0.0
   python -m build
   twine check dist/*
   ```

2. **Test Installation from Built Package**
   ```bash
   # Create clean environment
   python -m venv test_env
   source test_env/bin/activate
   
   # Test installation
   pip install torch>=2.0.0
   pip install dist/allin1fix-*.whl --no-build-isolation
   
   # Verify
   python -c "import allin1fix; print('Success!')"
   ```

3. **Test Installation from TestPyPI**
   ```bash
   # Upload to TestPyPI first
   twine upload --repository testpypi dist/*
   
   # Test installation from TestPyPI
   pip install --index-url https://test.pypi.org/simple/ torch>=2.0.0
   pip install --index-url https://test.pypi.org/simple/ allin1fix --no-build-isolation
   ```

4. **Verify Version Consistency**
   - Check `src/allin1fix/__about__.py`
   - Ensure version matches across all files

## Publishing Process

### Option 1: GitHub Actions (Recommended)

1. **Create Git Tag**
   ```bash
   git tag v<version>
   git push origin v<version>
   ```

2. **Create GitHub Release**
   - Go to GitHub → Releases → Create new release
   - Select the tag you just created
   - Add release notes
   - Publish release

3. **Workflow Automatically:**
   - Builds wheel and source distribution
   - Checks package with `twine check`
   - Publishes to PyPI using trusted publishing

### Option 2: Manual Publishing

```bash
# 1. Install tools
pip install build twine torch>=2.0.0

# 2. Build
python -m build

# 3. Check
twine check dist/*

# 4. Upload to TestPyPI (recommended first)
twine upload --repository testpypi dist/*

# 5. Test from TestPyPI
pip install --index-url https://test.pypi.org/simple/ torch>=2.0.0
pip install --index-url https://test.pypi.org/simple/ allin1fix --no-build-isolation

# 6. Upload to PyPI
twine upload dist/*
```

## Post-Publishing Verification

### 1. Check PyPI Page
- Visit: https://pypi.org/project/allin1fix/
- Verify README renders correctly
- Check all metadata

### 2. Test Installation from PyPI
```bash
# Clean environment
python -m venv test_pypi
source test_pypi/bin/activate

# Install from PyPI
pip install torch>=2.0.0
pip install allin1fix --no-build-isolation

# Verify
allin1fix --help
python -c "import allin1fix; print(allin1fix.__version__)"
```

## Important Notes for Users

### Installation Requirements

**⚠️ Critical:** Users must install `torch>=2.0.0` **before** installing `allin1fix` and use `--no-build-isolation`:

```bash
# Correct installation
pip install torch>=2.0.0 && pip install allin1fix --no-build-isolation

# This will FAIL:
pip install allin1fix  # ❌ Missing --no-build-isolation
```

### Why This Limitation Exists

- `natten` (a dependency) requires `torch` during its **build** process
- pip/uv's build isolation prevents access to installed packages during build
- This is a security feature of PEP 517/518 build backends
- There's no standard way to bypass this for individual dependencies

### User-Friendly Solutions

1. **Clear Documentation**: README.md now includes prominent installation instructions
2. **Multiple Methods**: Users can choose pip, uv, or shell aliases
3. **Troubleshooting Section**: Common issues and solutions documented

## Limitations & Future Improvements

### Current Limitations

1. **Cannot use single standard command**: `pip install allin1fix` won't work without `--no-build-isolation`
2. **Requires torch pre-installation**: Users must install torch first
3. **Build isolation**: Cannot be bypassed for individual dependencies

### Potential Future Solutions

1. **Pre-built wheels for natten**: If natten maintainers provide wheels, this issue disappears
2. **Custom build backend**: Could create custom backend, but adds complexity
3. **Vendor natten**: Include natten source, but increases package size significantly

## Summary

### What's Ready ✅

- ✅ Package configuration optimized
- ✅ Documentation updated with clear instructions
- ✅ GitHub workflow configured
- ✅ Publishing guide created

### What You Need to Do 📋

1. **Test locally** before publishing
2. **Test on TestPyPI** first
3. **Verify installation** from PyPI after publishing
4. **Monitor issues** and update documentation as needed

### Key Takeaway

The package is ready for PyPI, but users **must** follow the two-step installation process:
1. Install `torch>=2.0.0` first
2. Install `allin1fix` with `--no-build-isolation`

This is clearly documented in the README and should minimize user confusion.
