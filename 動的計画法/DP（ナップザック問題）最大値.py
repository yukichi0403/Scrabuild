#動的計画法（ナップザック問題）
#配るDP
#最大値を求めるDP。横軸を価値にして重さを格納
n,w = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(n)]
inf = 10 ** 9

dp = [[inf] * 20001  for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(20001):
        dp[i + 1][j] = min(dp[i][j],dp[i][j - wv[i][1]] + wv[i][0])

#最大値からループを回し規定の重さ以下のものが出てきたらそれが価値の最大値のため出力
for i in range(20000,-1,-1):
    if dp[n][i] <= w:
        print(i)
        break