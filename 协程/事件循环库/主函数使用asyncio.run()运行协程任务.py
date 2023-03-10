# -*- coding: utf-8 -*-
# Time    : 2023/3/10 20:10
# Author  : Walter
# File    : 主函数使用asyncio.run()运行协程任务.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


# 协程函数，可以被异步执行
# async 是 Python 3.5 及以上版本中引入的一个关键字，用于声明一个协程函数
# 使用 async 关键字修饰的函数体可以包含 await 表达式，用于挂起协程的执行，等待异步操作的完成
async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# 无需显式创建事件循环对象，asyncio.run() 函数会自动创建一个事件循环对象，并在其中执行协程任务
# 这种方法只适用于 Python 3.7 及以上版本
asyncio.run(hello())  # 在主函数中使用 asyncio.run() 来运行协程任务
