# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 15:40
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : SetResolution.py
# @Software: PyCharm
from selenium import webdriver


class SetResolution(object):
    def __init__(self):
        self.WIDTH = 320
        self.HEIGHT = 640
        self.PIXEL_RATIO = 3.0  # 像素比
        self.mobileEmulation = {
            "deviceMetrics": {"width": self.WIDTH, "height": self.HEIGHT, "pixelRatio": self.PIXEL_RATIO}}
        self.options = webdriver.ChromeOptions()

    def set_current_resolution(self):
        self.options.add_experimental_option('mobileEmulation', self.mobileEmulation)
        return self.options


if __name__ == "__main__":
    driver = webdriver.Chrome()
    SetResolution = SetResolution()
    print(SetResolution.setting_current_resolution())
