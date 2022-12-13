# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 18:03
# @Author  : Walter
# @File    : TimeRunSum04.py
# @License : (C)Copyright Walter
# @Desc    :
# 语法糖：让你开心的语法
import time


# 装饰器
def timmer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res

    return wrapper


# 在被装饰对象正上方的单独一行写@装饰器名字
@timmer  # index=timmer(index)
def index(x, y, z):
    time.sleep(3)
    print('index %s %s %s' % (x, y, z))


@timmer  # home=timmer(home)
def home(name):
    time.sleep(2)
    print('welcome %s to home page' % name)


index(x=1, y=2, z=3)
home('egon')
