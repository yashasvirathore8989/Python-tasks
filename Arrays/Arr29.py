A = [1, 3, 5, 7, 9] 
B = [10, 8, 6, 4, 2] 
M = len(A)
N = len(B)
C = [0] * (M + N)
i = 0
j = N - 1
k = 0
while i < M and j >= 0:
    if A[i] < B[j]:
        C[k] = A[i]
        i += 1
    else:
        C[k] = B[j]
        j -= 1
    k += 1
while i < M:
    C[k] = A[i]
    i += 1
    k += 1
while j >= 0:
    C[k] = B[j]
    j -= 1
    k += 1
print("Array C (Ascending):", C)