from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
# 1) IMPLICIT WAIT
driver.implicitly_wait(10)
print("Implicit wait applied: 10 seconds")
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# 2) EXPLICIT WAIT
# Click Enable button
enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
enable_button.click()
print("Clicked Enable button...")
# Explicit wait for textbox to become clickable
wait = WebDriverWait(driver, 10)
textbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
print("Explicit Wait: Textbox is now clickable!")
#  3) FLUENT WAIT
fluent_wait = WebDriverWait(driver, timeout=15, poll_frequency=2)
textbox_fluent = fluent_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
print("Fluent Wait: Textbox is available for interaction!")
# INTERACT WITH ELEMENT
textbox_fluent.send_keys("Hello Selenium Waits!")
print("Successfully entered text inside textbox!")
time.sleep(3)
driver.quit()
