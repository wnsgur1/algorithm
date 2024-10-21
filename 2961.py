def recur(idx, dan, zzan, use):
    global answer

    # 재료의 갯수를 다 사용했을때
    if idx == N:
        if use == 0: # 재료를 사용하지 않으면
            return
    
        result = abs(dan - zzan)
        answer = min(answer, result)
        return

    # 재료를 사용한 경우
    recur(idx+1, dan*ingre[idx][0], zzan+ingre[idx][1], use + 1)

    # 재료를 사용하지 않는 경우
    recur(idx+1, dan, zzan, use)



N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')

recur(0, 1, 0, 0)

print(answer)