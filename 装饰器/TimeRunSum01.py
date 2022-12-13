# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 18:00
# @Author  : Walter
# @File    : TimeRunSum01.py
# @License : (C)Copyright Walter
# @Desc    :
# 需求：在不修改index函数的源代码以及调用方式的前提下为其添加统计运行时间的功能
import time


def index(x, y):
    time.sleep(3)
    print('index %s %s' % (x, y))


index(111, 222)
# index(y=111,x=222)
# index(111,y=222)


# 解决方案一：失败
# 问题：没有修改被装饰对象的调用方式，但是修改了其源代码
# import time
#
#
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     stop = time.time()
#     print(stop - start)
#
#
# index(111, 222)


# 解决方案二：失败
# 问题：没有修改被装饰对象的调用方式，也没有修改了其源代码，并且加上了新功能
#      但是代码冗余
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#
#
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)
