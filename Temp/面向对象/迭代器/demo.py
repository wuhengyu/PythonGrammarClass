a = 10
b = 20
print(a and b)
print(a or b)
print(not (a and b))
print("--------------")
a1 = True
b1 = False
print(a1 and b1)
print(a1 or b1)
print(not (a1 and b1))
print("--------------")
a1 = 10
b1 = 10
print(a1 and b1)
print(a1 or b1)
print(not (a1 and b1))
print("------sort函数--------")
list = [2, 4, 1, 5, 9, 7, 8]
list.sort(reverse=True)  # 降序
print(list)
print("-------sorted函数-------")
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda s: s[2]))  # 按年龄排序
print(sorted(students, key=lambda s: s[2], reverse=True))  # 按降序
