def recur(idx, price):
    global answer  # 최대 수익 저장

    if idx >= N:  # 상담 날짜가 N일을 넘으면 종료
        answer = max(answer, price)  # 최대 수익 갱신
        return

    # 상담을 하는 경우
    if idx + interview[idx][0] <= N:  # 상담이 N일 내 끝나면
        recur(idx + interview[idx][0], price + interview[idx][1])

    # 상담을 하지 않는 경우
    recur(idx + 1, price)


N = int(input())  # 상담 일수
interview = [list(map(int, input().split())) for _ in range(N)]  # 상담 정보
answer = 0  # 최대 수익 저장
recur(0, 0)  # 재귀 호출
print(answer)  # 결과 출력