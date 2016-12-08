from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import selenium
success = True
desired_caps = {}
desired_caps['browserName'] = 'iOS'
desired_caps['platform'] = 'Mac'
desired_caps['version'] = '6.1'
desired_caps['device'] = 'iPad'
desired_caps['app'] = os.path.abspath('/Users/marshall/Library/Developer/Xcode/DerivedData/TestAutomation-empzzpwyyxctxidnwdsrtlssueqi/Build/Products/Debug-iphonesimulator/TestAutomation.app')
wd = selenium.webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)


















x=startapp()

yp=0
while (yp<>-1):
        yp=yp+1
        a=str(yp)
        a1=tvtitle(a)
        #print y
        print x.find_element_by_xpath(a1).text
        log(x.find_element_by_xpath(a1).text)
        x.find_element_by_xpath("//*[@text='购票'][1]").click()
        #x.find_element_by_name("立即购票").click()
        x.implicitly_wait(30)
        yy=0
        while (yy<>0):
                yy=yy+1
                b=str(yy)
                b1=tvname(b)
                print b1
                print x.find_element_by_xpath(b1).text
                log(x.find_element_by_xpath(b1).text)
                x.find_element_by_xpath(b1).click()
                x.implicitly_wait(30)
                rq=0
                while (rq<>0):
                        rq=rq+1
                        c=str(rq)
                        c1=filmdata(c)
                        print x.find_element_by_xpath(c1).text
                        log(x.find_element_by_xpath(c1).text)
                        x.find_element_by_xpath(c1).click()
                        x.implicitly_wait(30)
                        cc=0
                        while (cc<>0):
                                cc=cc+1
                                d=str(cc)
                                d1=price(x,d)

        #x.implicitly_wait(30)



