from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

GRID_URL = "http://192.168.1.12:4444/wd/hub"
browsers = ["chrome", "firefox", "edge"]
for browser in browsers:
    print("\n====================================")
    print(f"Running Test on Browser: {browser.upper()}")
    # Set browser options
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    elif browser == "firefox":
        options = FirefoxOptions()

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    else:
        raise ValueError("Browser not supported")
    # Connect to Selenium Grid
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )
    driver.maximize_window()
    # Get browser + platform details
    caps = driver.capabilities
    browser_name = caps.get("browserName")
    platform_name = caps.get("platformName")

    print("Browser Name :",browser_name)
    print("Platform     :",platform_name)

    # Navigate to website
    driver.get("https://www.google.com/")
    time.sleep(2)

    # Verify title
    expected_title = "Google"
    actual_title = driver.title
    print("Page Title   :", actual_title)
    if expected_title in actual_title:
        print("Title Verified Successfully!")
    else:
        print("Title Verification Failed!")
    driver.quit()
