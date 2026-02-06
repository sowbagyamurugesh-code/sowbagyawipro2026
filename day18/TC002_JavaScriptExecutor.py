from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

driver.maximize_window()
time.sleep(3)
#driver.execute_script("alert('Hello Amazon')")
driver.execute_script("window.scrollTo(0,900)")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

driver.quit()
