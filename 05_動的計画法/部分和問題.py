N, S = map(int, stdin.readline().split())
A = map(int, stdin.readline().split())

dp = [[True] + [False]*S for _ in range(N)]

for i in range(N):
    for j in range(S+1):
        if j >= A[i]:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i]]
        else:
            dp[i][j] = dp[i-1][j]

print("Yes" if dp[-1][-1] else "No")
