# 深さ優先探索
def dfs(G, v, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen)

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
seen = [False] * N
for v in range(N):
    if seen[v]:
        continue
    dfs(G, v, seen)
    count += 1

#答え
print(count)
