# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 14:15
# @Author  : Walter
# @File    : 生成器01.py
# @License : (C)Copyright Walter
# @Desc    :
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
