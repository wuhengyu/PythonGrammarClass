# -*- coding: utf-8 -*-
# Time    : 2023/3/17 10:38
# Author  : Walter
# File    : 两个列表转换字典.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

a_list = ["a", "b", "c", "d", "e", "f"]
b_list = [1, 2, 3, 4, 5, 6]

c_dict = {}
for i, k in enumerate(a_list):
    c_dict[k] = b_list[i]
print(c_dict)

# 使用字典推导式将两个列表转换为字典
my_dict = {a_list[i]: b_list[i] for i in range(len(a_list))}
print(my_dict)
