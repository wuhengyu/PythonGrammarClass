# 斐波那契数列
def fin(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        tmp = a
        a = b
        b = tmp + b
        # print(a, b)
        yield b
        count += 1


f = fin(20)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
