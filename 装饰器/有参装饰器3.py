# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 11:47
# @Author  : Walter
# @File    : 有参装饰器3.py
# @License : (C)Copyright Walter
# @Desc    :
import time

# 直接通过参数传递
# 通过闭包函数

# def g_outer(name):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(name)
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return outer
#
# outer = g_outer("鲁班")
#
# @outer # outer(home())
# def home():
#     """这是home函数"""
#     time.sleep(2)
#     print("welcome")
#
# home()
#
#
# outer = g_outer("海月")
#
# @outer # outer(home())
# def index():
#     """这是home函数"""
#     time.sleep(2)
#     print("welcome")
#
# index()


# 改进方案
def g_outer(name, age): # outer home=outer(home) home=wrapper
    # outer参数受到语法糖的影响也不能动，所以外面包了一层g_outer
    def outer(func):
        # wrapper需要func参数，但是又不能动wrapper的参数
        def wrapper(*args, **kwargs):
            print(name, age)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outer

@g_outer("鲁班", 19) # outer(home())
def home():
    """这是home函数"""
    time.sleep(2)
    print("welcome")

home()

@g_outer("海月", 20) # outer(home())
def index():
    """这是home函数"""
    time.sleep(2)
    print("welcome")

index()


