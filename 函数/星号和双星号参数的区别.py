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


# 10
print(sum_numbers(1, 2, 3, 4))
# 12
print(sum_numbers(2, 4, 6))
# 0
print(sum_numbers())


def merge_dicts(**dicts):
    result = {}
    # dicts = {'a': {'x': 1, 'y': 2}, 'b': {'z': 3}}
    for d in dicts.values():
        if not isinstance(d, dict):
            raise TypeError('所有参数必须是字典！')
        result.update(d)
    return result


# {'x': 1, 'y': 2, 'z': 3}
print(merge_dicts(a={'x': 1, 'y': 2}, b={'z': 3}))
print(merge_dicts(x={'a': 1}, y={'b': 2}, z={'c': 3}))
print(merge_dicts())


def my_func(a, b, *args):
    print(a, b, args)


print(my_func(1, 2))
print(my_func(1, 2, 3, 4, 5))


def my_func(a, b, **kwargs):
    print(a, b, kwargs)


print(my_func(1, 2, x=3, y=4))
