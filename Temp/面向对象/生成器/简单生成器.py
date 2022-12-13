list1 = [x * x for x in range(1, 20) if x % 2 == 0]
list2 = (x * x for x in range(1, 20) if x % 2 == 0)

print(type(list1))
print(type(list2))
print(list1)
print(list2)
for n in list2:
    print(n)
for n in list2:
    print(n)
