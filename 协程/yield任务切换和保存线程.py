# -*- coding: utf-8 -*-
# Time    : 2023/3/10 11:55
# Author  : Walter
# File    : yield任务切换和保存线程.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :


def func1():
    for i in range(11):
        # yiled可以保存状态，yield的状态保存与操作系统的保存线程状态很像，但是yield是代码级别控制的，更轻量级
        yield
        print('这是我第%s次打印啦' % i)
        # time.sleep(1)


def func2():
    g = func1()
    # next(g)
    for k in range(11):
        print('哈哈，我第%s次打印了' % k)
        # time.sleep(1)
        # next(g)


# 不写yield，下面两个任务是执行完func1里面所有的程序才会执行func2里面的程序，有了yield，我们实现了两个任务的切换+保存状态
func1()
func2()

# g = func1()
# print(next(g))
# print(next(g))
