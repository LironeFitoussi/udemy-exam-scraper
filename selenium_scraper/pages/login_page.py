from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for Udemy login page"""

    # Udemy login page locators
    GOOGLE_BUTTON = (By.XPATH, "//button[@aria-label='Continue with Google ID']")

    # Google OAuth form locators
    GOOGLE_EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    GOOGLE_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_google_button(self):
        self.click(*self.GOOGLE_BUTTON)
        print("[+] Clicked Google login button")

    def login_with_google(self, email, password):
        """Full Google OAuth login - auto-fills email and password"""
        try:
            # Capture existing windows before clicking
            existing_handles = set(self.driver.window_handles)
            main_window = self.driver.current_window_handle

            self.click_google_button()
            print("[*] Waiting for Google auth window...")

            # Switch to the new Google OAuth popup window
            new_handle = self.wait_for_new_window(existing_handles, timeout=15)
            if not new_handle:
                raise Exception("Google auth window did not open")
            self.driver.switch_to.window(new_handle)
            print("[+] Switched to Google auth window")

            # Enter email then press Enter
            email_field = self.find_element(*self.GOOGLE_EMAIL_FIELD, timeout=15)
            email_field.clear()
            email_field.send_keys(email)
            email_field.send_keys(Keys.ENTER)
            print(f"[+] Entered email: {email}")

            # Enter password then press Enter
            # Must wait for visibility (not just presence) - Google animates the transition
            password_field = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.GOOGLE_PASSWORD_FIELD)
            )
            password_field.clear()
            password_field.send_keys(password)
            password_field.send_keys(Keys.ENTER)
            print("[+] Entered password")

            print("[*] Submitted credentials, waiting for redirect...")
            # Wait until only one window remains (popup closed, main window still open)
            # OR until the popup navigates away from accounts.google.com
            try:
                WebDriverWait(self.driver, 30).until(
                    lambda d: len(d.window_handles) == 1 or new_handle not in d.window_handles
                )
                print("[+] Google auth completed")
            except Exception:
                print("[!] Timeout waiting for auth to complete")

            # Switch to whichever window is still alive (main_window or any remaining)
            handles = self.driver.window_handles
            if main_window in handles:
                self.driver.switch_to.window(main_window)
            elif handles:
                self.driver.switch_to.window(handles[0])
            print("[+] Switched back to main window")

        except Exception as e:
            print(f"[x] Google login failed: {e}")
            # Always try to recover to main window
            try:
                self.driver.switch_to.window(main_window)
            except Exception:
                pass
            raise

    def is_google_button_visible(self, timeout=10):
        return self.is_element_visible(*self.GOOGLE_BUTTON, timeout=timeout)
