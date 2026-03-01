# /run - Execute Scraper

## Purpose
Run the Udemy exam scraper with interactive mode or headless mode.

## Syntax
```
/run              # Interactive mode (default)
/run-headless     # Headless mode for automation
/run --debug      # Debug mode with verbose logging
```

## Behavior

### Interactive Mode (`/run`)
1. Prompts user for Udemy URL
2. Asks to select browser (Chrome/Firefox/Edge)
3. Launches browser with Selenium
4. Begins exam question scraping
5. Saves results to `data/exams.json`
6. Shows progress in console

### Headless Mode (`/run-headless`)
- Same as interactive but without browser UI
- Useful for automated/scheduled scraping
- Output to log file
- No user interaction needed

### Debug Mode (`/run --debug`)
- Verbose logging to console
- Pauses on errors for inspection
- Takes screenshots on failures
- Keeps browser window open for debugging

## Implementation
Executes:
```bash
python main.py [options]
```

## Exit Codes
- `0`: Success
- `1`: URL validation failed
- `2`: Browser selection invalid
- `3`: Scraping error occurred
- `4`: Data export failed

## Example
```
User: "Run the scraper on udemy.com/course/python-101"
Claude uses /run to execute with that URL
```

## Related Commands
- `/test` - Run test suite before scraping
- `/validate` - Validate scraped output
- `/export-exams` - Export data after scraping
