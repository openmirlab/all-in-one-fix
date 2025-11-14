# PyPI Publishing Guide for all-in-one-fix

This guide covers best practices for publishing `all-in-one-fix` to PyPI, including handling the `natten` build requirement.

**Note:** 
- PyPI project name: `all-in-one-fix` (matches repository name)
- Python package name: `allin1fix` (used in imports: `import allin1fix`)
- Install with: `pip install all-in-one-fix` (uses PyPI project name)

## Pre-Publishing Checklist

### 1. Version Management
- [ ] Update version in `src/allin1fix/__about__.py`
- [ ] Ensure version is consistent across all files
- [ ] Create a git tag: `git tag v<version>`

### 2. Dependency Verification
- [ ] Verify `torch>=2.0.0` is listed **before** `natten==0.17.5` in `dependencies`
- [ ] Test installation in a clean environment
- [ ] Verify all dependencies resolve correctly

### 3. Build Testing
```bash
# Test build locally
python -m pip install --upgrade pip build hatchling torch>=2.0.0
python -m build
twine check dist/*
```

### 4. Installation Testing
```bash
# Test installation from built wheel
pip install torch>=2.0.0
pip install dist/allin1fix-*.whl --no-build-isolation

# Test installation from source distribution
pip install torch>=2.0.0
pip install dist/allin1fix-*.tar.gz --no-build-isolation
```

## Publishing Process

### Option 1: GitHub Actions (Recommended)

1. **Create a GitHub Release:**
   ```bash
   git tag v<version>
   git push origin v<version>
   ```
   Then create a release on GitHub with the tag.

2. **The workflow will automatically:**
   - Build the package (wheel + sdist)
   - Check the package with `twine check`
   - Publish to PyPI using trusted publishing

### Option 2: Manual Publishing

```bash
# 1. Install build tools
pip install build twine torch>=2.0.0

# 2. Build the package
python -m build

# 3. Check the package
twine check dist/*

# 4. Upload to TestPyPI first (recommended)
twine upload --repository testpypi dist/*

# 5. Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ allin1fix --no-build-isolation

# 6. Upload to PyPI
twine upload dist/*
```

## Post-Publishing Verification

### 1. Verify Package on PyPI
- Visit: https://pypi.org/project/all-in-one-fix/
- Check that README renders correctly
- Verify all metadata is correct

### 2. Test Installation from PyPI
```bash
# Create a clean virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Test installation
pip install torch>=2.0.0
pip install allin1fix --no-build-isolation

# Verify installation
python -c "import allin1fix; print(allin1fix.__version__)"
allin1fix --help
```

## Important Notes for Users

### Installation Requirements
- **Python 3.9+** (required for `scipy>=1.13` and `madmom`)
- **torch>=2.0.0** must be installed **before** `allin1fix`
- Use `--no-build-isolation` flag when installing

### Why `--no-build-isolation`?
- `natten` (a dependency) requires `torch` during its build process
- pip's build isolation prevents access to installed packages during build
- `--no-build-isolation` allows `natten` to access the already-installed `torch`

### Recommended Installation Commands

**For pip users:**
```bash
pip install torch>=2.0.0 && pip install allin1fix --no-build-isolation
```

**For uv users:**
```bash
uv add torch && uv add allin1fix --no-build-isolation
```

## Troubleshooting

### Common Issues

1. **Build fails with "No module named 'torch'"**
   - **Solution:** Ensure `torch>=2.0.0` is installed before building/installing
   - Use `--no-build-isolation` flag

2. **Installation fails with scipy version conflict**
   - **Solution:** Ensure Python 3.9+ is used (required for `scipy>=1.13`)

3. **madmom installation fails**
   - **Solution:** `madmom` is installed from GitHub, ensure git is available
   - Check network connectivity to GitHub

### Testing Before Publishing

Always test in a clean environment before publishing:

```bash
# Create clean environment
python -m venv test_clean
source test_clean/bin/activate

# Test installation
pip install torch>=2.0.0
pip install allin1fix --no-build-isolation

# Test functionality
allin1fix --help
python -c "import allin1fix; print('Success!')"
```

## PyPI Project Page Configuration

### Description
The README.md will be automatically used as the long description.

### Keywords
- music
- beat
- downbeat
- tracking
- structure
- analysis
- allin1fix
- source-separation

### Classifiers
- Development Status :: 5 - Production/Stable
- Intended Audience :: Developers
- Intended Audience :: Science/Research
- License :: OSI Approved :: MIT License
- Operating System :: OS Independent
- Programming Language :: Python :: 3
- Topic :: Multimedia :: Sound/Audio
- Topic :: Scientific/Engineering :: Artificial Intelligence

## Version History

Track versions in:
- `src/allin1fix/__about__.py` - Version definition
- `docs/CHANGELOG.md` - Detailed changelog
- GitHub Releases - Release notes
