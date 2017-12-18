# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 15:34
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : home_page.py
# @Software: PyCharm
import time
from lib import SetResolution
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.url = self.base_url
        self.navigate()

    @property
    def detail_link(self):
        """跳转文章详情"""
        return self.by_xpath_name('//*[@id="pullrefresh"]/div[2]/ul/li[1]/a/div/span').click()

    @property
    def drawer_menu_link(self):
        """跳转设置界面"""
        return self.by_id('drawerMenu').click()

    @property
    def down_refresh_data(self):
        """下拉刷新"""
        Action = TouchActions(self.driver)
        clickHoldElement = self.by_xpath_name('//*[@id="191936765"]/div[1]/span')
        Action.scroll_from_element(clickHoldElement, 0, -200).perform()  # 下拉刷新是负数
        time.sleep(3)

    @property
    def async_loading(self):
        """上拉分页"""
        time.sleep(3)
        Action = TouchActions(self.driver)
        clickHoldElement = self.by_xpath_name('//*[@id="191936765"]/div[1]/span')
        Action.scroll_from_element(clickHoldElement, 0, 2500).perform()
        time.sleep(3)

    @property
    def qr_code_link(self):
        """打开二维码弹窗"""
        return self.by_xpath_name('//*[@id="scanCode"]').click()

    @property
    def close_qr_code(self):
        """关闭二维码弹窗"""
        self.driver.switch_to_alert()
        return self.by_xpath_name('//*[@id="eee"]/div[5]/div[2]/span/a/span').click()


if __name__ == "__main__":
    pass
    # Set_Resolution = SetResolution.SetResolution()
    # options = Set_Resolution.set_current_resolution()
    # driver = webdriver.Chrome(chrome_options=options)
    # HomePage = HomePage(driver)
    # time.sleep(3)
    # HomePage.down_refresh_data
    # time.sleep(3)
    # driver.quit()
