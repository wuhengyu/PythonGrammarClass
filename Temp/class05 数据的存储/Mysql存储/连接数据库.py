# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 23:56
# @Author  : Walter
# @File    : 连接数据库.py
# @License : (C)Copyright Walter
# @Desc    :
import pymysql

db = pymysql.connect(host='192.168.81.184', user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print(data)
db.close()
