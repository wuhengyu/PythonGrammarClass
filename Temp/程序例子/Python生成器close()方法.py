def foo():
    try:
        yield 1
    except GeneratorExit:
        print('捕获到 GeneratorExit')


f = foo()
# 当程序在生成器函数中遇到 yield 语句暂停运行
print(next(f))
# 此时如果调用 close() 方法，会阻止生成器函数继续执行，该函数会在程序停止运行的位置抛出 GeneratorExit 异常。
f.close()
