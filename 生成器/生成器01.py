# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 23:44
# @Author  : Walter
# @File    : 生成器01.py
# @License : (C)Copyright Walter
# @Desc    :

# 生成器是一种自定义的迭代器

def wrapper(x):
    while x < 5:
        yield x
        x += 1

# generator类型
print(wrapper(1))
res = wrapper(1)
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())

# StopIteration
# print(res.__next__())