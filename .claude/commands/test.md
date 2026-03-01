# /test - Run Tests

## Purpose
Execute pytest test suite with various options for test development and verification.

## Syntax
```
/test                    # Run all tests
/test [file_or_path]     # Run specific test file
/test [file]::[func]     # Run specific test function
/test --cov              # With coverage report
/test --cov --html       # Coverage report as HTML
/test -v                 # Verbose output
/test-watch              # Watch mode (rerun on changes)
```

## Behavior

### Standard Run
- Discovers all tests in `tests/` directory
- Runs tests in parallel for speed
- Shows pass/fail status per test
- Displays summary at end

### Coverage Mode
- Measures code coverage
- Reports uncovered lines
- Generates HTML report in `htmlcov/`
- Shows coverage percentage

### Watch Mode
- Monitors `pages/`, `utils/`, and `tests/` directories
- Reruns relevant tests on file changes
- Useful during development

## Implementation
Executes:
```bash
pytest tests/ [options]
```

## Exit Codes
- `0`: All tests passed
- `1`: One or more tests failed
- `2`: Test execution error
- `5`: No tests collected

## Pre-Run Checks
- Virtual environment activated
- pytest installed (`pip install pytest pytest-cov`)
- No syntax errors in test files

## Example
```
User: "Run the test suite and show coverage"
Claude uses /test --cov to run tests with coverage report
```

## Related Commands
- `/run` - Run scraper
- `/lint` - Check code style
- `/debug` - Debug specific test failure
