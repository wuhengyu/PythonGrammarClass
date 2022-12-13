'''
sort 与 sorted 区别：
sort 是应用在 list 上的方法。
sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
'''

a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)
print(b)

L = [('b', 2), ('a', 1), ('c', 0), ('d', 4)]
print(sorted(L, key=lambda x: x[1]))

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# 按年龄排序
print(sorted(students, key=lambda s: s[2]))
# 按年龄降序
print(sorted(students, key=lambda s: s[2], reverse=True))

# <class 'list'>
print(sorted({'1': 1, '3': 4, '2': 6}))
# <class 'str'>
print(str(sorted({'1': 1, '3': 4, '2': 6})))
