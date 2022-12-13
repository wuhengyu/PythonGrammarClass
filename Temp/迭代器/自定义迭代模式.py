# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 13:00
# @Author  : Walter
# @File    : 自定义迭代模式.py
# @License : (C)Copyright Walter
# @Desc    :

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))
print(sum(frange(0, 1, 0.125)))
