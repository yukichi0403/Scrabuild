#いもす法（２次元）

N, M, K = map(int, input().split())
A = [[0] * (M + 1) for _ in range(N + 1)]

#K 個の長方形領域の左上の座標 (a, b) と右下の座標 (c, d) が与えられる
#この範囲に対して、その範囲に含まれるマスに 1 を加算していく
for i in range(K):
    a, b, c, d = map(int, input().split())
    A[b - 1][a - 1] += 1
    #右下は１つ座標の値を増やす
    A[d][c] += 1
    A[b - 1][c] -= 1
    A[d][a - 1] -= 1

#横の累積和を求める
for i in range(N + 1):
    for j in range(M):
        A[i][j + 1] += A[i][j]
#縦の累積和を求める
for i in range(N):
    for j in range(M + 1):
        A[i + 1][j] += A[i][j]

max_value = 0

for line in A:
    max_value = max(max_value, max(line))

print(max_value)