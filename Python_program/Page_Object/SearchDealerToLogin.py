from selenium.webdriver.common.by import By

from Python_program.Page_Object.BaseObject import BaseObject


class SearchDealerPage(BaseObject):

    input_dealer_box=(By.ID,"selectOrInputDealerForm:dealerNum")
    search_button_loc=(By.ID,"selectOrInputDealerForm:inputDealerButton")
    search_dealer_radio=(By.ID,"selectOrInputDealerForm:j_id270:1")

    def click_radio(self):
        self.find_element(*self.search_dealer_radio).click()

    def search_input_dealer(self,dealer_number):
        self.find_element(*self.input_dealer_box).clear()
        self.find_element(*self.input_dealer_box).send_keys(dealer_number)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()


