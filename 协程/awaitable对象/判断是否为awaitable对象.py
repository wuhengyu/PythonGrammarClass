# -*- coding: utf-8 -*-
# Time    : 2023/3/11 20:41
# Author  : Walter
# File    : 判断是否为awaitable对象.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio
import collections.abc
# Python 3.4及更高版本引入了一个名为tracemalloc的内置模块，可以用来跟踪和分析Python应用程序中的内存分配情况。
import tracemalloc


# 协程对象是 awaitable 对象的一种，因此这个判断结果是 True
async def coro():
    await asyncio.sleep(1)
    return 'hello'


# async def main():
# 在Python中，协程是异步执行的函数。当您调用一个协程时，它会返回一个协程对象，您需要将其包装在 asyncio 中的 await 语句中来等待协程执行完成。
#     result = await coro()
#     print(result)

# 启用tracemalloc，并开始跟踪内存分配
tracemalloc.start()

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# task = loop.create_task(coro())
# loop.run_until_complete(task)
# loop.close()

# 或者将协程对象传递给 asyncio.run() 的 main 参数，这将在内部使用 await 等待协程的完成
# asyncio.run(coro())

# 在 Python 3.10 中，asyncio.coroutines._CoroutineABC 已经被移除
# print(isinstance(coro(), asyncio.coroutines._CoroutineABC))  # True
print(isinstance(asyncio.run(coro()), collections.abc.Awaitable))

# 获取分配对象的堆栈跟踪
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
