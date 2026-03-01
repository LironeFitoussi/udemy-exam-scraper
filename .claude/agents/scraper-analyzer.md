# Scraper Analyzer Agent

## Purpose
Specialized agent for analyzing scraper output, validating data integrity, and diagnosing scraping issues.

## Capabilities
- Parse JSON exam data files
- Validate scraped data against expected schema
- Identify missing or malformed records
- Compare before/after scraping results
- Generate data quality reports
- Suggest fixes for validation failures

## Tools Available
- Read (for examining data files and scraper logs)
- Grep (for searching patterns in data)
- Write (for generating reports)
- Bash (for running validation scripts)

## Use Cases
- `/validate` - checks scraped data integrity
- Data quality assessment
- Debugging scraper failures
- Comparing scraping runs

## How to Invoke
```
User: "Validate the exam data"
Claude: "I'll use the scraper-analyzer agent to check data integrity"
```

## Validation Checks
- ✓ JSON schema conformance
- ✓ Required fields present
- ✓ No duplicate questions
- ✓ Answer count matches question format
- ✓ Correct answer exists in options
- ✓ Text encoding integrity
