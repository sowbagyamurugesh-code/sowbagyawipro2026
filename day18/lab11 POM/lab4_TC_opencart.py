from selenium import webdriver
import time
from lab4_opencartpage import loginpage

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

obj = loginpage(driver)

# Step 3: Click Desktops
obj.click_desktop()
time.sleep(2)

# Step 4: Click Mac
obj.click_mac()
time.sleep(3)

# Step 5: Verify Mac Heading
heading = obj.verify_mac_heading()
print("Heading is:", heading)

if heading == "Mac":
    print("Mac Heading Verified Successfully!")
else:
    print("Mac Heading Verification Failed!")

# Step 6: Select Name (A-Z)
obj.select_sort_name_az()
time.sleep(2)

# Step 7: Add to Cart
obj.click_addcart()
time.sleep(3)

print("Mac product added to cart successfully!")

# Step 8: Enter Mobile in Search box
obj.enter_search_text("Mobile")
obj.click_search_button()
time.sleep(3)

# Step 9: Clear Search Criteria textbox
# obj.clear_search_criteria()
# time.sleep(2)

# Step 9: Click Search in product descriptions checkbox
obj.click_description_checkbox()
time.sleep(2)

# Step 10: Click Search button again
obj.click_search_criteria_button()
time.sleep(3)
# Step 11:Clear Search Criteria textbox
obj.clear_search_criteria()
time.sleep(2)

# Step 12: Enter Monitors in Search box
obj.enter_search_text("Monitors")
obj.click_search_button()
time.sleep(3)
print("Search completed successfully!")

driver.quit()
