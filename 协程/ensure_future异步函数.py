# -*- coding: utf-8 -*-
# Time    : 2023/3/17 23:19
# Author  : Walter
# File    : ensure_future异步函数.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def coroutine():
    print('Coroutine')


async def main():
    # 使用asyncio.ensure_future函数将该协程对象包装成一个Future对象，并将其提交给事件循环执行。
    # 使用run_until_complete方法运行事件循环，等待协程完成。
    fut = asyncio.ensure_future(coroutine())
    await fut


asyncio.run(main())
