# -*- coding: utf-8 -*-
# Time    : 2023/3/18 0:11
# Author  : Walter
# File    : run_in_executor函数.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio
import concurrent.futures
import time


def blocking_function(seconds):
    print(f"Starting blocking function for {seconds} seconds")
    time.sleep(seconds)
    print("Blocking function completed")


async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        # asyncio.get_running_loop().run_in_executor(executor, func, *args)
        # executor参数指定了用于执行阻塞函数的线程池或进程池
        # func参数是要执行的阻塞函数
        # *args参数是传递给阻塞函数的参数
        await loop.run_in_executor(pool, blocking_function, 2)
        # 通过await关键字等待run_in_executor函数返回的Future对象，从而避免了阻塞事件循环。
        await loop.run_in_executor(pool, blocking_function, 3)


asyncio.run(main())
