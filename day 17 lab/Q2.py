from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the alert demo page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

# 1. Trigger JS Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(2)

# 2. Accept alert and print message
alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()
time.sleep(2)

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result after accepting alert:", result)

#3. Dismiss Confirmation Pop-up
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(2)

confirm_alert = driver.switch_to.alert
print("Confirm Alert Message:", confirm_alert.text)
confirm_alert.dismiss()
time.sleep(2)

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result after dismissing confirm:", result)

#  4. Enter text in Prompt Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(2)

prompt_alert = driver.switch_to.alert
print("Prompt Alert Message:", prompt_alert.text)

# Enter text and accept
prompt_alert.send_keys("Sowbagya")
prompt_alert.accept()
time.sleep(2)

# 5. Verify result displayed
result = driver.find_element(By.ID, "result").text
print("Final Result after prompt:", result)

# Verification
if "Sowbagya" in result:
    print("Test Passed: Prompt text verified successfully!")
else:
    print("Test Failed: Prompt text not found!")

# Close browser
driver.quit()
