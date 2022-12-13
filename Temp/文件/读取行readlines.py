f3 = open('readlines.txt', 'r')
result2 = list()
for line in f3.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'):
        continue
    result2.append(line)
result2.sort()
print(result2)
# 读写追加模式
open('result2.txt', 'a+').write('%s' % '\n'.join(result2) + '\n')

f4 = open('readlines.txt', 'r')
print(f4.readline(3))
print(f4.readline())
f5 = open('readlines.txt', 'r')
print(f5.readlines(100))
print(f5.readlines())

import pprint

print(open('readlines.txt', 'r').readlines())
pprint.pprint(open('readlines.txt', 'r').readlines())
