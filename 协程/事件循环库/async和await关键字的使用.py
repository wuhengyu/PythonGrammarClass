# -*- coding: utf-8 -*-
# Time    : 2023/3/10 20:15
# Author  : Walter
# File    : async和await关键字的使用.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    : 两个协程函数：do_something() 和 main()

import asyncio


async def do_something():
    print('Start doing something...')
    await asyncio.sleep(1)  # 模拟一个异步操作，暂停协程1秒钟
    print('Finish doing something!')


async def main():
    print('Start main function...')
    await do_something()  # 等待 do_something() 协程执行完成
    print('Finish main function!')


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())  # 运行 main() 协程

# 或者

# 1.创建事件循环
loop = asyncio.new_event_loop()
# 2.设置为当前事件循环对象
asyncio.set_event_loop(loop)
# 3.创建了任务对象并添加到事件循环中
task = loop.create_task(main())
# 4.运行事件循环
loop.run_until_complete(task)
# 5.关闭事件循环对象
loop.close()

# 或者

# asyncio.run(main())
