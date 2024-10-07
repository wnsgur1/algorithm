# memoization을 위한 캐시를 생성합니다.
def fibonacci_count(n):
    # DP 배열 초기화
    zero_count = [0] * (n + 1)
    one_count = [0] * (n + 1)

    # 초기 값 설정
    if n >= 0:
        zero_count[0] = 1  # fibonacci(0)은 0을 1번 호출
        one_count[0] = 0   # fibonacci(0)은 1을 호출하지 않음
    if n >= 1:
        zero_count[1] = 0  # fibonacci(1)은 0을 호출하지 않음
        one_count[1] = 1   # fibonacci(1)은 1을 1번 호출

    # DP를 통해 각 피보나치 수에서 0과 1의 호출 횟수 계산
    for i in range(2, n + 1):
        zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
        one_count[i] = one_count[i - 1] + one_count[i - 2]

    return zero_count[n], one_count[n]

n = int(input())

for i in range(n):
    num = int(input())
    zeroC, oneC = fibonacci_count(num)
    print(zeroC, oneC)
