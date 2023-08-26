N = len(h)  #　Nはリストhの長さ

i = 0
res = 0

while i < N:
    #　0なら何もせず次に進む
    if h[i] == 0:
        i += 1
    #　0以外＝区間の始まり
    else:
        #　区間の数を増やす
        res += 1
        　#　0が出てくるま一気に進む
        while i < N and h[i] > 0:
            i += 1
