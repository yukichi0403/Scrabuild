
import collections
import heapq


class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d = collections.defaultdict(lambda: float('inf'))
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev

    def getDijkstraShortestPath(self, start, goal):
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]
