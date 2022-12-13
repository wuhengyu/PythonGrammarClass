# fibonacci数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
        print(a)
    return 'done'


print(fib(10))
'''
a = 0, b = 1
a = b = 1, b = a+b = 0+1 = 1, 输出a = 1, b = 1
a = b = 1, b = a+b = 1+1 = 2, 输出a = 1, b = 2
a = b = 2, b = a+b = 1+2 = 3, 输出a = 2, b = 3
a = b = 3, b = a+b = 2+3 = 5, 输出a = 3, b = 5
a = b = 5, b = a+b = 3+5 = 8, 输出a = 5, b = 8
a = b = 8, b = a+b = 5+8 = 13, 输出a = 8, b = 13
依次递推
'''
