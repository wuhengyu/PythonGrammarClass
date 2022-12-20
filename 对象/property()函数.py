# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 23:05
# @Author  : Walter
# @File    : property()函数.py
# @License : (C)Copyright Walter
# @Desc    :

class CLanguage:
    # 构造函数
    def __init__(self, name):
        self.name = name

    # 设置 name 属性值的函数
    def setname(self, name):
        self.name = name

    # 访问nema属性值的函数
    def getname(self):
        return self.name

    # 删除name属性值的函数
    def delname(self):
        self.name = "xxx"


clang = CLanguage("C语言中文网")
# 获取name属性值
print(clang.getname())
# 设置name属性值
clang.setname("Python教程")
print(clang.getname())
# 删除name属性值
clang.delname()
print(clang.getname())
