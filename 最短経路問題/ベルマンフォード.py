inf = float('inf')
class BellmanFord():
    def __init__(self, N):
        self.N = N
        self.edges = []

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
        else:
            self.edges.append([u, v, d])


    def BellmanFord_search(self, start):
        """
        :param s: 始点
        :return: d[i] 始点sから各点iまでの最短経路
        """
        #  infならたどり着けず
        # -infなら"通りたいパスに"負の閉路が存在する
        D = [inf for i in range(self.N)]
        D[start] = 0
        for i in range(self.N*2):
            for u,v,d in self.edges:
                if D[v] > D[u] + d:
                    D[v] = D[u] + d
                    #2巡目負経路が存在する場合の動き
                    if i>=self.N:
                        D[v]=-inf
        return D

