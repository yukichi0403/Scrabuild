#フォード・ファルカーソン法
N, M = map(int, input().split())
capacity = [[0] * N for _ in range(N)]

max_flow = 0

for _ in range(M):
    u,v,c = map(int, input().split())
    capacity[u - 1][v - 1] = c


def dfs_ff(s, e, flow):
    if s == e:
        return flow

    visited[s] = True
    # 流せる容量がある辺をすべてチェック
    # まだ⾒ていない辺があればDFS
    for i in range(N):
        if not visited[i] and capacity[s][i] > 0:
            f = dfs_ff(i, e, min(flow, capacity[s][i]))
            # 順⽅向，逆⽅向の容量を更新
            if f > 0:
                capacity[s][i] -= f
                capacity[i][s] += f
                return f
    return 0

#流せる量がある限り流し続ける
while True:
    visited = [False] * N
    flow = dfs_ff(0, N - 1, 10 ** 9)
    if not flow:
        break
    max_flow += flow

print(max_flow)