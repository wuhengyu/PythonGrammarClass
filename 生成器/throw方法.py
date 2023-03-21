# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 15:04
# @Author  : Walter
# @File    : throw方法.py
# @License : (C)Copyright Walter
# @Desc    :

def my_generator():
    while True:
        try:
            x = yield
        except ValueError:
            print('Invalid value!')
        else:
            print('Received:', x)


g = my_generator()
next(g)  # 启动生成器
g.send('Hello')  # Received: Hello
g.throw(ValueError, '表示异常的参数（值）')  # Invalid value!
g.throw(ValueError)
g.send('World')  # Received: World
