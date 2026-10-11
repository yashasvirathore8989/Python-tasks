#first non-repeating element

arr=[3,5,7,5,7,3,6,8]
for i in range(len(arr)):
    is_repeating = False
    for j in range(len(arr)):
        if i!=j and arr[i]==arr[j]:
            is_repeating = True
            break
    if not is_repeating:
        print("First non-repeating is",arr[i])
        break
else:
    print("NON-Repeating element not found!")