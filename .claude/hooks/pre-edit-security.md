# Pre-Edit Security Hook

## Purpose
Detect and warn about potential security issues before editing files.

## Triggers
Runs when user attempts to edit or write to any Python file.

## Checks

### Credential Detection
- ⚠️ Warns if editing `config/` files that might contain secrets
- ⚠️ Detects hardcoded API keys, passwords, tokens
- ⚠️ Checks for environment variable references

### Sensitive Patterns
- ⚠️ SQL query construction (SQL injection risk)
- ⚠️ Shell command execution (command injection risk)
- ⚠️ File path manipulation (path traversal risk)
- ⚠️ Direct user input usage without validation

### Common Issues
- ⚠️ Missing input validation
- ⚠️ Logging sensitive data
- ⚠️ Storing credentials in code

## Warning Message Format
```
⚠️  SECURITY WARNING: Potential {issue} detected
   Location: {file}:{line}
   Issue: {description}
   Fix: {suggestion}
```

## Allowed Actions
User can:
- Proceed with edit (acknowledging risk)
- Cancel edit and fix issue first
- View suggested fix

## Example
```
User tries to add hardcoded password to config.py

Hook warns:
⚠️  SECURITY WARNING: Hardcoded credential detected
   Issue: 'password="secret123"' in config.py
   Fix: Use environment variables instead

User can proceed or cancel.
```

## Exceptions
Security checks are bypassed for:
- Changes to existing files that already have the issue
- Lines marked with `# noqa: security` comment

## Related
- Commit hooks also check for credentials before pushing
- `/lint --strict` detects security issues
