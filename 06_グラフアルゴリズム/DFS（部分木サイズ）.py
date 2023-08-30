import sys
sys.setrecursionlimit(10 ** 9)

# 深さ優先探索
def dfs(G, pos, parent): 
    subtree[pos] = 1
    
    # 次の位置を探索する
    for next_pos in G[pos]:
        if subtree[next_pos]:
            continue
        dfs(G, next_pos, pos)
        subtree[pos] += subtree[next_pos]

# 頂点数と辺数
N = int(input())
subtree = [0] * N

# グラフ入力受取
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dfs(G, 0, -1)

print(subtree)
