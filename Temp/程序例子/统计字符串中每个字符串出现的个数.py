a = "afnklshglsxdhgjlsjglkvsjgsfsjgflsdxjgvlsxjgvlsdjgdkglhgfidghidhgik"
b = {}

for x in a:
    if x not in b:
        b[x] = 1
    else:
        b[x] += 1
print(b)
