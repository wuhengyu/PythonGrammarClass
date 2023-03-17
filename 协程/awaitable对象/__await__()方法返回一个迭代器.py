# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:58
# Author  : Walter
# File    : __await__()方法返回一个迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def async_func():
    await asyncio.sleep(1)
    return "Hello, World!"


async def main():
    coro = async_func()
    iterator = coro.__await__()

    print(iterator)
    # 使用 next() 函数获取迭代器中的值
    result = next(iterator)
    print(result)

    # 将迭代器转换为列表
    # print(type(iterator)) # 协程封装器
    # RuntimeError: await wasn't used with future
    # results = list(iterator)
    # print(results)


asyncio.run(main())
