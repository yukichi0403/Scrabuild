#動的計画法（ナップザック問題②）
n,s = map(int,input().split())
A = list(map(int,input().split()))

dp = [['No'] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 'Yes'

for i in range(n):
    for j in range(s + 1):
        if j >= A[i]:
            if dp[i][j] == 'Yes':
                dp[i+1][j] = 'Yes'
            elif dp[i][j - A[i]] == 'Yes':
                dp[i+1][j] = 'Yes'
        else:
            dp[i+1][j] = dp[i][j]

print(dp[n][s])