from utils.driver_factory import DriverFactory
from pages.udemy_page import UdemyPage
from pages.login_page import LoginPage
from pages.exam_page import ExamPage
from dotenv import load_dotenv
import json
import os
import sys


def main():
    load_dotenv()
    email = os.getenv("UDEMY_EMAIL")
    password = os.getenv("UDEMY_PASSWORD")

    if not email or not password:
        print("[x] Missing credentials in .env file")
        sys.exit(1)

    driver = None
    try:
        print("[*] Launching Chrome...")
        driver = DriverFactory.get_driver("chrome", headless=False)

        udemy_page = UdemyPage(driver)

        # Resolve exam URL - use .env default or prompt if not set
        default_url = os.getenv("UDEMY_EXAM_URL", "")
        if default_url:
            exam_url = default_url
            print(f"\n[*] Using exam URL from .env")
        else:
            print("\n" + "=" * 60)
            exam_url = input("Paste the Udemy exam URL to scrape: ").strip()
            if not exam_url:
                print("[x] No URL provided")
                sys.exit(1)

        # Navigate directly to exam URL - if session is active (persistent profile)
        # the page loads straight in; otherwise we detect the login wall and auth
        print(f"[*] Navigating to: {exam_url}")
        driver.get(exam_url)
        udemy_page.wait_for_url_change("about:blank", timeout=15)

        if udemy_page.is_logged_in(timeout=5):
            print("[+] Session active - already logged in")
        else:
            print("[*] Not logged in - starting Google login...")
            udemy_page.navigate_to_home()
            udemy_page.click_sign_in()

            login_page = LoginPage(driver)
            if login_page.is_google_button_visible():
                login_page.login_with_google(email, password)

                if udemy_page.is_logged_in(timeout=30):
                    print("[+] Login successful!")
                else:
                    print("[!] Login may have failed - check browser")
                    sys.exit(1)
            else:
                print("[x] Google login button not found")
                sys.exit(1)

            # Return to the exam URL after login
            print(f"[*] Returning to exam URL...")
            driver.get(exam_url)
            udemy_page.wait_for_url_change("about:blank", timeout=15)

        print(f"[+] Opened: {udemy_page.get_current_url()}")
        print(f"    Title: {udemy_page.get_page_title()}")

        exam_page = ExamPage(driver)
        exam_page.click_begin_or_retake()
        exam_page.click_practice_mode()

        # Scraping loop
        scraped = []
        question_num = 0
        output_path = "data/exam_results.json"
        os.makedirs("data", exist_ok=True)

        while True:
            question_num += 1
            print(f"\n[*] Question {question_num} - waiting for question to load...")

            question_text = exam_page.get_question_text()
            if not question_text:
                print("[!] Could not read question text - stopping")
                break

            options = exam_page.get_answer_options()
            print(f"[+] Got {len(options)} answer options")

            exam_page.select_random_answers()
            exam_page.submit_answer()

            if not exam_page.wait_for_result():
                print("[!] Result pane did not appear - stopping")
                break

            data = exam_page.scrape_current_question()
            scraped.append(data)

            # Live update JSON after every question
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(scraped, f, indent=2, ensure_ascii=False)

            correct_preview = " | ".join(data["correct_answers"])[:80]
            print(f"[+] Scraped Q{question_num} ({data['question_type']}): {question_text[:60]}...")
            print(f"    Correct: {correct_preview}...")
            print(f"    [saved {output_path}]")

            if exam_page.has_next():
                exam_page.click_next()
            else:
                print("\n[+] No more questions - exam complete")
                break

        print(f"\n[+] Scraping complete: {len(scraped)} questions collected -> {output_path}")

        input("\nPress Enter to close...")

    except Exception as e:
        print(f"\n[x] An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    finally:
        DriverFactory.quit_driver(driver)


if __name__ == "__main__":
    main() 