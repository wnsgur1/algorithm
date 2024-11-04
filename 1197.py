import heapq

# 정점 개수 n과 간선 개수 m 입력 받기
n, m = map(int, input().split())

# 그래프 초기화 (1번 인덱스부터 사용)
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]  # 방문 여부 체크 리스트

# 간선 정보를 그래프에 추가
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  # (가중치, 연결 노드) 형태로 추가
    graph[b].append((c, a))  # 양방향이므로 반대 방향도 추가

answer = 0  # 최소 스패닝 트리의 가중치 합
cnt = 0     # 방문한 노드 수

# 시작 노드 1에 대한 초기화
q = []  # 최소 힙 초기화
visited[1] = 1  # 시작 노드 방문 처리
for next in graph[1]:  # 노드 1의 인접 노드를 큐에 추가
    heapq.heappush(q, next)

# 큐가 빌 때까지 반복
while q:
    weight, node = heapq.heappop(q)  # 최소 가중치 간선을 선택

    if visited[node] == 1:  # 이미 방문한 노드는 무시
        continue

    visited[node] = 1  # 노드 방문 처리
    answer += weight  # 가중치 추가
    cnt += 1  # 방문한 노드 수 증가

    # 현재 노드와 연결된 모든 인접 노드를 큐에 추가
    for next in graph[node]:
        if not visited[next[1]]:  # 아직 방문하지 않은 노드만 추가
            heapq.heappush(q, next)



# 최소 스패닝 트리의 가중치 출력
print(answer)
