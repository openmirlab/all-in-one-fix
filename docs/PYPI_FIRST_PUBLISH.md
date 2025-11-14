# First-Time PyPI Publishing Guide

## Problem

PyPI trusted publishing (OIDC) **cannot create new projects**. It can only upload to existing projects.

If you see this error:
```
Non-user identities cannot create new projects. This was probably caused by successfully using a pending publisher but specifying the project name incorrectly...
```

This means the project `allin1fix` doesn't exist on PyPI yet and needs to be created manually first.

## Solution: Two-Step Process

### Step 1: Create Project on PyPI (Manual - One Time Only)

You need to create the project on PyPI using a **user account** (not OIDC):

1. **Log in to PyPI:**
   - Visit: https://pypi.org/account/login/
   - Log in with your PyPI user account

2. **Create the project:**
   - Option A: Upload a dummy package first
     ```bash
     # Build the package locally
     pip install build setuptools wheel torch>=2.0.0
     python -m build
     
     # Upload using twine with your PyPI credentials
     pip install twine
     twine upload dist/* --repository pypi
     ```
     - You'll be prompted for your PyPI username and password/API token
   
   - Option B: Use PyPI web interface
     - Go to: https://pypi.org/manage/projects/
     - Click "Add new project"
     - Enter project name: `allin1fix`
     - Fill in basic metadata
     - Upload an initial version

3. **Verify project exists:**
   - Check: https://pypi.org/project/allin1fix/
   - The project should now exist (even if empty or with a dummy version)

### Step 2: Configure Trusted Publishing (For Future Uploads)

Once the project exists, configure trusted publishing:

1. **Go to PyPI Account Settings:**
   - Visit: https://pypi.org/manage/account/publishing/
   - Log in to your PyPI account

2. **Add Trusted Publisher:**
   - Click "Add a new pending publisher"
   - Fill in:
     - **PyPI project name:** `allin1fix` (must match exactly!)
     - **Owner:** `openmirlab`
     - **Repository name:** `all-in-one-fix`
     - **Workflow filename:** `publish.yml`
     - **Environment name:** (leave empty)

3. **Verify Configuration:**
   - The publisher should appear as "pending"
   - After the next successful workflow run, it becomes "active"

### Step 3: Use Trusted Publishing (Automated)

After Step 1 and 2 are complete, all future releases will use trusted publishing automatically:

```bash
# Create a release (triggers workflow automatically)
gh release create v2.0.1 --title "v2.0.1" --notes "Release notes"

# Or manually trigger workflow
gh workflow run publish.yml
```

## Quick Checklist

- [ ] Project `allin1fix` exists on PyPI (check https://pypi.org/project/allin1fix/)
- [ ] Trusted publisher configured in PyPI settings
- [ ] Project name in trusted publisher matches `allin1fix` exactly
- [ ] GitHub repository owner is `openmirlab`
- [ ] Repository name is `all-in-one-fix`
- [ ] Workflow filename is `publish.yml`

## Troubleshooting

### Error: "Non-user identities cannot create new projects"
- **Cause:** Project doesn't exist on PyPI yet
- **Fix:** Complete Step 1 above (create project manually)

### Error: "Project name mismatch"
- **Cause:** Trusted publisher project name doesn't match `pyproject.toml`
- **Fix:** Verify trusted publisher uses exact name `allin1fix` (case-sensitive)

### Error: "Repository not found"
- **Cause:** Wrong owner or repository name in trusted publisher
- **Fix:** Verify owner is `openmirlab` and repository is `all-in-one-fix`

## After First Manual Upload

Once you've created the project manually and configured trusted publishing:
- ✅ All future releases will be automatic via GitHub Actions
- ✅ No more manual uploads needed
- ✅ Secure OIDC authentication (no API tokens to manage)
