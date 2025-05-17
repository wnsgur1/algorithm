n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()                 
B_sorted = sorted(B, reverse=True)

S = 0
for i in range(n):
    S += A[i] * B_sorted[i]

print(S)