# -*- coding: utf-8 -*-
# Time    : 2023/3/17 23:51
# Author  : Walter
# File    : 线程池执行器2.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio
import concurrent.futures
import time

def blocking_io(n):
    print('Start blocking IO')
    time.sleep(n)
    print('Finish blocking IO')
    return 'Blocking IO result'


async def coroutine():
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        # 通过await关键字等待run_in_executor函数返回的Future对象，从而避免了阻塞事件循环
        result = await loop.run_in_executor(pool, blocking_io, 1)
    print(f'Result: {result}')


# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine())
asyncio.run(coroutine())
