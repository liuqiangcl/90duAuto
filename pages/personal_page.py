# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 22:13
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : personal_page.py
# @Software: PyCharm
import time
from lib import Login
from lib import SetResolution
from selenium import webdriver
from lib.ReadConfig import ReadConfig
from readData.read_element import ReadElement


class PersonalPage(Login.Login):
    def __init__(self, driver):
        super(PersonalPage, self).__init__(driver)
        self.url = self.base_url + "/personalData.html"
        self.navigate()

    @property
    def login_btn(self):
        """登陆按钮"""
        loginBtnElement = ReadElement().read_element("PersonalPage", 'loginBtn')
        return self.by_xpath_name(loginBtnElement)

    @property
    def set_message(self):
        """消息设置"""
        setMessageElement = ReadElement().read_element("PersonalPage", 'setMessage')
        self.by_xpath_name(setMessageElement).click()


if __name__ == "__main__":
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    personal_page = PersonalPage(driver)
    time.sleep(3)
    personal_page.login(ReadConfig().get_username, ReadConfig().get_password)
    time.sleep(3)
    personal_page.set_message
    time.sleep(3)
    driver.quit()
