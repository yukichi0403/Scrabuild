n = int(input())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

#スタート地点と連結成分のリストを引数として関数を定義
def dfs(v, connected_comp):
    for i in ad_list[v]:
        if i not in connected_comp:
            connected_comp.append(i)
            dfs(i, connected_comp)
    return connected_comp


cnt = 0
#まだ訪れていない頂点のsetを定義
not_visit = set(range(1, n + 1))

#訪れていない頂点が存在するまでループ
while len(not_visit) > 0:
    v = not_visit.pop()
    #vから連結している頂点を訪問済みとして削除
    not_visit -= set(dfs(v, [v]))
    #連結成分のカウントをプラス1
    cnt += 1


print(cnt)