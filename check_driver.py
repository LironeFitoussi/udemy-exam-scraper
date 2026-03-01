from utils.driver_factory import DriverFactory

driver = DriverFactory.get_driver("chrome", headless=True)
print("[+] Chrome started! URL:", driver.current_url)
driver.quit()
print("[+] Chrome closed")
