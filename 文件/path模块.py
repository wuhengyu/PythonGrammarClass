# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 21:26
# @Author  : Walter
# @File    : path模块.py
# @License : (C)Copyright Walter
# @Desc    :

from os import path

# 获取绝对路径
print(path.abspath("my_file.txt"))
# 获取共同前缀
print(path.commonprefix(['C://my_file.txt', 'C://a.txt']))
# 获取共同路径
print(path.commonpath(['http://www.baidu.com/python/', 'http://www.baidu.com/shell/']))
# 获取目录
print(path.dirname('C://my_file.txt'))
# 判断指定目录是否存在
print(path.exists('my_file.txt'))
