# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 22:54
# @Author  : Walter
# @File    : __init__函数.py
# @License : (C)Copyright Walter
# @Desc    :


class TestInit():
    def __init__(self):
        print('init函数')

    def func(self):
        print('func函数')


testInit = TestInit()
testInit.func()
