arr = [8, 3, 1, 2]
n = len(arr)
S = 0
for i in range(n):
    S = S + arr[i]
R = 0
for i in range(n):
    R = R + i * arr[i]
max_sum = R
for i in range(n-1):
    R = R + n * arr[i] - S
    if R > max_sum:
        max_sum = R
print(max_sum)