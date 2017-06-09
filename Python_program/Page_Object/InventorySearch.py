from selenium.webdriver.common.by import By

from Python_program.Page_Object.BaseObject import BaseObject


class InventorySearch(BaseObject):
    model_lines_loc = (By.ID, "f1:modelLines")
    add_notes_loc = (By.LINK_TEXT, "Add Notes")
    edit_notes_loc = (By.LINK_TEXT, 'Edit Notes')
    close_note_window_loc = (By.XPATH, "//*[@id='ancn_title']/a")
    action_menu_loc = (By.XPATH,
                       'html/body/div[2]/div[6]/form/div[2]/div[1]/div[4]/span/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/div')
    vehicle_detail = (By.LINK_TEXT, "View Vehicle Detail")
    colors_table = 'f1:colorCheckBoxList'
    options_table_xpath = "//*[@id='f1:divoptions']/table"
    colors_option_loc = (By.ID, colors_table)
    options_table_loc = (By.XPATH, options_table_xpath)
    print_button_loc = (By.XPATH, "html/body/div[2]/div[5]/div[2]/span/form/div/a")
    print_close_button_loc = (By.ID, "close_button_top")
    page_flag_loc = (By.CLASS_NAME, "inventorySearchDiv")
    vehicle_detail_flag_loc = (By.XPATH, "//*[@id='f2']/table[1]")

    def click_color(self):
        tr1 = self.table_random_tr(*self.colors_option_loc)
        td = tr1.find_element_by_tag_name('td')
        input = td.find_element_by_tag_name('input')
        input.click()
        # colors_option_loc = (By.ID, (self.colors_table + ':'+tr))
        # self.find_element(colors_option_loc).click()

    def click_option(self):
        tr1 = self.table_random_tr(*self.options_table_loc)
        td = tr1.find_element_by_tag_name('td')
        img = td.find_element_by_tag_name('img')
        img.click()
        # options_option_loc = (By.XPATH, self.options_table_xpath + '/tbody/' + 'tr[' + tr + ']' + '/td/img')
        # self.find_element(options_option_loc).click()

    def action_menu(self):
        self.find_element(*self.action_menu_loc)

    def click_print_close_button(self):
        self.find_element(*self.print_close_button_loc).click()

    def select_model_lines(self):
        self.select_random_option(*self.model_lines_loc)

    def click_add_notes(self):
        self.find_element(*self.add_notes_loc).click()

    def notes_window_close_button(self):
        self.find_element(*self.close_note_window_loc)

    def click_edit_notes(self):
        self.find_element(*self.edit_notes_loc).click()

    def click_view_vehicle_detail(self):
        self.find_element(*self.vehicle_detail).click()

    def move_to_action_menu(self):
        self.move_to(*self.action_menu_loc)

    def print_button(self):
        self.find_element(*self.print_button_loc).click()
