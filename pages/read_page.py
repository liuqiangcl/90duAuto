# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 14:46
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : read_page.py
# @Software: PyCharm
import time
from lib import SetResolution
from selenium import webdriver
from lib.Login import Login
from selenium.webdriver.common.touch_actions import TouchActions
from lib.Slide import Slide
from lib.ReadConfig import ReadConfig


class ReadPage(Login):
    def __init__(self, driver):
        super(ReadPage, self).__init__(driver)
        self.url = self.base_url + "/read.html"
        self.navigate()

    @property
    def login_btn(self):
        return self.by_xpath_name('/html/body/div[2]/div[2]/form/div[3]/button')

    @property
    def scroll_up(self):
        Action = TouchActions(self.driver)
        Action.scroll(0, 500).perform()
        time.sleep(1)

    def del_history(self, article_num):
        base_xpath = '//*[@id="pullrefresh"]/div[2]/ul/li[%s]' % article_num
        clickHoldElement = self.by_xpath_name(base_xpath + '/div[2]/div/a')
        Slide(self.driver).slide(clickHoldElement, 75, 0)
        self.by_xpath_name(base_xpath + '/div[1]/a').click()  # 点击删除按钮

    @property
    def confirm_del(self):
        self.by_xpath_name("/html/body/div[5]/div[2]/span[1]").click()

    @property
    def cancel_del(self):
        self.by_xpath_name('/html/body/div[5]/div[2]/span[2]').click()


if __name__ == "__main__":
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    read_page = ReadPage(driver)
    read_page.login(ReadConfig().get_username, ReadConfig().get_password)
    time.sleep(3)
    read_page.del_history(2)
    time.sleep(3)
    read_page.cancel_del
    time.sleep(3)
    # while True:
    #     read_page.scroll_up
    #     # time.sleep(3)
    #     if "没有更多数据了" in driver.page_source:
    #         print("滚动到底部")
    #         time.sleep(3)
    #         break

    driver.quit()
