from itertools import accumulate

L = list(range(1,7)) #[1,2,3,4,5,6]
AC = list(accumulate(L)) #[1,3,6,10,15,21]

#インデックスずれが起きないように AND lが０でもエラーにならないように先頭に0を追加
AC.insert(0,0)

l,r = 3,5
print(AC[r]-AC[l-1])# 12 AC[r]からAC[l-1]を引くと範囲となる
