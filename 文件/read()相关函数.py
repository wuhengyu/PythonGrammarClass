# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 17:32
# @Author  : Walter
# @File    : read()相关函数.py
# @License : (C)Copyright Walter
# @Desc    :

with open('a.txt', 'r+', encoding="utf-8") as f:
    print(f.read(3))
    print(f.readline())
    print(f.readlines())
    f.close()
