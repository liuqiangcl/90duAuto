# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 15:34
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : home_page.py
# @Software: PyCharm
import time
from lib import SetResolution
from selenium import webdriver
from lib.Slide import Slide
from pages.base_page import BasePage
from readData.read_element import ReadElement


class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.url = self.base_url
        self.navigate()

    @property
    def detail_link(self):
        """跳转文章详情"""
        detailElement = ReadElement().read_element("HomePage", 'detail')
        return self.by_xpath_name(detailElement).click()

    @property
    def drawer_menu_link(self):
        """跳转设置界面"""
        drawerElement = ReadElement().read_element("HomePage", 'drawer')
        return self.by_xpath_name(drawerElement).click()

    @property
    def down_refresh_data(self):
        """下拉刷新"""
        pullrefreshElement = ReadElement().read_element("HomePage", 'pullrefresh')
        clickHoldElement = self.by_xpath_name(pullrefreshElement)
        Slide(self.driver).slide(clickHoldElement, 0, -200)  # 下拉刷新是负数
        time.sleep(3)

    @property
    def async_loading(self):
        """上拉分页"""
        time.sleep(3)
        loadElement = ReadElement().read_element("HomePage", 'load')
        clickHoldElement = self.by_xpath_name(loadElement)
        Slide(self.driver).slide(clickHoldElement, 0, 2500)  # 上拉加载
        time.sleep(3)

    @property
    def qr_code_link(self):
        """打开二维码弹窗"""
        qrCodeOpenElement = ReadElement().read_element("HomePage", 'qr_code_open')
        return self.by_xpath_name(qrCodeOpenElement).click()

    @property
    def close_qr_code(self):
        """关闭二维码弹窗"""
        qrCodeCloseElement = ReadElement().read_element("HomePage", 'qr_code_close')
        self.driver.switch_to_alert()
        return self.by_xpath_name(qrCodeCloseElement).click()


if __name__ == "__main__":
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    HomePage = HomePage(driver)
    time.sleep(3)
    HomePage.detail_link
    time.sleep(3)
    driver.quit()
