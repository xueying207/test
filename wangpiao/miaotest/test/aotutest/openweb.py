from selenium import webdriver


dir(selenium)

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")   #打开浏览器
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()