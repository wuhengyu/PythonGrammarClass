# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 19:38
# @Author  : Walter
# @File    : 有参装饰器应用1.py
# @License : (C)Copyright Walter
# @Desc    :

# 有参装饰器实时模版
# def g_outer(params):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return outer

def auth(func):
    def wrapper(*args, **kwargs):
        name = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        print("基于file此类验证")
        if name == "admin" and password == "123":
            print("登录成功，欢迎回来！")
            res = func(*args, **kwargs)
            return res
        else:
            print("登录失败，请重试！")
    return wrapper

@auth
def home(): # 文件
    print("欢迎来到我的主页！")
home()

@auth
def index(): # 数据库
    print("welcome to index page")
index()