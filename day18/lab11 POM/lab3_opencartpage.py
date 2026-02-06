from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class loginpage:

    def __init__(self, driver):
        self.driver = driver

    desktop = (By.LINK_TEXT, "Desktops")
    mac = (By.LINK_TEXT, "Mac (1)")
    sort_by = (By.ID, "input-sort")
    addcart = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    def click_desktop(self):
        self.driver.find_element(*self.desktop).click()

    def click_mac(self):
        self.driver.find_element(*self.mac).click()

    def select_sort_name_az(self):
        dropdown = self.driver.find_element(*self.sort_by)
        select = Select(dropdown)
        select.select_by_visible_text("Name (A - Z)")

    def click_addcart(self):
        self.driver.find_element(*self.addcart).click()
