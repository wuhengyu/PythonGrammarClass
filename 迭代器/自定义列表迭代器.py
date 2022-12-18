# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 16:32
# @Author  : Walter
# @File    : 自定义列表迭代器.py
# @License : (C)Copyright Walter
# @Desc    : 实现__next__和__iter__方法
class listDemo:
    def __init__(self):
        self.__date = []
        self.__step = 0

    def __next__(self):
        if self.__step <= 0:
            raise StopIteration
        self.__step -= 1
        # 返回下一个元素
        return self.__date[self.__step]

    def __iter__(self):
        # 实例对象本身就是迭代器对象，因此直接返回 self 即可
        return self

    # 添加元素
    def __setitem__(self, key, value):
        self.__date.insert(key, value)
        self.__step += 1


mylist = listDemo()
mylist[0] = 1
mylist[1] = 2
# 迭代器__next__()方法
# print(mylist.__next__())

for i in mylist:
    print(i)

print(iter(mylist))
