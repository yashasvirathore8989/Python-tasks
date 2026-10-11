arr = [4, 2, 3, 1, 6]
found = False
for i in range(len(arr)):
    curr_sum = 0
    for j in range(i, len(arr)):
        curr_sum = curr_sum + arr[j]
        if curr_sum == 0:
            found = True
            break
    if found:
        break
if found==True:
    print("Yes, subarray with 0 sum exists")
else:
    print("No, subarray with 0 sum does not exist")