# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:14
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : ReadExcel.py
# @Software: PyCharm
import xlrd


class ReadExcel(object):
    def __init__(self, excele_name):
        self.data = xlrd.open_workbook(excele_name)

    def excel_to_dict(self, sheet_name):
        """
        :return dict
        """
        content = []
        table = self.data.sheet_by_name(sheet_name)
        for i in range(1, table.nrows):
            # table.ncols获取列数  table.row_values获取整行
            row_content = table.row_values(i, 1, table.ncols)
            content.append(row_content)
        return dict(content)


if __name__ == "__main__":
    print(ReadExcel('..\\pageElement\\PageElement.xlsx').excel_to_dict(u'Sheet1'))
