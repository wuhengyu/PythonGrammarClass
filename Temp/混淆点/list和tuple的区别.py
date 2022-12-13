# 1、都是一个可以放置任意数据类型的有序集合
# 2、支持负数索引，支持切片，支持嵌套
# 3、存储空间差异，tuple是静态的固定大小的，而list是动态分配存储空间，自动扩容的。
a = [1, 2, 3, 4, 5]
print("list大小：", a.__sizeof__())
a = tuple(a)
print("tuple大小：", a.__sizeof__())
# 4、使用场景，存储数据固定不变的用tuple，如函数返回值，可以返回多个值，存储数据可变的情况用用list.
# 5、list 是可变的对象，元组 tuple 是不可变的对象，使用 tuple 可以使代码更安全
# 6、多线程并发的时候，tuple 是不需要加锁的，tuple 放弃了对元素的增删（内存结构设计上变的更精简），换取的是性能上的提升：创建 tuple 比 list 要快，存储空间比 list 占用更小。
# 7、Python的回收机制会在这个元组不再被使用的时候自动删除

# list有删除、更新、位置插入
b = [1, 2, 3]
b.append(4)
b.insert(0, 0)
b.remove(4)
print(b)

print("tuple只能间接删除5")
c = (1, 2, 3, 4, 5)
c = c[:2] + c[2:4]
print(c)

print("tuple只能间接更新")
d = (1, 2, 3, 4, 5)
d = d + (6,)
print(d)

print("del去删除整个元组")
e = (1, 2, 3, 4, 5)
del e
# print(e)

print("成员关系操作符 in 和 not in 也可以直接应用在元组上，这跟列表是一样的")
f = (1, 2, 3, 4, 5)
g = 2
h = (2, 3)
i = g in f
j = h in f
k = h not in f
print(i, j, k)
