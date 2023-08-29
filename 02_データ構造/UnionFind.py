#UnionFind木
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        #親を全て-1で初期化
        self.parents = [-1] * n
    
    #要素xが属するグループの根を返す
    def find(self, x):
        #parentsの値がマイナス＝一番親なのでその番号を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        #より小さい方が高さがあるので、x > yの場合はyにくっつけたい
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        #子には親のインデックスを格納する（常に0以上）
        self.parents[y] = x
    
    def size(self, x):
        #子が増えるたびに-1増えるので、これを正に直した数がグループに所属する要素の数
        return -self.parents[self.find(x)]
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
    #各要素をその所属する集合の根要素でグループ分けした辞書を返すメソッド
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
    #all_group_members() メソッドを呼び出し辞書の内容を文字列として整形して、各グループの情報を表示
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
