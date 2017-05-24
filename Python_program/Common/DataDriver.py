from xml.dom.minidom import parse
import xml.dom.minidom

from Python_program.Common import Browser

xml_loc = 'C:\CODE\python\Python_program\data\data.xml'


class DataDriver:
    def __init__(self):
        self.UserType = ''
        self.UserName = ''
        self.DivisionCode = ''
        self.DealerCode = ''
        self.RegionCode = ''

    dom = xml.dom.minidom.parse(xml_loc)
    root = dom.documentElement

    currentUser = root.getElementsByTagName('CurrentUser')[0].firstChild.data

    envs = root.getElementsByTagName('ENV')
    env = envs[0].getAttribute('name')

    # print 'env: %s' % env

    users = root.getElementsByTagName('User')

    for user in users:
        if user.getAttribute('title') == currentUser:
            UserType = user.getElementsByTagName('UserType')[0].firstChild.data
            if UserType == 'Internal User':
                UserName = user.getElementsByTagName('UserName')[0].firstChild.data
                RegionCode = user.getElementsByTagName('RegionCode')[0].firstChild.data
                DealerCode = user.getElementsByTagName('DealerCode')[0].firstChild.data
                DivisionCode = ''
            else:
                UserName = user.getElementsByTagName('UserName')[0].firstChild.data
                RegionCode = user.getElementsByTagName('RegionCode')[0].firstChild.data
                DivisionCode = user.getElementsByTagName('DivisionCode')[0].firstChild.data
                DealerCode = user.getElementsByTagName('DealerCode')[0].firstChild.data

                # print 'UserType:' + UserType
                # print 'UserName:' + UserName
                # print 'RegionCode:' + RegionCode
                # print 'DivisionCode:' + DivisionCode
                # print 'DealerCode:' + DealerCode

# if __name__ == '__main__':
#     driver=Browser.browser()
#     snapShot(driver,'test')
