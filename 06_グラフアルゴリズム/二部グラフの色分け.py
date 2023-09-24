import sys
sys.setrecursionlimit(10 ** 9)

# 深さ優先探索
def dfs(G, pos, c):   
    color[pos] = c
    
    # 次の位置を探索する
    for next_pos in G[pos]:
      #色分け済みの場合は飛ばす
        if color[next_pos]:
            continue
        dfs(G, next_pos, -c)

# 頂点数と辺数
N = int(input())

# グラフ入力受取
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

#色分けの配列（0が塗りつぶし前、1と-1に色分けする）
color = [0] * N
dfs(G, 0, 1)

odd = []
even = []

for i in range(N):
    if color[i] == 1:
        odd.append(i + 1)
    else:
        even.append(i + 1)

#1の頂点と同じ色のものを出力する
print(odd)
