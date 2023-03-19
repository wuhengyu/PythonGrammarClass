# -*- coding: utf-8 -*-
# Time    : 2023/3/19 22:07
# Author  : Walter
# File    : 字典推导式.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
a_list = ['a', 'b', 'c', 'd', 'e']
b_list = [1, 2, 3, 4, 5]

aa = {a_list[i]: b_list[i] for i in range(5)}
print(aa)
