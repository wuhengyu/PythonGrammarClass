# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 18:03
# @Author  : Walter
# @File    : TimeRunSum06.py
# @License : (C)Copyright Walter
# @Desc    :

# 需求 ：写个认证功能（输入账号密码，进行认证），当然账号密码是要从文件中取出。
def auth(func):
    def wrapper(*args, **kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        name = input('your name>>: ').strip()
        pwd = input('your password>>: ').strip()
        if name == 'root' and pwd == '123':
            res = func(*args, **kwargs)
            return res
        else:
            print('账号密码错误')

    return wrapper


@auth
def index(name):
    print('This name is %s' % name)


index('walter')
