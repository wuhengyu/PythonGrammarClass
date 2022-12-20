# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 21:55
# @Author  : Walter
# @File    : 局部变量.py
# @License : (C)Copyright Walter
# @Desc    :

# 局部变量直接以“变量名=值”的方式进行定义
class CLanguage:
    # 下面定义了一个say实例方法
    def count(self, money):
        sale = 0.8 * money
        print("优惠后的价格为：", sale)


clang = CLanguage()
clang.count(100)
