dict = {'a': 100, 'b': 200, 'c': 300}
dict_sum1 = 0
for x in dict.values():
    dict_sum1 += x
print(dict_sum1)

dict_sum2 = 0
for x in dict:
    dict_sum2 += dict[x]
print(dict_sum2)
