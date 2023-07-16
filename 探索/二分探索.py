#二分探索(基本版）
def binary_search(seq, key):
    left = 0; right = len(seq) - 1
    
    while right >= left:
        pivot = (left + right) // 2
        if seq[pivot] == key: 
            return pivot # 見つかった
        elif seq[pivot] < key:     
            left = pivot + 1 # 対象の値より小さい場合は右側に絞る
        else: 
            right = pivot - 1 # 対象の値より大きい場合は左側に絞る

    # 見つからなかったら-1を返す
    return -1