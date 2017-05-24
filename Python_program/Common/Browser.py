from selenium import webdriver


def browser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(30)
    return driver

'''
if __name__ == '__main__':
    td=browser()
'''