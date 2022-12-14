# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 0:40
# @Author  : Walter
# @File    : 遍历100次网站.py
# @License : (C)Copyright Walter
# @Desc    :
import logging
import time

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
TOTAL_NUMBER = 100
URL = 'https://www.httpbin.org/delay/5'
start_time = time.time()
for _ in range(1, TOTAL_NUMBER + 1):
    logging.info('scraping %s', URL)
    response = requests.get(URL)
end_time = time.time()
logging.info('total time %s seconds', end_time - start_time)
