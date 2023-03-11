# -*- coding: utf-8 -*-
# Time    : 2023/3/11 1:52
# Author  : Walter
# File    : 抓取书籍3.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import asyncio
import os

import aiofiles
import aiohttp
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.182 Safari/537.36'
}

COOKIES = {
    'PHPSESSID': '1dafi928roo2es28ogfbkoeutu',
    'N_userLogin': '4e70b8ca2277313511c50d63263f88be%2Ce10adc3949ba59abbe56e057f20f883e%2C1649642175%2C2964444%2C14'
                   '%2C112.0.52.63',
    'lookbook': '/book/8778/2026717.html',
    'N_BookCase': '8778,2026763|41718,15307986|103118,39712042|8633,1979716|26923,9587347|67587,25752670|103866,'
                  '40041020|88170,33105054|100620,38263765|99134,37462768|101779,38653160|102745,39296257|94331,'
                  '39158625|75303,28458311|25111,8958360',
}


async def fetch_html(session, url):
    async with session.get(url, headers=HEADERS, cookies=COOKIES) as response:
        return await response.text()


async def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string.strip()
    return title


async def fetch_chapter(session, url):
    async with session.get(url, headers=HEADERS, cookies=COOKIES) as response:
        return await response.text()


async def save_to_file(file_name, content):
    async with aiofiles.open(file_name, 'w', encoding='utf-8') as f:
        await f.write(content)


async def parse_chapter_content(chapter):
    soup = BeautifulSoup(chapter, 'html.parser')
    chapter_title = soup.title.string.strip()
    chapter_content = soup.find('div', {'class': 'main-body-box'}).get_text().strip().replace('\n', '').replace('\r',
                                                                                                                '').replace(
        '\t', '').replace('\xa0', '')
    return chapter_title, chapter_content


async def main():
    book_url = 'https://www.luochen.com/book/8778/chapter.html'
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, book_url)
        book_title = await parse_html(html)
        print(f"开始抓取<<{book_title}>>...")
        chapter_urls = []
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', class_='link-chapter-catalogue clearfix'):
            chapter_urls.append("https://www.luochen.com" + a_tag['href'])
        tasks = []
        for url in chapter_urls:
            task = asyncio.ensure_future(fetch_chapter(session, url))
            tasks.append(task)
        chapters = await asyncio.gather(*tasks)

        folder_name = book_title.replace('/', ' ')  # 防止书名中的'/'对文件名的影响
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        for i, chapter in enumerate(chapters):
            try:
                chapter_title, chapter_content = await parse_chapter_content(chapter)
                file_name = os.path.join(folder_name, f"{i + 1}_{chapter_title}.txt")
                await save_to_file(file_name, chapter_content)
                print(f"{file_name} 已保存")
            except Exception as e:
                print(f"第{i + 1}章保存出错：{e}")
        print("全部抓取完毕！")


if __name__ == '__main__':
    asyncio.run(main())
