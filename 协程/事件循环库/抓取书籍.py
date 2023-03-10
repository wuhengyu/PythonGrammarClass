# -*- coding: utf-8 -*-
# Time    : 2023/3/11 1:04
# Author  : Walter
# File    : 抓取书籍.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio

import aiohttp
from bs4 import BeautifulSoup


async def fetch_html(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string.strip()
    content = soup.find('div', id='chaptercontent').get_text().strip()
    return title, content


async def fetch_chapter(session, base_url, chapter):
    url = f"{base_url}/chapter_{chapter}.html"
    html = await fetch_html(session, url)
    return await parse_html(html)


async def fetch_book(base_url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, base_url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.strip()
        chapters = [c.get('value') for c in soup.find_all('option')]

        tasks = []
        for chapter in chapters:
            task = asyncio.ensure_future(fetch_chapter(session, base_url, chapter))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        for i, result in enumerate(results):
            title, content = result
            with open(f"{title}.txt", 'w', encoding='utf-8') as f:
                f.write(f"Chapter {i + 1}: {title}\n\n{content}\n")


if __name__ == '__main__':
    base_url = 'https://www.luochen.com/book/41718/'
    asyncio.run(fetch_book(base_url))
