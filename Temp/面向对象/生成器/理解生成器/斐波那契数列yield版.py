# 1,1,2,3,5,8,13,21,34,55
# 返回的不再是一个值，而是一个生成器<generator object fib at 0x00000231376457B0>,那么这样就不占内存了
# generator和函数的执行流程，函数是顺序执行的，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# a=0,b=1
# a=0,b=1,a=b=1,b=a+b=1
# a=1,b=1
# a=1,b=1,a=b=1,b=a+b=2
# a=1,b=2
# a=1,b=2,a=b=2,b=a+b=3
# a=2,b=3
# a=2,b=3,a=b=3,b=a+b=5

# a = fib(5)
# print(a.__next__())
# print(a.__next__())
# print(next(a))
# print(next(a))
# print(next(a))


# generator也是可迭代对象，用在for，while等语句中
for i in fib(20):
    print(i)

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果拿不到返回值，那么就会报错，所以为了不让报错，就要进行异常处理，拿到返回值，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
# a = fib(15)
# while True:
#     try:
#         x = next(a)
#         print('generator: ', x)
#     except StopIteration as e:
#         print("生成器返回值：", e.value)
#         break
