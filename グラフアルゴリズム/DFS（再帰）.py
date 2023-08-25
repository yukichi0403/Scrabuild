import sys
sys.setrecursionlimit(10 ** 9)

# 深さ優先探索
def dfs(G, pos, visited):   
    visited[pos] = True
    # いきがけ順の処理（帰りがけの処理とどっちがいいかは問題次第）
    """問題ごとに追記（path.append(pos)など）"""
    
    # 次の位置を探索する
    for next_pos in G[pos]:
        if visited[next_pos]:
            continue
        dfs(G, next_pos, visited)

    # 帰りがけ順の処理
    """問題ごとに追記（path.append(pos)など）"""


# 頂点数と辺数
N, M = map(int, input().split())

# グラフ入力受取
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


dfs(G, 0, [False] * N)

