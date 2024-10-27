def recur(idx, weight):
    global answer  

    
    if weight > B:
        return -99999

    
    if idx == N:
        return 0 
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx] = max(recur(idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx+1, weight))


    return dp[idx]


N, B = map(int, input().split())  
items = [list(map(int, input().split())) for _ in range(N)]

answer = 0  
dp = [[-1 for _ in range(100_001)] for _ in range(N)]

recur(0, 0)

print(answer)