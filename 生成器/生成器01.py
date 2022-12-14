# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 14:15
# @Author  : Walter
# @File    : 生成器01.py
# @License : (C)Copyright Walter
# @Desc    : intNum() 函数的返回值用的是 yield 关键字，而不是 return 关键字，此类函数又成为生成器函数。
def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")


num = intNum()
# 调用 next() 内置函数
print(next(num))
# 调用 __next__() 方法
print(num.__next__())
# 通过for循环遍历生成器
for i in num:
    print(i)

# 使用 list() 函数和 tuple() 函数，直接将生成器能生成的所有值存储成列表或者元组的形式
# list() 和 tuple() 底层实现和 for 循环的遍历过程是类似的
# num = intNum()
# print(list(num))
# print(tuple(num))
