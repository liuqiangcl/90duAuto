# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 21:57
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Login.py
# @Software: PyCharm
from pages.base_page import BasePage


class Login(BasePage):
    def __init__(self, drvier):
        super(Login, self).__init__(drvier)

    @property
    def login_title_text(self):
        """详情登录提示"""
        return self.by_xpath_name('/html/body/div[4]/div[1]/h3').text

    @property
    def user_text_field(self):
        """手机号字段"""
        return self.by_xpath_name('//*[@id="phone"]')

    @property
    def password_text_field(self):
        """验证码字段"""
        return self.by_xpath_name('//*[@id="get_code"]')

    @property
    def login_btn(self):
        """登陆按钮"""
        return self.by_xpath_name('//*[@id="eee"]/div[2]/div[2]/form/div[3]/button')
