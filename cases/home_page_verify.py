# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 16:38
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : home_page_verify.py
# @Software: PyCharm
import time
import unittest
from lib import Common, SetResolution
import pages.home_page as Homepage
from selenium import webdriver


class HomePageCase(unittest.TestCase):
    def setUp(self):
        set_resolution = SetResolution.SetResolution()
        self.options = set_resolution.set_current_resolution()
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def test_home_page(self):
        """主页"""
        print("========【case_0001】 主页测试=============")
        homepage = Homepage.HomePage(self.driver)
        time.sleep(1)
        homepage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "90度地产")  # 判断title是否是90度地产

    def test_detail_link(self):
        """文章详情"""
        print("========【case_0002】 文章详情链接测试=============")
        homepage = Homepage.HomePage(self.driver)
        time.sleep(1)
        homepage.detail_link
        time.sleep(1)
        homepage.screenshot(Common.get_pic_path())
        self.assertIn("责任编辑", self.driver.page_source)  # 判断文章内容是否包含责任编辑

    def test_drawer_menu_link(self):
        """我的页面"""
        print("========【case_0003】 我的页面测试=============")
        homepage = Homepage.HomePage(self.driver)
        time.sleep(1)
        homepage.drawer_menu_link
        time.sleep(1)
        homepage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "我的")  # 判断title是否是我的

    def test_async_loading(self):
        """上拉分页"""
        print("========【case_0004】 分页测试=============")
        homepage = Homepage.HomePage(self.driver)
        time.sleep(3)
        homepage.async_loading
        time.sleep(3)
        homepage.screenshot(Common.get_pic_path())
        self.assertIn('北京二手房中介门店门可罗雀市场成交量低迷', self.driver.page_source)  # 判断内容是否包含《北京二手房中介门店门可罗雀市场成交量低迷》文章

    def test_qr_code_link(self):
        """二维码"""
        print("========【case_0005】 二维码页面测试=============")
        homepage = Homepage.HomePage(self.driver)
        time.sleep(3)
        homepage.qr_code_link  # 打开二维码
        time.sleep(3)
        homepage.screenshot(Common.get_pic_path())
        homepage.close_qr_code  # 关闭二维码
        time.sleep(3)
        homepage.screenshot(Common.get_pic_path())

    def test_down_refresh_data(self):
        """下拉更新"""
        print("========【case_0006】 下拉更新测试=============")
        homepage = Homepage.HomePage(self.driver)
        time.sleep(3)
        homepage.down_refresh_data
        homepage.screenshot(Common.get_pic_path())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
