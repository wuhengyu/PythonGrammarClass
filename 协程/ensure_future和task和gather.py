# -*- coding: utf-8 -*-
# Time    : 2023/3/17 23:40
# Author  : Walter
# File    : ensure_future和task和gather.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def coroutine1():
    print('Coroutine 1')
    await asyncio.sleep(1)
    return 1


async def coroutine2():
    print('Coroutine 2')
    await asyncio.sleep(2)
    return 2


async def main():
    task1 = asyncio.ensure_future(coroutine1())
    task2 = asyncio.ensure_future(coroutine2())
    results = await asyncio.gather(task1, task2)
    print(results)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
asyncio.run(main())
