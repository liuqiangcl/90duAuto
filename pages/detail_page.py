# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 10:47
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : detail_page.py
# @Software: PyCharm
import time
from lib.Login import Login
from selenium import webdriver
from lib import SetResolution, Common
from selenium.webdriver.common.touch_actions import TouchActions


class DetailPage(Login):
    def __init__(self, drvier):
        super(DetailPage, self).__init__(drvier)
        self.url = self.base_url + "/detail.html?id=191936765"
        self.navigate()

    @property
    def like(self):
        """点赞"""
        return self.by_xpath_name('//*[@id="theme_zan"]/i').click()

    @property
    def like_num(self):
        return self.by_xpath_name('//*[@id="theme_zan"]/span').text

    @property
    def collect(self):
        """收藏"""
        return self.by_xpath_name('//*[@id="theme_star"]/i').click()

    @property
    def set_font(self):
        """设置字体"""
        return self.by_xpath_name('/html/body/nav/a[4]/i').click()

    @property
    def set_font_small(self):
        """设置小字体"""
        Action = TouchActions(self.driver)
        clickHoldElement = self.by_xpath_name('/html/body/div[3]/ul/li[2]/div/input')
        Action.scroll_from_element(clickHoldElement, 100, 0).perform()  # 左加右减

    @property
    def set_font_big(self):
        """设置大字体"""
        Action = TouchActions(self.driver)
        clickHoldElement = self.by_xpath_name('/html/body/div[3]/ul/li[2]/div/input')
        Action.scroll_from_element(clickHoldElement, -100, 0).perform()  # 左加右减

    @property
    def cancel_set_font(self):
        """取消字体模式"""
        return self.by_xpath_name('/html/body/div[3]/ul/li[3]/span').click()

    @property
    def set_night_mode(self):
        """设置夜间|白天模式"""
        return self.by_xpath_name('//*[@id="switch"]/div').click()

    @property
    def goto_home_page(self):
        """返回首页"""
        return self.by_xpath_name('/html/body/div[1]/a').click()

    @property
    def login_btn(self):
        """登陆按钮"""
        return self.by_xpath_name('/html/body/div[4]/div[2]/form/div[3]/button')


if __name__ == "__main__":
    # pass
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    HomePage = DetailPage(driver)
    time.sleep(3)
    HomePage.like
    time.sleep(3)
    HomePage.login('xxxx', '2327')
    time.sleep(3)
    driver.quit()
