from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UdemyPage(BasePage):
    """Page object for Udemy main page interactions"""

    # Locators
    SIGN_IN_BUTTON = (By.XPATH, "//a[@data-purpose='header-login']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search for anything']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'search')]")
    MY_LEARNING_LINK = (By.XPATH, "//a[contains(@href, '/home/my-courses')]")
    USER_MENU = (By.XPATH, "//button[contains(@aria-label, 'user menu')]")
    PROFILE_DROPDOWN = (By.XPATH, "//div[@role='menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Log out')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.udemy.com"

    def navigate_to_home(self):
        """Navigate to Udemy home page - waits for page to load"""
        self.driver.get(self.base_url)
        # Wait for search input to appear (indicates page loaded)
        self.is_element_visible(*self.SEARCH_INPUT, timeout=15)
        print("[+] Navigated to Udemy home page")

    def is_logged_in(self, timeout=5):
        """Check if user is logged in by looking for My Learning link"""
        return self.is_element_visible(*self.MY_LEARNING_LINK, timeout=timeout)

    def click_sign_in(self):
        """Click on the sign in button - waits for it to be clickable"""
        self.click(*self.SIGN_IN_BUTTON, timeout=10)
        print("[+] Clicked sign in button")

    def search_course(self, course_name):
        """Search for a course by name - waits for results"""
        self.send_keys(*self.SEARCH_INPUT, course_name, timeout=10)
        self.click(*self.SEARCH_BUTTON, timeout=10)
        print(f"[+] Searched for course: {course_name}")

    def navigate_to_my_courses(self):
        """Navigate to my learning/courses page - waits for page to load"""
        current_url = self.get_url()
        self.click(*self.MY_LEARNING_LINK, timeout=10)
        # Wait for URL to change to my-courses
        self.wait_for_url_change(current_url, timeout=15)
        print("[+] Navigated to My Courses")

    def get_page_title(self):
        """Get the current page title"""
        return self.get_title()

    def get_current_url(self):
        """Get the current page URL"""
        return self.get_url()
