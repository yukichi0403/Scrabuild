#普通の辞書と違って存在しないキーに参照してもエラーにならない
#dictなのでlenはできないので注意
from collections import defaultdict

A=[int(i) for i in input().split()]
dd=defaultdict(int)
for a in A:
    dd[a]+=1



#キーでソートする場合
#降順でのソート
dd_sorted = sorted(dd.items(), reverse = True, key=lambda x: x[0])
