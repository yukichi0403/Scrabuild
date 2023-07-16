#BFS
from collections import deque

n, m, s, t = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

q = deque()
q.append(s - 1)
#sからの距離を保持する配列を定義して-1で初期化
dist = [-1] * n
dist[s - 1] = 0

while q:
    #pop()に変えるとDFSになる
    now = q.popleft()
    for nxt in graph[now]:
        #未探索の地点の場合のみ探索を続ける
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

#今回はtまでの距離を出力
print(dist[t - 1])