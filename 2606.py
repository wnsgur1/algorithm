n = int(input())  # 컴퓨터의 수를 입력받음
m = int(input())  # 직접 연결된 컴퓨터 쌍의 수를 입력받음

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]  # 방문 여부를 기록할 리스트

# 네트워크 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())  # 연결된 두 컴퓨터 입력
    graph[a].append(b)  # a와 b 연결
    graph[b].append(a)  # b와 a 연결

def recur(node):
    visited[node] = 1  # 현재 노드를 방문으로 표시

    for next in graph[node]:  # 연결된 다음 노드들 탐색
        if visited[next] == 1:  # 이미 방문한 노드면 건너뜀
            continue

        recur(next)  # 재귀 호출로 다음 노드 방문

recur(1)  # 1번 컴퓨터에서 시작

print(sum(visited) - 1)  # 감염된 컴퓨터 수 (1번 컴퓨터 제외) 출력
