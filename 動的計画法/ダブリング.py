#ダブリング

# 二次元配列作成
# 操作する回数のlog分だけループをまわす
# Xは同時点で必要な状態の数（ワープ問題なら地点の数だし、余剰を求める漸化式の問題ならModの値
dv = [[0] * X for _ in range(int(math.log2(K)) + 1)]

# dv[0][0:X]を初期化
"""問題の制約ごとに初期化"""

# ダブリングで表を構築
for k in range(1, int(math.log2(K)) + 1):
    for n in range(N):
        dv[k][n] = dv[k - 1][dv[k - 1][n]]

#答えを求める部分
a = []
for i in range(int(math.log2(K)) + 1):
    #bit演算でダブリング表のどのインデックスの部分を遷移すれば答えが出せるかをaに格納
    if K>>i & 1:
        a.append(i)

#答えを計算
"""問題の制約ごとに対応（基本ループを回す）"""
