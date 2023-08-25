import sys
sys.setrecursionlimit(10 ** 9) #再帰回数の限界を変更

def dfs(A):
    # 数列の長さが N に達したら打ち切り
    if len(A) == N:
        # 処理
        return
    for v in range(M):
        dfs(A+[v])

dfs([])
