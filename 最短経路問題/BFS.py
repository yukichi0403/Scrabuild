#BFS
N = int(input())
S = [list(map(int, input().split())) for _ in range(N - 1)]

# 無向グラフの典型入力
from collections import deque,defaultdict
adj = defaultdict(list)
for a, b in S:
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

def bfs(start):
    todo = deque()
    todo.append((0, start))   # 初期探索場所をpush
    seen = [False] * N

    while todo:
        dist, pos = todo.popleft()   # popにするとDFS

        #訪問済みの場合はスルー
        if seen[pos]:
            continue
        seen[pos] = True

        # 行きがけ順の処理
        """問題ごとに必要に応じて書く"""

        # 次の位置を探索する
        for next_ in adj[pos]:
            todo.append((dist + 1, next_))
            
    return dist
