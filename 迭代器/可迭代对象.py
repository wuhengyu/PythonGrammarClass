# -*- coding: utf-8 -*-
# Time    : 2023/3/19 23:31
# Author  : Walter
# File    : 可迭代对象.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
from collections.abc import Iterable

aa = "可迭代对象"
for i in aa:
    print(i)

# 判断是否是可迭代对象
# 字符串True
print(isinstance(aa, Iterable))
# 列表
print(isinstance([], Iterable))
# 集合True
print(isinstance({"a", "b"}, Iterable))
# 元组True
print(isinstance((), Iterable))
# 整型False
print(isinstance(11, Iterable))
# 浮点型False
print(isinstance(11.11, Iterable))
# 字典True
print(isinstance({"a": 1}, Iterable))
