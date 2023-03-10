# -*- coding: utf-8 -*-
# Time    : 2023/3/10 20:30
# Author  : Walter
# File    : 使用异步IO和协程实现并发爬取多个网页.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio

import aiohttp
import aiohttp_socks
from bs4 import BeautifulSoup


async def get_html(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string
        return title
    except Exception as e:
        print(f"Failed to parse HTML: {e}")
        return None


async def fetch_urls(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(get_html(session, url))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    return responses


async def main():
    urls = ['https://www.sogou.com', 'https://www.qidian.com', 'https://www.qq.com']
    proxy_url = 'http://192.168.31.162:10800'  # 设置代理
    # 从aiohttp3.7.0版本开始，ProxyConnector被标记为过时，推荐使用aiohttp_socks库来代替。
    conn = aiohttp_socks.ProxyConnector.from_url(proxy_url)
    async with aiohttp.ClientSession(connector=conn) as session:
        responses = await fetch_urls(session, urls)
        tasks = []
        for response in responses:
            task = asyncio.ensure_future(parse_html(response))
            tasks.append(task)
        titles = await asyncio.gather(*tasks)
        print(titles)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    # 或者

    # # 1.创建事件循环
    # loop = asyncio.new_event_loop()
    # # 2.设置为当前事件循环对象
    # asyncio.set_event_loop(loop)
    # # 3.创建了任务对象并添加到事件循环中
    # task = loop.create_task(main())
    # # 4.运行事件循环
    # loop.run_until_complete(task)
    # # 5.关闭事件循环对象
    # loop.close()

    # 或者
    asyncio.run(main())
