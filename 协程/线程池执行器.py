# -*- coding: utf-8 -*-
# Time    : 2023/3/17 22:49
# Author  : Walter
# File    : 线程池执行器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio
import concurrent.futures


def my_sync_function(x):
    return x ** 2


async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        loop = asyncio.get_event_loop()
        tasks = []
        for i in range(3):
            tasks.append(loop.run_in_executor(executor, my_sync_function, i))
        results = await asyncio.gather(*tasks)
        print(results)


asyncio.run(main())
