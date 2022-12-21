# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 11:47
# @Author  : Walter
# @File    : 有参装饰器.py
# @License : (C)Copyright Walter
# @Desc    :
import time


# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper()
#
# @outer
# def home():
#     """这是home函数"""
#     time.sleep(2)
#     print("welcome")




def g_outer(name):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(name)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outer

outer = g_outer("walter")

@outer # outer(home())
def home():
    """这是home函数"""
    time.sleep(2)
    print("welcome")


home()