class DirectionHelper:
    def __init__(self, app):
        self.app = app

    def open_form_sklad (self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, ".l-icon-top").double_click()

    def add_new_sklad(self, name_sklad, num_sklad):
        # add_new_sklad
        wd = self.app.wd
        self.open_form_sklad()
        wd.find_element(By.CSS_SELECTOR, "#tb-AddReference2001116302995449 .l-btn-icon").click()
        wd.find_element(By.ID, "2001116302995449_id-wh_elem").send_keys(num_sklad)
        wd.find_element(By.ID, "2001116302995449_name-wh_elem").click()
        wd.find_element(By.ID, "2001116302995449_name-wh_elem").send_keys(name_sklad)
        wd.find_element(By.CSS_SELECTOR, ".textbox:nth-child(4) .textbox-icon").click()
        wd.find_element(By.CSS_SELECTOR, "#datagrid-row-r15-2-1 .datagrid-cell-c15-3").click()
        wd.find_element(By.CSS_SELECTOR, "#workplace_reference-edit_ok2001116302995449 .l-btn-text").click()

    def del_first_sklad (self):
        wd = self.app.wd
        self.open_form_sklad()
        #select first sklad
        wd.find_element(By.CSS_SELECTOR, "#datagrid-row-r15-2-1 .datagrid-cell-c15-3").click()
        #submit deletion
        wd.find_element(By.CSS_SELECTOR, "##tb-DeleteReference2001116302995449 .l-btn-icon").click()
        wd.find_element(By.LINK_TEXT, "OK").click()

