n, m = map(int, input().split())

a = list(map(int, input().split()))
v = -1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = a[i] + a[j] + a[k] 
            if s > v and s <= m:
                v = s

print(v)