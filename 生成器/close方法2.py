# -*- coding: utf-8 -*-
# Time    : 2023/3/21 19:49
# Author  : Walter
# File    : close方法2.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print('Generator closing!')


g = my_generator()
print(next(g))  # 输出 1
g.close()
