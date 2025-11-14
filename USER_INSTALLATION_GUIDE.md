# User Installation Guide for allin1fix

## What Users Will Do

When users want to install `allin1fix` from PyPI, here's exactly what they'll do:

## 🎯 Simple Answer: Copy & Paste This

```bash
pip install torch>=2.0.0 && pip install allin1fix --no-build-isolation
```

That's it! This single command installs everything needed.

## 📋 Detailed Steps

### Step 1: Install PyTorch
```bash
pip install torch>=2.0.0
```

**Why first?** The `natten` dependency needs `torch` during its build process.

### Step 2: Install allin1fix
```bash
pip install allin1fix --no-build-isolation
```

**Why `--no-build-isolation`?** This flag allows `natten` to access the `torch` you just installed during its build.

## 🔄 Alternative: Using UV (Faster)

If users have `uv` installed (or want to install it):

```bash
# Install UV (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install allin1fix
uv add torch && uv add allin1fix --no-build-isolation
```

## ❌ What Won't Work

**This will FAIL:**
```bash
pip install allin1fix  # ❌ Missing torch and --no-build-isolation
```

**Error you'll see:**
```
ModuleNotFoundError: No module named 'torch'
hint: This error likely indicates that `natten@0.17.5` depends on `torch`, 
but doesn't declare it as a build dependency.
```

## ✅ What Will Work

**All of these work:**

1. **Single command (recommended):**
   ```bash
   pip install torch>=2.0.0 && pip install allin1fix --no-build-isolation
   ```

2. **Two separate commands:**
   ```bash
   pip install torch>=2.0.0
   pip install allin1fix --no-build-isolation
   ```

3. **With UV:**
   ```bash
   uv add torch && uv add allin1fix --no-build-isolation
   ```

4. **In a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install torch>=2.0.0 && pip install allin1fix --no-build-isolation
   ```

## 🎮 GPU Support

For users who want GPU acceleration:

```bash
# Install PyTorch with CUDA (example: CUDA 12.1)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Then install allin1fix
pip install allin1fix --no-build-isolation
```

## ✅ Verify Installation

After installation, users can verify it worked:

```bash
# Check if installed
python -c "import allin1fix; print('✅ allin1fix installed successfully!')"

# Check version
python -c "import allin1fix; print(allin1fix.__version__)"

# Test CLI
allin1fix --help
```

## 🐛 Common Issues & Solutions

### Issue 1: "No module named 'torch'"
**Cause:** Didn't install torch first or didn't use `--no-build-isolation`

**Solution:**
```bash
pip install torch>=2.0.0
pip install allin1fix --no-build-isolation
```

### Issue 2: "scipy version conflict"
**Cause:** Using Python < 3.9

**Solution:** Upgrade to Python 3.9+

### Issue 3: "madmom installation failed"
**Cause:** `madmom` is installed from GitHub, requires git and internet

**Solution:** Ensure git is installed and you have internet access

## 📝 Summary

**What users need to remember:**
1. Install `torch>=2.0.0` first
2. Use `--no-build-isolation` flag
3. Python 3.9+ required

**Simplest command:**
```bash
pip install torch>=2.0.0 && pip install allin1fix --no-build-isolation
```

That's all users need to know! 🎉
