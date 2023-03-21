# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 15:05
# @Author  : Walter
# @File    : close方法.py
# @License : (C)Copyright Walter
# @Desc    :

def g():
    print('Started')
    x = None
    try:
        while True:
            x = yield x
            print('Got:', x)
    except GeneratorExit:
        print('Closed')


gen = g()
next(gen)
# Started
gen.send(10)
gen.close()
# StopIteration错误，close之后不在产生新的值
# gen.send(10)
