import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestQ1day16():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_q1day16(self):
    self.driver.get("https://tutorialsninja.com/demo/")
    self.driver.set_window_size(789, 816)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-user").click()
    self.driver.find_element(By.LINK_TEXT, "Register").click()

    self.driver.find_element(By.ID, "input-firstname").click()
    self.driver.find_element(By.ID, "input-firstname").send_keys("sow")
    self.driver.find_element(By.ID, "input-lastname").click()
    self.driver.find_element(By.ID, "input-lastname").send_keys("m")
    self.driver.find_element(By.ID, "input-email").click()
    self.driver.find_element(By.ID, "input-email").send_keys("bagya@gmail.com")
    self.driver.find_element(By.ID, "input-telephone").click()
    self.driver.find_element(By.ID, "input-telephone").send_keys("7894563212")
    self.driver.find_element(By.ID, "input-password").click()
    self.driver.find_element(By.ID, "input-password").send_keys("abc")
    self.driver.find_element(By.ID, "input-confirm").click()
    self.driver.find_element(By.ID, "input-confirm").send_keys("abc")
    self.driver.find_element(By.NAME, "agree").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "#content > h1")
    assert len(elements) > 0

    #validation
    success_text = self.driver.find_element(By.CSS_SELECTOR, "#content h1").text
    assert success_text == "Register Account"
    print(success_text)
  
