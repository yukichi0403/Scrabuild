import sys
sys.setrecursionlimit(10 ** 9)

# 深さ優先探索
def dfs(G, pos, visited):   
    visited[pos] = True
    # 次の位置を探索する
    for next_pos in G[pos]:
        if visited[next_pos]:
            continue
        dfs(G, next_pos, visited)


# 頂点数と辺数
N, M = map(int, input().split())

# グラフ入力受取
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# 全頂点が訪問済みになるまで探索
count = 0
visited = [False] * N
for v in range(N):
    if visited[v]:
        continue
    dfs(G, v, visited)
    count += 1

#答え
print(count)
