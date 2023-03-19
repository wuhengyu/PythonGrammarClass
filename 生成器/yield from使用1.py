# -*- coding: utf-8 -*-
# Time    : 2023/3/19 21:56
# Author  : Walter
# File    : yield from使用1.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :


# 简单的生成器函数
def nested_generator(n):
    for i in range(n):
        yield i


def outer_generator():
    yield from nested_generator(5)


for num in outer_generator():
    print(num)
