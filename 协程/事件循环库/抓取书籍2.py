# -*- coding: utf-8 -*-
# Time    : 2023/3/11 1:10
# Author  : Walter
# File    : 抓取书籍2.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio

import aiofiles
import aiohttp
from bs4 import BeautifulSoup


async def fetch_html(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string.strip()
    return title


async def fetch_chapter(session, url):
    async with session.get(url) as response:
        return await response.text()


async def save_to_file(file_name, content):
    async with aiofiles.open(file_name, 'a', encoding='utf-8') as f:
        await f.write(content)


async def main():
    book_url = 'https://www.luochen.com/book/8778/chapter.html'
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, book_url)
        book_title = await parse_html(html)
        print(f"开始抓取<<{book_title}>>...")
        chapter_urls = []
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', class_='link-chapter-catalogue clearfix'):
            chapter_urls.append(a_tag['href'])
        tasks = []
        for url in chapter_urls:
            url = "https://www.luochen.com/" + url
            task = asyncio.ensure_future(fetch_chapter(session, url))
            tasks.append(task)
        chapters = await asyncio.gather(*tasks)
        for i, chapter in enumerate(chapters):
            chapter_title = await parse_html(chapter)
            content = f"{chapter_title}\n\n{chapter}\n\n"

            soup = BeautifulSoup(content, 'html.parser')
            text = ''.join(soup.find('div', {'class': 'main-body-box'}).get_text())
            content = text.strip().replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', '')

            file_name = f"{i + 1}_{chapter_title}.txt"
            await save_to_file(file_name, content)
            print(f"{file_name} 已保存")
        print("全部抓取完毕！")


if __name__ == '__main__':
    asyncio.run(main())
