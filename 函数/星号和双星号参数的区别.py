# -*- coding: utf-8 -*-
# Time    : 2023/3/11 19:42
# Author  : Walter
# File    : 星号和双星号参数的区别.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


sum_numbers(1, 2, 3, 4)  # 返回 10
sum_numbers(2, 4, 6)  # 返回 12
sum_numbers()  # 返回 0


def merge_dicts(**dicts):
    result = {}
    for d in dicts.values():
        if not isinstance(d, dict):
            raise TypeError('所有参数必须是字典！')
        result.update(d)
    return result


merge_dicts(a={'x': 1, 'y': 2}, b={'z': 3})  # 返回 {'x': 1, 'y': 2, 'z': 3}
merge_dicts(x={'a': 1}, y={'b': 2}, z={'c': 3})  # 返回 {'a': 1, 'b': 2, 'c': 3}
merge_dicts()  # 返回 {}


def my_func(a, b, *args):
    print(a, b, args)


my_func(1, 2)  # 输出 (1, 2, ())
my_func(1, 2, 3, 4, 5)  # 输出 (1, 2, (3, 4, 5))


def my_func(a, b, **kwargs):
    print(a, b, kwargs)


my_func(1, 2, x=3, y=4)  # 输出 (1, 2,
