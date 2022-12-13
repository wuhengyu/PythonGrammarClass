# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 18:03
# @Author  : Walter
# @File    : TimeRunSum05.py
# @License : (C)Copyright Walter
# @Desc    :

# 无参装饰器模板
def outter(func):
    def wrapper(*args, **kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        res = func(*args, **kwargs)
        return res

    return wrapper
