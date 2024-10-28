N = int(input())
arr = list(map(int, input().split()))

# dp[i]는 arr[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이를 저장
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        # arr[i]가 arr[j]보다 크다면, 증가하는 부분 수열을 만들 수 있음
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)  # dp 갱신: 이전 길이 + 1

# dp 배열에서 가장 큰 값이 가장 긴 증가하는 부분 수열의 길이
print(max(dp))