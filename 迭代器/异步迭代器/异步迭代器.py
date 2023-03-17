# -*- coding: utf-8 -*-
# Time    : 2023/3/17 19:23
# Author  : Walter
# File    : 异步迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import asyncio


# 异步生成器，它每秒产生一个新的值
async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


# 异步迭代器，它通过异步迭代 async_generator() 的值来打印每个元素。
async def async_iterator():
    async for i in async_generator():
        print(i)


asyncio.run(async_iterator())
