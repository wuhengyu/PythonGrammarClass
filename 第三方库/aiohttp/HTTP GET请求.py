# -*- coding: utf-8 -*-
# Time    : 2023/3/11 14:36
# Author  : Walter
# File    : HTTP GET请求.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        # 暂停异步函数的执行，等待异步操作完成后再继续执行函数，避免了阻塞主线程的情况
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.example.com')
        print(html)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

asyncio.run(main())
