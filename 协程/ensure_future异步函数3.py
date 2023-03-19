# -*- coding: utf-8 -*-
# Time    : 2023/3/18 19:28
# Author  : Walter
# File    : ensure_future异步函数3.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def coro():
    await asyncio.sleep(1)
    return 42


async def main():
    fut = asyncio.ensure_future(coro())
    # 使用asyncio.gather函数等待它的执行结果
    # asyncio.gather可以接受元组参数，接受多个协程函数
    result = await asyncio.gather(fut)
    # 返回列表
    print(result)

    # 或者

    # asyncio.ensure_future将coro函数转换为一个Future对象fut，并将fut提交给事件循环执行。
    # 然后，我们使用await关键字等待fut的执行结果。最后，我们使用asyncio.run来运行异步程序。
    await fut
    # 返回return实际值
    print(await fut)


asyncio.run(main())
