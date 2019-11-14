
class DirectionHelper:
    def __init__(self, app):
        self.app = app

    def open_form_sklad (self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, ".l-icon-top").double_click()

    def add_new_sklad(self,group):
        wd = self.app.wd
        self.open_form_sklad()
        self.fill_form(group)
        #submit save edit
        wd.find_element(By.ID, "workplace_reference-edit_ok2001116302995449").click()

    def fill_form(self, group):
        wd = self.app.wd
        if group.num_sklad is not "None":
            wd.find_element(By.ID, "tb-AddReference2001116302995449").click()
            wd.find_element(By.ID, "2001116302995449_id-wh_elem").send_keys(group.num_sklad)
        if group.name_sklad is not "None":
            wd.find_element(By.ID, "2001116302995449_name-wh_elem").click()
            wd.find_element(By.ID, "2001116302995449_name-wh_elem").send_keys(group.name_sklad)
        wd.find_element(By.CSS_SELECTOR, ".textbox:nth-child(4) .textbox-icon").click()
        wd.find_element(By.CSS_SELECTOR, "#datagrid-row-r15-2-1 .datagrid-cell-c15-3").click()

    def modify_first_sklad(self,group):
        wd = self.app.wd
        self.open_form_sklad()
        self.select_sklad()
        #change_sklad
        self.fill_form(group)
        #submit save edit
        wd.find_element(By.ID, "workplace_reference-edit_ok2001116302995449").click()

    def del_first_sklad (self):
        wd = self.app.wd
        self.open_form_sklad()
        self.select_sklad()
        #submit deletion
        wd.find_element(By.ID, "tb-DeleteReference2001116302995449").click()
        wd.find_element(By.LINK_TEXT, "OK").click()

    def select_sklad(self):
        wd = self.app.wd
        wd.find_element(By.css_Selector("tr# datagrid-row-r15-2-1").click()