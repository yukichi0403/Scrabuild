#動的計画法（ナップザック問題）
#貰うDP
N,W = map(int,input().split())
Val = []
Wei = []

for _ in range(N):
    v,w = map(int,input().split())
    Val.append(v)
    Wei.append(w)

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j < Wei[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            #個数制限なしの場合とはdp[i][j - Wei[i]]の部分だけ違う
            #制限があるので真上からしか移動できない
            dp[i + 1][j] = max(dp[i][j], dp[i][j - Wei[i]] + Val[i])

print(dp[N][W])
