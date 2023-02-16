# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 15:46
# @Author  : Walter
# @File    : 装饰器叠加1.py
# @License : (C)Copyright Walter
# @Desc    :

def outer1(func1):
    def wrapper1(*args, **kwargs):
        print("开始执行outer1.wrapper1")
        res1 = func1(*args, **kwargs) # func1 = 原home
        print("执行outer1.wrapper1结束")
        return res1
    return wrapper1



def outer2(x):
    def outer(func2):
        def wrapper2(*args, **kwargs):
            print("开始执行outer2.wrapper2")
            res2 = func2(*args, **kwargs)  # func2 = outer1.wrapper1
            print("执行outer2.wrapper2结束")
            return res2
        return wrapper2
    return outer


def outer3(func3):
    def wrapper3(*args, **kwargs):
        print("开始执行outer3.wrapper3")
        res3 = func3(*args, **kwargs)  # func3 = outer2.wrapper2
        print("执行outer3.wrapper3结束")
        return res3
    return wrapper3

# 互相传递内存地址
# home = outer1.wrapper1
# outer2的home=outer1.wrapper1
# outer3的home=outer2.wrapper2
# home = outer3.wrapper3
@outer3 # home = outer3(home) # outer3.wrapper3
@outer2(10) # outer = outer2(10) => @outer => home = outer(home) # outer2.wrapper2
@outer1 # home = outer1(home) # outer1.wrapper1
def home(z):
    print("执行home功能", z)
    return '海月'

# 全局调用home，其实调用的是outer3.wrapper
print(home(0))