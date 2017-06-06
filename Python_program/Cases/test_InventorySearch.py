import time

from Python_program.Common import UnitTest
from Python_program.Common.DataDriver import DataDriver
from Python_program.Page_Object.HomePage import HomePage
from Python_program.Page_Object.InventorySearch import InventorySearch
from Python_program.Page_Object.LoginPage import LoginPage
from Python_program.Page_Object.SearchDealerToLogin import SearchDealerPage


class test_InventorySearch(UnitTest.MyTest):
    UserName = DataDriver.UserName
    UserType = DataDriver.UserType
    RegionCode = DataDriver.RegionCode
    DealerCode = DataDriver.DealerCode
    DivisionCode = DataDriver.DivisionCode
    child_dir = 'InventorySearch'

    global isearch

    def test_open_inventory_search(self):
        isearch = InventorySearch(self.driver)
        lo = LoginPage(self.driver)
        hp = HomePage(self.driver)
        lo.login_action(self.UserName, self.RegionCode, self.DealerCode, self.DivisionCode)
        self.driver.implicitly_wait(5)
        sdtl = SearchDealerPage(self.driver)
        hp.move_to_sales()
        hp.open_vehicle_search()
        self.driver.implicitly_wait(5)
        if self.UserType == 'Internal User':
            sdtl.click_radio()
            self.driver.implicitly_wait(2)
            sdtl.search_input_dealer(self.DealerCode)
            sdtl.click_search_button()
        isearch.check_element_display(isearch.page_flag_loc, self.child_dir, 'inventorypage')
        isearch.wait_element_presence(isearch.page_flag_loc)

    def test_select_model_lines(self):
        isearch = InventorySearch(self.driver)
        isearch.select_model_lines()
        isearch.check_element_display(isearch.action_menu_loc, self.child_dir, 'modellines')
        isearch.wait_element_presence(isearch.action_menu_loc)

    def test_notes(self):
        isearch = InventorySearch(self.driver)
        if self.UserType == 'Dealer User':
            isearch.move_to_action_menu()
            isearch.click_add_notes()
            isearch.check_element_display(isearch.notes_window_close_button, self.child_dir, 'notes')
            isearch.wait_element_presence(isearch.notes_window_close_button)
            isearch.notes_window_close_button().click()
            # self.isearch.click_view_vehicle_detail()

    def test_vehicle_detail(self):
        isearch = InventorySearch(self.driver)
        now_handle = self.driver.current_window_handle
        isearch.move_to_action_menu()
        isearch.click_view_vehicle_detail()
        time.sleep(2)
        all_handles = self.driver.window_handles
        isearch.switch_current_handle(now_handle, all_handles)
        isearch.check_element_display(isearch.vehicle_detail_flag_loc, self.child_dir, 'vehicledetail')
        isearch.wait_element_presence(isearch.vehicle_detail_flag_loc)
        self.driver.close()
        self.driver.switch_to.window(now_handle)

    def test_options(self):
        isearch = InventorySearch(self.driver)
        isearch.click_color()
        time.sleep(2)
        isearch.check_element_display(isearch.action_menu_loc, self.child_dir, 'colors')
        isearch.wait_element_presence(isearch.action_menu_loc)
        isearch.click_option()
        time.sleep(2)
        isearch.check_element_display(isearch.action_menu_loc, self.child_dir, 'options')
        isearch.wait_element_presence(isearch.action_menu_loc)

    def test_print_function(self):
        isearch = InventorySearch(self.driver)
        now_handle = self.driver.current_window_handle
        isearch.print_button()
        self.driver.implicitly_wait(10)
        all_handles = self.driver.window_handles
        isearch.switch_current_handle(now_handle, all_handles)
        isearch.check_element_display(isearch.print_close_button_loc, self.child_dir, 'print')
        isearch.wait_element_presence(isearch.print_close_button_loc)
        isearch.click_print_close_button()
        self.driver.switch_to.window(now_handle)
