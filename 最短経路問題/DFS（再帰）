import sys
import resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

n, m, s, t = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[s] = True

for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def dfs(s):
    for j in edges[s]:
        if not visited[j]:
            visited[j] = True
            if visited[t]:
                break
            else:
                dfs(j)
    return visited[t]