#オープンアドレス法
def hash_put(mod,hashlist,num):
    #追加の場合のクエリ
    ind = num % mod
    #すでに値が入っている場合はその1つ右に入れる
    while hashlist[ind] != -1:
        ind += 1
    hashlist[ind] = num

def hash_search(mod,hashlist,num):
    #余剰のインデックスから線形探索を始める
    start = num % mod
    #対象のインデックスに値が入っていない(＝-1)場合はループが続く（インデクスが右にいき続ける）
    while hashlist[start] != -1 and start < len(hashlist):
        #探索対象の値が見つかったらfoundを返す
        if hashlist[start] == num:
            return 'found'
            break
        start += 1
    #ループを抜けたらnot foundを返す
    return 'not found'


#modの例
mod = 10**6
search_list = [-1] * (mod + 1) 