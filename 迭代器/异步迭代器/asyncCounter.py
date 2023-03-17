# -*- coding: utf-8 -*-
# Time    : 2023/3/17 19:20
# Author  : Walter
# File    : asyncCounter.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current - 1
        else:
            raise StopAsyncIteration


async def main():
    async for i in AsyncCounter(5):
        print(i)


asyncio.run(main())
