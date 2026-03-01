from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os


class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome", headless=False):
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)

            # Persist Chrome profile so Udemy sees the same session across runs
            profile_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".chrome_profile")
            options.add_argument(f"--user-data-dir={profile_dir}")

            # Explicitly use the system Google Chrome installation (not Chromium)
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

            return webdriver.Chrome(options=options)

        raise Exception("Provide a valid browser name (chrome)")

    @staticmethod
    def quit_driver(driver):
        if driver:
            try:
                driver.quit()
            except:
                pass
