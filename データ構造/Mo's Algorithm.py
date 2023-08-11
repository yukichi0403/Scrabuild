"""Mo's Algorithm

・使い方
mo=Mo(A,queries): インスタンス生成
ans=mo.ans: 各クエリに対する答えが順番に入ってるリスト
MoStatusの中のTODOのところは、問題ごとに変える

参考URL(ありがとうございます！)
ei3333さんの記事【https://ei1333.hateblo.jp/entry/2017/09/11/211011】
Nyaanさんの記事【https://nyaannyaan.github.io/library/misc/mo.hpp.html】
"""

import math
from operator import itemgetter


class MoStatus():
    def __init__(self, max_element):
        self.cnt = [0] * (max_element + 1)
        self.val = 0

    def add(self, element):
        self.cnt[element] += 1
        # TODO

    def discard(self, element):
        self.cnt[element] -= 1
        # TODO


class Mo():
    def __init__(self, lis, init_queries):
        self.N = len(lis)
        self.lis = lis

        self.Q = len(init_queries)
        self.max_r = -1
        self.init_queries = []
        for qi, query in enumerate(init_queries):
            l, r = query
            self.init_queries.append((l, r, qi))
            if self.max_r < r:
                self.max_r = r

        self.status = MoStatus(max_element=max(self.lis))

        self.section_width = None
        self.separate_cnt = None
        self.separated_queries = None
        self.separated_queries_generator()

        self.ans = [0] * self.Q
        self.solve()

    def separated_queries_generator(self):
        self.section_width = int(
            math.sqrt(3) * self.max_r / math.sqrt(2 * self.Q)) + 1
        self.separate_cnt = (
                                    self.max_r + self.section_width - 1) // self.section_width
        self.separated_queries = [[] for _ in range(self.separate_cnt + 1)]
        for query in self.init_queries:
            l, r, qi = query
            idx = l // self.section_width
            self.separated_queries[idx].append(query)
        for i in range(self.separate_cnt):
            self.separated_queries[i].sort(key=itemgetter(1), reverse=i % 2)

    def solve(self):
        prev_l, prev_r = 0, -1
        for queries_list in self.separated_queries:
            for query in queries_list:
                nl, nr, qi = query
                if nl < prev_l:
                    for i in range(nl, prev_l):
                        element = self.lis[i]
                        self.status.add(element)
                else:
                    for i in range(prev_l, nl):
                        element = self.lis[i]
                        self.status.discard(element)
                if prev_r < nr:
                    for i in range(nr, prev_r, -1):
                        element = self.lis[i]
                        self.status.add(element)
                else:
                    for i in range(prev_r, nr, -1):
                        element = self.lis[i]
                        self.status.discard(element)
                prev_l, prev_r = nl, nr
                self.ans[qi] = self.status.val

