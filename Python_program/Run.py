import unittest

from Python_program.Cases.test_InventorySearch import test_InventorySearch
from Python_program.Common.DataDriver import DataDriver

if __name__ == "__main__":
    # test_dir='.\Cases'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    suite = unittest.TestSuite()
    # suite.addTest(login_test('test_login_successful'))
    suite.addTest(test_InventorySearch('test_open_inventory_search'))
    suite.addTest(test_InventorySearch('test_select_model_lines'))
    if DataDriver.UserType=='Dealer User':
        suite.addTest(test_InventorySearch('test_notes'))
    # suite.addTest(test_InventorySearch('test_vehicle_detail'))
    suite.addTest(test_InventorySearch('test_options'))
    # suite.addTest(test_InventorySearch('test_print_function'))



    # filename = 'C:\CODE\python\Python_program\TestResult\Test\\result.html'
    # fp = file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='BAT report', description='BAT report')
    runner = unittest.TextTestRunner()
    runner.run(suite)
