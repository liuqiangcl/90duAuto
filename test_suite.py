# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 10:38
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : test_suite.py
# @Software: PyCharm

import time
import unittest
from lib import HTMLTestRunner
# from cases.home_page_verify import HomePageCase
# from cases.drawe_rmenu_page_verify import DrawerMenuCase
# from cases.detail_page_verify import DetailPageCase
from cases.personal_page_verify import PersonalPageCase

# testcases = [HomePageCase, DrawerMenuCase, DetailPageCase, PersonalPageCase]
testcases = [PersonalPageCase]


def test_report():
    testunit = unittest.TestSuite()  # 构建测试套间
    # 循环读取数组中的用例
    for case in testcases:
        testunit.addTest(unittest.makeSuite(case))
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
    reportName = 'result/' + 'Result_' + current_time + '.html'  # 定义报告路径
    fp = open(reportName, 'wb')  # 测试报告模板
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
    return runner.run(testunit)


if __name__ == '__main__':
    test_report()
