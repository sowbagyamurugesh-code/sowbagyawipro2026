from selenium import webdriver
import time
from lab3_opencartpage import loginpage

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

obj = loginpage(driver)
obj.click_desktop()
time.sleep(2)

obj.click_mac()
time.sleep(3)

obj.select_sort_name_az()
time.sleep(2)

obj.click_addcart()
time.sleep(3)

print("Product added to cart successfully!")

driver.quit()
