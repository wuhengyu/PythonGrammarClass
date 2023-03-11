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

    # 使用 await 等待协程完成并获取结果
    result = await coro
    print(result)

    # 使用 await 等待迭代器中的下一个元素并获取结果
    result = await iterator.__anext__()
    print(result)

    # 将迭代器转换为列表
    results = [value async for value in iterator]
    print(results)


asyncio.run(main())
