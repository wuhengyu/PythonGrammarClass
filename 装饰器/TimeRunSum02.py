# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 18:00
# @Author  : Walter
# @File    : TimeRunSum02.py
# @License : (C)Copyright Walter
# @Desc    :
# 方案三的优化一：将index的参数写活了
import time


def index(x, y, z):
    time.sleep(3)
    print('index %s %s %s' % (x, y, z))


def wrapper(*args, **kwargs):
    start = time.time()
    # index(111, 222)
    index(*args, **kwargs)  # index(3333,z=5555,y=44444)
    stop = time.time()
    print(stop - start)


wrapper(3333, 4444, 5555)
wrapper(3333, z=5555, y=44444)
