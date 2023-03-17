# -*- coding: utf-8 -*-
# Time    : 2023/3/17 19:00
# Author  : Walter
# File    : aiter方法.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
async def async_gen():
    for i in range(3):
        yield i


# async_iter = async_gen().__aiter__()

async def async_main():
    async for value in async_gen():
        print(value)


await async_main()
