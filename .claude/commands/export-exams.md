# /export-exams - Export Scraped Data

## Purpose
Export validated scraped exam data to various formats for use outside the scraper.

## Syntax
```
/export-exams                 # Interactive export options
/export-exams --format json   # Export as JSON
/export-exams --format csv    # Export as CSV
/export-exams --format xlsx   # Export as Excel
/export-exams --format pdf    # Export as PDF (with formatting)
```

## Export Formats

### JSON (Default)
- Complete data structure preserved
- Suitable for re-import
- Nested questions within exams
- File: `exports/exams.json`

### CSV
- Flat format (one row per question)
- Columns: course_id, course_name, exam_id, exam_title, question_id, question_text, answers, correct_answer
- File: `exports/exams.csv`
- Note: Array fields (answers) delimited by `|`

### Excel (XLSX)
- Multiple sheets per course
- One sheet per exam with question data
- Formatted headers and auto-width columns
- File: `exports/exams.xlsx`

### PDF
- Human-readable formatted report
- Organized by course and exam
- Includes answer keys
- File: `exports/exams.pdf`

## Behavior

1. Validates data before export
2. Creates `exports/` directory if missing
3. Checks if file exists and asks for overwrite
4. Generates file with timestamp
5. Shows file path and file size
6. Opens file in default application (optional)

## Options

### --validate
Run validation before export (default: yes)

### --no-open
Don't open file after export (default: opens)

### --compress
For JSON export, compresses with gzip

## Examples
```
User: "Export the exam data as Excel"
/export-exams --format xlsx

User: "Save exams as CSV for importing"
/export-exams --format csv --no-open
```

## Output Files
```
exports/
├── exams.json              # JSON export
├── exams.csv               # CSV export
├── exams.xlsx              # Excel export
└── exams.pdf               # PDF report
```

## Exit Codes
- `0`: Export successful
- `1`: No data to export (empty file)
- `2`: Validation failed
- `3`: File write error
- `4`: Format not supported

## Related Commands
- `/validate` - Validate before export
- `/run` - Generate data to export
