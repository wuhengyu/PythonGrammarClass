# 1,1,2,3,5,8,13,21,34,55
# fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
# 非常类似generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
        print(a)
    return 'done'


print(fib(10))
