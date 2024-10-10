def recur(number):
    if number == m:
        print(*arr)
        return
    
    for i in range(1, n + 1):  # 매번 1부터 N까지 선택 가능
        arr.append(i)
        recur(number + 1)
        arr.pop()

n, m = map(int, input().split())
arr = []
recur(0)
