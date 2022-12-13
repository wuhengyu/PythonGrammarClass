# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 14:53
# @Author  : Walter
# @File    : 手动迭代.py
# @License : (C)Copyright Walter
# @Desc    :
def manual_iter1():
    with open('./etc/passwd.txt', encoding='utf-8') as f:
        try:
            while True:
                line = next(f)
                print(line, end=" ")
        except StopIteration:
            pass


def manual_iter2():
    with open('./etc/passwd.txt', encoding='utf-8') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


manual_iter1()
print('-' * 50)
manual_iter2()
