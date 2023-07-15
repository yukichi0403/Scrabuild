#プリム法
#辺に重みがなければdequeでも可
import heapq

def prim(N, e_list):
    # edges_from[i]はノードiからのすべての辺を格納
    edges_from = [[] for _ in range(N)]

    #ヒープでソートされるために距離を最初の要素にする
    #e_list.sort(key=lambda e: e[2])などのようにラムダ関数使ってコストでソートしてもOK
    for e in e_list:
        edges_from[e[0]].append(e[2],e[0],e[1])
    
    e_heapq = []
    mst = [] #最小全域木
    included = [False] * N # ノードが最⼩全域⽊に⼊ったかどうかのフラグ

    #ノードをまず1つ選ぶ．何でも良いがこの実装ではノード0を選ぶことにする
    included[0] = True

    #ノード0に接続する辺を全てヒープに⼊れる
    for e in edges_from[0]:
        heapq.heappush(e_heapq, e)

    while e_heapq:
        min_edges = heapq.heappop(e_heapq)
        #その辺の到達先（ノードj）が未訪問なら追加
        if not included[min_edges[2]]:
            included[min_edges[2]] = True
            mst.append([min_edges[1],min_edges[2]])

            #ノードjから伸びる辺をe_heapqに⼊れる
            for e in edges_from[min_edges[2]]:
                if not included[e[2]]:
                    #ここではheapqに突っ込むだけ
                    #mstへの記録とincludedフラグの更新は次のループで行う
                    heapq.heappush(e_heapq, e)
    
    #ソートして出力
    mst.sort()
    print(mst)