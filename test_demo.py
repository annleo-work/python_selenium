# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestDemo():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demo(self):
    # Test name: demo
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("https://ioblik.com/")
    # 2 | setWindowSize | 1382x744 |  | 
    self.driver.set_window_size(1382, 744)
    # 3 | click | linkText=Начать работу |  | 
    self.driver.find_element(By.LINK_TEXT, "Начать работу").click()
    # 4 | click | linkText=Главная |  | 
    self.driver.find_element(By.LINK_TEXT, "Главная").click()
    # 5 | click | linkText=Преимущества |  | 
    self.driver.find_element(By.LINK_TEXT, "Преимущества").click()
    # 6 | click | linkText=Интеграция |  | 
    self.driver.find_element(By.LINK_TEXT, "Интеграция").click()
    # 7 | click | linkText=Видео |  | 
    self.driver.find_element(By.LINK_TEXT, "Видео").click()
    # 8 | click | linkText=Справка |  | 
    self.driver.find_element(By.LINK_TEXT, "Справка").click()
    # 9 | click | linkText=Тарифы |  | 
    self.driver.find_element(By.LINK_TEXT, "Тарифы").click()
    # 10 | click | linkText=Контакты |  | 
    self.driver.find_element(By.LINK_TEXT, "Контакты").click()
    # 11 | click | id=demoLoginImg |  | 
    self.driver.find_element(By.ID, "demoLoginImg").click()
    # 12 | click | css=div > .combo .textbox-icon |  | 
    self.driver.find_element(By.CSS_SELECTOR, "div > .combo .textbox-icon").click()
    # 13 | click | css=div > .combo .textbox-icon |  | 
    self.driver.find_element(By.CSS_SELECTOR, "div > .combo .textbox-icon").click()
    # 14 | click | css=#user_select_pos .l-btn-text |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#user_select_pos .l-btn-text").click()
    # 15 | mouseOver | css=.workplace |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".workplace")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 16 | mouseOut | css=.workplace |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 17 | mouseOver | id=desktopdesktop_desktopdesktopdesktop |  | 
    element = self.driver.find_element(By.ID, "desktopdesktop_desktopdesktopdesktop")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 18 | mouseOut | id=desktopdesktop_desktopdesktopdesktop |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 19 | mouseOver | id=workplace-tabicon-7 |  | 
    element = self.driver.find_element(By.ID, "workplace-tabicon-7")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 20 | mouseOut | id=workplace-tabicon-7 |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 21 | click | css=#icon-_7_379325050 > .l-icon-top |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#icon-_7_379325050 > .l-icon-top").click()
    # 22 | doubleClick | css=#icon-_7_379325050 > .l-icon-top |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#icon-_7_379325050 > .l-icon-top")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    # 23 | click | css=#mainLogoutButton .l-btn-text |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#mainLogoutButton .l-btn-text").click()
  