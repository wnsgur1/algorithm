def recur(idx, weight, value):
    global answer  # 최대 가치를 저장할 전역 변수

    # 현재 선택한 물건들이 배낭의 허용 무게를 넘으면 종료
    if weight > B:
        return 0

    # 모든 물건을 탐색한 경우, 최대 가치를 갱신
    if idx == N:
        answer = max(answer, value)  # 현재까지의 최대 가치를 업데이트
        return

    # 현재 물건을 선택하는 경우
    recur(idx + 1, weight + items[idx][0], value + items[idx][1])

    # 현재 물건을 선택하지 않는 경우
    recur(idx + 1, weight, value)

    return 0  # 종료 시 반환 (필요는 없지만 구조 유지)


# 입력 처리
N, B = map(int, input().split())  # 물건의 개수와 배낭의 최대 무게 입력
items = [list(map(int, input().split())) for _ in range(N)]  # 각 물건의 무게와 가치 입력

answer = 0  # 최대 가치를 저장할 변수

# 재귀 호출 시작 (0번째 물건부터 탐색, 초기 무게와 가치는 0)
recur(0, 0, 0)

# 결과 출력 (최대 가치)
print(answer)