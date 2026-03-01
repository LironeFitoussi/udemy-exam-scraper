# Data Validation Hook

## Purpose
Automatically validate scraped exam data whenever it's modified, ensuring data quality.

## Triggers
Runs when:
- `/run` completes and generates new data
- `/export-exams` is called
- Data files in `data/` are modified

## Validation Steps

### 1. Schema Check
- ✓ Valid JSON format
- ✓ Required fields present
- ✓ Correct data types

### 2. Data Integrity
- ✓ No duplicate IDs
- ✓ Correct answer in options
- ✓ Answer counts match question type

### 3. Quality Assessment
- ✓ Minimum content per field
- ✓ No encoding issues
- ✓ No malicious patterns
- ✓ Text sanitization

### 4. Summary Stats
- Shows course count, question count
- Flags incomplete exams
- Reports any missing data

## Success Report

```
✅ DATA VALIDATION PASSED

File: data/exams.json
Courses: 5
Exams: 12
Questions: 247

Quality: EXCELLENT
- No duplicates
- All answers valid
- All fields present

Ready to export!
```

## Warning Report

```
⚠️  DATA VALIDATION WARNINGS

File: data/exams.json
Courses: 5
Exams: 12
Questions: 247

Issues Found:
- Exam 'e_005': Only 2 questions (expected 10+)
- Question 'q_089': Answer text appears truncated
- Course 'c_003': Missing course description

Recommendations:
1. Re-scrape exam e_005 for completeness
2. Manually review question q_089
3. Add course description for c_003

Use /validate --fix to auto-correct, or proceed with caution.
```

## Failure Report

```
❌ DATA VALIDATION FAILED

File: data/exams.json

Critical Issues:
- Invalid JSON format (line 156)
- Missing required field: 'correct_answer' in question q_045
- Duplicate exam ID: 'e_003' appears 2 times

Cannot export corrupted data.

Solutions:
1. Use /validate --fix to auto-repair
2. Manually fix data/exams.json
3. Re-run /run to re-scrape
```

## Auto-Fix Behavior

When using `/validate --fix`:
- Fixes JSON formatting issues
- Removes duplicate IDs (keeps first occurrence)
- Validates answer references
- Removes malformed records
- Creates backup: `data/exams.json.backup`

## Automatic Backups
- Backup created before validation
- Format: `data/exams.json.backup-TIMESTAMP`
- Automatic cleanup of old backups (>7 days)

## Disabling Hook
If needed temporarily:
```python
# In your scraper code
# VALIDATE: skip
```

Note: Only use in development, never in production!

## Related
- `/validate` - Manual validation
- `/export-exams` - Export validated data
- `/run` - Generate data to validate
