from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("http://www.google.com")
title=driver.title
current_url=driver.current_url
pagesource=driver.page_source
print(title)
print(current_url)
print(pagesource)
