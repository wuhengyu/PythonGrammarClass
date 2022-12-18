# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:45
# @Author  : Walter
# @File    : iter()函数创建迭代器.py
# @License : (C)Copyright Walter
# @Desc    :

class CreatesAnIterator:
    def __init__(self):
        self.__date = []
        self.__step = 0

    def __setitem__(self, key, value):
        self.__date.insert(key, value)
        self.__step += 1

    # 使该类实例对象成为可调用对象
    def __call__(self):
        self.__step -= 1
        return self.__date[self.__step]


mylist = CreatesAnIterator()
mylist[0] = 1
mylist[1] = 2
# 可迭代对象无__next__()方法
# print(mylist.__next__())

# 将 mylist 变为迭代器
a = iter(mylist, 1)
# 抛出 StopIteration 异常，是因为这里原本要输出的元素 1 和 iter() 函数的第 2 个参数相同
print(a.__next__())
print(a.__next__())
