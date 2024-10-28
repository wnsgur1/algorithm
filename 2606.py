n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node):
    visited[node] = 1

    for next in graph[node]:
        if visited[next] == 1:
            continue

        recur(next)

recur(1)

print(sum(visited)-1)