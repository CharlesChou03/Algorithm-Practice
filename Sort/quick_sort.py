#!/opt/anaconda3/bin/python3
arr = [64, 34, 25, 12, 22, 11, 90]
ans = [11, 12, 22, 25, 34, 64, 90]
n = len(arr)
def quick_sort(arr, left, right):
    if left > right:
        return

    i = left
    j = right
    key = arr[left]

    while i != j:
        while arr[j] > key and i < j:
            j -= 1
        while arr[i] <= key and i < j:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[i] = arr[i], arr[left]
    quick_sort(arr, left, i - 1)
    quick_sort(arr, i + 1, right)

quick_sort(arr, 0, len(arr) - 1)
assert(arr == ans)
print(arr)
