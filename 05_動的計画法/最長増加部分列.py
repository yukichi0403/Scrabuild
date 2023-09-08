from bisect import bisect

# N: 数列の長さ
# A[i]: a_i の値
def lis(N, A):
    INF = float('inf')

    dp = [INF]*(N+1)
    dp[0] = -1
    # A[i]ごとに非連続なLISの長さを出したい場合
    # dp2 = [INF] * N
    for i in range(N):
        #idx = dp上のインデックス = A全体におけるその時点（A[i]まで）で非連続なLISの長さ
        idx = bisect(dp, A[i] - 1)
        dp[idx] = min(A[i], dp[idx])
        # A[i]ごとの非連続なLISの長さ
        # dp2[i] = idx
    return max(i for i in range(N+1) if dp[i] < INF)

# 例: A = [3,1,4,1,5,9,2,6]
# 全体LIS:         [1, 2, 5, 6, inf, inf, inf, inf]
# その時点までのLIS: [1, 1, 2, 1, 3, 4, 2, 4]
    
