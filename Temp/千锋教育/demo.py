# class abc(object):
#     def hhh(self):
#         print("aaaa")
#
# def defg():
#     x = abc()
#     return x
#
# defg().hhh()
# abc().hhh()

# 取模，余数
print(5 % 2)
# 精确除法
print(5 / 2)
# 取整除法
print(5 // 2)
print("随机整数")
from random import randint

for x in range(1, 10):
    print(x, randint(1, 2))
