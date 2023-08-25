#動的計画法（カエル問題）
#iからjにいくコストは|hi - hj|
n = int(input())
h = list(map(int,input().split()))

#0で初期化
dp = [0] * (n+1)
#最初の状態として１つ目だけコストを追加
dp[1] = abs(h[1] - h[0])

# i番⽬の⾜場に⾄るケースは2通り．
# i-1番⽬の⾜場から1つジャンプして， i番⽬に来た．
# i-2番⽬の⾜場から2つジャンプして， i番⽬に来た．
for i in range(2,n):
    dp1 = dp[i-1] + abs(h[i] - h[i-1])
    dp2 = dp[i-2] + abs(h[i] - h[i-2])
    dp[i] = min(dp1,dp2)

print(dp[n-1])
