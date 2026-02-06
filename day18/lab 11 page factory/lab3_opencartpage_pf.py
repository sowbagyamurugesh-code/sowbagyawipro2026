from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class loginpage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def desktop(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")
    @property
    def mac(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")
    @property
    def sort_by(self):
        return self.driver.find_element(By.ID, "input-sort")
    @property
    def addcart(self):
        return self.driver.find_element(By.XPATH, "//button[contains(@onclick,'cart.add')]")



    def click_desktop(self):
        self.desktop.click()

    def click_mac(self):
        self.mac.click()

    def select_sort_name_az(self):
        dropdown = self.sort_by
        select = Select(dropdown)
        select.select_by_visible_text("Name (A - Z)")

    def click_addcart(self):
        self.addcart.click()
