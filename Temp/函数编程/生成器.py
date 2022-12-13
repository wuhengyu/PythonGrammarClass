a = [1, 3, 5, 7, 9]
b = (x * x for x in range(10))
print(next(b))
print(next(b))
print(next(b))

for x in b:
    print(x)
