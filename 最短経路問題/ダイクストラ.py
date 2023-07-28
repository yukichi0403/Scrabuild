import heapq

def dijkstra(N, S, graph):
    inf = float('inf')
    dist = [inf] * N
    dist[S] = 0
    done = [False] * N

    node_heap = []
    heapq.heappush(node_heap, (dist[S], S))

    while node_heap:
        cost, index = heapq.heappop(node_heap)
        cur_node = index

        if not done[cur_node]:
            for i, c in graph[cur_node]:
                if dist[i] > dist[cur_node] + c:
                    dist[i] = dist[cur_node] + c
                    heapq.heappush(node_heap, (dist[i], i))

            done[cur_node] = True

    return dist



N, M, S = map(int, input().split())

graph = [[] for _ in range(N)]
#有向グラフのケース
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))


dist = dijkstra(N, M, S, graph)

