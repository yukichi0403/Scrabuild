#BFS
N = int(input())
S = [list(map(int, input().split())) for _ in range(N - 1)]

# 無向グラフの典型入力
from collections import deque,defaultdict
graph = defaultdict(list)
for a, b in S:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(start):
    todo = deque()
    todo.append((0, start))   # 初期探索場所をpush
    seen = [False] * N
    #dist_list = [float('inf')] * N

    while todo:
        dist, pos = todo.popleft()   # popにするとDFS

        #訪問済みの場合はスルー
        if seen[pos]:
            continue
        seen[pos] = True
        #dist_list[pos] = dist

        # 次の位置を探索する
        for next_ in graph[pos]:
            todo.append((dist + 1, next_))
            
    return dist
