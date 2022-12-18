# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:59
# @Author  : Walter
# @File    : 字符串逆序输出02.py
# @License : (C)Copyright Walter
# @Desc    :

class Reverse:
    def __init__(self, string):
        self.__string = string
        self.__index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == 0:
            raise (StopIteration)
        self.__index -= 1
        return self.__string[self.__index]


revstr = Reverse('Python')
for c in revstr:
    print(c, end=" ")
