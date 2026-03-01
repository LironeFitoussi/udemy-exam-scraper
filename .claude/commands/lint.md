# /lint - Code Quality Checks

## Purpose
Run code style and quality checks using flake8, black, and other linters.

## Syntax
```
/lint                    # Check code style
/lint --fix              # Auto-fix style issues
/lint --strict           # Strict mode (treat warnings as errors)
```

## Checks Performed

### Style (flake8)
- ✓ PEP 8 compliance
- ✓ Line length (max 100 chars)
- ✓ Unused imports
- ✓ Undefined names
- ✓ Whitespace issues

### Formatting (black)
- ✓ Code formatting consistency
- ✓ String quote style
- ✓ Line breaks

### Security (bandit)
- ✓ Hardcoded passwords/secrets
- ✓ SQL injection patterns
- ✓ Insecure function usage
- ✓ Missing input validation

## Output Example
```
pages/exam_page.py:45:1: E302 expected 2 blank lines, found 1
utils/driver_factory.py:12:0: F401 'time' imported but unused

Found 2 issues. Use --fix to auto-correct.
```

## Installation
```bash
pip install flake8 black bandit
```

## Exit Codes
- `0`: No issues found
- `1`: Issues found (fixable)
- `2`: Issues found (not fixable)
- `3`: Lint tool error

## Using --fix
- Automatically corrects style issues
- Reformats code to black standards
- Removes unused imports
- May require manual review for complex changes

## Example
```
User: "Check code quality"
/lint

User: "Fix style issues"
/lint --fix
```

## Related Commands
- `/test` - Run tests after linting
- `/run` - Execute after validation
