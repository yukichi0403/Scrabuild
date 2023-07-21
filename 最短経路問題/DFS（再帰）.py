n, m, s, t = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

#再帰のDFS
def dfs(s, visited):
    #visitedのリストを関数の引数として保持
    for j in edges[s]:
        if j not in visited:
            visited.append(j)
            if t in visited:
                break
            else:
                dfs(j,visited)
    return visited

#スタート地点をvisitedリストにも入れた状態で引数として与える
dfs(s,[s])