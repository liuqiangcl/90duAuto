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
from lib import SetResolution, Common


class DrawerMenuPage(Login):
    def __init__(self, driver):
        super(DrawerMenuPage, self).__init__(driver)
        self.url = self.base_url + "/drawerMenu.html"
        self.navigate()

    @property
    def login_element(self):
        """头像"""
        return self.by_xpath_name('//*[@id="photo"]/img').click()

    @property
    def is_element_exist(self):
        """登陆状态判断"""
        return self.by_xpath_name('//*[@id="drawerMenu"]/div/header/div[2]/h3').text

    @property
    def login_title(self):
        """登陆标题"""
        return self.by_xpath_name('//*[@id="eee"]/div[2]/div[1]/h3').text

    @property
    def night_mode_text(self):
        """白天/夜间模式"""
        return self.by_xpath_name('//*[@id="night"]/p').text

    @property
    def recent_read(self):
        """最近阅读"""
        self.by_xpath_name('//*[@id="read"]/p').click()

    @property
    def my_collect(self):
        """我的收藏"""
        self.by_xpath_name('//*[@id="collection"]/p').click()

    @property
    def night_mode(self):
        """夜间模式"""
        self.by_xpath_name('//*[@id="night"]/p').click()

    @property
    def share(self):
        """分享"""
        self.by_xpath_name('//*[@id="share"]/div/span').click()

    @property
    def close_share(self):
        """关闭分享"""
        self.driver.switch_to_alert()
        self.by_xpath_name('//*[@id="eee"]/div[7]/div[2]/span/a/span').click()

    @property
    def edit_personal_data(self):
        """编辑个人资料"""
        self.by_xpath_name('//*[@id="edit"]/span').click()

    @property
    def news_link(self):
        """咨询"""
        self.by_xpath_name('//*[@id="drawerMenu"]/div/ul[2]/li[1]/a/p').click()

    @property
    def original_link(self):
        """独家原创"""
        self.by_xpath_name('//*[@id="drawerMenu"]/div/ul[2]/li[2]/a/p').click()

    @property
    def big_data_link(self):
        """地产大数据"""
        self.by_xpath_name('//*[@id="drawerMenu"]/div/ul[2]/li[3]/a/p').click()

    def login(self, username, password):
        """登录"""
        self.login_element
        self.user_text_field.send_keys(username)  # username:xxxx
        self.password_text_field.send_keys(password)  # password:2327
        self.login_btn.click()

    def head_update(self, picture):
        """更新头像"""
        self.login_element
        time.sleep(1)
        self.by_id('filed').send_keys(picture)
        self.by_id('clipBtnd').click()
        time.sleep(1)


if __name__ == "__main__":
    # pass
    Set_Resolution = SetResolution.SetResolution()
    options = Set_Resolution.set_current_resolution()
    driver = webdriver.Chrome(chrome_options=options)
    HomePage = DrawerMenuPage(driver)
    time.sleep(3)
    HomePage.login('xxxx', '2327')
    time.sleep(3)
    HomePage.head_update()
    time.sleep(3)
    driver.quit()
