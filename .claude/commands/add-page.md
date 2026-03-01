# /add-page - Create Page Object

## Purpose
Generate a new page object class scaffold following POM patterns and project conventions.

## Syntax
```
/add-page [PageName]          # Create basic page object
/add-page [PageName] --with-tests # Include test file
```

## Behavior
Creates a new file `pages/page_name.py` with:
- Proper class definition inheriting from BasePage
- Docstring describing the page
- Common locator placeholders
- Template methods for typical interactions
- Type hints
- Docstrings for methods

## Generated Structure
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PageNamePage(BasePage):
    """Page object for PageName page."""

    # Locators
    LOCATOR_NAME = (By.ID, "selector")

    def method_name(self) -> str:
        """Describe what this method does."""
        pass
```

## Options

### --with-tests
Creates companion test file in `tests/test_page_name.py`:
```python
import pytest
from pages.page_name import PageNamePage

class TestPageNamePage:
    def test_page_loads(self, driver):
        page = PageNamePage(driver)
        assert page.is_loaded()
```

## Examples
```
User: "Create a page object for the exam questions page"
/add-page ExamPage

User: "Create page object for login with tests"
/add-page LoginPage --with-tests
```

## Conventions
- Class name in PascalCase: `ExamPage`, `LoginPage`
- File name in snake_case: `exam_page.py`, `login_page.py`
- Locators in UPPER_SNAKE_CASE
- Methods in lowercase with underscores: `click_submit()`, `get_error_message()`

## Related Commands
- `/run` - Test your new page object
- `/test` - Run tests for the page object
- `/lint` - Check code style of generated file
