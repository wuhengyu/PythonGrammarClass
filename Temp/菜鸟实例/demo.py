str = "sgdgdhg"
print(str[0:])

arr = [1, 2, 3, 4, 5, 6, 7]
for y in range(3):
    temp = arr[0]
    for x in range(len(arr) - 1):
        arr[x] = arr[x + 1]
    arr[-1] = temp
print(arr)
