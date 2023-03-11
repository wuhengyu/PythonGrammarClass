# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:42
# Author  : Walter
# File    : awaitable对象之协程函数返回迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import asyncio


async def async_func():
    fut = asyncio.Future()
    asyncio.get_event_loop().call_later(1, fut.set_result, 'hello')
    result = await fut
    return result


coro = async_func()
iterator = coro.__await__()
result = await iterator
