# -*- coding: utf-8 -*-
# Time    : 2023/3/19 22:08
# Author  : Walter
# File    : 生成器推导式.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

aa = (x * x for x in range(10))
print(aa.__next__())
print(aa.__next__())
print(aa.__next__())
print(aa.__next__())
print(aa.__next__())
