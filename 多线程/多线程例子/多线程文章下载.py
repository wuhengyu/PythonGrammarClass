# -*- coding: utf-8 -*-
# Time    : 2023/3/4 22:44
# Author  : Walter
# File    : 多线程文章下载.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading

import requests
from bs4 import BeautifulSoup


def download_article(url):
    """
    从网站下载文章并保存在本地文件中
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', {'class': 'post-title'}).text.strip()
    content = soup.find('div', {'class': 'post-content'}).text.strip()

    with open(f"{title}.txt", "w") as f:
        f.write(content)


def main():
    """
    多线程下载文章
    """
    base_url = "https://www.luochen.com/page/"
    threads = []

    for i in range(1, 11):
        url = base_url + str(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_links = soup.find_all('a', {'class': 'post-item-title'})

        for link in article_links:
            article_url = link['href']
            thread = threading.Thread(target=download_article, args=(article_url,))
            threads.append(thread)

    # 启动所有线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有文章已下载完毕！")


if __name__ == '__main__':
    main()
