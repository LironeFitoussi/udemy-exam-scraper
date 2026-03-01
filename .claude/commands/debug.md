# /debug - Debug Scraper

## Purpose
Run the scraper in debug mode with enhanced logging, screenshots on failure, and paused execution for investigation.

## Syntax
```
/debug                   # Run with debug logging
/debug --pause           # Pause on errors for investigation
/debug --screenshot      # Take screenshot on each step
/debug [test_name]       # Debug specific test
```

## Features

### Enhanced Logging
- Verbose console output
- Detailed element finding logs
- Wait timeout information
- Exception stack traces

### Screenshots on Failure
- Automatic screenshot when element not found
- Screenshot on exception
- Saves to `debug_screenshots/` with timestamp

### Pause on Error
- Pauses execution when exception occurs
- Allows browser inspection
- User presses Enter to continue or debug further

### Browser Window
- Keeps browser open for inspection
- Shows all interactions visually
- Helpful for understanding locator issues

## Usage Example

```
User: "The scraper is failing on the exam page"
/debug --pause

# Shows verbose logs
# Takes screenshots on errors
# Pauses when it fails so you can investigate
```

## Output Structure
```
debug_screenshots/
├── 2026-03-01_14-30-45_element_not_found.png
├── 2026-03-01_14-30-50_exception_raised.png
└── ...

Debug log: debug.log
```

## Debugging Tips
1. Use `/debug --screenshot` to see what scraper "sees"
2. Check `debug_screenshots/` for visual clues
3. Look at `debug.log` for timing issues
4. Use browser developer tools while paused
5. Check locators against actual page structure

## Exit Codes
- `0`: Completed without errors
- `1`: Error occurred (paused for debugging)
- `2`: Timeout in debug mode
- `3`: No recovery possible

## Performance Note
Debug mode runs slower due to:
- Extra logging overhead
- Screenshot generation
- Pause waits
- Detailed element introspection

## Related Commands
- `/run` - Run in normal mode
- `/test` - Run unit tests for debugging
- `/lint` - Check code for issues
