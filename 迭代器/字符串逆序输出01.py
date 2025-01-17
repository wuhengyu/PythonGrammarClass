# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:52
# @Author  : Walter
# @File    : 字符串逆序输出01.py
# @License : (C)Copyright Walter
# @Desc    :

class Reverse:
    def __init__(self, string):
        self.__string = string
        self.__index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        self.__index -= 1
        return self.__string[self.__index]


# 没有设置遍历的终止条件，换句话说，没有对 __index 私有变量的值对限制，所以输出两遍
revstr = Reverse('Python')
for c in revstr:
    print(c, end=" ")
