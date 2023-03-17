# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 15:20
# @Author  : Walter
# @File    : asyncCounter.py
# @License : (C)Copyright Walter
# @Desc    :

with open('test.txt', 'r', encoding='utf-8') as f:
    response = f.readlines()
    response[1].split(',')[0]