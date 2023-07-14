#普通の辞書と違って存在しないキーに参照してもエラーにならない
from collections import defaultdict

A=[int(i) for i in input().split()]
dd=defaultdict(int)
for a in A:
    dd[a]+=1
