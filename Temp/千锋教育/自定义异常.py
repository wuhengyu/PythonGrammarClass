# 系统内置异常


# ZeroDivisionError
# print(1/0)

# FileNotFoundError
# open("1111")

# FileExistsError
# windows不支持该方法
# os.mknod("浮点数输出.py")
# os.mkdir("test")

# ValueError
# int("hello")

# KeyError
# person = {'name': 'zhangsan'}
# 错误
# person['age']
# 正确
# person['age'] = 14
# print(person)

# SyntaxError
# example1:
# a = "1111"
# print("aaa"， a)
# example2:
# if 3>2
#     print("aaa")

# IndexError
# a = [1, 2, 3, 4, 5]
# print(a[8])

# 自定义异常：
class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须在{}和{}之间'.format(self.x, self.y)


password = input("请输入密码:")
m = 6
n = 12
if m <= len(password) < n:
    print("输入正确")
else:
    raise LengthError(m, n)
