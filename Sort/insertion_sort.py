#!/opt/anaconda3/bin/python3
arr = [11, 12, 22, 25, 34, 64, 90]
n = len(arr)
for i in range(1, n):
    while i > 0 and arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i -= 1
print(arr)
