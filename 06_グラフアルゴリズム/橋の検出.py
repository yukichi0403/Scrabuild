V,M = map(int,input().split()) # 頂点数を設定する
G = [[] for _ in range(V)]  # 頂点の隣接リスト

for _ in range(M):
    a,b = map(int,input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

INF = float('inf')
ord_pre = [INF] * V  # 行きがけ順の記録
lowlink = [INF] * V  # lowlinkの記録
Bridges = []  # 橋のリスト

pre = 0  # 行きがけ順序

def recdfs(p, u):
    global pre
    ord_pre[u] = pre
    pre += 1
    #lowlinkの初期値はその頂点のpre
    lowlink[u] = ord_pre[u]

    for v in G[u]:
        # 次の頂点をまだ訪れていない場合は、その頂点に対してDFSを続ける。
        # そして、その頂点へのDFSが終了した際に、lowがpreより小さくなっていれば、その頂点へ向かう辺は橋。
        if ord_pre[v] == INF:
            recdfs(u, v)
            lowlink[u] = min(lowlink[u], lowlink[v])
            
            if ord_pre[u] < lowlink[v]:
                Bridges.append((u, v))
        
        # 次の頂点が、すでに訪れてある（preの値が存在する）場合は
        # 自分のlowを、次の頂点のlowと比べて小さい方に更新する。
        # 自己ループを排除する条件：v != p
        elif v != p:
            lowlink[u] = min(lowlink[u], ord_pre[v])
        
        

        
recdfs(-1,0)
print(Bridges)
