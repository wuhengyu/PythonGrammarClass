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

    # 使用 next() 函数获取迭代器中的值
    result = next(iterator)
    print(result)

    # 将迭代器转换为列表
    results = list(iterator)
    print(results)


asyncio.run(main())

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# task = loop.create_task(async_func())
# loop.run_until_complete(task)
# iterator = task.__await__()
# print(iterator.__next__())
