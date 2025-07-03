from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 2배로 늘려서 경계선 표현 정확히 하기 (중간 경로 회피)
    board = [[0] * 102 for _ in range(102)]

    # 1. 모든 사각형을 채운다
    for rec in rectangle:
        x1, y1, x2, y2 = [r * 2 for r in rec]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] = 1

    # 2. 내부를 0으로 바꿔서 테두리만 남긴다
    for rec in rectangle:
        x1, y1, x2, y2 = [r * 2 for r in rec]
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = 0

    # 3. BFS로 최단거리 찾기
    visited = [[0] * 102 for _ in range(102)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((characterX * 2, characterY * 2))
    visited[characterX * 2][characterY * 2] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return (visited[x][y] - 1) // 2  # 거리 2배 계산했으므로 복구

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
