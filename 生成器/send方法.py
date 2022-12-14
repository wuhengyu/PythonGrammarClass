# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 13:05
# @Author  : Walter
# @File    : send方法.py
# @License : (C)Copyright Walter
# @Desc    :

from collections.abc import Generator


# 生成器函数
def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b = b, a + b
        i += 1


print(fib(3))
print(isinstance(fib(1), Generator))
"""
True
"""

# 生成器表达式
g = (i for i in (1, 2, 3))
print(isinstance(g, Generator))
"""
True
"""
