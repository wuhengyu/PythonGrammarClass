import json

# 用dumps将python编码成json字符串
import os

b = {'a': '1', 'b': '2', 'c': '3', 'e': '哈哈'}
print(json.dumps(b, ensure_ascii=False, indent=4))

path = os.getcwd()
print(path)

with open(path + '/test.json', encoding='utf-8') as f:
    a = json.load(f)
print(a)
print(a['a'])
