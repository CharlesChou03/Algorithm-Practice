arr = [64, 34, 25, 12, 22, 11, 90]
ans = [11, 12, 22, 25, 34, 64, 90]
length = len(arr)
def merge_sort(arr):
    #print("Splitting ", arr)
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ", arr)

merge_sort(arr)
assert(arr == ans)
print(arr)
