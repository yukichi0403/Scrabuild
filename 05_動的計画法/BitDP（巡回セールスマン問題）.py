N = int(input())

#都市の座標を保持
cities = [list(map(int,input().split())) for _ in range(N)]

#city1からcity2までの移動距離を計算する関数を定義
def cal_dist(city1,city2):
    dist = """問題ごとに距離を算出する式を定義"""
    return dist

#各都パターンの距離を保持するリストを無限大で初期化
#dist[都市名：i][都市の集合=S] → 都市の集合Sを巡回するiまでの経路の距離
dist = [[float('inf')] * (1 << N) for _ in range(N)]


#dpテーブルの初期化
#都市0からiまでの距離で初期化（都市0をでて都市0に戻るまでの距離を計算するため）
for i in range(1, N):
    dist[i][1 << i] = cal_dist(0, i)

#探索開始
#集合の添字を全て試す
for s in range(1 << N):
    #現在の都市
    for i in range(N):
        #現在の都市を含めない集合Sはとばす
        if s >> i & 1 == 0:
            continue
        #行き先の都市
        for j in range(N):
            #既に集合Sにjが含まれている（訪問済み）の場合は飛ばす
            if (s >> j) == 1:
                continue
            tmp = dist[i][s] + cal_dist(i,j)

            #集合Sを巡回するjまでの距離＋iからjまでの距離が、集合Sを巡回するjまでの距離（既に格納されている値）よりも小さい場合値を更新
            if tmp < dist[j][s | 1 << j]:
                dist[j][s | 1 << j] = tmp

#集合Sを全て経由して都市0にたどり着く最短距離を出力
print(dist[0][2**N - 1])
