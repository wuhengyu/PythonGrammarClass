# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:42
# Author  : Walter
# File    : awaitable对象之协程函数返回迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import asyncio


async def async_func():
    await asyncio.sleep(1)
    return "Hello, World!"


task = asyncio.create_task(async_func())
result = await task
