arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
max_so_far = arr[0]
curr_max = arr[0]
for i in range(1, n):
    if curr_max + arr[i] > arr[i]:
        curr_max = curr_max + arr[i]
    else:
        curr_max = arr[i]
    if curr_max > max_so_far:
        max_so_far = curr_max
print(max_so_far)