# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 20:39
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : ReadConfig.py
# @Software: PyCharm
from configparser import ConfigParser


class ReadConfig(object):
    def __init__(self, file_name):
        self.config = ConfigParser()
        self.config.read(file_name)

    def get_node_value(self, section, key):
        return self.config.get(section, key)


if __name__ == "__main__":
    print(ReadConfig("../conf/user.ini").get_node_value("Login", "username"))
