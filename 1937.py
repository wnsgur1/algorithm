import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

def recur(y, x):
    # 이미 계산된 값이 있으면 그 값을 반환
    if dp[y][x] != 0:
        return dp[y][x]
    
    # 상, 하, 좌, 우 방향으로 이동 가능
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ey = y + dy
        ex = x + dx

        # 이동할 위치가 대나무 숲 내에 있고, 대나무 양이 현재 위치보다 많을 경우
        if 0 <= ey < n and 0 <= ex < n and graph[y][x] < graph[ey][ex]:
            # 최대 탐색 칸 수 갱신
            dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)
            
    return dp[y][x]
    
# 입력 및 초기 설정
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

# 각 위치에서의 최대 탐색 칸 수를 dp에 기록
for y in range(n):
    for x in range(n):
        recur(y, x)

# dp 배열에서 최대값을 찾고, 초기 위치 포함하여 1을 더해 출력
print(max(map(max, dp)) + 1)