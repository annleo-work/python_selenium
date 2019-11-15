from selenium.webdriver.common.action_chains import ActionChains

class DirectionHelper:
    def __init__(self, app):
        self.app = app

    def open_form_sklad(self):
        wd = self.app.wd
        wd.implicitly_wait(15)
        wd.find_element_by_css_selector("a#icon-_1_302995449.l-btn-big.l-btn-big-plain").click()
        element = wd.find_element_by_css_selector("a#icon-_1_302995449.l-btn-big.l-btn-big-plain")
        actions = ActionChains(wd)
        actions.double_click(element).perform()

    def add_new_sklad(self, group):
        wd = self.app.wd
        self.open_form_sklad()
        wd.find_element_by_id("tb-AddReference2001116302995449").click()
        self.fill_form(group)
        # submit save edit
        wd.find_element_by_id("workplace_reference-edit_ok2001116302995449").click()

    def fill_form(self, group):
        wd = self.app.wd
        wd.implicitly_wait(10)
        if group.num_sklad is not None:
            wd.find_element_by_id("2001116302995449_id-wh_elem").send_keys(group.num_sklad)
        if group.name_sklad is not None:
            wd.find_element_by_id("2001116302995449_name-wh_elem").click()
            wd.find_element_by_id("2001116302995449_name-wh_elem").send_keys(group.name_sklad)
        wd.find_element_by_css_selector(".textbox:nth-child(4) .textbox-icon").click()
        wd.find_element_by_css_selector("#datagrid-row-r15-2-1 .datagrid-cell-c15-3").click()

    def modify_first_sklad(self, group):
        wd = self.app.wd
        self.open_form_sklad()
        self.select_sklad()
        # change_sklad
        wd.find_element_by_id("tb-EditReference2001116302995449").click()
        self.fill_form(group)
        # submit save edit
        wd.find_element_by_id("workplace_reference-edit_ok2001116302995449").click()

    def del_first_sklad(self):
        wd = self.app.wd
        self.open_form_sklad()
        self.select_sklad()
        # submit deletion
        wd.find_element_by_id("tb-DeleteReference2001116302995449").click()
        wd.find_element_by_link_text("OK").click()

    def select_sklad(self):
        wd = self.app.wd
        wd.implicitly_wait(10)
        wd.find_element_by_css_selector("tr#datagrid-row-r12-2-2.datagrid-row").click()
