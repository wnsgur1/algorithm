n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    if s == 0:
        break
    
    max_val = arr[i]
    max_idx = i
    
    for j in range(i + 1, min(i + s + 1, n)):
        if arr[j] > max_val:
            max_val = arr[j]
            max_idx = j
    
    while max_idx > i and s > 0:
        arr[max_idx], arr[max_idx - 1] = arr[max_idx - 1], arr[max_idx]
        max_idx -= 1
        s -= 1

print(*arr)