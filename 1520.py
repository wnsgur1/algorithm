import sys
sys.setrecursionlimit(10**6)

def recur(y, x):
    # 목표 지점에 도달한 경우 경로 수를 1로 반환
    if y == Y - 1 and x == X - 1:
        return 1
    
    # 이미 계산된 경로 수가 있다면 해당 값을 반환
    if dp[y][x] != -1:
        return dp[y][x]
    
    # 현재 위치에서 이동 가능한 경로 수를 저장할 변수
    route = 0
    
    # 상하좌우로 이동하기 위한 방향 배열
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = y + dy  # 이동 후 y좌표
        ex = x + dx  # 이동 후 x좌표

        # 이동할 위치가 지도 내에 있고, 높이가 더 높은 지점으로만 이동 가능
        if 0 <= ey < Y and 0 <= ex < X:
            if graph[y][x] > graph[ey][ex]:  # 현재 높이보다 낮은 지점으로만 이동
                route += recur(ey, ex)  # 재귀 호출하여 경로 수를 누적

    dp[y][x] = route  # 현재 위치에서 가능한 경로 수 저장
    return dp[y][x]  # 경로 수 반환


# 입력 받기
Y, X = map(int, input().split())

# 지도 정보 입력 받기
graph = [list(map(int, input().split())) for _ in range(Y)]

# 메모이제이션을 위한 DP 배열 초기화
dp = [[-1 for _ in range(X)] for _ in range(Y)]

# 시작 위치에서 가능한 경로 수 계산
answer = recur(0, 0)

# 결과 출력
print(answer)