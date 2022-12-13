def test():
    while True:
        n = yield
        print("test", n)


g = test()
g.__next__()
for i in range(10):
    g.send(i)
