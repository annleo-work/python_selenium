# -*- Coding: -UTF-8 -*-
from selenium import webdriver
import unittest


class test(unittest.TestCase):
    def setup(self):
        self.wd = webdriver.Firefox('c:\\geckodriver')

    def open_main_page(self, wd):
        wd.get("https://ioblik.com/")

    def login(self, wd, user_name, password):
        wd.find_element(by.ID, "edit-saas-login").click()
        wd.find_element(By.ID, "edit-saas-login").send_keys(user_name)
        wd.find_element(By.ID, "edit-saas-pass").click()
        wd.find_element(By.ID, "edit-saas-pass").send_keys(password)
        wd.find_element(By.ID, "edit-submit").click()

    def logout(self, wd):
        wd.find_element(By.CSS_SELECTOR, "#mainLogoutButton .l-btn-text").click()

    def test_login(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, user_name="user101", password="123456")
        self.logout(wd)

    def teardown_method(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
