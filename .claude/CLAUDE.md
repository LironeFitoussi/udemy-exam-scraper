# Udemy Exam Scraper - Claude Project Configuration

## Project Overview

This is a **Selenium-based web scraper** designed to extract exam questions and answers from Udemy courses. Built on a professional Page Object Model (POM) architecture for maintainability and scalability.

### Current Architecture
- **Framework**: Python + Selenium 4.21.0
- **Pattern**: Page Object Model (POM)
- **Structure**: Modular with separate config, pages, and utils
- **Target**: Automated Udemy exam scraping

---

## Development Workflow

### Running the Scraper
```bash
# Option 1: Direct execution
python main.py

# Option 2: Using npm
npm start

# Option 3: Using Claude command
/run          # Runs the scraper with interactive prompts
/run-headless # Runs in headless mode for automation
```

### Testing
```bash
# Run all tests
/test

# Run specific test file
/test tests/test_exam_scraper.py

# Run with coverage
/test --cov
```

### Adding New Page Objects
```bash
# Create a new page object class
/add-page ExamPage    # Creates pages/exam_page.py

# Create a page object for a specific component
/add-page UdemyHeader
```

### Managing Scraped Data
```bash
# Export exam data
/export-exams   # Interactive export options

# Validate scraped data
/validate       # Run validation checks on data
```

---

## Code Organization

### Key Directories
- **`config/`**: Configuration files, URLs, credentials
- **`pages/`**: Page object classes (one per page/component)
- **`utils/`**: Utilities like DriverFactory, data handlers
- **`tests/`**: Pytest test files (to be created)
- **`data/`**: Scraped exam data (gitignored)

### Page Object Conventions
1. Create one class per page/component in `pages/`
2. Inherit from `BasePage` for common methods
3. Use By locators at class level
4. Write descriptive method names: `click_start_exam()`, `get_question_text()`
5. Use explicit waits in BasePage methods

Example:
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ExamPage(BasePage):
    # Locators
    START_EXAM_BTN = (By.ID, "start-exam")
    QUESTION_TEXT = (By.CLASS_NAME, "question-content")

    def click_start_exam(self):
        self.click(self.START_EXAM_BTN)

    def get_current_question(self):
        return self.get_text(self.QUESTION_TEXT)
```

---

## Data Handling

### Scraping Output Format
Scraped exam data is saved as JSON with structure:
```json
{
  "course_id": "123456",
  "course_name": "Course Title",
  "exams": [
    {
      "exam_id": "exam_1",
      "title": "Midterm Exam",
      "questions": [
        {
          "id": "q1",
          "text": "Question text",
          "answers": ["A", "B", "C"],
          "correct_answer": "A"
        }
      ]
    }
  ]
}
```

### Data Validation
- Ensure all required fields present
- Validate answer format matches question
- Check for duplicate questions
- Run `/validate` before export

---

## Environment Setup

### Requirements
- Python 3.6+
- Virtual environment (recommended)
- Selenium 4.21.0
- pytest (for testing)

### Installation
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows Git Bash)
source .venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies (testing)
pip install pytest pytest-cov
```

---

## Debugging & Troubleshooting

### Common Issues
1. **WebDriver not found**: `webdriver-manager` auto-manages drivers
2. **Element not found**: Check selector, add explicit waits in BasePage
3. **Login failures**: Store credentials in `config/config.py` (gitignored)

### Debug Mode
```bash
/debug         # Run with verbose logging
/debug --pause # Pause on failures for inspection
```

### Taking Screenshots
```python
# In page objects
driver.save_screenshot('debug_screenshot.png')
```

---

## Security & Best Practices

### Credentials
- **Never commit** credentials to git
- Store in `config/credentials.json` (gitignored)
- Load via `config/config.py`

### Scraping Ethics
- Respect Udemy's Terms of Service
- Use delays between requests (`time.sleep()`)
- Identify as a bot in User-Agent if needed
- Check `robots.txt` compliance

### Error Handling
- Use try/except in scraping loops
- Log failures with timestamps
- Continue scraping on recoverable errors
- Stop on authentication failures

---

## Commands Available

| Command | Purpose |
|---------|---------|
| `/run` | Run scraper interactively |
| `/run-headless` | Run in headless mode |
| `/test` | Run pytest suite |
| `/test-watch` | Watch for changes and rerun tests |
| `/add-page [name]` | Create new page object |
| `/export-exams` | Export scraped data |
| `/validate` | Validate scraped data |
| `/debug` | Run with verbose logging |
| `/lint` | Run code quality checks |

---

## Git Workflow

### Commit Message Format
```
feat: Add ExamPage object for parsing questions
fix: Handle dynamic wait for answer options
docs: Update README with scraping instructions
test: Add tests for ExamPage
```

### Before Pushing
1. Run `/test` - all tests must pass
2. Run `/lint` - check code style
3. Verify no credentials in staged files
4. Use `/commit` for guided commits

---

## Questions? Need Help?

- Check existing page objects in `pages/` for patterns
- Review `BasePage` for available helper methods
- Look at test examples in `tests/`
- Ask Claude Code `/help` for feature documentation
