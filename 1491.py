def is_in_range(i, j, N, M):
    return 0 <= i < N and 0 <= j < M

def solution(N, M):
    is_visited = [[False] * M for _ in range(N)]
    
    cur_i = 0
    cur_j = 0
    cur_direction = 1 

    di = [0, -1, 0, 1] 
    dj = [1, 0, -1, 0]

    while True:
        is_visited[cur_i][cur_j] = True
        next_i = cur_i + di[cur_direction]
        next_j = cur_j + dj[cur_direction]

        if not is_in_range(next_i, next_j, N, M) or is_visited[next_i][next_j]:
            for _ in range(4): 
                cur_direction = (cur_direction + 1) % 4
                next_i = cur_i + di[cur_direction]
                next_j = cur_j + dj[cur_direction]

                if is_in_range(next_i, next_j, N, M) and not is_visited[next_i][next_j]:
                    break
            else:
                break  

        cur_i = next_i
        cur_j = next_j

    print(cur_i, cur_j)

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)