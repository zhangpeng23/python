# coding=utf-8#定义编码
from selenium import webdriver
driver= webdriver.Firefox()#调用火狐
driver.get("http://www.baidu.com")#打开百度
driver.find_element_by_id("kw").send_keys("Selenium3")#找到输入框输入查询内容
driver.find_element_by_id("su").click()#点击"百度一下"
driver.quit()#关闭