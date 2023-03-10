# -*- coding: utf-8 -*-
# Time    : 2023/3/11 1:42
# Author  : Walter
# File    : demo.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import requests
from bs4 import BeautifulSoup


def get_book_content(url):
    # 发送 HTTP GET 请求获取 HTML 内容
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    # 解析 HTML 内容，提取书籍正文部分
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', {'class': 'main-body-box'}).get_text()

    # 进一步处理，去除 HTML 标签和其他无用信息
    content = content.replace('\n', '')
    content = content.replace('\r', '')
    content = content.replace('    ', '\n')
    content = content.replace('     ', '\n')
    content = content.strip()

    # 返回提取的书籍正文内容
    return content


if __name__ == '__main__':
    url = 'https://www.luochen.com/book/8778/2026682.html'
    content = get_book_content(url)
    print(content)
