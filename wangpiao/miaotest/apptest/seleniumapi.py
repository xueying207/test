#coding=utf-8
from selenium import webdriver

#引入Keys类包

driver = webdriver.Firefox()   #调用火狐浏览器
driver=webdriver.Chrome()  #调用chrome浏览器
driver=webdriver.Ie()   #调用ie浏览器
driver=webdriver.Safari() #调用Safari浏览器
dirver= webdriver.get('c:\\program files\\internet explorer\\iexplore8.exe') #按路径打开浏览器
driver.get("http://www.baidu.com")  #输入网址
driver.maximize_window() #将浏览器最大化显示
driver.set_window_size(480, 800)  #设置浏览器大小
driver.back()  #后退网页
driver.forward() #网页前进
driver.title #获取网页title
driver.quit() #退出所有窗口
driver.close() #退出当前窗口

driver.find_element_by_id("id")  #ID定位
driver.find_element_by_name("name") #name定位
driver.find_element_by_class_name("class") #class定位
driver.find_element_by_tag_name("tag_name") #标签定位
driver.find_element_by_link_text("text") #文本定位
driver.find_element_by_partial_link_text("部分文本") #部分文本定位
driver.find_element_by_xpath("xpath") #xpath定位
driver.find_element_by_xpath("//input[@id=’input’]") #通过自身的 id 属性定位
driver.find_element_by_xpath("//span[@id=’input-container’]/input") #通过上一级目录的id属性定位
driver.find_element_by_xpath("//div[@id=’hd’]/form/span/input") #通过上三级目录的 id 属性定位
driver.find_element_by_xpath("//div[@name=’q’]/form/span/input")#通过上三级目录的 name 属性定位
driver.find_element_by_css_selector("css")  #css定位
div=driver.find_element_by_class_name("tang-content").find_element_by_name("userName")  #层级定位

driver.find_element_by_id("user_name").clear()    #清除元素内容
driver.find_element_by_id("user_name").send_keys("username")  #输入元素内容
driver.find_element_by_id("dl_an_submit").click()  #点击元素
driver.find_element_by_id("dl_an_submit").submit() #提交表单

size=driver.find_element_by_id("kw").size  #获取元素的尺寸
text=driver.find_element_by_id("cp").text  #获取元素文本信息
attribute=driver.find_element_by_id("kw").get_attribute('type')  #获取元素的其它属性
result=driver.find_element_by_id("kw").is_displayed()   #获取元素是否可见

from selenium.webdriver.common.action_chains import ActionChains
#ActionChains  类方法
#context_click() 右击
#double_click() 双击
#drag_and_drop() 拖动
#move_to_element() 鼠标悬停在一个元素上
#click_and_hold() 按下鼠标左键在一个元素上
double =driver.find_element_by_xpath("xxx") #对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(double).perform()

element = driver.find_element_by_name("xxx") #定位元素的原位置
target = driver.find_element_by_name("xxx")  #定位元素要移动到的目标位置
ActionChains(driver).drag_and_drop(element, target).perform() #执行元素的移动操作


from selenium.webdriver.common.keys import Keys
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

import time
time.sleep(5) #设置固定休眠时间
driver.implicitly_wait(30)  #设置时间范围内等待
from selenium.webdriver.support.ui import WebDriverWait
element=WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw")) #设置元素等待

#获取一组元素
inputs = driver.find_elements_by_tag_name('input') #然后从中过滤出tpye为checkbox的元素，单击勾选
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

#切换窗口
nowhandle=driver.current_window_handle #获得当前窗口
allhandles=driver.window_handles    #获取所有窗口
driver.switch_to_window(nowhandle) #切换窗口

#对话框处理
alert = driver.switch_to_alert()  #接受警告信息
alert.accept()
alert = driver.switch_to_alert()
print alert.text() #得到文本信息并打印
alert = driver.switch_to_alert()
alert.dismiss() #取消对话框（如果有的话）
alert = driver.switch_to_alert()
alert.send_keys("xxx") #输入值（如果有的话）

#定位下拉框
m=driver.find_element_by_id("ShippingMethod") #先定位到下拉框
m.find_element_by_xpath("//option[@value='10.69']").click() #再点击下拉框下的选项

#上传文件
driver.find_element_by_name("file").send_keys('D:\\selenium_use_case\uploa d_file.txt') #定位上传按钮，添加本地文件
#下载文件
#获取cookie
cookie= driver.get_cookies() # 获得cookie信息
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})  #向cookie的name 和value添加会话信息
driver.delete_cookie("CookieName") # 删除一个特定的cookie
driver.delete_all_cookies()  # 删除所有cookie