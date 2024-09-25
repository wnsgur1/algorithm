def is_in_range(i, j, N, M):
    # 다음으로 이동한 위치가 판의 크기보다 큰가?
    return 0 <= i < N and 0 <= j < M

def solution(N, M):
    # 판 만들기
    is_visited = [[False] * M for _ in range(N)]
    
    # 현재 위치
    cur_i = 0
    cur_j = 0

    # 현재 이동 방향
    cur_direction = 1 

    # 인덱스 순서대로 동북서남으로 이동
    di = [0, -1, 0, 1] 
    dj = [1, 0, -1, 0]

    while True:
        # 현재 위치를 방문했다고 표시
        is_visited[cur_i][cur_j] = True

        # 다음으로 이동할 위치
        next_i = cur_i + di[cur_direction]
        next_j = cur_j + dj[cur_direction]

        # 다음 위치가 판을 벗어났는가? 다음 위치를 간적있는가?
        if not is_in_range(next_i, next_j, N, M) or is_visited[next_i][next_j]:
            for _ in range(4):
                # 방향 돌리기 
                cur_direction = (cur_direction + 1) % 4

                # 다음 방향으로 이동
                next_i = cur_i + di[cur_direction]
                next_j = cur_j + dj[cur_direction]

                # 이동했는데 넘어가면 멈추기
                if is_in_range(next_i, next_j, N, M) and not is_visited[next_i][next_j]:
                    break
            else:
                break  

        # 현재 위치에서 다음 위치로 이동하기
        cur_i = next_i
        cur_j = next_j

    print(cur_i, cur_j)

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)