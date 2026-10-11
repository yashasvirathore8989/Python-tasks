arr = [10, 5, 20, 8, 15]
largest = arr[0]
smallest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]
print("Largest =", largest)
print("Smallest =", smallest)