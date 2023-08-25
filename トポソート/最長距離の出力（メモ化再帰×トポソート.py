import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# 隣接関係は隣接リストで管理する
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    # 最初のindexをゼロにする
    graph[a - 1].append(b - 1)
# dp[v] := ノードvを始点とした時の有向パスの長さの最大値
# -1 未訪問で初期化。
dp = [-1] * N


# メモ化再帰
def dfs(v):
    # 既に更新済み
    if dp[v] != -1:
        return dp[v]
    
    ans = 0
    for nv in graph[v]:
        ans = max(ans,dfs(nv) + 1)
    dp[v] = ans
    return dp[v]

# 全ての点に対して更新する
ans = 0
for v in range(N):
    ans = max(ans, dfs(v))

print(ans)


'''
試しにテストケースでdfs(0)をした結果
行きがけ_0_[-1,_-1,_-1,_-1]
行きがけ_1_[-1,_-1,_-1,_-1]
行きがけ_3_[-1,_-1,_-1,_-1]
帰りがけ_3_[-1,_-1,_-1,_0]
帰りがけ_1_[-1,_1,_-1,_0]
行きがけ_2_[-1,_1,_-1,_0]
帰りがけ_2_[-1,_1,_2,_0]
帰りがけ_0_[3,_1,_2,_0]
'''
