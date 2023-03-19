# -*- coding: utf-8 -*-
# Time    : 2023/3/19 21:56
# Author  : Walter
# File    : yield from使用1.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :


# 简单的生成器函数
# 生成从 0 到 n-1 的整数
def nested_generator(n):
    for i in range(n):
        yield i


# 外部生成器
# 使用 yield from 关键字委托 nested_generator() 生成器
# outer_generator() 可以直接迭代 nested_generator() 的结果
# 无需自己实现逻辑来处理 nested_generator() 的每个元素
def outer_generator():
    yield from nested_generator(5)


for num in outer_generator():
    print(num)
