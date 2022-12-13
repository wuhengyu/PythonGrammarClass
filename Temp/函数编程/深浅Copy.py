import copy

# 直接赋值，全部改变
# 浅拷贝: 引用对象
# s1 = {"a": "1", "b": "2", "c": {"d": "3", "e": "4"}}
# s2 = s1
# print(s1, s2)
# print(id(s1))
# print(id(s2))


# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象，如子字典
# 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 改变父对象值不会影响其他对象值，但子对象会影响，共享一份内存地址
# s1 = {"a": "1", "b": "2", "c": {"d": "3", "e": "4"}}
# print(id(s1))
# s2 = s1.copy()
# s2["a"] = "111"
# s2["c"]["d"] = "333"
# print(id(s2))
# print(s1, s2)


# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
# 完全独立
s1 = {"a": "1", "b": "2", "c": {"d": "3", "e": "4"}}
print(id(s1))
s2 = copy.deepcopy(s1)
s2["a"] = "111"
s2["c"]["d"] = "333"
print(id(s2))
print(s1, s2)
