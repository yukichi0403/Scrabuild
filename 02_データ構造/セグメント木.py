#セグメント木
#区間和
class CSumSegTree:
#整数nよりも大きい最小の2のべき乗を求める.
    def get_2pow(self, n):
        ret = 1
        while ret < n:
            ret *= 2 
        return ret
    
    #seq: 一番最初に与えられる配列 
    def __init__(self, seq):
        #完全二分木として実装
        size = self.get_2pow(len(seq))

        #0番目は使わない
        #葉ノードよりも上の階層の枝の部分も格納するために×２して配列作成
        self.array = [0 for i in range(2*size)]
        #葉ノード（配列の値をそのまま格納する部分）はsizeのインデックスからスタート
        self.leaf_start = size
        
        #葉ノードの位置に与えられた配列を格納
        for i in range(self.leaf_start, self.leaf_start + len(seq)):
            self.array[i] = seq[i - self.leaf_start]
        
        self.initialize() # セグメント木の構築

    def initialize(self): # セグメント木の構築
        start_i = self.leaf_start
        # 下の層（最下層は葉ノード）から順に値を計算し格納
        while start_i > 1:
            for i in range(start_i, start_i * 2, 2): 
                parent_i = i // 2
                #今回は区間和をもとめる。左右の子ノードの値の合計を親の値として格納
                self.array[parent_i] = self.array[i] + self.array[i+1]
            #１つ上の階層に移動
            start_i = start_i // 2

    def update(self, i, val): # 配列の要素の更新
        node_i = i + self.leaf_start
        self.array[node_i] = val # 葉ノードの更新
        while node_i > 1: # 上に遡って更新
            parent_i = node_i // 2
            self.array[parent_i] = self.array[parent_i*2] +self.array[parent_i*2+1]
            node_i = parent_i

    def findSum(self, l, r, k=1, le=0, re=-1): # 部分和を求める関数
    # l: 指定する区間の左端，r: 指定する区間の右端
    # 半開区間として指定(l番目からr-1番目の部分和)
    # k: self.arrayのインデックス
    # le: self.array[k]に保持されている部分和の区間の左端 
    # re: self.array[k]に保持されている部分和の区間の右端 
    # (le，reも半開区間として指定される.)

        # 最初に呼び出した時は全区間(根ノード) 
        if re==-1:
            re = self.leaf_start
        # 指定する範囲以外なら0を返す 
        if (re < l) or (r <= le):
            return 0
        # 指定する範囲に完全に含まれているなら， # その値を利用する
        if (l <= le) and (re < r): 
            return self.array[k]

        # 子ノードに下がる.sum_lは左側，sum_rは右側の子ノードを見ていることになる.
        sum_l = self.findSum(l, r, 2*k, le, (le+re-1)//2) 
        sum_r = self.findSum(l, r, 2*k+1, (le+re-1)//2+1, re)
        return sum_l + sum_r