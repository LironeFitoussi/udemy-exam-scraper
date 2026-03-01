# /validate - Validate Scraped Data

## Purpose
Check scraped exam data for quality, completeness, and conformance to expected schema.

## Syntax
```
/validate                    # Validate all data files
/validate [file_path]        # Validate specific file
/validate --strict           # Strict validation (fail on warnings)
/validate --fix              # Attempt to auto-fix issues
```

## Validation Checks

### Schema Validation
- ✓ Valid JSON format
- ✓ Required fields present (course_id, course_name, exams)
- ✓ Exam fields valid (exam_id, title, questions)
- ✓ Question fields valid (id, text, answers, correct_answer)

### Data Integrity
- ✓ No duplicate question IDs
- ✓ No duplicate course IDs
- ✓ Correct answer exists in answers list
- ✓ Answer count matches question type (MCQ should have 2-5 options)
- ✓ Text fields not empty
- ✓ Valid Unicode encoding

### Quality Checks
- ✓ Minimum question count per exam
- ✓ Answer text not malformed (HTML, encoding issues)
- ✓ Question text length reasonable
- ✓ No suspicious patterns (scripts, malicious content)

## Output Format
```
Validation Report
================
File: data/exams.json
Status: PASS with warnings

Courses: 5
Questions: 247
Issues: 2

Warnings:
- Question q_123: Answer text truncated?
- Exam e_456: Only 1 question (expected 10+)

Use --fix to auto-correct, or review data manually.
```

## Exit Codes
- `0`: All validations passed
- `1`: Validation errors found
- `2`: File not found
- `3`: Invalid JSON

## Example
```
User: "Check if the exam data is valid"
/validate data/exams.json

User: "Fix any issues in the data"
/validate --fix
```

## Related Commands
- `/run` - Generate data to validate
- `/export-exams` - Export validated data
