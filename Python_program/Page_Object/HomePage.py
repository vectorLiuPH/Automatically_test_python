from selenium.webdriver.common.by import By

from Python_program.Page_Object.BaseObject import BaseObject


class HomePage(BaseObject):
    sales_menu_loc = (By.XPATH, 'html/body/div[2]/div[3]/form[1]/div/ul/li[2]/a')
    vehicle_search = (By.LINK_TEXT, 'Inventory Search')

    def move_to_sales(self):
        self.move_to(*self.sales_menu_loc)

    def open_vehicle_search(self):
        self.find_element(*self.vehicle_search).click()
