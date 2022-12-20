# -*- coding: utf-8 -*-
# @Time    : 2022/12/19 18:27
# @Author  : Walter
# @File    : 基于生成器的上下文管理器.py
# @License : (C)Copyright Walter
# @Desc    :

from contextlib import contextmanager


# 基于类的上下文管理器和基于生成器的上下文管理器，这两者在功能上是一致的
@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


with file_manager('a.txt', 'a') as f:
    f.write('hello world\n')
