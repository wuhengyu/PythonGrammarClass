# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:17
# Author  : Walter
# File    : awaitable对象之异步函数返回迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import asyncio


async def async_func():
    await asyncio.sleep(1)
    return "Hello, World!"


# coro = async_func()
# iterator = coro.__await__()
# result = await iterator


def sync_func():
    coro = async_func()
    # 使用__await__()方法返回了一个迭代器
    iterator = coro.__await__()
    # 使用yield from 表达式可以等待异步操作完成并获取其返回值
    return (yield from iterator)


# 获取异步函数的返回值
sync_func()
