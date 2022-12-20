# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 21:47
# @Author  : Walter
# @File    : 类变量.py
# @License : (C)Copyright Walter
# @Desc    :

class CLanguage:
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://www.baidu.com"

    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)


clan = CLanguage()
# 通过类对象是无法修改类变量的。通过类对象对类变量赋值，其本质将不再是修改类变量的值，而是在给该对象定义新的实例变量
clan.add = '111'
print(CLanguage.add)

CLanguage.add = '222'
print(CLanguage.add)
