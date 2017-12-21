# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 21:57
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Login.py
# @Software: PyCharm
from pages.base_page import BasePage
from readData.read_element import ReadElement


class Login(BasePage):
    def __init__(self, drvier):
        super(Login, self).__init__(drvier)

    @property
    def login_title_text(self):
        """详情登录提示"""
        loginTitleElement = ReadElement().read_element("LoginPage", 'loginTitleText')
        return self.by_xpath_name(loginTitleElement).text

    @property
    def user_text_field(self):
        """手机号字段"""
        userTextElement = ReadElement().read_element("LoginPage", 'userText')
        return self.by_xpath_name(userTextElement)

    @property
    def password_text_field(self):
        """验证码字段"""
        passwordTextElement = ReadElement().read_element("LoginPage", 'passwordText')
        return self.by_xpath_name(passwordTextElement)

    @property
    def login_btn(self):
        """登陆按钮"""
        loginBtnElement = ReadElement().read_element("LoginPage", 'loginBtn')
        return self.by_xpath_name(loginBtnElement)

    def login(self, username, password):
        """登录"""
        self.user_text_field.send_keys(username)
        self.password_text_field.send_keys(password)
        self.login_btn.click()
