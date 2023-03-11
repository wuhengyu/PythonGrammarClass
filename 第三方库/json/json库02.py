# -*- coding: utf-8 -*-
# Time    : 2023/2/24 13:16
# Author  : Walter
# File    : json库02.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import json

# json和字典
# json=》dict使用load
# dict=》json使用dump

# 字符串和字典
# dict=》string使用dumps
# string=》dict使用loads

# load 和 loads （反序列化）
# load:
# load：针对文件句柄，将json格式的字符转换为dict，从文件中读取 (将string转换为dict)
print("-" * 20 + "load" + "-" * 20)
a_json = json.load(open('json_data.txt', 'r', encoding='utf-8'))
a_json2 = json.load(open('json_data.json', 'r', encoding='utf-8'))
# <class 'dict'>,转换python对象,反序列化
print(type(a_json))
print(a_json)
print(type(a_json2))
print(a_json2)

# loads:
# loads：针对内存对象，将string转换为dict (将string转换为dict)
print("-" * 20 + "loads" + "-" * 20)
b_json = json.loads('{"aaa": 111, "bbb": 222}')
# <class 'dict'>,转换python对象,反序列化
print(type(b_json))
print(b_json)

# dump 和 dumps（序列化）
# dump:
# dump：将dict类型转换为json字符串格式，写入到文件 （易存储）
print("-" * 20 + "dump" + "-" * 20)
a_dict = {'a': '1111', 'b': '2222'}
# dump写入
c_json = json.dump(a_dict, open('json_data.json', 'w'))

# dumps:
# dumps：将dict转换为string (易传输)
print("-" * 20 + "dumps" + "-" * 20)
a_dict = {'a': '1111', 'b': '2222'}
a_str = json.dumps(a_dict)
print(type(a_str))
print(a_str)

# 根据序列化和反序列的特性
#
# loads： 是将string转换为dict
# dumps： 是将dict转换为string
# load： 是将里json格式字符串转化为dict，读取文件
# dump： 是将dict类型转换为json格式字符串，存入文件


# Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢。
#
# 变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
