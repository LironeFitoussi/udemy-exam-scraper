import re
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ExamPage(BasePage):
    """Page object for Udemy exam/practice test page"""

    # Pre-exam
    BEGIN_TEST_BUTTON = (By.XPATH, "//button[@data-purpose='start-quiz']")
    RETAKE_BUTTON = (By.XPATH, "//button[.//span[text()='Retake test']]")
    PRACTICE_MODE_CARD = (By.XPATH, "//div[contains(@class,'mode-card--mode-card--')]//h4[text()='Practice mode']/ancestor::div[contains(@class,'mode-card--mode-card--')]")

    # Question
    QUESTION_TEXT = (By.XPATH, "//*[@id='question-prompt']//*[@data-purpose[contains(.,'rich-text-viewer')]]")
    ANSWER_INPUTS = (By.XPATH, "//input[@name='answer']")
    ANSWER_LABELS = (By.XPATH, "//input[@name='answer']/following-sibling::*//div[@data-purpose[contains(.,'rich-text-viewer')]]")

    # Result pane - matches both "Correct answer" (single) and "Correct selection" (multi)
    RESULT_CONTAINER = (By.XPATH, "//div[@class[contains(.,'question-result--question-result')]]")
    CORRECT_ANSWER_PANES = (By.XPATH, "//div[@data-purpose='answer'][contains(@class,'answer-result-pane--answer-correct--')]//div[@data-purpose='answer-body']//*[@data-purpose[contains(.,'rich-text-viewer')]]")
    EXPLANATION = (By.XPATH, "//*[@id='overall-explanation']")

    # Navigation
    NEXT_BUTTON = (By.XPATH, "//button[@data-purpose='go-to-next-question']")
    CHECK_ANSWER_BUTTON = (By.XPATH, "//button[@data-purpose='submit-answer' or @data-purpose='check-answer']")

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def _html_to_text_with_images(html):
        """Convert innerHTML to text, preserving image URLs as ![image](url) markers."""
        if not html:
            return None
        # Replace <img> tags with markdown-style image references
        text = re.sub(
            r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>',
            r'\n![image](\1)\n',
            html,
        )
        # Replace <br> and block-level closing tags with newlines
        text = re.sub(r'<br\s*/?>',  '\n', text)
        text = re.sub(r'</(?:p|div|li|h[1-6])>', '\n', text)
        # Replace <a> tags - keep the href
        text = re.sub(
            r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
            r'\2',
            text,
        )
        # Strip all remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Collapse excessive blank lines
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def click_begin_or_retake(self):
        """Click 'Begin test' or 'Retake test' - whichever appears first"""
        try:
            WebDriverWait(self.driver, 15).until(
                EC.any_of(
                    EC.element_to_be_clickable(self.BEGIN_TEST_BUTTON),
                    EC.element_to_be_clickable(self.RETAKE_BUTTON),
                )
            )
        except Exception:
            print("[!] Neither 'Begin test' nor 'Retake test' appeared")
            return False

        if self.is_element_visible(*self.BEGIN_TEST_BUTTON, timeout=1):
            self.click(*self.BEGIN_TEST_BUTTON)
            print("[+] Clicked 'Begin test' button")
        else:
            self.click(*self.RETAKE_BUTTON)
            print("[+] Clicked 'Retake test' button")
        return True

    def click_practice_mode(self):
        """Click the Practice mode card to start practice mode"""
        self.click(*self.PRACTICE_MODE_CARD, timeout=15)
        print("[+] Clicked Practice mode card")

    def get_question_text(self):
        """Get the current question text (preserves image URLs)"""
        el = self.find_element(*self.QUESTION_TEXT, timeout=15)
        if not el:
            return None
        html = el.get_attribute("innerHTML")
        return self._html_to_text_with_images(html)

    def get_answer_options(self):
        """Return list of {index, text} for all answer options (preserves image URLs)"""
        inputs = self.find_elements(*self.ANSWER_INPUTS, timeout=10)
        labels = self.find_elements(*self.ANSWER_LABELS, timeout=10)
        options = []
        for inp, label in zip(inputs, labels):
            idx = inp.get_attribute("data-index")
            html = label.get_attribute("innerHTML")
            text = self._html_to_text_with_images(html)
            options.append({"index": int(idx), "text": text})
        return options

    def _is_multi_select(self):
        """Detect if current question uses checkboxes (multi-select) or radios (single)"""
        inputs = self.find_elements(*self.ANSWER_INPUTS, timeout=5)
        if not inputs:
            return False
        return inputs[0].get_attribute("type") == "checkbox"

    def select_random_answers(self):
        """
        Select random answers appropriate to question type.
        - Single (radio): picks 1 random option
        - Multi (checkbox): picks a random subset of 2+ options
        Returns list of selected indices.
        """
        inputs = self.find_elements(*self.ANSWER_INPUTS, timeout=10)
        if not inputs:
            return []

        is_multi = inputs[0].get_attribute("type") == "checkbox"

        if is_multi:
            # Pick a random subset - at least 2, at most len-1 to avoid trivial all/none
            k = random.randint(2, max(2, len(inputs) - 1))
            chosen = random.sample(inputs, k)
            print(f"[*] Multi-select question - picking {k} of {len(inputs)} options")
        else:
            chosen = [random.choice(inputs)]

        selected = []
        for inp in chosen:
            idx = int(inp.get_attribute("data-index"))
            label_xpath = f"//label[@for='{inp.get_attribute('id')}']"
            self.click(By.XPATH, label_xpath)
            selected.append(idx)

        print(f"[+] Selected answer indices: {selected}")
        return selected

    def submit_answer(self):
        """Click the Check Answer / submit button"""
        self.click(*self.CHECK_ANSWER_BUTTON, timeout=10)
        print("[+] Submitted answer")

    def wait_for_result(self):
        """Wait for the result pane to appear after submitting"""
        return self.is_element_visible(*self.RESULT_CONTAINER, timeout=15)

    def get_correct_answers(self):
        """
        Get all correct answer texts from the result pane.
        Returns a list (single-item for radio, multi-item for checkbox questions).
        """
        els = self.find_elements(*self.CORRECT_ANSWER_PANES, timeout=10)
        return [self._html_to_text_with_images(el.get_attribute("innerHTML"))
                for el in els if el.get_attribute("innerHTML").strip()]

    def get_explanation(self):
        """Get the overall explanation text (preserves image URLs)"""
        el = self.find_element(*self.EXPLANATION, timeout=10)
        if not el:
            return None
        html = el.get_attribute("innerHTML")
        return self._html_to_text_with_images(html)

    def scrape_current_question(self):
        """
        Scrape full question data after result is shown.
        Returns dict: question, options, question_type, correct_answers, explanation.
        """
        question = self.get_question_text()
        options = self.get_answer_options()
        is_multi = self._is_multi_select()
        correct_answers = self.get_correct_answers()
        explanation = self.get_explanation()

        return {
            "question": question,
            "question_type": "multi_select" if is_multi else "single_select",
            "options": options,
            "correct_answers": correct_answers,
            "explanation": explanation,
        }

    def click_next(self):
        """Click the Next question button"""
        self.click(*self.NEXT_BUTTON, timeout=10)
        print("[+] Clicked Next question")

    def has_next(self):
        """Check if there is a Next button available"""
        return self.is_element_visible(*self.NEXT_BUTTON, timeout=3)
