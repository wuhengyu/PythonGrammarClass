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
    result = await iterator.__anext__()
    print(result)


asyncio.run(main())
