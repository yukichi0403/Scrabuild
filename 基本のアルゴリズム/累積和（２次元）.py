#累積和（２次元）
N, M, Q = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
#累積和のリスト
#index=0,0のセルには0を格納するためN,Mとも１つ要素を増やす
s = [[0] * (M + 1) for _ in range(N + 1)]

#s[i][j]が重複部分、A[i][j]が足りない１マス
for i in range(N):
    for j in range(M):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

# 左上をa, b, 右下をc, dとしたとき、これに囲まれる長方形領域内の整数の和
for i in range(Q):
    a, b, c, d = map(int, input().split())
    print(s[c + 1][d + 1] - s[a][d + 1] - s[c + 1][b] + s[a][b])