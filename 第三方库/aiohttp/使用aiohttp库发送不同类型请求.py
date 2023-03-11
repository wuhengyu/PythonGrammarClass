# -*- coding: utf-8 -*-
# Time    : 2023/3/11 14:47
# Author  : Walter
# File    : 使用aiohttp库发送不同类型请求.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio

import aiohttp


async def fetch(session, method, url, params=None, headers=None, data=None, json=None, cookies=None, timeout=None,
                allow_redirects=True, auth=None, ssl=None):
    async with session.request(method=method, url=url, params=params, headers=headers, data=data, json=json,
                               cookies=cookies, timeout=timeout, allow_redirects=allow_redirects, auth=auth,
                               ssl=ssl) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        # GET请求
        html = await fetch(session, 'GET', 'http://httpbin.org/basic-auth/', params={'key': 'value'},
                           headers={'User-Agent': 'Mozilla/5.0'}, cookies={'name': 'value'}, timeout=5,
                           allow_redirects=False,
                           auth=aiohttp.BasicAuth('username', 'password'))
        print(html)

        # POST请求
        data = {'key1': 'value1', 'key2': 'value2'}
        html = await fetch(session, 'POST', 'http://httpbin.org/post',
                           headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data)
        print(html)

        # PUT请求
        json_data = {'key': 'value'}
        html = await fetch(session, 'PUT', 'http://httpbin.org/put', headers={'Content-Type': 'application/json'},
                           json=json_data)
        print(html)

        # DELETE请求
        html = await fetch(session, 'DELETE', 'http://httpbin.org/delete')
        print(html)


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
