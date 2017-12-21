# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 17:17
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Slide.py
# @Software: PyCharm
import time
from selenium.webdriver.common.touch_actions import TouchActions


class Slide(TouchActions):
    def __init__(self, driver):
        super(Slide, self).__init__(driver)

    def slide(self, click_hold_element, xcoord, ycoord):
        self.scroll_from_element(click_hold_element, xcoord, ycoord).perform()  # 向左滑动
        time.sleep(3)
