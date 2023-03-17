# -*- coding: utf-8 -*-
# Time    : 2023/3/17 20:50
# Author  : Walter
# File    : await关键字.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
import asyncio


async def my_async_function():
    print('Start my_async_function')
    await asyncio.sleep(1)
    print('Finish my_async_function')


async def main():
    print('Start main')
    await my_async_function()
    print('Finish main')


asyncio.run(main())
