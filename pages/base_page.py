# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 15:33
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : base_page.py.py
# @Software: PyCharm


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def base_url(self):
        return 'http://m.test.90dichan.com'

    def url(self):
        return self.url

    def navigate(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def by_id(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.driver.find_element_by_name(the_name)

    def by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_xpath_name(self, xpath_name):
        return self.driver.find_element_by_xpath(xpath_name)

    def screenshot(self, screenshot_name):
        return self.driver.save_screenshot(screenshot_name)

    def del_cookies(self):
        return self.driver.delete_all_cookies()

    def set_window(self, width, height):
        return self.driver.set_window_size(width, height)
