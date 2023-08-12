N = int(input())
S = [list(map(int, input().split())) for _ in range(N - 1)]

# 無向グラフの典型入力
from collections import defaultdict
adj = defaultdict(list)
for a, b in S:
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

import sys
sys.setrecursionlimit(10 ** 9)

def dfs(pos, visited):   
    visited[pos] = True
    
    # 次の位置を探索する
    for next_ in adj[pos]:
        if not visited[next_]:
            dfs(next_, visited)

    # 帰りがけ順の処理
    """問題ごとに追記"""


dfs(0, [False] * N)

