#ダブリング

# 操作する回数のlog2だけループをまわす
# Xは同時点で必要な状態の数（ワープ問題なら地点の数だし、余剰を求める漸化式の問題ならModの値)
# 初期条件 = dv[0][j] = f[j]
# 漸化式 = dv[i][j] = dv[i - 1][dv[i - 1][j]]
dv = [[0] * X for _ in range(int(math.log2(K)) + 1)]

# dv[0][0:X]を、初期状態の次の状態で初期化
# 初期条件(i=0)については、2^0= 1回遷移したときの到達点は f(j)の値をそのまま入れておけばよいというだけである。
for j in range(X):
    dp[0][j] =  """問題の制約ごとに対応"""

# ダブリングで表を構築
# 「j番目の要素から 2^i-1回遷移したときの到達点」 は dp[i−1][j]に入っているので、
# 「そこから更に2^i-1」 回遷移した結果はdp[i−1][dp[i−1][j]]に格納されている。
for i in range(1, int(math.log2(K)) + 1):
    for j in range(X):
        dv[i][j] = dv[i - 1][dv[i - 1][j]]

#答えを求める部分
a = []
for i in range(int(math.log2(K)) + 1):
    #bit演算でダブリング表のどのインデックスの部分を遷移すれば答えが出せるかをaに格納
    if K　>>　i & 1:
        a.append(i)
