# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 14:02
# @Author  : Walter
# @File    : 有参装饰器1.py
# @License : (C)Copyright Walter
# @Desc    :
import time


def outer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@outer
def home():
    """这是home函数"""
    time.sleep(2)
    print("welcome")

home()