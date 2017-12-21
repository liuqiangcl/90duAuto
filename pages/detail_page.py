# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 10:47
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : detail_page.py
# @Software: PyCharm
import time
from lib.Login import Login
from lib.Slide import Slide
from lib import SetResolution
from selenium import webdriver
from readData.read_config import ReadUser
from readData.read_element import ReadElement


class DetailPage(Login):
    def __init__(self, drvier):
        super(DetailPage, self).__init__(drvier)
        self.url = self.base_url + "/detail.html?id=191936765"
        self.navigate()

    @property
    def like(self):
        """点赞"""
        likeElement = ReadElement().read_element("DetailPage", 'like')
        return self.by_xpath_name(likeElement).click()

    @property
    def like_num(self):
        likeNumElement = ReadElement().read_element("DetailPage", 'likeNum')
        return self.by_xpath_name(likeNumElement).text

    @property
    def collect(self):
        """收藏"""
        collectElement = ReadElement().read_element("DetailPage", 'collect')
        return self.by_xpath_name(collectElement).click()

    @property
    def set_font(self):
        """设置字体"""
        setFontElement = ReadElement().read_element("DetailPage", 'setFont')
        return self.by_xpath_name(setFontElement).click()

    @property
    def set_font_small(self):
        """设置小字体"""
        setFontSmallElement = ReadElement().read_element("DetailPage", 'setFontSmall')
        clickHoldElement = self.by_xpath_name(setFontSmallElement)
        Slide(self.driver).slide(clickHoldElement, 100, 0)  # 左加右减
        clickHoldElement.click()

    @property
    def set_font_big(self):
        """设置大字体"""
        setFontBigElement = ReadElement().read_element("DetailPage", 'setFontBig')
        clickHoldElement = self.by_xpath_name(setFontBigElement)
        Slide(self.driver).slide(clickHoldElement, -100, 0)
        clickHoldElement.click()

    @property
    def cancel_set_font(self):
        """取消字体模式"""
        cancelSetFontElement = ReadElement().read_element("DetailPage", 'cancelSetFont')
        return self.by_xpath_name(cancelSetFontElement).click()

    @property
    def set_night_mode(self):
        """设置夜间|白天模式"""
        setNightModeElement = ReadElement().read_element("DetailPage", 'setNightMode')
        return self.by_xpath_name(setNightModeElement).click()

    @property
    def goto_home_page(self):
        """返回首页"""
        gotoHomePageElement = ReadElement().read_element("DetailPage", 'gotoHomePage')
        return self.by_xpath_name(gotoHomePageElement).click()

    @property
    def login_btn(self):
        """登陆按钮"""
        loginBtnElement = ReadElement().read_element("DetailPage", 'loginBtn')
        return self.by_xpath_name(loginBtnElement)


if __name__ == "__main__":
    # pass
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    HomePage = DetailPage(driver)
    time.sleep(3)
    HomePage.like
    time.sleep(3)
    print(HomePage.login_title_text)
    time.sleep(3)
    HomePage.login(ReadUser().get_username, ReadUser().get_password)
    time.sleep(3)
    driver.quit()
