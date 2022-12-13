import os
import time

print("转换正常格式时间")
a = os.path.getctime('E:\PycharmProjects\pythonProject\LuFeiPython\内置模块\os模块.py')
a = time.localtime(a)
print(time.strftime('%Y-%m-%d %H:%M:%S', a))
print(os.path.abspath(__file__))
os.path.dirname(os.path.abspath(__file__))
