# -*- coding: utf-8 -*-
# Time    : 2023/3/11 21:48
# Author  : Walter
# File    : await等待Future对象返回的结果.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio


# 在事件循环中调度一个定时器，让其在 1 秒后设置一个 Future 对象的结果值为 'hello'。
# 具体来说，它会调用 asyncio.get_event_loop() 获取当前的事件循环对象，
# 然后调用它的 call_later(delay, callback, *args) 方法，传递一个延迟时间 delay 和一个回调函数 callback，以及一些参数 args。
# 在这个例子中，延迟时间是 1 秒，回调函数是 fut.set_result，它将 Future 对象的结果值设置为 'hello'。
async def coro():
    fut = asyncio.Future()
    asyncio.get_event_loop().call_later(1, fut.set_result, 'hello')
    result = await fut
    print(result)
    return result


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task = loop.create_task(coro())
loop.run_until_complete(task)
loop.close()
