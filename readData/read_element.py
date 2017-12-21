# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 11:31
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : read_element.py
# @Software: PyCharm
from lib.ReadExcel import ReadExcel


class ReadElement(object):
    def __init__(self):
        self.ExcelData = ReadExcel("..\\pageElement\\PageElement.xlsx")

    def read_element(self, sheet_name, element_name):
        return self.ExcelData.excel_to_dict(sheet_name)[element_name]


if __name__ == "__main__":
    print(ReadElement().read_element("Sheet1", "detail"))
