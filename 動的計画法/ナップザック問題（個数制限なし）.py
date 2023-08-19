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
            #個数制限ありの場合とはdp[i + 1][j - Wei[i]]の+１の部分だけ違う
            #制限がないので真横移動も行える 
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - Wei[i]] + Val[i])

print(dp[N][W])
            
