import bisect

N,T = map(int,input().split()) 
A = list(map(int,input().split()))

#偶数番目の和の全パターンのリスト
gusu = [0]
#奇数番目の和の全パターンのリスト
kisu = [0]

for i in range(N):
    #偶数番目の和の全パターンを格納
    if i % 2 == 0:
        for j in range(len(gusu)):
            gusu.append(A[i] + gusu[j])
    #偶数番目の和の全パターンを格納
    else:
        for k in range(len(kisu)):
            kisu.append(A[i] + kisu[k])

gusu.sort()
kisu.sort()

ans = 0
for g in gusu:
    #求めている数を超えた場合は即終了
    if g > T:
        break
    #bisect_right-1でT-g以下で最も大きい値を特定
    ind = bisect.bisect_right(kisu,T - g) - 1
    k = kisu[ind]
    ans = max(ans, g + k)

"""ちょうどK個選んでP以下となる組み合わせの数
import bisect
from itertools import combinations

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

group1, group2 = A[:N // 2], A[N // 2:]
group1_price = [[] for _ in range(K + 1)]  # 0~K個選んだときの価格を格納

for i in range(K + 1):
    for c in combinations(group1, i):  # group1からi個選んだときの組み合わせ
        group1_price[i].append(sum(c))
    group1_price[i].sort()  # 価格を昇順にソートする→後で二分探索を行うため

ans = 0
for i in range(K + 1):
    for c in combinations(group2, i):  # group2からi個選んだときの組み合わせ
        # group1からK-i個選んだときの組み合わせの内、金額がP-sum(c)以下の数
        # 二分探索を行う
        index = bisect.bisect(group1_price[K - i], (P - sum(c)))
        ans += index
print(ans)
"""
