from selenium.webdriver.support.select import Select

from Python_program.Common.DataDriver import DataDriver
from Python_program.Page_Object.BaseObject import BaseObject


class LoginPage(BaseObject):
    UserType = DataDriver.UserType

    def login_user_name(self, username):
        self.find_element_by_id("userId").clear()
        self.find_element_by_id("userId").send_keys(username)

    def login_user_type(self, usertype):
        Select(self.find_element_by_id("userType")).select_by_visible_text(usertype)

    def login_dlr_region_code(self, regioncode):
        self.select_element_by_id("dlrRegionCode", regioncode)

    def login_int_region_code(self, regioncode):
        Select(self.find_element_by_id("intRegionCode")).select_by_visible_text(regioncode)

    def login_dealer_code(self, dealercode):
        self.find_element_by_id("dealerCode").clear()
        self.find_element_by_id("dealerCode").send_keys(dealercode)

    def login_division_code(self, divisioncode):
        Select(self.find_element_by_id("vehicleMadeCode")).select_by_visible_text(divisioncode)

    def login_button(self):
        self.find_element_by_id("loginBtn").click()

    def login_action(self, UserName, RegionCode, DealerCode, DivisionCode, ):
        if self.UserType == 'Internal User':
            self.login_user_type('Internal User')
            self.login_user_name(UserName)
            self.login_int_region_code(RegionCode)
            self.login_button()
        else:
            self.login_user_type("Dealer User")
            self.login_user_name(UserName)
            self.login_dlr_region_code(RegionCode)
            self.login_division_code(DivisionCode)
            self.login_dealer_code(DealerCode)
            self.login_button()
