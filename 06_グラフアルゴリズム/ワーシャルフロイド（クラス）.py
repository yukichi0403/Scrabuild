class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)]
                  for i in range(N)]  # d[u][v] : 辺uvのコスト(存在しないときはinf)

    def add(self, u, v, c, directed=False):
        """
        0-indexedであることに注意
        u = from, v = to, c = cost
        directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search(self):
        # これを d[i][j]: iからjへの最短距離 にする
        # 本来無向グラフでのみ全域木を考えるが、二重辺なら有向でも行けそう
        # d[i][i] < 0 なら、グラフは負のサイクルを持つ
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        hasNegativeCycle = False
        for i in range(self.N):
            if self.d[i][i] < 0:
                hasNegativeCycle = True
                break
        for i in range(self.N):
            self.d[i][i] = 0
        return hasNegativeCycle, self.d
