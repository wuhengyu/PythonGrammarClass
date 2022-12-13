def even_squares(start, end):
    for n in range(start, end):
        if n % 2 == 0:
            yield n * n


list = even_squares(1, 20)
print(type(list))
print(list)
for n in list:
    print(n)
