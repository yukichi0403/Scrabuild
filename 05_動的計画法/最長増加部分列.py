from bisect import bisect

# N: 数列の長さ
# A[i]: a_i の値
def lis(N, A):
    INF = float('inf')

    dp = [INF]*(N+1)
    dp[0] = -1
    # A[i]ごとにLISの長さを出したい場合
    # dp2 = [INF] * N
    for i in range(N):
        #dp上のインデックス
        idx = bisect(dp, A[i] - 1)
        dp[idx] = min(A[i], dp[idx])
        # A[i]ごとにその時点でのLISの長さを求めたい場合
        # dp2[i] = idx
    return max(i for i in range(N+1) if dp[i] < INF)
    
    
