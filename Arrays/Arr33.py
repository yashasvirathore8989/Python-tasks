arr = [10, 25, 30, 15, 40, 50]
val = int(input("Enter value to search: "))
found = False
for i in range(len(arr)):
    if arr[i] == val:
        print(f"element found at index {i}")
        found = True
        break
if not found:
    print("element not found")