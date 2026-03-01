# Running Your Udemy Exam Scraper

## Quick Start

```bash
python main.py
```

That's it! The app will:
1. Launch Firefox (non-headless, you'll see the browser)
2. Navigate to Udemy.com
3. Show you an interactive menu
4. Let you explore and test

## What You Can Do Now

### 1. Browse Udemy
- Menu option 1: Navigate to "My Courses"
- Menu option 2: Search for courses by name
- Menu option 3: View current page info (URL, title, login status)

### 2. Login to Udemy (Experimental)
When you run the app:
1. It checks if you're logged in
2. If not, offers to login
3. You enter email/password
4. It attempts to authenticate

**Current Status**: Login button selector is ready, but full authentication may need adjustment based on Udemy's current UI

## Finding Selectors

To find element selectors for exams and questions, use the debug tool:

```bash
python debug_selectors.py
```

This gives you an interactive inspector to:
- See all links, buttons, and forms on a page
- Search for elements by text
- Find elements by ID, class, or any attribute
- Take screenshots
- Navigate to different pages

## Example: Finding Login Button

```bash
python debug_selectors.py
(press 1) -> "SHOW PAGE STRUCTURE"
(look for login button in output)
(press 2) -> FIND BY TEXT
(type "Log in")
(app shows the selector!)
```

## If Something Doesn't Work

### Issue: Browser doesn't launch
```bash
python fix_drivers.py
```
This will test all browsers and tell you which one works.

### Issue: Can't find a button or element
Use `debug_selectors.py` to:
1. Navigate to that page in the browser
2. Search for the element interactively
3. Get the selector information
4. Add it to the appropriate page object

### Issue: Page loads but nothing happens
Check:
1. Is Firefox running? (look for Firefox window)
2. Is the element actually there? (use `debug_selectors.py`)
3. Does it need more wait time? (increase `time.sleep()`)

## Current Locators

These are already configured:

**UdemyPage (pages/udemy_page.py)**
- `SIGN_IN_BUTTON`: Login button on homepage
- `MY_LEARNING_LINK`: My Courses link
- `SEARCH_INPUT`: Search box
- `SEARCH_BUTTON`: Search submit button

**LoginPage (pages/login_page.py)**
- `EMAIL_INPUT`: Email field
- `PASSWORD_INPUT`: Password field
- `LOGIN_BUTTON`: Login submit button

## Finding Exam Selectors

You need to find:
1. **Courses List**: Where courses with exams are shown
2. **Exam Link**: How to enter an exam section
3. **Questions**: Question text and options
4. **Submit**: How to submit answers

**Steps**:
1. `python debug_selectors.py`
2. Navigate to a course with exams
3. Use menu options to find buttons and links
4. Record the selectors
5. Create `ExamPage` with those selectors

Example what you'll find:
```
1. Course link: //a[contains(text(), 'Python')]
2. Exam button: //button[@data-exam-id='123']
3. Question: //div[@class='question-content']
4. Answer options: //label[@class='answer-option']
5. Submit: //button[contains(text(), 'Submit')]
```

## Creating New Page Objects

Once you have selectors:

```python
# pages/exam_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ExamPage(BasePage):
    QUESTION_TEXT = (By.CLASS_NAME, "question-content")
    ANSWER_OPTIONS = (By.CLASS_NAME, "answer-option")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")

    def get_question(self):
        return self.get_text(*self.QUESTION_TEXT)

    def get_answers(self):
        elements = self.find_elements(*self.ANSWER_OPTIONS)
        return [elem.text for elem in elements]

    def submit_exam(self):
        self.click(*self.SUBMIT_BUTTON)
```

Then use it in main.py:
```python
from pages.exam_page import ExamPage

exam_page = ExamPage(driver)
question = exam_page.get_question()
answers = exam_page.get_answers()
```

## Files Available

| File | Purpose |
|------|---------|
| `main.py` | Main scraper application |
| `debug_selectors.py` | Interactive element finder |
| `fix_drivers.py` | WebDriver troubleshooting |
| `test_drivers.py` | Quick driver test |
| `pages/base_page.py` | Base class for all pages |
| `pages/udemy_page.py` | Udemy homepage interactions |
| `pages/login_page.py` | Login page interactions |
| `pages/inspect_page.py` | Element inspection utility |

## Workflow

```
1. Run the app
   python main.py

2. Test basic navigation
   (use menu options)

3. Find exam selectors
   python debug_selectors.py
   (navigate to exam, find buttons/questions)

4. Create ExamPage
   (new file: pages/exam_page.py)

5. Add exam scraping to main.py
   (use ExamPage to extract questions)

6. Export data
   (save to JSON/CSV)

7. Test and iterate
   (refine selectors, add more features)
```

## Pro Tips

1. **Right-click in browser** -> "Inspect" to see HTML
2. **Record selectors** as you find them (keep notes)
3. **Take screenshots** for debugging
4. **Use simple waits** - wait for elements, not arbitrary time
5. **Test one selector at a time** before moving on

## Next Phase

Once you have exam selectors:
1. Create `ExamPage` class
2. Build course listing scraper
3. Extract questions and answers
4. Export data (JSON/CSV/Excel)
5. Add error handling and logging

Ready? Start with:
```bash
python main.py
```
