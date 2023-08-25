#累積和（1次元）
#XからYまでの区間和を求める
N, X, Y = map(int, input().split())
a = [int(x) for x in input().split()]

#累積和のリスト
#index=0のセルには0を格納するためNより１つ要素を増やす
cumu_sum = [0] * (N + 1)

for i in range(N):
    cumu_sum[i + 1] = cumu_sum[i] + a[i]

print(cumu_sum[Y + 1] - cumu_sum[X])
