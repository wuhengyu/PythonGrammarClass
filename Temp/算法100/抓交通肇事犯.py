# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 23:02
# @Author  : Walter
# @File    : demo01.py
# @License : (C)Copyright Walter
# @Desc    : 抓交通肇事犯

for i in range(10):
    for j in range(10):
        if i != j:
            k = 1000 * i + 100 * i + 10 * j + j
            for temp in range(31, 100):
                if temp * temp == k:
                    print("车牌号:", k)
