#動的計画法（ナップザック問題）
#配るDP
N,K = map(int,input().split())
a = list(map(int,input().split()))
MOD = 998244353

dp = [[0] * (K + 1) for _ in range(N + 1)]

for x in range(N + 1):
  dp[x][0] = 1

for i in range(1, N + 1):
  for j in range(1,K + 1):
    if j > a[i - 1]:
      dp[i][j] = (dp[i][j - 1] - dp[i - 1][j - a[i - 1]- 1] + dp[i - 1][j]) % MOD
    
    else:
      dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD

print(dp[N][K])