# 和 return 相比，yield 除了可以返回相应的值，还有一个更重要的功能，即每当程序执行完该语句时，程序就会暂停执行。不
# 仅如此，即便调用生成器函数，Python 解释器也不会执行函数中的代码，它只会返回一个生成器（对象）。
# 和普通函数不同，intNum() 函数的返回值用的是 yield 关键字，而不是 return 关键字，此类函数又成为生成器函数

def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")


# 创建了一个 num 生成器对象
num = intNum()
print(num)

# 使用 list() 函数和 tuple() 函数，直接将生成器能生成的所有值存储成列表或者元组
# print(list(num))
num = intNum()
# print(tuple(num))

# Python 解释器开始执行 intNum() 生成器函数中的代码，因此会输出“开始执行”，程序会一直执行到yield i，而此时的 i==0，
# 因此 Python 解释器输出“0”。由于受到 yield 的影响，程序会在此处暂停。
# print(intNum().__next__())
# print(intNum().__next__())
# print(intNum().__next__())

# 调用__next__()方法迭代生成器
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())

# 调用 next() 内置函数迭代生成器
# print(next(num))
# print(next(num))
# print(next(num))

# 通过 for 循环遍历生成器
# for i in num:
#     print(i)

# send(None) 的功能是 next() 完全相同，但更推荐使用 next()，不推荐使用 send(None)
print(num.send(None))
print(num.send(None))
print(num.send(None))
print(num.send(None))
print(num.send(None))
