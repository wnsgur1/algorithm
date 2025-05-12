n = int(input())
start = max(1, n - 9 * len(str(n)))
for i in range(start, n):
    arr = list(map(int, list(str(i))))
    if i + sum(arr) == n:
        print(i)
        exit()
print(0)