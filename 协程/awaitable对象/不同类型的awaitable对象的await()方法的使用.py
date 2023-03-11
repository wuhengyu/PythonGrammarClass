# -*- coding: utf-8 -*-
# Time    : 2023/3/11 22:00
# Author  : Walter
# File    : 不同类型的awaitable对象的await()方法的使用.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def coro():
    print('coro before sleep')
    await asyncio.sleep(1)
    print('coro after sleep')
    return 'coro'


async def agen():
    print('agen before yield')
    await asyncio.sleep(1)
    yield 'agen'
    print('agen after yield')


class MyAwaitable:
    def __await__(self):
        yield 'MyAwaitable'


# 报错代码
# TypeError: Passing coroutines is forbidden, use tasks explicitly.
# 禁止传递协程，显式使用任务。
# sys:1: RuntimeWarning: coroutine 'coro' was never awaited
# 运行时警告：从未等待协程“coro”

# async def main():
#     fut = asyncio.Future()
#     awaitables = [
#         coro(),
#         agen().__anext__(),
#         MyAwaitable(),
#         fut
#     ]
#     done, pending = await asyncio.wait(awaitables, timeout=2)
#     for task in done:
#         print(task.result())

async def main():
    tasks = [asyncio.create_task(coro()) for _ in range(10)]
    done, pending = await asyncio.wait(tasks, timeout=2)
    for task in done:
        print(task.result())


asyncio.run(main())
