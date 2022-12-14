# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 19:24
# @Author  : Walter
# @File    : HowMuchTime03.py
# @License : (C)Copyright Walter
# @Desc    : 给某个函数加上一个装饰器


import threading
# 为函数添加一个统计运行时长的功能
import time


def how_much_time(func):
    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start, ))

    return inner


@how_much_time
# @how_much_time等价于sleep_5s = how_much_time(sleep_5s)
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5,))


@how_much_time
def sleep_6s():
    time.sleep(6)
    print("%d秒结束了" % (6,))


t1 = threading.Thread(target=sleep_5s)
t2 = threading.Thread(target=sleep_6s)
t1.start()
t2.start()
