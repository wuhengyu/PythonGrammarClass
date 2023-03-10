# -*- coding: utf-8 -*-
# Time    : 2023/3/10 19:38
# Author  : Walter
# File    : asyncio显式创建事件循环对象.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# 提示 Warning：DeprecationWarning: There is no current event loop
# loop = asyncio.get_event_loop()

# 第一种解决办法：显式创建事件循环对象
# 显式创建事件循环对象
loop = asyncio.new_event_loop()
# 设置为当前事件循环对象
asyncio.set_event_loop(loop)
# 创建了任务对象并添加到事件循环中
task = loop.create_task(hello())
# 运行事件循环
loop.run_until_complete(task)
# 关闭事件循环
loop.close()
