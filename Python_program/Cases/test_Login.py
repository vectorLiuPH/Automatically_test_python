from Python_program.Common import UnitTest
from Python_program.Common.DataDriver import DataDriver
from Python_program.Page_Object.LoginPage import LoginPage


class login_test(UnitTest.MyTest):

    UserName=DataDriver.UserName
    UserType=DataDriver.UserType
    RegionCode=DataDriver.RegionCode
    DealerCode=DataDriver.DealerCode
    DivisionCode=DataDriver.DivisionCode


    def test_login_successful(self):
        lo=LoginPage(self.driver)
        # lo.open()
        lo.login_action(self.UserName,self.RegionCode,self.DealerCode,self.DivisionCode)
