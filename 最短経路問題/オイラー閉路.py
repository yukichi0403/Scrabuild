#オイラー閉路の検出
#頂点 s を始点終点として出力

n, s = map(int, input().split())
ad_list = {}
edge_num = 0
for i in range(1, n + 1):
    #辺の数を頂点の数としてカウント
    edge_num += len(ad_list[i])
    ad_list[i] = list(map(int, input().split()))

#たとえば1→2と2→1は同じ辺なので//2する
edge_num //= 2

def dfs(v, visited, edge):
    for i in ad_list[v]:
        e = sorted((i, v))
        if e not in edge:
            visited.append(i)
            #辺を保持するリストを保持。一度通った辺は通らない
            edge.append(e)
            if i == s and len(edge) == edge_num:
                print(*visited)
                exit()
            dfs(i, visited, edge)
            edge.pop()
            visited.pop()


dfs(s, [s], [])