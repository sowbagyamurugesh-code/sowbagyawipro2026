from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class loginpage:

    def __init__(self, driver):
        self.driver = driver

    # Desktops and Mac
    desktop = (By.LINK_TEXT, "Desktops")
    mac = (By.LINK_TEXT, "Mac (1)")
    mac_heading = (By.XPATH, "//h2[text()='Mac']")

    # Sort and Add to cart
    sort_by = (By.ID, "input-sort")
    addcart = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    # Search
    search_box = (By.NAME, "search")
    search_btn = (By.XPATH, "//button[@type='button' and contains(@class,'btn-default')]")

    # Search Criteria Page
    search_criteria_box = (By.ID, "input-search")
    description_checkbox = (By.ID, "description")
    criteria_search_btn = (By.ID, "button-search")

    # ------------------- METHODS -------------------

    def click_desktop(self):
        self.driver.find_element(*self.desktop).click()

    def click_mac(self):
        self.driver.find_element(*self.mac).click()

    def verify_mac_heading(self):
        heading = self.driver.find_element(*self.mac_heading).text
        return heading

    def select_sort_name_az(self):
        dropdown = self.driver.find_element(*self.sort_by)
        select = Select(dropdown)
        select.select_by_visible_text("Name (A - Z)")

    def click_addcart(self):
        self.driver.find_element(*self.addcart).click()

    # Search Monitors
    def enter_search_text(self, text):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(text)

    def click_search_button(self):
        self.driver.find_element(*self.search_btn).click()

    def clear_search_criteria(self):
        self.driver.find_element(*self.search_criteria_box).clear()

    def click_description_checkbox(self):
        self.driver.find_element(*self.description_checkbox).click()

    def click_search_criteria_button(self):
        self.driver.find_element(*self.criteria_search_btn).click()
