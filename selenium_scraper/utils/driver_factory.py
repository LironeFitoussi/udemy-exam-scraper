from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import glob
import os


class DriverFactory:
    @staticmethod
    def _find_chromedriver():
        """Find chromedriver.exe from Selenium Manager or wdm cache"""
        search_paths = [
            os.path.expanduser(r"~\.cache\selenium\chromedriver\**\chromedriver.exe"),
            os.path.expanduser(r"~\.wdm\drivers\chromedriver\**\chromedriver.exe"),
        ]
        for pattern in search_paths:
            matches = glob.glob(pattern, recursive=True)
            if matches:
                matches.sort(reverse=True)
                return matches[0]
        return None

    @staticmethod
    def get_driver(browser="chrome", headless=False):
        if browser.lower() != "chrome":
            raise Exception("Only 'chrome' is supported")

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # Persist Chrome profile so Udemy sees the same session across runs
        profile_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".chrome_profile")
        options.add_argument(f"--user-data-dir={profile_dir}")

        # Pin to system Google Chrome (not Chromium)
        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        # Use cached chromedriver directly so Selenium Manager can't substitute Chromium
        chromedriver = DriverFactory._find_chromedriver()
        service = ChromeService(chromedriver, log_output=os.devnull) if chromedriver else ChromeService(log_output=os.devnull)
        return webdriver.Chrome(service=service, options=options)

    @staticmethod
    def quit_driver(driver):
        if driver:
            try:
                driver.quit()
            except:
                pass
