from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
# Launch Firefox Browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open Home Page
driver.get("https://demo.opencart.com/")
driver.maximize_window()

# Verify Title
print("Home Page Title:", driver.title)

# Click My Account Dropdown
my_account = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']")))
my_account.click()

# Select Register
register_option = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
register_option.click()

# Verify Register Account Heading
heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
print("Register Page Heading:", heading)

if heading == "Register Account":
    print("Register Account page opened successfully!")
else:
    print("Register Account page NOT opened!")

# First Name
driver.find_element(By.ID, "input-firstname").send_keys("Sowbagya")

# Last Name
driver.find_element(By.ID, "input-lastname").send_keys("M")

# Random Email (to avoid duplicate registration)
random_number = random.randint(1000, 9999)
email = f"sowbagya{random_number}@gmail.com"
driver.find_element(By.ID, "input-email").send_keys(email)
print("Email used:", email)

# Password
driver.find_element(By.ID, "input-password").send_keys("Test@123")

# Newsletter Subscribe Yes
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

# Privacy Policy Checkbox
driver.find_element(By.NAME, "agree").click()

# Click Continue button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Verify Success Message
success_heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
print("Success Page Heading:", success_heading)
if success_heading == "Your Account Has Been Created!":
    print("Account successfully created!")
else:
    print("Account creation failed!")
time.sleep(3)
driver.quit()
