#coding=utf-8
from appium import webdriver
#from time import sleep
import time

def startapp():
        appset = {}
        appset['platformName'] = 'Android'
        appset['platformVersion'] = '5.1.1'
        appset['deviceName'] = '59d5d0f8'
        appset['appPackage'] = 'com.tencent.movieticket'
        appset['appActivity'] = '.activity.QQMovieTicketActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub',appset)
        driver.implicitly_wait(30)
        print "启动成功"
        return driver

def log(r1):
        x=time.strftime("%Y-%m-%d", time.localtime())
        x1="E:\\log\\log"+x+".txt"
        fo = open(x1,"a+")
        r2=r1.encode('utf-8')+" "
        fo.write(r2);



#获取地区信息
def cityname(dq1):

        x1 =("//*[@resource-id='com.tencent.movieticket:id/city_name']["+dq1+"]")
        return x1

#获取影片名称信息
def tvtitle(yp1):

        x1 = ("//*[@resource-id='com.tencent.movieticket:id/tv_title']["+yp1+"]")
        return x1

#获取影院名称
def tvname(yy1):
        x2 = ("//*[@resource-id='com.tencent.movieticket:id/tv_name']["+yy1+"]")
        return x2

#获取日期
def filmdata(rq1):

        x3 = ("//*[@resource-id='com.tencent.movieticket:id/film_sched_date']["+rq1+"]")
        return x3

#获取影片场次信息
def price(x,cc1):
        x4=[]
        x4[1] = x.find_element_by_xpath("//*[@resource-id='com.tencent.movieticket:id/tv_start_time']["+cc1+"]").text
        x4[2] = x.find_element_by_xpath("//*[@resource-id='com.tencent.movieticket:id/tv_end_time']["+cc1+"]").text
        x4[3] = x.find_element_by_xpath("//*[@resource-id='com.tencent.movieticket:id/tv_language']["+cc1+"]").text
        x4[4] = x.find_element_by_xpath("//*[@resource-id='com.tencent.movieticket:id/tv_room']["+cc1+"]").text
        x4[5] = x.find_element_by_xpath("//*[@resource-id='com.tencent.movieticket:id/tv_price']["+cc1+"]").text
        x4[6] = "\n"
        return x4

app=startapp()
app.implicitly_wait(30)
yp=1
while   (yp<>0):
        yyp=""
        ypp=str(yp)
        ypname=""
        ypname=app.find_element_by_xpath("(//*[@resource-id='com.tencent.movieticket:id/tv_title'])["+ypp+"]").text
        log(ypname)
        #app.swipe(711,1440,711,1027,800)
        app.find_element_by_xpath("(//*[@resource-id='com.tencent.movieticket:id/tv_title'])["+ypp+"]").click()
        app.implicitly_wait(30)
        app.find_element_by_name("立即购票").click()
        #app.implicitly_wait(30)
        yp=yp+1
        yya=0
        while   (yya<>-1):
                print yya,
                yya=yya+1
                yy=""
                yy=str(yya)
                yymame=""
                yyname=app.find_element_by_xpath("(//*[@resource-id='com.tencent.movieticket:id/tv_name'])[1]").text
                log(yyname)
                app.find_element_by_xpath("(//*[@resource-id='com.tencent.movieticket:id/tv_name'])[1]").click()
                time.sleep(1)
                app.find_element_by_xpath("(//*[@resource-id='com.tencent.movieticket:id/title_bar_back'])").click()
                #app.implicitly_wait(30)
                #app.keyevent(4)
                #app.swipe(startx=711, starty=1440, endx=711, endy=1027, duration=800)
                app.swipe(711,1440,711,1027,100)


