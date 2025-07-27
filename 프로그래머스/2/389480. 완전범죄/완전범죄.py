def solution(info, n, m):
    from collections import defaultdict
    INF = float('inf')
    length = len(info)


    dp = [defaultdict(lambda: INF) for _ in range(length + 1)]
    dp[0][0] = 0

    for i in range(length):
        a_tr, b_tr = info[i]
        for b_trace, a_trace in dp[i].items():

            na = a_trace + a_tr
            nb = b_trace
            if na < n:
                dp[i + 1][nb] = min(dp[i + 1][nb], na)


            na = a_trace
            nb = b_trace + b_tr
            if nb < m:
                dp[i + 1][nb] = min(dp[i + 1][nb], na)


    result = min([a for b, a in dp[length].items() if b < m and a < n], default=INF)

    return result if result != INF else -1
