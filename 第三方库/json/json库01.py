# -*- coding: utf-8 -*-
# Time    : 2023/2/24 12:54
# Author  : Walter
# File    : json库01.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import json

# 变量从内存中变成可存储或传输的过程称之为序列化
# 序列化是将对象状态转化为可保存或可传输格式的过程。
# 变量内容从序列化的对象重新读到内存里称之为反序列化
# 反序列化是流转换为对象。

# load和loads方法是把其他类型的对象转为Python对象
# Python基本数据类型，列表，元组，字典，自己定义的类等等，不包括Python的字符串类型
# loads操作的是字符串
# load操作的是文件流
# load 和 loads 都实现反序列化
# load 和 loads除了第一个参数（要转换的对象）类型不同，其他所有的参数都相同，最终都是转换成Python对象
# loads和load两个方法只是处理的数据源不同，其他的参数都是相同的，返回的结果类型也相同

with open("json_data.txt", 'r', encoding='utf-8') as file:
    res = file.read()
    # 读取json数据为字符串
    print(type(res))

    # 字符串转换为字典类型，转换python对象
    res = json.loads(res)
    print(type(res))

    # 字典类型转换为字符串
    res = json.dumps(res)
    print(type(res))

    print(res)

with open("json_data.txt", 'r', encoding='utf-8') as file:
    # 读取json数据为字典类型，转换python对象
    res = json.load(file)
    print(type(res))
    print(res)

# json的loads方法不仅可以把字符串转为字典，还可以转为任何Python对象，但是不能把转为字符串。
print('json.loads 将整数类型的字符串转为int类型: type(json.loads("123456"))) --> {}'.format(type(json.loads("123456"))))
print('json.loads 将浮点类型的字符串转为float类型: type(json.loads("123.456")) --> {}'.format(
    type(json.loads("123.456"))))
print(
    'json.loads 将boolean类型的字符串转为bool类型: type(json.loads("true")) --> {}'.format((type(json.loads("true")))))
print('json.loads 将列表类型的字符串转为列表: type(json.loads(\'["a", "b", "c"]\')) --> {}'.format(
    type(json.loads('["a", "b", "c"]'))))
print(
    'json.loads 将字典类型的字符串转为字典: type(json.loads(\'{"a": 1, "b": 1.2, "c": true, "d": "ddd"}\')) --> %s' % str(
        type(json.loads('{"a": 1, "b": 1.2, "c": true, "d": "ddd"}'))))

# json.dumps()用于将python对象转换为json字符串，返回转换后的json字符串
# 将python对象转换为json字符串
persons = [
    {
        'username': "zhaoji",
        "age": "18",
        "country": "China"
    },
    {
        "username": "cyj",
        "age": "18",
        "country": "China"
    }
]
# 调用dumps方法转换python对象
json_str = json.dumps(persons)
# 打印转换后的json字符串的数据类型
print(type(json_str))
# 打印转换后的json字符串
print(json_str)

# son.dump()用于将python对象转换为字符串并且写入文件
# 将python对象转换为json字符串
persons = [
    {
        'username': "zhaoji",
        "age": "18",
        "country": "China"
    },
    {
        "username": "cyj",
        "age": "18",
        "country": "China"
    }
]
with open("json_dump.json", "w") as fp:
    json.dump(persons, fp)

# 方法	作用
# json.dumps()	将python对象编码成Json字符串
# json.loads()	将Json字符串解码成python对象
# json.dump()	将python中的对象转化成json储存到文件中
# json.load()	将文件中的json的格式转化成python对象提取


# json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
# allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)

# obj:转化成json的对象。
# sort_keys =True:是告诉编码器按照字典排序(a到z)输出。如果是字典类型的python对象，就把关键字按照字典排序。
# indent:参数根据数据格式缩进显示，读起来更加清晰。
# separators:是分隔符的意思，参数意思分别为不同dict项之间的分隔符和dict项内key和value之间的分隔符，把：和，后面的空格都除去了。
