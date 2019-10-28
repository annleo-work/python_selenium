from selenium.webdriver.firefox.webdriver import WebDriver
class Application:

    def __init__(self):
        self.driver = WebDriver
        self.vars = {}

    def logout(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, "#mainLogoutButton .l-btn-text").click()

    def login(self, group):
        driver = self.driver
        self.open()
        # login
        driver.find_element(By.ID, "edit-saas-login").send_keys(group.user_name)
        driver.find_element(By.ID, "edit-saas-pass").click()
        driver.find_element(By.ID, "edit-saas-pass").send_keys(group.password)
        driver.find_element(By.ID, "edit-submit").click()
        driver.find_element(By.CSS_SELECTOR, "#user_select_pos .l-btn-text").click()

    def open(self):
        driver = self.driver
        driver.get("https://ioblik.com/")

    def destroy(self):
        self.driver.quit()