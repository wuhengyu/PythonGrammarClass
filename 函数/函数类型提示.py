# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 20:02
# @Author  : Walter
# @File    : 函数类型提示.py
# @License : (C)Copyright Walter
# @Desc    :

# python是一门解释型的强类型编程语言
# 1、编译型or解释型
# 2、强类型or弱类型
# 强类型：数据类型一经指定，不可忽略。弱类型：数据类型可以忽略
# 3、动态型or静态型
# 动态型：定义的时候就不规定是什么类型的数据类型，赋值完成后在会确定数据类型
# 静态型：定义的时候就规定是什么类型的数据类型

# 行参类型动态型
# def func(name, age):
#     print(name)
#     print(age)
#     return 10
#
# func(3.14, [1, 2, 3])

# 函数的参数类型提示(3.5后)，没有强制
def func(name: str, age: int, nums: int=88) -> int:
    print(name)
    print(age)
    print(nums)
    return 10

# func(3.14, [1, 2, 3])
func('张三', 11)
# 查看函数的提示参数类型信息
print(func.__annotations__)
