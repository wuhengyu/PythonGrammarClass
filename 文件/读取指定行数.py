# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 17:48
# @Author  : Walter
# @File    : 读取指定行数.py
# @License : (C)Copyright Walter
# @Desc    :

# with open('test02.txt', 'w+', encoding='utf-8') as f:
#     for x in range(101):
#         f.write(str(x)+'\n')


with open('test02.txt', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'第100行的内容为：{lines[100]}')


# with open('test02.txt', encoding='utf-8') as f:
#     for lineno, line in enumerate(f):
#         if lineno == 100:
#             print(f'第100行的内容为：{line}')

import linecache
text = linecache.getline('test02.txt', 101)
print(f'第100行的内容为：{text}')

# for循环
# for line in open('test02.txt', encoding='utf-8'):
#     print(line)

# 使用fileinput模块
# import fileinput
# for line in fileinput.input("test02.txt"):
#     print(line)


# 一次性读取多行，可以提升读取速度，但内存使用稍大， 可根据情况调整一次读取的行数
# f = open('test02.txt', encoding='utf-8')
# while 1:
#     lines = f.readlines(10000)
#     if not lines:
#         break
#     # for line in lines:
#     #     print(line)
#     print(lines[100])
# f.close()


# readline函数
# 优点：节省内存，不需要一次性把文件内容放入内存中
# 缺点：速度相对较慢
# f = open('test02.txt', encoding='utf-8')
# line = f.readline()
# while line:
#     print(line, end='')
#     line = f.readline()
# f.close()