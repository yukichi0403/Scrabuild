#https://paiza.jp/works/mondai/bfs_dfs_problems_advanced/bfs_dfs_problems_advanced__du/edit?language_uid=python3
#子のコストの合計を親のコストとする
import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]
name = []
cost = []

for i in range(n):
    Data = input().split()
    name.append(Data[0])
    cost.append(int(Data[1]))
    for j in range(int(Data[2])):
        graph[i].append(int(Data[j + 3]) - 1)


def dfs(s, cost):
    for j in graph[s]:
        dfs(j,cost)
        #親側でこの情報を収集
        #そのためdfsを呼び出した後に値を更新
        cost[s] += cost[j]

dfs(0,cost)

for m in range(n):
    print(name[m],cost[m])


#次の書き方もある
#だた計算量に注意
def dfs(s, cost):
    sum = 0
    if not graph[s]:
        return cost[s]
    else:
        for j in graph[s]:
            sum += dfs(j,cost)
        return sum

for m in range(n):
    c = dfs(m,cost)
    print(name[m],c)