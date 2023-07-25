#トポロジカルソート
#Kahnさんバージョン
N,M = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(M)]

#辞書順にするためheapqを使用. dequeでも実装可能
import heapq

# 入次数を格納する配列
indeg = [0] * N
# 出力辺を保持する配列
out_edge = [[] for _ in range(N)]

# 入次数と出力辺の情報を整理する
for v_from,v_to in edge:
    indeg[v_to] += 1
    out_edge[v_from].append(v_to)

#入次数0のものを予めリストにしておく
node_heap = list(N for N in range(N) if indeg[N] == 0)

heapq.heapify(node_heap)
ans = []

while node_heap:
    #入次数0のノードを見つけ出し，それをグラフから取り除き，ソート済の場所に入れていく
    v = heapq.heappop(node_heap)
    ans.append(v)

    #ノードを取り出すたびに入次数の値を更新
    for to_node in out_edge[v]:
        #入次数を減らす
        indeg[to_node] -= 1
        #辺のカウントもへらす
        M -= 1
        if indeg[to_node] == 0:
            heapq.heappush(node_heap,to_node)

if M != 0:
    print(-1)
else:
    print(*ans)
