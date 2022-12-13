a = [1, 3, 5, 7, 9]

# 第一种
# for i,x in enumerate(a):
#     a[i]+=1
# print(a)

# 第二种
# a = list(map(lambda x:x+1,a))
# print(a)

# 第三种
b = [i + 1 for i in a]
print(b)
