#https://paiza.jp/works/mondai/bfs_dfs_problems_advanced/bfs_dfs_problems_advanced__architecture/edit?language_uid=python3
#パーツそのもののコストとより小さいパーツ（子ノード）のコストの合計のうちのより小さいコストを採用
import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]
cost = [0] * n

for i in range(n):
    Recipe = input().split()
    cost[i] = int(Recipe[0])
    for j in range(int(Recipe[1])):
        part = int(Recipe[j + 2]) - 1
        graph[i].append(part)

def dfs(cost, now):
    sum = 0  
    for next in graph[now]:
        #再帰でより子のノードのコストを呼び出し
        sum += dfs(cost, next)
    #子供がいない（一番子供）のノードに行き着いたらコストをそのままかえす
    if not graph[now]:
        return cost[now]
    #パーツそのもののコストとより小さいパーツ（子ノード）のコストの合計のうちのより小さいコストを採用
    else:
        return min(cost[now], sum)

print(dfs(cost, 0))
