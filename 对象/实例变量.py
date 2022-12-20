# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 21:55
# @Author  : Walter
# @File    : 实例变量.py
# @License : (C)Copyright Walter
# @Desc    :

class CLanguage:
    name = "xxx"  # 类变量
    add = "http://"  # 类变量

    def __init__(self):
        self.name = "C语言中文网"  # 实例变量
        self.add = "http://c.baidu.net"  # 实例变量

    # 下面定义了一个say实例方法
    def say(self):
        self.catalog = 13  # 实例变量


clang = CLanguage()
# 修改 clang 对象的实例变量
clang.name = "python教程"
clang.add = "http://c.baidu.net/python"
print(clang.name)
print(clang.add)
clang2 = CLanguage()
print(clang2.name)
print(clang2.add)
# 输出类变量的值
print(CLanguage.name)
print(CLanguage.add)
