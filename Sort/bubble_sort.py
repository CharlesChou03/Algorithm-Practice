#!/opt/anaconda3/bin/python3
arr = [64, 34, 25, 12, 22, 11, 90]
ans = [11, 12, 22, 25, 34, 64, 90]
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
assert(arr == ans)
print(arr)
