# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 00:02
# @Author  : Walter
# @File    : 匿名函数2.py
# @License : (C)Copyright Walter
# @Desc    :

# 有名函数需要多次调用，匿名函数只需要调用一次
# lambda x, y: x + y 是一个内存地址
# func = (lambda x, y: x + y)
# print(func(1, 2))


info = {
    "zhangsan": 11,
    "lisi": 22,
    "wangwu": 33,
    "lucy": 44,
    "james": 55
}

# 直接比是比集合key值ascii码首字母，依次排比
# print(max(info))

# def func(k):
#     return info[k]
#
# print(max(info, key=func))

# 方法二：
print(max(info, key=lambda k: info[k]))


a = [10, 8, 15]
# print(sorted(a))
# [0, 1, 2] 为基础排序数据，key是排序规则
# key是匿名函数，传入[0, 1, 2]，a[0], a[1], a[2]的值作为大小比较
print(sorted(range(len(a)), key=lambda i: a[i]))

# 两种方法
b = [(11, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
b.sort(key=lambda item: item[1])
print(b)

c = [(11, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(sorted(c, key=lambda item: item[1]))