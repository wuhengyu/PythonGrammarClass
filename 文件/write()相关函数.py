# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 17:38
# @Author  : Walter
# @File    : write()相关函数.py
# @License : (C)Copyright Walter
# @Desc    :

# with open('a.txt', 'r+', encoding="utf-8") as f:
#     print(f.write("写入一行新数据"))
#     print(f.writelines("写入一行新数据2"))
#     f.close()


# 写之前清空，不清空用a，a+，r+
h = open('a.txt', 'r', encoding="utf-8")
f = open('b.txt', 'w', encoding="utf-8")
# f.write("写入一行新数据")
# f.writelines(h.readlines())
# 将字符串列表写入文件中
f.writelines("写入一行新数据2")
f.close()
h.close()
