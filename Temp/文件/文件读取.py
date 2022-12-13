f = open('test.txt', 'w')
f.write('hello，word')
# 写入位置向后偏移
f.seek(3)
f.write('11111111')
f.close()

f1 = open('test.txt', 'r')
# 部分读取
print(f1.read(3))
f1.close()

# 文件行读取
f2 = open('readine.txt', 'r')
print(f2.readline(3))
print(f2.readline())

result = []
for line in open('readine.txt'):
    line2 = f2.readline()
    print(line2)
    result.append(line2)
print(result)
f2.close()

resultString = '\n'.join(result)
open('result-readline.txt', 'w').write('%s' % resultString)

# python中非空即为真,空即为假,因此也常用来判断变量是否为空
if not 5:
    print('55555')
