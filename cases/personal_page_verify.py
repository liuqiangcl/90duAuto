# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 11:54
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : personal_page_verify.py
# @Software: PyCharm
import time
import unittest
from lib import Common, SetResolution
from pages.personal_page import PersonalPage
from selenium import webdriver


class PersonalPageCase(unittest.TestCase):
    def setUp(self):
        set_resolution = SetResolution.SetResolution()
        self.options = set_resolution.set_current_resolution()
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def test_personal_page(self):
        """编辑个人资料"""
        print("========【case_0027】 编辑个人资料测试=============")
        personalpage = PersonalPage(self.driver)
        time.sleep(1)
        personalpage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "编辑个人资料")  # 增加断言判断title是否是编辑个人资料

    def test_set_message(self):
        """消息设置"""
        print("========【case_0028】 消息设置测试=============")
        personalpage = PersonalPage(self.driver)
        time.sleep(1)
        personalpage.login('xxxx', '2327')
        time.sleep(1)
        personalpage.set_message
        personalpage.screenshot(Common.get_pic_path())
        self.assertEquals(self.driver.title, "消息设置")  # 增加断言判断title是否是消息设置

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
