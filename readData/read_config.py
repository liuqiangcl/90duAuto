# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 17:16
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : read_config.py
# @Software: PyCharm

from lib.ReadConfig import ReadConfig


class ReadUser(object):
    def __init__(self):
        self.ConfigData = ReadConfig("..\\conf\\user.ini")

    @property
    def get_username(self):
        return self.ConfigData.get_node_value("Login", "username")

    @property
    def get_password(self):
        return self.ConfigData.get_node_value("Login", "password")


if __name__ == "__main__":
    print(ReadUser().get_username)
    print(ReadUser().get_password)
