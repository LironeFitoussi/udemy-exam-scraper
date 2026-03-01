# Post-Test Report Hook

## Purpose
Generate and display test summary after running pytest.

## Triggers
Runs after `/test` command completes.

## Behavior

### On Success
Shows:
- ✅ Test count passed
- ⏱️  Execution time
- 📊 Coverage percentage (if available)
- 🎯 Recommendation: "Great! All tests passing. Ready to commit."

### On Failure
Shows:
- ❌ Count of failed tests
- 📋 List of failed test names
- 🔍 Suggested next steps
- 💡 Link to failed test files

### Coverage Report
If coverage enabled:
- Shows overall coverage percentage
- Lists files below coverage threshold
- Suggests which files need more tests

## Example Output

```
TEST SUMMARY
============
Status:     ✅ PASSED
Tests:      42 passed
Duration:   3.45s
Coverage:   87%

All tests passing! Ready for commit.

Next steps:
- /lint to check code style
- /commit to save your changes
```

## Failure Example

```
TEST SUMMARY
============
Status:     ❌ FAILED
Tests:      40 passed, 2 failed
Duration:   4.12s

Failed Tests:
❌ tests/test_exam_page.py::TestExamPage::test_get_questions
❌ tests/test_driver_factory.py::TestDriverFactory::test_edge_browser

Next steps:
1. Review failed test output above
2. Check implementation in pages/exam_page.py
3. Run: /debug tests/test_exam_page.py
```

## Actions Offered
- Review test output
- Jump to failing test file
- Run failing test in debug mode
- Check coverage report

## Disabled For
- CI/CD environments (GITHUB_ACTIONS env var)
- Quiet mode (`/test --quiet`)
- Watch mode (reports per-test, not summary)
