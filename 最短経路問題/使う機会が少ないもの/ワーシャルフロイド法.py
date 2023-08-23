N,M = map(int,input().split())
inf = float('inf')

graph = [[inf] * N for _ in range(N)]

#隣接行列の初期化
for _ in range(M):
    a,b,d = map(int,input().split())
    graph[a][b] = d
for n in range(N):
    graph[n][n] = 0

#ワーシャルフロイド法
#三重ループ（大外は経由地のループにする）
for transit in range(N):
    for start in range(N):
        for end in range(N):
            graph[start][end] = min(graph[start][end],graph[start][transit] + graph[transit][end])

Q = int(input())
for q in range(Q):
    s,e = map(int,input().split())
    if graph[s][e] == inf:
        print('INF')
    else:
        print(graph[s][e])
