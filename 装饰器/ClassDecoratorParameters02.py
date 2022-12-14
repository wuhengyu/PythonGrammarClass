# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 20:00
# @Author  : Walter
# @File    : ClassDecoratorParameters02.py
# @License : (C)Copyright Walter
# @Desc    :
import time


class Decorator:
    def __init__(self, func):
        self.func = func

    def defer_time(self, time_sec):
        time.sleep(time_sec)
        print(f"{time_sec}s延时结束了")

    def __call__(self, time):
        self.defer_time(time)
        self.func()


@Decorator
def f1():
    print("延时之后我才开始执行")


f1(5)
