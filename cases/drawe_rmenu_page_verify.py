# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 21:59
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : drawe_rmenu_page_verify.py
# @Software: PyCharm
import time
import unittest
from lib import Common, SetResolution
from pages import drawer_menu_page
from selenium import webdriver


class DrawerMenuCase(unittest.TestCase):
    def setUp(self):
        set_resolution = SetResolution.SetResolution()
        self.options = set_resolution.set_current_resolution()
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def test_login_failed_recent_read(self):
        """未登录状态最近阅读"""
        print("========【case_0007】 未登录状态最近阅读测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(1)
        drawerMenuPage.recent_read
        time.sleep(1)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(drawerMenuPage.login_title, "欢迎来到90度地产")  # 判断是否弹出登录窗口

    def test_login_succeed_recent_read(self):
        """登录状态最近阅读"""
        print("========【case_0008】 登录状态最近阅读测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        Common.is_login_status_fail(self.driver, 'xxxx', '2327')
        time.sleep(1)
        drawerMenuPage.recent_read
        time.sleep(1)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "最近阅读")  # 判断是否打开最近阅读

    def test_login_failed_my_collect(self):
        """未登录状态我的收藏"""
        print("========【case_0009】 未登录状态我的收藏测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(1)
        drawerMenuPage.my_collect
        time.sleep(1)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(drawerMenuPage.login_title, "欢迎来到90度地产")  # 判断是否弹出登录窗口

    def test_login_succeed_my_collect(self):
        """登录状态我的收藏"""
        print("========【case_0010】 登录状态我的收藏测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(1)
        Common.is_login_status_fail(self.driver, 'xxxx', '2327')
        time.sleep(1)
        drawerMenuPage.my_collect
        time.sleep(1)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "我的收藏")  # 判断是否打开我的收藏

    def test_night_mode(self):
        """夜间模式"""
        print("========【case_0011】 夜间模式测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(3)
        drawerMenuPage.night_mode
        time.sleep(3)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(drawerMenuPage.night_mode_text, '白天模式')  # 判断切换为夜间模式，显示是否为白天模式

    def test_daytime_mode(self):
        """白天模式"""
        print("========【case_0012】 白天模式测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(3)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(drawerMenuPage.night_mode_text, '夜间模式')  # 判默认为白天模式，并且是否切换夜间模式

    def test_share(self):
        """分享"""
        print("========【case_0013】 分享测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(3)
        drawerMenuPage.share
        time.sleep(3)
        drawerMenuPage.screenshot(Common.get_pic_path())
        drawerMenuPage.close_share
        time.sleep(3)
        drawerMenuPage.screenshot(Common.get_pic_path())

    def test_news_link(self):
        """咨询"""
        print("========【case_0014】 咨询链接测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(3)
        drawerMenuPage.news_link
        time.sleep(3)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, '90度地产')  # 判断标题是否为90度地产

    def test_original_link(self):
        """独家专题"""
        print("========【case_0015】 独家专题链接测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(3)
        drawerMenuPage.original_link
        time.sleep(3)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, '独家原创')  # 判断标题是否为独家原创

    def test_big_data_link(self):
        """地产大数据报告"""
        print("========【case_0016】 地产大数据报告链接测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(1)
        drawerMenuPage.big_data_link
        time.sleep(1)
        drawerMenuPage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, '地产大数据')  # 判断标题是否为地产大数据

    def test_head_update(self):
        """头像更新"""
        print("========【case_0029】 头像更新测试=====")
        drawerMenuPage = drawer_menu_page.DrawerMenuPage(self.driver)
        time.sleep(1)
        Common.is_login_status_fail(self.driver, 'xxxx', '2327')
        time.sleep(1)
        drawerMenuPage.head_update('D:\\20171218160332.png')
        time.sleep(1)
        drawerMenuPage.screenshot(Common.get_pic_path())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
