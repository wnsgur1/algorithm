def recur(number, start):
    if number == m:
        print(*arr)
        return
    
    for i in range(start, n + 1):
        if i in arr:
            continue
        arr.append(i)
        recur(number + 1, i + 1)
        arr.pop()

n, m = map(int, input().split())
arr = []
recur(0, 1)