# 상근이가 가진 숫자 카드의 개수 N 입력
N = int(input())

# 숫자 카드에 적힌 정수를 입력받아 정렬하여 arr1 리스트에 저장
arr1 = sorted(list(map(int, input().split())))

# 확인할 숫자의 개수 M 입력
M = int(input())

# 확인할 M개의 정수를 arr2 리스트에 저장
arr2 = list(map(int, input().split()))

# arr2의 각 숫자에 대해 반복
for number in arr2:
    s = 0           # 시작 포인터 초기화
    e = N - 1       # 끝 포인터 초기화
    flag = False    # 카드의 존재 여부를 표시할 플래그 초기화

    # 이진 탐색 수행
    while s <= e:
        mid = (s + e) // 2  # 중간 인덱스 계산

        # 중간 값이 찾고자 하는 숫자와 같으면
        if arr1[mid] == number:
            flag = True  # 플래그를 True로 설정
            break  # 반복문 종료
        # 중간 값이 찾고자 하는 숫자보다 크면
        elif arr1[mid] > number:
            e = mid - 1  # 오른쪽 포인터를 중간 값의 왼쪽으로 이동
        # 중간 값이 찾고자 하는 숫자보다 작으면
        elif arr1[mid] < number:
            s = mid + 1  # 왼쪽 포인터를 중간 값의 오른쪽으로 이동
    
    # 플래그에 따라 결과 출력
    if flag:
        print(1, end=" ")  # 숫자가 카드에 있으면 1 출력
    else:
        print(0, end=" ")  # 숫자가 카드에 없으면 0 출력