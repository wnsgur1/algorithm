def solution(n, computers):
    answer = 0
    v = [False]*n
    
    def dfs(node):
        v[node] = True
        for i in range(n):
            if computers[node][i] == 1 and v[i]==False:
                dfs(i)
    
    for i in range(n):
        if not v[i]:
            dfs(i)
            answer+=1
    
    
    return answer














# def solution(n, computers):
#     visited = [False] * n

#     def dfs(node):
#         visited[node] = True
#         for i in range(n):
#             if computers[node][i] == 1 and not visited[i]:
#                 dfs(i)

#     count = 0
#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             count += 1

#     return count