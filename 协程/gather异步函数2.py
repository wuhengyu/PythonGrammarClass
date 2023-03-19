# -*- coding: utf-8 -*-
# Time    : 2023/3/19 22:05
# Author  : Walter
# File    : gather异步函数2.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def coroutine1():
    print('coroutine1 start')
    await asyncio.sleep(1)
    print('coroutine1 end')


async def coroutine2():
    print('coroutine2 start')
    await asyncio.sleep(2)
    print('coroutine2 end')


async def coroutine3():
    print('coroutine3 start')
    await asyncio.sleep(3)
    print('coroutine3 end')


async def main():
    print('main start')
    await asyncio.gather(coroutine1(), coroutine2(), coroutine3())
    print('main end')


if __name__ == '__main__':
    asyncio.run(main())
