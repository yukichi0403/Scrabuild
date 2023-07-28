L = list(input())

#中略(要素に対して色々と書き換えを行う)

print(''.join(map(str, L)))
#空白区切りで出力する場合→ print(' '.join(map(str, L)))
#カンマ区切りで出力する場合→ print(','.join(map(str, L)))

print(int(''.join(map(str,  sorted(L, reverse = True)))))
#ソートしたうえで結合する場合
