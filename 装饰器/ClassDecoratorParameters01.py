# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 20:00
# @Author  : Walter
# @File    : ClassDecoratorParameters01.py
# @License : (C)Copyright Walter
# @Desc    :

import time


class Decorator:
    def __init__(self, func):
        self.func = func

    def defer_time(self):
        time.sleep(5)
        print("延时结束了")

    def __call__(self, *args, **kwargs):
        self.defer_time()
        self.func()


@Decorator
def f1():
    print("延时之后我才开始执行")


f1()
