import pytest
from driverfactory import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_title(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_serach(browser):
    driver = get_driver(browser)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.google.com/")

    searchbox = wait.until(EC.presence_of_element_located(("name", "q")))
    searchbox.send_keys("Selenium Grid")
    searchbox.submit()

    # wait until title contains Selenium Grid
    wait.until(EC.title_contains("Selenium Grid"))

    assert "Selenium Grid" in driver.title
    driver.quit()
