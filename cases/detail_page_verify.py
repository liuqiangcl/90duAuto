# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 17:52
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : detail_page_verify.py
# @Software: PyCharm
import time
import unittest
from lib import Common, SetResolution, Login
from pages import detail_page
from selenium import webdriver


class DetailPageCase(unittest.TestCase):
    def setUp(self):
        set_resolution = SetResolution.SetResolution()
        self.options = set_resolution.set_current_resolution()
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def test_detail_page(self):
        """详情页面"""
        print("========【case_0017】 详情页面测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "详情页")  # 判断title是否是详情页

    def test_goto_home_page(self):
        """回到首页"""
        print("========【case_0018】 详情页面回到首页测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(1)
        detailpage.goto_home_page
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "90度地产")  # 判断title是否是90度地产

    def test_login_failed_like(self):
        """未登录下点赞"""
        print("========【case_0019】 未登录下点赞测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(1)
        detailpage.like
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())
        self.assertEquals(Login.Login(self.driver).login_title_text, "欢迎来到90度地产")  # 判断是否弹出登录对话框

    def test_login_succeed_like(self):
        """登录下点赞"""
        print("========【case_0020】 登录下点赞测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(1)
        start = int(detailpage.like_num)
        print(start)
        time.sleep(1)
        detailpage.like
        if detailpage.login_title_text == '欢迎来到90度地产':
            detailpage.login('xxxx', '2327')
            detailpage.like
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())
        end = int(detailpage.like_num)
        print(end)
        # self.assertGreater(end, start)

    def test_login_failed_collect(self):
        """未登录下收藏"""
        print("========【case_0021】 未登录下收藏测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(1)
        detailpage.collect
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())
        self.assertEquals(Login.Login(self.driver).login_title_text, "欢迎来到90度地产")  # 判断是否弹出登录对话框

    def test_login_succeed_collect(self):
        """登录下收藏"""
        print("========【case_0022】 登录下收藏测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(2)
        detailpage.collect
        if detailpage.login_title_text == '欢迎来到90度地产':
            detailpage.login('xxxx', '2327')
            detailpage.collect
        time.sleep(2)
        detailpage.screenshot(Common.get_pic_path())

    def test_set_font_small(self):
        """小字体"""
        print("========【case_0023】 设置小字体测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(2)
        detailpage.set_font
        time.sleep(1)
        detailpage.set_font_small
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())

    def test_set_font_small(self):
        """大字体"""
        print("========【case_0024】 设置大字体测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(2)
        detailpage.set_font
        time.sleep(1)
        detailpage.set_font_big
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())

    def test_set_font_small(self):
        """夜间模式"""
        print("========【case_0025】 设置夜间模式测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(2)
        detailpage.set_font
        time.sleep(1)
        detailpage.set_night_mode
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())

    def test_cancel_set_font(self):
        """取消字体设置"""
        print("========【case_0026】 取消字体测试=============")
        detailpage = detail_page.DetailPage(self.driver)
        time.sleep(2)
        detailpage.set_font
        time.sleep(1)
        detailpage.cancel_set_font
        time.sleep(1)
        detailpage.screenshot(Common.get_pic_path())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
