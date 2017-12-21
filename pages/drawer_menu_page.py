# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 16:38
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : drawer_menu_page.py
# @Software: PyCharm
# from .base_page import BasePage
import time
from lib.Login import Login
from selenium import webdriver
from lib import SetResolution
from readData.read_element import ReadElement


class DrawerMenuPage(Login):
    def __init__(self, driver):
        super(DrawerMenuPage, self).__init__(driver)
        self.url = self.base_url + "/drawerMenu.html"
        self.navigate()

    @property
    def login_element(self):
        """头像"""
        headElement = ReadElement().read_element("DrawerMenuPage", 'head')
        return self.by_xpath_name(headElement)

    @property
    def is_element_exist(self):
        """登陆状态判断"""
        loginStatusElement = ReadElement().read_element("DrawerMenuPage", 'loginStatus')
        return self.by_xpath_name(loginStatusElement).text

    @property
    def login_title(self):
        """登陆标题"""
        loginTitleElement = ReadElement().read_element("DrawerMenuPage", 'loginTitle')
        return self.by_xpath_name(loginTitleElement).text

    @property
    def recent_read(self):
        """最近阅读"""
        recentReadElement = ReadElement().read_element("DrawerMenuPage", 'recentRead')
        self.by_xpath_name(recentReadElement).click()

    @property
    def my_collect(self):
        """我的收藏"""
        myCollectElement = ReadElement().read_element("DrawerMenuPage", 'myCollect')
        self.by_xpath_name(myCollectElement).click()

    @property
    def night_mode(self):
        """夜间模式"""
        nightModeElement = ReadElement().read_element("DrawerMenuPage", 'nightMode')
        return self.by_xpath_name(nightModeElement)

    @property
    def share(self):
        """分享"""
        openShareElement = ReadElement().read_element("DrawerMenuPage", 'openShare')
        self.by_xpath_name(openShareElement).click()

    @property
    def close_share(self):
        """关闭分享"""
        closeShareElement = ReadElement().read_element("DrawerMenuPage", 'closeShare')
        self.driver.switch_to_alert()
        self.by_xpath_name(closeShareElement).click()

    @property
    def edit_personal_data(self):
        """编辑个人资料"""
        editPersonalDataElement = ReadElement().read_element("DrawerMenuPage", 'editPersonalData')
        self.by_xpath_name(editPersonalDataElement).click()

    @property
    def news_link(self):
        """咨询"""
        newsLinkElement = ReadElement().read_element("DrawerMenuPage", 'newsLink')
        self.by_xpath_name(newsLinkElement).click()

    @property
    def original_link(self):
        """独家原创"""
        originalLinkElement = ReadElement().read_element("DrawerMenuPage", 'originalLink')
        self.by_xpath_name(originalLinkElement).click()

    @property
    def big_data_link(self):
        """地产大数据"""
        bigDataLinkElement = ReadElement().read_element("DrawerMenuPage", 'bigDataLink')
        self.by_xpath_name(bigDataLinkElement).click()

    def head_update(self, picture):
        """更新头像"""
        self.login_element.click()
        time.sleep(1)
        photoChoiceElement = ReadElement().read_element("DrawerMenuPage", 'photoChoice')
        clipBtndElement = ReadElement().read_element("DrawerMenuPage", 'clipBtnd')
        self.by_xpath_name(photoChoiceElement).send_keys(picture)
        self.by_xpath_name(clipBtndElement).click()
        time.sleep(1)


if __name__ == "__main__":
    # pass
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    HomePage = DrawerMenuPage(driver)
    time.sleep(3)
    print(HomePage.night_mode.text)
    time.sleep(3)
    driver.quit()
