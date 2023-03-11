# -*- coding: utf-8 -*-
# Time    : 2023/3/11 10:23
# Author  : Walter
# File    : demo2.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :


import asyncio

import aiohttp

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}

COOKIES = {
    'PHPSESSID': '1dafi928roo2es28ogfbkoeutu',
    'N_userLogin': '4e70b8ca2277313511c50d63263f88be%2Ce10adc3949ba59abbe56e057f20f883e%2C1649642175%2C2964444%2C14%2C112.0.52.63',
    'lookbook': '/book/8778/2026717.html',
    'N_BookCase': '8778,2026763|41718,15307986|103118,39712042|8633,1979716|26923,9587347|67587,25752670|103866,40041020|88170,33105054|100620,38263765|99134,37462768|101779,38653160|102745,39296257|94331,39158625|75303,28458311|25111,8958360',
}


async def fetch_html(session, url):
    async with session.get(url, headers=HEADERS, cookies=COOKIES) as response:
        return await response.text()


async def main():
    book_url = 'https://www.luochen.com/book/8778/2026717.html'
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, book_url)
        print(html)


if __name__ == '__main__':
    asyncio.run(main())
