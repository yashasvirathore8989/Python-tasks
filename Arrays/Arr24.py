arr = [1, 2, 3, 4, 5]
if len(arr) > 1:
    temp = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = temp
print(arr)