# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 23:01
# @Author  : Walter
# @File    : 有参装饰器应用2.py
# @License : (C)Copyright Walter
# @Desc    :

def auth(sources):
    def outer(func):
        def wrapper(*args, **kwargs):
            name = input("请输入用户名：").strip()
            password = input("请输入密码：").strip()
            if sources == "file":
                print("基于file此类验证")
                # with open('test.txt', 'r', encoding='utf-8') as f:
                #     response = f.readlines()
                #     name = response[1].split(',')[0]
                #     password = response[1].split(',')[1]
                if name == "admin" and password == "123":
                    print("登录成功，欢迎回来！")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("登录失败，请重试！")
            elif sources == "mysql":
                print("基于mysql此类验证")
            elif sources == "ldap":
                print("基于ldap此类验证")
            else:
                print("不支持此类验证")
        return wrapper
    return outer

@auth("file")
def home(): # 文件
    print("欢迎来到我的主页！")
home()

@auth("mysql")
def index(): # 数据库
    print("welcome to index page")
index()

@auth("ldap")
def defalut(): # LDAP
    print("this is a index page")
defalut()