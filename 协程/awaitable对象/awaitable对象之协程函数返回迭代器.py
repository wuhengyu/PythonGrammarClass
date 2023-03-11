# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:42
# Author  : Walter
# File    : awaitable对象之协程函数返回迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

async def coro_func():
    yield "Hello, "
    yield "World!"


coro = coro_func()
iterator = coro.__await__()
result = await iterator.__anext__() + await iterator.__anext__()
