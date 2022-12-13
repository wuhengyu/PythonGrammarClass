arr = [55, 45, 56, 78, 2, 345, 435, 21, 67]
arr_len = len(arr)
for i in range(arr_len):
    for j in range(0, arr_len - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
for i in range(len(arr)):
    print("%d" % arr[i])
