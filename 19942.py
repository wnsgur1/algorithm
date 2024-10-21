def recur(idx, A, B, C, D, E, selected):
    global answer, selected_items

    # 재료의 갯수를 다 사용했을 때
    if idx == N:
        if A >= a and B >= b and C >= c and D >= d:
            if E < answer:  # 더 작은 비용을 찾았을 때
                answer = E
                selected_items = selected[:]
            elif E == answer:  # 비용이 같으면 사전순 비교
                if selected < selected_items:
                    selected_items = selected[:]
        return

    # 재료를 사용한 경우 (현재 재료를 선택한 경우)
    recur(idx + 1, 
          A + ingre[idx][0], 
          B + ingre[idx][1], 
          C + ingre[idx][2], 
          D + ingre[idx][3], 
          E + ingre[idx][4], 
          selected + [idx + 1])

    # 재료를 사용하지 않는 경우 (현재 재료를 선택하지 않은 경우)
    recur(idx + 1, A, B, C, D, E, selected)


N = int(input())  # 재료 개수 입력
a, b, c, d = map(int, input().split())  # 최소 영양소 조건 입력
ingre = [list(map(int, input().split())) for _ in range(N)]  # 재료 정보 입력

answer = float('inf')  # 최소 비용을 저장할 변수 (초기값은 매우 크게 설정)
selected_items = []  # 최소 비용을 만족하는 재료 번호들을 저장할 리스트

recur(0, 0, 0, 0, 0, 0, [])  # 재귀 함수 호출 (처음에는 모든 값 0에서 시작)

# 결과 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)
    print(' '.join(map(str, selected_items)))
