from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, by, value, timeout=None):
        """Wait for element to be present"""
        wait_time = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            return None

    def find_elements(self, by, value, timeout=None):
        """Wait for elements to be present"""
        wait_time = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located((by, value))
            )
        except TimeoutException:
            return []

    def click(self, by, value, timeout=None):
        """Wait for element to be clickable, then click"""
        wait_time = timeout or self.timeout
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def send_keys(self, by, value, text, timeout=None):
        """Wait for element to be visible, clear it, and send keys"""
        element = self.find_element(by, value, timeout)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, by, value, timeout=None):
        """Wait for element and get text"""
        element = self.find_element(by, value, timeout)
        return element.text if element else None

    def is_element_visible(self, by, value, timeout=None):
        """Wait for element to be visible"""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url_change(self, current_url, timeout=None):
        """Wait for URL to change from current URL"""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.url_changes(current_url)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url(self, url, timeout=None):
        """Wait for specific URL"""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.url_to_be(url)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_text(self, by, value, text, timeout=None):
        """Wait for element text to contain specific text"""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.text_to_be_present_in_element((by, value), text)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_new_window(self, existing_handles, timeout=None):
        """Wait for a new browser window/tab to open and return its handle"""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda d: len(d.window_handles) > len(existing_handles)
            )
            new_handles = [h for h in self.driver.window_handles if h not in existing_handles]
            return new_handles[0] if new_handles else None
        except TimeoutException:
            return None

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url