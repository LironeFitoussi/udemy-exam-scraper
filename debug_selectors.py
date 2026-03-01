#!/usr/bin/env python
"""
Debug script to find and test selectors on any page
Use this to discover the correct locators for elements
"""

from utils.driver_factory import DriverFactory
from pages.inspect_page import InspectPage
import time


def main():
    print("=" * 60)
    print("Udemy Selector Debugger")
    print("=" * 60)

    # Get browser
    browser = input("\nSelect browser (default: firefox): ").strip().lower() or "firefox"
    url = input("Enter URL to inspect (default: https://www.udemy.com): ").strip() or "https://www.udemy.com"

    driver = None
    try:
        print(f"\nLaunching {browser}...")
        driver = DriverFactory.get_driver(browser, headless=False)

        print(f"Navigating to {url}...")
        driver.get(url)
        time.sleep(3)

        inspect = InspectPage(driver)

        while True:
            print("\n" + "=" * 60)
            print("INSPECTOR MENU")
            print("=" * 60)
            print("1. Show page structure (links, buttons, forms)")
            print("2. Find element by text")
            print("3. Find element by ID")
            print("4. Find element by class")
            print("5. Find element by attribute")
            print("6. Take screenshot")
            print("7. Print current URL")
            print("8. Refresh page")
            print("9. Navigate to new URL")
            print("0. Exit")

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                inspect.print_page_structure()

            elif choice == "2":
                text = input("Enter text to find: ").strip()
                try:
                    element = inspect.find_element_by_text(text)
                    if element:
                        print(f"[+] Found element!")
                        print(f"    Tag: {element.tag_name}")
                        print(f"    Text: {element.text}")
                        print(f"    HTML: {element.get_attribute('outerHTML')[:100]}...")
                except Exception as e:
                    print(f"[x] Not found: {e}")

            elif choice == "3":
                elem_id = input("Enter ID to find: ").strip()
                try:
                    element = inspect.find_by_id(elem_id)
                    if element:
                        print(f"[+] Found element with ID '{elem_id}'")
                        print(f"    Tag: {element.tag_name}")
                        print(f"    Class: {element.get_attribute('class')}")
                except Exception as e:
                    print(f"[x] Not found: {e}")

            elif choice == "4":
                class_name = input("Enter class name: ").strip()
                try:
                    element = inspect.find_by_class(class_name)
                    if element:
                        print(f"[+] Found element with class '{class_name}'")
                        print(f"    Tag: {element.tag_name}")
                        print(f"    Text: {element.text[:50]}")
                except Exception as e:
                    print(f"[x] Not found: {e}")

            elif choice == "5":
                attr = input("Enter attribute name (e.g., data-purpose): ").strip()
                value = input("Enter attribute value: ").strip()
                try:
                    element = inspect.find_by_attribute(attr, value)
                    if element:
                        print(f"[+] Found element!")
                        print(f"    Tag: {element.tag_name}")
                        print(f"    {attr}: {value}")
                        print(f"    Text: {element.text}")
                        print(f"    HTML: {element.get_attribute('outerHTML')[:150]}...")
                except Exception as e:
                    print(f"[x] Not found: {e}")

            elif choice == "6":
                filename = input("Enter filename (default: debug.png): ").strip() or "debug.png"
                inspect.screenshot(filename)

            elif choice == "7":
                print(f"Current URL: {inspect.get_url()}")

            elif choice == "8":
                driver.refresh()
                print("Page refreshed")
                time.sleep(2)

            elif choice == "9":
                new_url = input("Enter new URL: ").strip()
                driver.get(new_url)
                print(f"Navigated to {new_url}")
                time.sleep(2)

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

    except Exception as e:
        print(f"[x] Error: {e}")
        import traceback
        traceback.print_exc()

    finally:
        print("\nClosing browser...")
        DriverFactory.quit_driver(driver)
        print("Done!")


if __name__ == "__main__":
    main()
