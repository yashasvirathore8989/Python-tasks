X = [9, 7, 5, 3, 1] 
Y = [10, 8, 6, 4, 2] 
M = len(X)
N = len(Y)
Z = [0] * (M + N)
i = 0 
j = 0 
k = 0 
while i < M and j < N:
    if X[i] > Y[j]:
        Z[k] = X[i]
        i += 1
    else:
        Z[k] = Y[j]
        j += 1
    k += 1
while i < M:
    Z[k] = X[i]
    i += 1
    k += 1
while j < N:
    Z[k] = Y[j]
    j += 1
    k += 1
print("Array Z (Descending):", Z)