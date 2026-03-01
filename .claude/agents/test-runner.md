# Test Runner Agent

## Purpose
Specialized agent for running pytest tests, managing test execution, and reporting results.

## Capabilities
- Run all tests in the suite
- Run specific test files or test functions
- Generate coverage reports
- Watch mode for development
- Parse and summarize test failures

## Tools Available
- Bash (for pytest execution)
- Read (for reviewing test files and results)
- Grep (for searching test patterns)

## Use Cases
- `/test` - runs pytest suite
- `/test-watch` - runs in watch mode
- Coverage analysis
- Debugging failed tests

## How to Invoke
```
User: "Run the tests"
Claude: "I'll use the test-runner agent to execute pytest"
```

## Success Criteria
- All tests pass (exit code 0)
- Coverage meets minimum threshold
- Clear output of pass/fail per test
- Summary statistics reported
