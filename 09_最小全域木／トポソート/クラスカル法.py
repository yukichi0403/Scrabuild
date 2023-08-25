#最小全域木／クラスカル法

#UnionFind木
class Union_Find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0 for _ in range(n)]

    def get_root(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]

    def unite(self, i, j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j:
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1

    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
# 全ての辺を距離の短い順にソート. 一番距離の短い辺からスタート.
graph.sort(key=lambda g: g[2])

uf_tree = Union_Find(N)
# 辺情報（graph[0][1]）を保持
mst = []
# 答えとなるコスト（graph[2]の合計）を保持
ans = 0

for start, end, cost in graph:
    # 今までに出来た木に辺を追加した時，閉路が新しく出来ないことを確認する.
    # 出来ない場合，この辺を最小全域木に追加.
    if not uf_tree.is_in_group(start, end):
        uf_tree.unite(start, end)
        #辺情報を保持
        mst.append((start, end))
        ans += cost

#今回はコストと最小全域木の辺の一覧を出力
print(ans)
for hen in mst:
    print(*hen)
