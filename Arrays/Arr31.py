A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]
M = len(A)
N = len(B)
C = [0] * (M + N)
left = 0
right = M + N - 1

# All even numbers of A from left to right 
for i in range(M):
    if A[i] % 2 == 0:
        C[left] = A[i]
        left += 1

# All odd numbers of A from left to right 
for i in range(M):
    if A[i] % 2!= 0:
        C[right] = A[i]
        right -= 1

# All even numbers of B from left to right 
for i in range(N):
    if B[i] % 2 == 0:
        C[left] = B[i]
        left += 1

# All odd numbers of B from left to right 
for i in range(N):
    if B[i] % 2!= 0:
        C[right] = B[i]
        right -= 1
print("A =", A)
print("B =", B)
print("C =", C)