# -*- coding: utf-8 -*-
# @Time    : 2022/12/18 19:44
# @Author  : Walter
# @File    : eval()和exec()函数.py
# @License : (C)Copyright Walter
# @Desc    :

'''
eval和exec都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供
eval() 执行完要返回结果，而 exec() 执行完不返回结果

__builtins__ 是系统加入的内置 key
a 为执行语句生成的变量
作用域字典
'''

# 参数 globals 作用域
dic = {}  # 定义一个字典
dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
print(dic.keys())  # exec 后，dic 的 key 多了一个

# 参数locals
a = 10
b = 20
c = 30
g = {'a': 6, 'b': 8}  # 定义一个字典
t = {'b': 100, 'c': 10}  # 定义一个字典
print(eval('a+b+c', g, t))  # 定义一个字典 116
print(eval('a+b+c'))
print(eval('b', g, t))
