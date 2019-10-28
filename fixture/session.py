
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, group):
        wd = self.app.wd
        self.app.open()
        # login
        wd.find_element(By.ID, "edit-saas-login").send_keys(group.user_name)
        wd.find_element(By.ID, "edit-saas-pass").click()
        wd.find_element(By.ID, "edit-saas-pass").send_keys(group.password)
        wd.find_element(By.ID, "edit-submit").click()
        wd.find_element(By.CSS_SELECTOR, "#user_select_pos .l-btn-text").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "#mainLogoutButton .l-btn-text").click()
