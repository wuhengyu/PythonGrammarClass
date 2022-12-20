# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 18:11
# @Author  : Walter
# @File    : tell() 函数.py
# @License : (C)Copyright Walter
# @Desc    :

f = open("a.txt", 'r', encoding='utf-8')
print(f.tell())
print(f.read(1))
print(f.tell())
