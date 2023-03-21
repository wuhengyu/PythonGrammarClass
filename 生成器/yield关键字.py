# -*- coding: utf-8 -*-
# Time    : 2023/3/21 20:44
# Author  : Walter
# File    : yield关键字.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
print(next(g))  # 输出 1
print(next(g))  # 输出 2
print(next(g))  # 输出 3
