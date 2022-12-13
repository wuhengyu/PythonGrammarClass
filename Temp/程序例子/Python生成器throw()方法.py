def foo():
    try:
        yield 1
    except ValueError:
        print('捕获到 ValueError')


f = foo()
print(next(f))
# 生成器 throw() 方法的功能是，在生成器函数执行暂停处，抛出一个指定的异常，
# 之后程序会继续执行生成器函数中后续的代码，直到遇到下一个 yield 语句。需要注意的是，
# 如果到剩余代码执行完毕没有遇到下一个 yield 语句，则程序会抛出 StopIteration 异常。
f.throw(ValueError)
# 生成器函数在 yield 1 处暂停执行，当执行 throw() 方法时，
# 它会先抛出 ValueError 异常，然后继续执行后续代码找到下一个 yield 语句，
# 该程序中由于后续不再有 yield 语句，因此程序执行到最后，会抛出一个 StopIteration 异常。
