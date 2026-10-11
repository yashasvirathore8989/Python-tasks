arr = [10, 20, 30, 40, 50, 60, 70]
val = int(input("Enter value to search: "))
low = 0
high = len(arr) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == val:
        found = True
        print(f"element found at index {mid}")
        break
    elif val > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("element not found")