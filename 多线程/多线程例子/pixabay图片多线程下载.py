# -*- coding: utf-8 -*-
# Time    : 2023/3/5 18:10
# Author  : Walter
# File    : pixabay图片多线程下载.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import os
import threading

import requests


class DownloadThread(threading.Thread):
    def __init__(self, url, save_path):
        # 调用父类的__init__()方法进行初始化
        # 继承自父类的子类可以通过调用父类的__init__()方法来获得父类的属性和方法，以确保线程能够正确地启动和运行
        super().__init__()
        self.url = url
        self.save_path = save_path

    def run(self):
        print(f"Downloading {self.url} to {self.save_path}")
        response = requests.get(self.url)
        with open(self.save_path, "wb") as f:
            f.write(response.content)


if __name__ == '__main__':
    urls = [
        "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg",
        "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492__340.jpg",
        "https://cdn.pixabay.com/photo/2014/06/03/19/38/camera-361478__340.jpg",
        "https://cdn.pixabay.com/photo/2017/09/18/16/03/book-2769658__340.jpg",
        "https://cdn.pixabay.com/photo/2018/01/04/19/43/kitty-3069569__340.jpg",
        "https://cdn.pixabay.com/photo/2015/09/02/13/24/girl-919048__340.jpg",
        "https://cdn.pixabay.com/photo/2017/05/02/15/54/alpaca-2272829__340.jpg",
        "https://cdn.pixabay.com/photo/2016/01/19/17/41/dog-1149963__340.jpg",
        "https://cdn.pixabay.com/photo/2015/03/26/09/54/graffiti-690572__340.jpg",
        "https://cdn.pixabay.com/photo/2017/05/13/21/08/clouds-2314900__340.jpg"
    ]

    # Create the save directory if it doesn't exist
    save_dir = "./downloads"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    threads = []
    for url in urls:
        file_name = url.split("/")[-1]
        save_path = os.path.join(save_dir, file_name)
        thread = DownloadThread(url, save_path)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All downloads completed.")
