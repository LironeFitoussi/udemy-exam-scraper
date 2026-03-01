#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fix WebDriver issues by clearing cache and reinstalling drivers
"""
import subprocess
import sys
import os
from pathlib import Path


def clear_cache():
    """Clear webdriver-manager cache"""
    print("[*] Clearing webdriver-manager cache...")
    cache_dir = Path.home() / ".wdm"
    if cache_dir.exists():
        import shutil
        shutil.rmtree(cache_dir)
        print(f"[+] Cleared cache: {cache_dir}")
    else:
        print(f"[i] Cache directory not found: {cache_dir}")


def reinstall_webdriver_manager():
    """Reinstall webdriver-manager"""
    print("\n[*] Reinstalling webdriver-manager...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "webdriver-manager"]
    )
    print("[+] Reinstalled webdriver-manager")


def test_driver(browser="firefox"):
    """Test driver initialization"""
    print(f"\n[*] Testing {browser} driver...", end=" ")
    try:
        from utils.driver_factory import DriverFactory
        driver = DriverFactory.get_driver(browser, headless=True)
        print(f"[+] Success")
        print(f"    Current URL: {driver.current_url}")
        driver.quit()
        print(f"    Driver closed successfully")
        return True
    except Exception as e:
        print(f"[x] Failed")
        print(f"    Error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("WebDriver Troubleshooting Tool")
    print("=" * 60)

    # Step 1: Clear cache
    clear_cache()

    # Step 2: Reinstall
    try:
        reinstall_webdriver_manager()
    except Exception as e:
        print(f"[x] Reinstall failed: {e}")
        sys.exit(1)

    # Step 3: Test browsers
    browsers = ["firefox", "edge", "chrome"]
    success = False

    for browser in browsers:
        if test_driver(browser):
            success = True
            print(f"\n[+] {browser} works! Using it in main.py")
            break

    if not success:
        print("\n[x] All browsers failed. Try:")
        print("    1. Ensure you have Chrome, Firefox, or Edge installed")
        print("    2. Check your internet connection")
        print("    3. Run again: python fix_drivers.py")
        sys.exit(1)
    else:
        print("\n[+] Driver fix successful!")
        print("    Run: python main.py")
