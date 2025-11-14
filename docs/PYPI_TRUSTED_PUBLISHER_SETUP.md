# PyPI Trusted Publisher Setup - Step by Step

## Error You're Seeing

```
Error: Trusted publishing exchange failure: 
Token request failed: the server refused the request for the following reasons:
* `invalid-publisher`: valid token, but no corresponding publisher
```

This means the trusted publisher is not configured on PyPI yet.

## Step-by-Step Setup

### Step 1: Create the Project on PyPI (One-Time)

**Important:** The project `all-in-one-fix` must exist on PyPI before trusted publishing can work.

1. **Log in to PyPI:**
   - Go to: https://pypi.org/account/login/
   - Log in with your PyPI account

2. **Create the project:**
   - Option A: Upload manually via web interface
     - Go to: https://pypi.org/manage/projects/
     - Click "Add new project"
     - Enter project name: `all-in-one-fix` (exactly, with hyphens)
     - Fill in basic metadata
     - Upload an initial version (you can upload a dummy version)
   
   - Option B: Upload via command line (recommended)
     ```bash
     # Build the package locally
     pip install build setuptools wheel torch>=2.0.0
     python -m build
     
     # Upload using twine (you'll need PyPI username/password or API token)
     pip install twine
     twine upload dist/*
     ```
     - You'll be prompted for your PyPI username and password/API token

3. **Verify project exists:**
   - Check: https://pypi.org/project/all-in-one-fix/
   - The project should now exist

### Step 2: Configure Trusted Publisher

1. **Go to PyPI Account Settings:**
   - Visit: https://pypi.org/manage/account/publishing/
   - Log in to your PyPI account

2. **Add Trusted Publisher:**
   - Click "Add a new pending publisher" button
   - Fill in the form with these **exact** values:

   **PyPI project name:**
   ```
   all-in-one-fix
   ```
   ⚠️ Must match exactly (with hyphens, lowercase)

   **Owner:**
   ```
   openmirlab
   ```
   ⚠️ Must match exactly (lowercase, no spaces)

   **Repository name:**
   ```
   all-in-one-fix
   ```
   ⚠️ Must match exactly (with hyphens, lowercase)

   **Workflow filename:**
   ```
   publish.yml
   ```
   ⚠️ Must match exactly (including `.yml` extension)

   **Environment name:**
   ```
   (leave empty)
   ```
   ⚠️ Leave this field empty

3. **Save the configuration:**
   - Click "Add" or "Save"
   - The publisher should appear as "pending"

### Step 3: Verify Configuration

The trusted publisher will show as "pending" until the next successful workflow run. After a successful run, it will become "active".

### Step 4: Re-run the Workflow

After configuring the trusted publisher, re-run the workflow:

```bash
gh workflow run publish.yml
```

Or create a new release to trigger it automatically.

## Verification Checklist

Before running the workflow, verify:

- [ ] Project `all-in-one-fix` exists on PyPI (check https://pypi.org/project/all-in-one-fix/)
- [ ] Trusted publisher is configured in PyPI settings (https://pypi.org/manage/account/publishing/)
- [ ] PyPI project name: `all-in-one-fix` (exact match)
- [ ] Owner: `openmirlab` (exact match)
- [ ] Repository name: `all-in-one-fix` (exact match)
- [ ] Workflow filename: `publish.yml` (exact match)
- [ ] Environment name: (empty)

## Troubleshooting

### Error: "Publisher with matching claims was not found"

**Possible causes:**
1. Trusted publisher not configured yet → Complete Step 2 above
2. Project doesn't exist on PyPI → Complete Step 1 above
3. Typo in configuration → Double-check all values match exactly (case-sensitive)

**Verify your configuration matches these claims:**
- `repository`: `openmirlab/all-in-one-fix`
- `repository_owner`: `openmirlab`
- `workflow_ref`: `openmirlab/all-in-one-fix/.github/workflows/publish.yml@refs/tags/v2.0.2`

### Error: "Non-user identities cannot create new projects"

**Cause:** Project doesn't exist on PyPI yet  
**Fix:** Complete Step 1 above (create project manually first)

### Publisher shows as "pending" but workflow fails

**Possible causes:**
1. Typo in one of the fields → Check for exact matches (case-sensitive, hyphens)
2. Wrong workflow filename → Should be `publish.yml` (not `publish.yaml`)
3. Project name mismatch → Should be `all-in-one-fix` (not `allin1fix`)

## After Successful Configuration

Once the trusted publisher is configured and the first workflow succeeds:
- ✅ Publisher status changes from "pending" to "active"
- ✅ All future releases will publish automatically
- ✅ No more manual uploads needed
- ✅ Secure OIDC authentication (no API tokens to manage)

## Reference: Current Claims

From the error message, these are the claims GitHub sends to PyPI:

```
* `sub`: `repo:openmirlab/all-in-one-fix:ref:refs/tags/v2.0.2`
* `repository`: `openmirlab/all-in-one-fix`
* `repository_owner`: `openmirlab`
* `repository_owner_id`: `241872330`
* `workflow_ref`: `openmirlab/all-in-one-fix/.github/workflows/publish.yml@refs/tags/v2.0.2`
* `job_workflow_ref`: `openmirlab/all-in-one-fix/.github/workflows/publish.yml@refs/tags/v2.0.2`
* `ref`: `refs/tags/v2.0.2`
```

Your trusted publisher configuration must match:
- **Owner:** `openmirlab` (from `repository_owner`)
- **Repository:** `all-in-one-fix` (from `repository`, after the `/`)
- **Workflow:** `publish.yml` (from `workflow_ref`, the filename part)
