# -*- coding: utf-8 -*-
# Time    : 2023/3/17 22:42
# Author  : Walter
# File    : gather异步函数.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    : 用于等待多个协程并发执行，并在所有协程完成时返回它们的结果

import asyncio


async def coroutine1():
    await asyncio.sleep(1)
    return 1


async def coroutine2():
    await asyncio.sleep(2)
    return 2


async def main():
    # results = await asyncio.gather(coroutine1(), coroutine2())

    # 或者create_task，创建task
    task = []
    task.append(asyncio.create_task(coroutine1()))
    task.append(asyncio.create_task(coroutine2()))
    # 用于等待多个协程并发执行，并在所有协程完成时返回它们的结果
    # *tasks是一个可变参数，表示一个或多个协程对象，可以使用它们来并发执行多个任务。
    results = await asyncio.gather(*task)
    print(results)

    # 或者ensure_future，创建task实例
    # tasks = []
    # task1 = asyncio.ensure_future(coroutine1())
    # task2 = asyncio.ensure_future(coroutine2())
    # tasks.append(task1)
    # tasks.append(task2)
    # results = await asyncio.gather(*tasks)
    # print(results)


asyncio.run(main())
