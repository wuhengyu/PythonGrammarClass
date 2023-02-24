# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 15:17
# @Author  : Walter
# @File    : 闭包.py
# @License : (C)Copyright Walter
# @Desc    :

# 在函数嵌套的条件下，内部函数引用了外部函数的变量，外部函数返回了内部函数的内存值
# 闭包的作用是在全局作用域中，实现间接对局部作用域的局部变量进行访问

# 有嵌套
def outer(a):
    # 局部变量
    b = 20
    def inner():
        # 有引用
        print(a)
        print(b)
    # 有返回
    return inner # 实际并没有执行，返回了内存地址


ou = outer(10)
# 返回inner的内存地址
print(ou)
# 加括号是调用
ou()