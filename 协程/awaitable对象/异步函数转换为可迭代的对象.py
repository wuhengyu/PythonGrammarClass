# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:08
# Author  : Walter
# File    : 异步函数转换为可迭代的对象.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def async_func():
    await asyncio.sleep(1)
    return "Hello, World!"


async def main():
    # coro = async_func()
    # iterator = coro.__await__()
    # result = await iterator

    # 使用asyncio.create_task()或asyncio.ensure_future()将协程函数封装为任务对象，
    # 然后使用await 表达式对任务进行调度
    task = asyncio.create_task(async_func())
    result = await task
    print(result)


asyncio.run(main())
