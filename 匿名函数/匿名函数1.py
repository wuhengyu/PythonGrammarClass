# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 23:54
# @Author  : Walter
# @File    : 匿名函数1.py
# @License : (C)Copyright Walter
# @Desc    :

# 有名函数
def func(x, y):
    return x + y


print(func(1, 1))
# 匿名函数
# lambda 后接参数，可以接默认值，冒号分割后，再接函数表达式，并以括号调用，print()输出
print((lambda x=1, y=1: x + y)())
print((lambda x=1, y=1: x + y)(2, 2))