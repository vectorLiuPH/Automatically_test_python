from selenium.webdriver.common.by import By

from Python_program.Page_Object.BaseObject import BaseObject


class SearchDealerPage(BaseObject):

    input_dealer_box=(By.ID,"selectOrInputDealerForm:dealerNum")
    search_button_loc=(By.ID,"selectOrInputDealerForm:inputDealerButton")
    search_dealer_radio = (By.XPATH, "html/body/div[2]/div[6]/span/form/div[2]/table/tbody/tr[2]/td[1]/input")

    def click_radio(self):
        # self.move_to(*self.search_dealer_radio).click()
        self.find_element(*self.search_dealer_radio).click()

    def search_input_dealer(self,dealer_number):
        self.find_element(*self.input_dealer_box).clear()
        self.find_element(*self.input_dealer_box).send_keys(dealer_number)

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()


