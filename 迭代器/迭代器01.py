# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:40
# @Author  : Walter
# @File    : 迭代器01.py
# @License : (C)Copyright Walter
# @Desc    : 使用 next() 内置函数来迭代，即 next(myIter)，和 __next__() 方法是完全一样的。

# 将列表转换为迭代器
myIter = iter([1, 2, 3])
try:
    # 依次获取迭代器的下一个元素
    print(myIter.__next__())
    print(myIter.__next__())
    print(myIter.__next__())
    print(myIter.__next__())
except StopIteration:
    print("StopIteration错误")
