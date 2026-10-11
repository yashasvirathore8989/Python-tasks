AR = [10, 20, 30, 40, 50, 60, 70, 80]
val = int(input("Enter value to search: "))
low = 0
high = len(AR) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if AR[mid] == VAL:
        found = True
        break
    elif val > AR[mid]:
        low = mid + 1
    else:
        high = mid - 1
if found == True:
    print("element found")
else:
    print("element not found")