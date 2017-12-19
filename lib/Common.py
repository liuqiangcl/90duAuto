# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 15:16
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Common.py
# @Software: PyCharm
import os
import time
from lib import Login
from pages.drawer_menu_page import DrawerMenuPage


def is_directory_exist(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)


def get_current_time():
    return time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def get_current_date():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def is_login_status_fail(driver, username, password):
    """判断设置页面是否是登录状态"""
    if DrawerMenuPage(driver).is_element_exist == "未登录":
        DrawerMenuPage(driver).login_element.click()
        time.sleep(1)
        Login.Login(driver).login(username, password)
        time.sleep(1)


def get_pic_path():
    base_path = "result\\image\\" + get_current_date()
    is_directory_exist(base_path)
    pic_path = base_path + '\\' + get_current_time() + '.png'
    print(pic_path)
    return pic_path


if __name__ == "__main__":
    print(get_current_date())
    print(get_current_time())
