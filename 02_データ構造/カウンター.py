import collections
#TLEしがちな合算
C1 = collections.Counter([1,1,2,3,5,8])
C2 = collections.Counter([2,4,6,8,10])
C1+=C2
print(C1) #Counter({1: 2, 2: 2, 8: 2, 3: 1, 5: 1, 4: 1, 6: 1, 10: 1})

#速度の早い合算
#（以下の例では行っていないですがC1とC2のlen比較を行って要素数の大きい方をベースとして結合する方が速度が早くなるようです）
C1 = collections.Counter([1,1,2,3,5,8])
C2 = collections.Counter([2,4,6,8,10])
C1.update(C2)
print(C1) #Counter({1: 2, 2: 2, 8: 2, 3: 1, 5: 1, 4: 1, 6: 1, 10: 1})

#most_commonを使うと出現回数でソートできる（タプルになる）
from collections import Counter
a = ['a', 'b', 'c', 'd', 'a', 'a', 'b']
c = Counter(a)
d = c.most_common()

print(d)  # 出現回数順のタプルのリスト
[('a', 3), ('b', 2), ('c', 1), ('d', 1)]

