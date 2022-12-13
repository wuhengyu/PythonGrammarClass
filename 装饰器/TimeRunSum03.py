# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 18:03
# @Author  : Walter
# @File    : TimeRunSum03.py
# @License : (C)Copyright Walter
# @Desc    :


# 方案三的优化三：将wrapper做的跟被装饰对象一模一样，以假乱真
import time


def index(x, y, z):
    time.sleep(3)
    print('index %s %s %s' % (x, y, z))


def home(name):
    time.sleep(2)
    print('welcome %s to home page' % name)


def outter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res

    return wrapper


# 偷梁换柱：home这个名字指向的wrapper函数的内存地址
home = outter(home)
res = home('egon')  # res=wrapper('egon')
