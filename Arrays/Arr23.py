arr = [10, 20, 30, 40, 50]
n = len(arr)
sum = 0
for i in range(n):
    sum = sum + arr[i]
avg = sum / n
print("Sum =", sum)
print("Average =", avg)