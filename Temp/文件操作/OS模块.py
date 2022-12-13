import os

# path()模块
ospath = os.getcwd() + '\\OS模块.py'
print(ospath)

print('返回绝对路径')
print(os.path.abspath(ospath))  # E:\PycharmProjects\pythonProject\pythonProject\文件操作OS模块.py

print('获取文件路径')
print(os.path.dirname(os.path.abspath(ospath)))  # E:\PycharmProjects\pythonProject\pythonProject
print(os.path.dirname(ospath))
print(os.path.dirname(__file__))

print('返回文件名')
print(os.path.basename(os.path.abspath(ospath)))  # E:\PycharmProjects\pythonProject\pythonProject

print(os.path.split(ospath))
