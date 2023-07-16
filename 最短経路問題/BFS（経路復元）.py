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

#１つ前の地点を保持する配列を定義
before = [0] * n
#スタート地点は-1を入れる（番兵）
before[s - 1] = -1

while q:
    #popleft()に変えるとDFSになる
    now = q.pop()
    for nxt in graph[now]:
        #未探索の地点の場合のみ探索を続ける
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            #経路復元のための配列に１つ前の地点を保持
            before[nxt] = now 
            q.append(nxt)

#今回はtまでの距離を出力
print(dist[t - 1])

#経路復元のコード
current = t - 1  # tまでの最短経路を復元する
tour = [current]
while current != -1:
    current = before[current]
    tour.append(current)

#最後のマイナス１を削除
tour.pop()

#経路を出力
for t in tour[::-1]:
    print(t + 1)
