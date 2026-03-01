# Pre-Commit Checks Hook

## Purpose
Run automated checks before allowing commits to catch issues early.

## Triggers
Runs when user attempts to create a commit with `/commit` or git commands.

## Checks Performed

### 1. No Credentials
- ✓ Scans staged files for hardcoded secrets
- ✓ Checks for .env, config files with credentials
- ✓ Detects API keys, passwords, tokens
- ⚠️ Fails commit if credentials found

### 2. Code Style
- ✓ Runs flake8 on changed Python files
- ✓ Checks for obvious violations (imports, syntax)
- ⚠️ Warns but doesn't block on style issues

### 3. Tests
- ✓ Ensures related tests exist for changed code
- ✓ Runs pytest on affected test files
- ⚠️ Fails if tests fail

### 4. File Validation
- ✓ JSON syntax check for any .json files
- ✓ Python syntax check for .py files
- ⚠️ Fails if syntax invalid

## Failure Example

```
❌ PRE-COMMIT CHECK FAILED

Issue: Hardcoded credentials detected
File: config/config.py
Line: 15: password = "secret123"

Solution:
1. Move credential to config/credentials.json (add to .gitignore)
2. Load from environment variable
3. Use: os.environ.get('DB_PASSWORD')

Remove the hardcoded value and try commit again.
```

## Warnings vs Blocks

### Blocks Commit ❌
- Hardcoded credentials
- Invalid syntax
- Failing tests

### Warns but Proceeds ⚠️
- Style issues (can fix with `/lint --fix`)
- Missing docstrings
- Low test coverage

## Allowing Override
If you're sure about a change, use:
```bash
git commit --no-verify
```

Note: This is only for emergency use! Proper fixes are better.

## Staged Files
Hook only checks FILES YOU'RE COMMITTING, not:
- Uncommitted changes
- Files not staged
- Previous commits

## Performance
Checks run in parallel for speed:
- Typical time: 2-5 seconds
- Can disable with `--no-verify` (not recommended)

## Related
- `/lint` - Fix style issues before commit
- `/test` - Run full test suite
- `/validate` - Check data integrity
