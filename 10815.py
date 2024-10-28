# 상근이가 가진 숫자 카드의 개수 N 입력
N = int(input())

# 숫자 카드에 적힌 정수를 입력받아 리스트에 저장
cards = list(map(int, input().split()))

# 수의 개수 M 입력
M = int(input())

# 상근이가 가지고 있는지 확인할 M개의 정수를 입력받음
sang = list(map(int, input().split()))

# 결과를 저장할 리스트
result = []

# 각 쿼리에 대해 상근이가 숫자 카드를 가지고 있는지 확인
for query in sang:
    if query in cards:  # 카드가 있으면 1, 없으면 0
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(*result)  # 공백으로 구분하여 출력