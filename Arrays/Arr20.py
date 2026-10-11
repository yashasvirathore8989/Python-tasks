arr = [100, 4, 200, 1, 3, 2]
arr.sort()
max_len = 1
curr_len = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]: 
        continue
    if arr[i] == arr[i-1] + 1:
        curr_len = curr_len + 1
    else:
        if curr_len > max_len:
            max_len = curr_len
        curr_len = 1
if curr_len > max_len:
    max_len = curr_len
print(max_len)