# -*- coding: utf-8 -*-
# Time    : 2023/3/4 22:48
# Author  : Walter
# File    : 获取书籍名称和链接.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import threading

import requests
from bs4 import BeautifulSoup


# 获取所有书籍名称和链接
def get_books():
    url = 'https://www.luochen.com/book/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = []
    print(soup.find_all('div', class_='book-name'))
    for book in soup.find_all('div', class_='book-name'):
        name = book.text
        # link = book.find('a')['href']
        books.append((name))
    print(books)
    return books


# 爬取书籍信息的线程
class CrawlerThread(threading.Thread):
    def __init__(self, book, save_lock, file_obj):
        super().__init__()
        self.book = book
        self.save_lock = save_lock
        self.file_obj = file_obj

    def run(self):
        url = self.book[1]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find('div', class_='book-intro').text.strip()
        with self.save_lock:
            self.file_obj.write(f"{self.book[0]}\n{url}\n{description}\n\n")


if __name__ == '__main__':
    books = get_books()

    # 创建一个线程锁，用于多线程写入文件
    save_lock = threading.Lock()
    with open('books.txt', 'w', encoding='utf-8') as f:
        threads = []
        for book in books:
            thread = CrawlerThread(book, save_lock, f)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
