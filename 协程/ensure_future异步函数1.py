# -*- coding: utf-8 -*-
# Time    : 2023/3/17 23:27
# Author  : Walter
# File    : ensure_future异步函数1.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def coroutine1():
    await asyncio.sleep(1)
    return 1


async def coroutine2():
    await asyncio.sleep(2)
    return 2


async def main():
    tasks = []
    # 通过asyncio.ensure_future创建的Future对象实际上也是Task对象的实例。
    task1 = asyncio.ensure_future(coroutine1())
    task2 = asyncio.ensure_future(coroutine2())
    tasks.append(task1)
    tasks.append(task2)
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
