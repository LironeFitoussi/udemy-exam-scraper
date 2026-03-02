"""
Utility for inspecting page elements and finding selectors
Useful for discovering correct locators during development
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InspectPage(BasePage):
    """Utility page object for element inspection"""

    def __init__(self, driver):
        super().__init__(driver)

    def find_element_by_text(self, text, tag="*"):
        """Find element containing specific text"""
        xpath = f"//{tag}[contains(text(), '{text}')]"
        return self.find_element(By.XPATH, xpath)

    def find_elements_by_text(self, text, tag="*"):
        """Find all elements containing specific text"""
        xpath = f"//{tag}[contains(text(), '{text}')]"
        return self.find_elements(By.XPATH, xpath)

    def find_by_class(self, class_name):
        """Find element by class name"""
        return self.find_element(By.CLASS_NAME, class_name)

    def find_by_id(self, element_id):
        """Find element by ID"""
        return self.find_element(By.ID, element_id)

    def find_by_attribute(self, attribute, value):
        """Find element by any attribute"""
        xpath = f"//*[@{attribute}='{value}']"
        return self.find_element(By.XPATH, xpath)

    def get_all_links(self):
        """Get all links on the page"""
        return self.find_elements(By.TAG_NAME, "a")

    def get_all_buttons(self):
        """Get all buttons on the page"""
        buttons = self.find_elements(By.TAG_NAME, "button")
        inputs = self.find_elements(By.XPATH, "//input[@type='button' or @type='submit']")
        return buttons + inputs

    def get_all_forms(self):
        """Get all forms on the page"""
        return self.find_elements(By.TAG_NAME, "form")

    def print_page_structure(self):
        """Print useful page info for debugging"""
        print("\n" + "="*60)
        print("PAGE INSPECTION")
        print("="*60)
        print(f"URL: {self.get_url()}")
        print(f"Title: {self.get_title()}")

        links = self.get_all_links()
        print(f"\nLinks found: {len(links)}")
        for i, link in enumerate(links[:5]):  # Show first 5
            try:
                text = link.text
                href = link.get_attribute("href")
                data_purpose = link.get_attribute("data-purpose")
                print(f"  {i+1}. Text: '{text}' | href: {href} | data-purpose: {data_purpose}")
            except:
                pass

        buttons = self.get_all_buttons()
        print(f"\nButtons found: {len(buttons)}")
        for i, btn in enumerate(buttons[:5]):  # Show first 5
            try:
                text = btn.text
                btn_type = btn.get_attribute("type")
                btn_class = btn.get_attribute("class")
                print(f"  {i+1}. Text: '{text}' | type: {btn_type} | class: {btn_class}")
            except:
                pass

        forms = self.get_all_forms()
        print(f"\nForms found: {len(forms)}")
        for i, form in enumerate(forms):
            try:
                form_id = form.get_attribute("id")
                form_method = form.get_attribute("method")
                form_action = form.get_attribute("action")
                print(f"  {i+1}. ID: {form_id} | method: {form_method} | action: {form_action}")
            except:
                pass

        print("="*60 + "\n")

    def screenshot(self, filename="screenshot.png"):
        """Take a screenshot for debugging"""
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
