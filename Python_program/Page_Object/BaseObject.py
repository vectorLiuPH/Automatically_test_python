import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject():
    def __init__(self, driver):
        self.driver = driver

    # def open(self):
    #     self.__init__()


    def find_element_by_id(self, *loc):
        return self.driver.find_element_by_id(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def select_element_by_id(self, id, item):
        return Select(self.find_element_by_id(id)).select_by_visible_text(item)

    def select_element_by_id(self, id, text):
        return Select(self.find_element_by_id(id)).select_by_visible_text(text)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def set_move_to(self, *loc):
        chain = ActionChains(self.driver)
        implement = self.find_element(*loc)
        chain.move_to_element(implement).perform()
        time.sleep(2)

    def move_to(self, *loc):
        return self.set_move_to(*loc)

    def select_random_option(self, *loc):
        select = self.find_element(*loc)
        options_list = select.find_elements_by_tag_name('option')
        for option in options_list:
            if option.get_attribute('disable') == None and option.get_attribute('selected') == None:
                option_value = option.get_attribute('value')
                Select(select).select_by_value(option_value)
                break

    def table_random_tr(self, *loc):
        tr1=0
        table = self.find_element(*loc)
        tr_list = table.find_elements_by_tag_name('tr')
        label_disalbe_list=table.find_elements_by_class_name('disablecheckbox')
        for tr in tr_list:
            label=tr.find_element_by_tag_name('label')
            if label not in label_disalbe_list:
                tr1 = tr
                break
            # td = tr.find_element_by_tag_name('td')
            # label = td.find_element_by_tag_name('label')
            # if label.value_of_css_property(label) != 'disablecheckbox':

        return tr1

    def switch_current_handle(self, now_handle, all_handles):
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to.window(handle)

    def wait_element_presence(self, loc):
        WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.presence_of_element_located(loc))

    def snap_successful_shot(self, child_dir, pic_name):
        base_dir = 'C:\CODE\python\Python_program\TestResult\successfully\\'
        path = base_dir + child_dir + '\\' + pic_name + '.png'
        self.driver.get_screenshot_as_file(path)

    def snap_fail_shot(self, child_dir, pic_name):
        base_dir = 'C:\CODE\python\Python_program\TestResult\\fail\\'
        path = base_dir + child_dir + '\\' + pic_name + '.png'
        self.driver.get_screenshot_as_file(path)

    def check_element_display(self, flag_loc, child_dir, pic_name):
        try:
            WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.presence_of_element_located(flag_loc))
        except:
            self.snap_fail_shot(child_dir, pic_name)
        else:
            self.snap_successful_shot(child_dir, pic_name)
