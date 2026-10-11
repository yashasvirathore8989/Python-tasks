arr = [6, -3, -10, 0, 2]
n = len(arr)
max_prod = arr[0]
min_prod = arr[0]
ans = arr[0]
for i in range(1, n):
    if arr[i] < 0:
        temp = max_prod
        max_prod = min_prod
        min_prod = temp
    if arr[i] > max_prod * arr[i]:
        max_prod = arr[i]
    else:
        max_prod = max_prod * arr[i]
    if arr[i] < min_prod * arr[i]:
        min_prod = arr[i]
    else:
        min_prod = min_prod * arr[i]
    if max_prod > ans:
        ans = max_prod
print(ans)