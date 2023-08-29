# https://qiita.com/kuuso1/items/318d42cd089a49eeb332
from collections import deque

def slide_max_index(a, K):
    # max_idx[i]: 区間 [i - K + 1, i] (両側閉区間)における a の最大値を与えるインデックス
    N = len(a)
    max_idx = [0] * N # (長さKに満たない左側領域もついでに計算する)
    deq = deque() # デック．番長順番待ちキューをシミュレートする．インデックスを格納しておく

    for i in range(0,N):
        while deq and deq[0] <= i - K : deq.popleft() # 卒業する
        while deq and a[deq[-1]] < a[i] : deq.pop()   # a[i] の入学で 望みがなくなった先輩達が脱落する
        deq.append(i)                                          # 新入生i は常に番長になる望みがある
        max_idx[i] = deq[0]                                    # 番長順番待ちキューの最左が番長

    return max_idx
