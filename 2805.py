# 나무 수 N과 필요한 길이 M 입력
N, M = map(int, input().split())

# 나무 높이 입력
arr = list(map(int, input().split()))

s = 1  # 시작 높이
e = max(arr)  # 최대 나무 높이

# 이진 탐색
while s <= e:
    mid = (s + e) // 2  # 중간 높이

    wood = 0  # 잘린 나무 길이 초기화
    for tree in arr:
        if tree >= mid:  # 현재 높이 이상인 나무만 잘림
            wood += tree - mid  # 잘린 길이 계산

    if wood >= M:  # 필요한 길이 이상이면
        s = mid + 1  # 높이 증가
    else:
        e = mid - 1  # 높이 감소

# 최댓값으로 설정할 수 있는 높이 출력
print(e)