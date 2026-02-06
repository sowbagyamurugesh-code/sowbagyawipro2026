from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open iframe page
driver.get("https://the-internet.herokuapp.com/iframe")
print("Parent Page Title:", driver.title)

# 1. Switch to iframe and enter text
driver.switch_to.frame("mce_0_ifr")

text_box = driver.find_element(By.ID, "tinymce")

# Clear using CTRL+A and DELETE 
text_box.send_keys(Keys.CONTROL + "a")
text_box.send_keys(Keys.DELETE)

text_box.send_keys("Hello! This text is entered inside iframe.")
print("Text entered inside iframe")

time.sleep(3)

#  Switch back to main page
driver.switch_to.default_content()
print("Switched back to main content")
time.sleep(2)

#  Open new tab/window
driver.execute_script("window.open('https://www.google.com', '_blank');")
time.sleep(3)

#  4. Switch between windows and print titles
windows = driver.window_handles
print("\nTotal Windows Opened:", len(windows))

for win in windows:
    driver.switch_to.window(win)
    print("Window Title:", driver.title)
    time.sleep(2)

#  5. Close child window and return to parent
parent_window = windows[0]
child_window = windows[1]

driver.switch_to.window(child_window)
print("\nClosing Child Window:", driver.title)
driver.close()

driver.switch_to.window(parent_window)
print("Back to Parent Window:", driver.title)

time.sleep(3)
driver.quit()
