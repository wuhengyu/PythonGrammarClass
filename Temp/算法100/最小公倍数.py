# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 18:46
# @Author  : Walter
# @File    : 最小公倍数.py
# @License : (C)Copyright Walter
# @Desc    :

print("请输入求最小公倍数的两个数：")
m = int(input())
n = int(input())
if m < n:
    m, n = n, m

i = m
while i != 0:
    if i % m == 0 and i % n == 0:
        print("%d和%d最小公倍数为%d" % (m, n, i))
        break
    i += 1
