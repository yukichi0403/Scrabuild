L = [[1,2,3],[2,3,4],[3,4,5]]

L = sorted(L, reverse=True, key=lambda x: x[1])  
#[1]に注目して降順ソート
#昇順の場合は「reverse=True」は不要

print(*L)
