# Quick Start Guide

## Installation

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python main.py
```

Or using npm:
```bash
npm start
```

## What You'll See

1. **Browser Selection** - Choose chrome (default), firefox, or edge
2. **Browser Opens** - Non-headless (you see it working)
3. **Udemy Loads** - Navigate to udemy.com
4. **Login Check** - App checks if you're logged in
5. **Interactive Menu** - Choose what to do:
   - Navigate to My Courses
   - Search for a course
   - Show page info
   - Exit

## Features Available Now

✓ **Navigate Udemy** - Browse the site
✓ **Login Support** - Enter email/password
✓ **Search Courses** - Find courses by name
✓ **Page Info** - Check URL, title, login status
✓ **Auto Driver Management** - No driver setup needed

## Page Objects Available

### UdemyPage
```python
from pages.udemy_page import UdemyPage

udemy_page = UdemyPage(driver)
udemy_page.navigate_to_home()
udemy_page.is_logged_in()  # Returns True/False
udemy_page.search_course("Python")
udemy_page.navigate_to_my_courses()
```

### LoginPage
```python
from pages.login_page import LoginPage

login_page = LoginPage(driver)
login_page.login("email@example.com", "password")
```

## Architecture

**Page Object Model (POM)**:
- Separates test logic from page interactions
- Reusable, maintainable code
- Easy to update when Udemy changes

**Directory Structure**:
```
pages/          → Page objects
  ├── base_page.py       → Common methods (wait, click, type, etc.)
  ├── udemy_page.py      → Udemy main page
  └── login_page.py      → Login page

utils/          → Utilities
  └── driver_factory.py  → WebDriver creation

main.py         → Entry point & menu
```

## Making Changes

### Update a Locator
If Udemy changes their HTML, find the locator in the page object and update it:

```python
# In pages/udemy_page.py
MY_LEARNING_LINK = (By.XPATH, "//a[contains(@href, '/home/my-courses')]")
# Change the xpath if needed
```

### Add a New Interaction
```python
def click_wishlist(self):
    """Click on wishlist button"""
    self.click(*self.WISHLIST_BUTTON)
```

### Test It
```python
# In main.py
udemy_page.click_wishlist()
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| WebDriver not found | webdriver-manager installs it automatically |
| Element not found | Check locator, wait time might be too short |
| Login fails | Check email/password, Udemy might have updated HTML |
| Browser doesn't open | Ensure Chrome/Firefox/Edge is installed |

## Notes

- **Non-headless mode**: You see the browser, can interact manually
- **No credentials saved**: You enter them when prompted (more secure)
- **Locators may change**: Udemy updates their HTML - update selectors when needed
- **Page Object Pattern**: Each page/component has its own class

## Next: Building Exam Scraping

To extract exams, we'll need:
1. ExamPage object (navigate exams, click questions)
2. QuestionPage object (extract question text, answers)
3. DataExporter (save to JSON/CSV/Excel)
4. Tests (verify scraping works)

Ready? Run: `python main.py`
