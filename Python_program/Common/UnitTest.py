import unittest

from Python_program.Common.Browser import browser
from Python_program.Common.DataDriver import DataDriver


class MyTest(unittest.TestCase):
    # def setUp(self):
    #     self.driver=browser()
    #
    # def tearDown(self):
    #     self.driver.quit()


    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        env = DataDriver.env
        cls.base_url = 'https://dbsapp.' + env + '.nnanet.com/login.html'
        cls.driver.get(cls.base_url)
        cls.driver.implicitly_wait(2)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
