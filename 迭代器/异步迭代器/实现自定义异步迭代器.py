# -*- coding: utf-8 -*-
# Time    : 2023/3/18 14:48
# Author  : Walter
# File    : 实现自定义异步迭代器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


class AsyncIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.index >= len(self.lst):
            raise StopAsyncIteration
        await asyncio.sleep(1)
        result = self.lst[self.index]
        self.index += 1
        return result


async def main():
    async for i in AsyncIterator([1, 2, 3, 4, 5]):
        print(i)


asyncio.run(main())
