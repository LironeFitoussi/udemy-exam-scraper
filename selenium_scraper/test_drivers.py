#!/usr/bin/env python
"""Quick driver test"""
import sys

print("Testing browser drivers...")
print("-" * 50)

browsers = ["firefox", "edge", "chrome"]

for browser in browsers:
    try:
        print(f"\n🧪 Testing {browser}...", end=" ")
        from utils.driver_factory import DriverFactory
        driver = DriverFactory.get_driver(browser, headless=True)
        print(f"✓ SUCCESS")
        driver.quit()
        print(f"   Use this browser: python main.py")
        sys.exit(0)
    except Exception as e:
        print(f"✗ Failed")
        continue

print("\n❌ All browsers failed")
print("\nTry running: python fix_drivers.py")
sys.exit(1)
