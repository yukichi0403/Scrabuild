#いもす法（１次元）

N, Q = map(int, input().split())
imos = [0] * (N + 1)

for i in range(Q):
    #加算タイミングと減算タイミング
    # 1 ≦ L ≦ R ≦ N
    L, R = map(int, input().split())
    imos[L - 1] += 1
    #Rのタイミングではまだ加算したままでR+1のタイミングでいなくなる
    imos[R] -= 1

for i in range(N):
    imos[i + 1] += imos[i]

#最大値を求める
print(max(imos))