# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 0:55
# @Author  : Walter
# @File    : classmethod() 函数.py
# @License : (C)Copyright Walter
# @Desc    : classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
'''
返回值
返回函数的类方法。
'''


class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化
