
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        wd = self.app.wd
        self.app.open()
        # login
        wd.find_element_by_id("edit-saas-login").send_keys(user_name)
        wd.find_element_by_id("edit-saas-pass").click()
        wd.find_element_by_id("edit-saas-pass").send_keys(password)
        wd.find_element_by_id("edit-submit").click()
        wd.find_element_by_id("user_select_pos").click()

    def logout(self):
        wd = self.app.wd
        wd.implicitly_wait(10)
        wd.find_element_by_id("mainLogoutButton").click()
