# json.loads()是针对内存对象，将string转换为dict。
# json.loads()

"""
import json

x = {'name': '你猜', 'age': 19, 'city': '四川'}

# 用dumps将python编码成json字符串
x = json.dumps(x, ensure_ascii=False)
print(x)

# 用loads将json编码成python
print(json.loads(x))
"""

# json.load()针对文件句柄，将json格式的字符转换为dict，从文件中读取 (将string转换为dict)
# json.load()

import json

y = {'name': '你猜', 'age': 19, 'city': '四川'}

filename = 'load.txt'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(y, f, ensure_ascii=False)
with open(filename, encoding='utf-8') as g:
    print(json.load(g))
