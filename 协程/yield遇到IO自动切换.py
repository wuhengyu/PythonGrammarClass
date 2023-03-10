# -*- coding: utf-8 -*-
# Time    : 2023/3/10 12:28
# Author  : Walter
# File    : yield遇到IO自动切换.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import time


def func1():
    while True:
        print('func1')
        yield


def func2():
    g = func1()
    for i in range(100):
        print(i + 1)
        next(g)
        # time.sleep(3)
        print('func2')


start = time.time()
func2()
stop = time.time()
print(stop - start)
