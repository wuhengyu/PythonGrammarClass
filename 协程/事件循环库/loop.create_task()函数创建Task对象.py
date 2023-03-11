# -*- coding: utf-8 -*-
# Time    : 2023/3/11 20:03
# Author  : Walter
# File    : loop.create_task()函数创建Task对象.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :


# Python 代码能够利用异步 I/O 技术更高效地处理 I/O 密集型任务
import asyncio


# 下面是使用 `loop.create_task()` 函数创建 `Task` 对象的例子：
async def coro():
    await asyncio.sleep(1)
    return 'hello'


# 使用 loop.create_task() 函数创建了 5 个 Task 对象，并将它们添加到任务列表 tasks 中
async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(coro())
        tasks.append(task)
    # 使用 asyncio.gather() 函数并发执行所有任务，并将返回结果保存在变量 results 中
    results = await asyncio.gather(*tasks)
    print(results)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

asyncio.run(main())
