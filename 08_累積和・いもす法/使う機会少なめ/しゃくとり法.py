#しゃくとり法
def two_pointers(input_list,limit):
    #右、左のポインターとも最初は0
    l,r = 0,0
    count = 0
    sumval = 0

    #rがリストの範囲内の間だけrを右にずらしていく
    while r < len(input_list):
        sumval += input_list[r]
        r += 1

        #和がlimitを超えたら左のポインターを右にずらしていく
        while sumval > limit:
            sumval -= input_list[l]
            l += 1
            
        #条件を満たす和の数をcountに追加
        count += r - l
    
    return count
