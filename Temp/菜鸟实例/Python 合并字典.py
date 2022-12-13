# 实例 1 : 使用 update() 方法，第二个参数合并第一个参数
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print(dict1)
dict2.update(dict1)
print(dict2)
# 实例 2 : 使用 **，函数将参数以字典的形式导入
dict3 = {'a': 10, 'b': 8}
dict4 = {'d': 6, 'c': 4}
res = {**dict3, **dict4}
print(res)
