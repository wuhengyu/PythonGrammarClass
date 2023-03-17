# -*- coding: utf-8 -*-
# Time    : 2023/3/17 19:06
# Author  : Walter
# File    : async for迭代异步生成器.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

async def async_gen():
    for i in range(3):
        yield i


async def async_main():
    async for value in async_gen():
        print(value)


await async_main()
