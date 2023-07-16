#条件付き二分探索
#keyより大きい最小の値を答える
def binary_search(line,key):
    left = 0
    right = len(line) - 1

    #回答の値を最小値で定義
    ans = -10**9-1
    while right >= left:
        pivot = (left + right) // 2
        if key < line[pivot]:
            right = pivot - 1
            #ターゲットより大きい場合は、その値をansに保持
            ans = line[pivot]
        else:
            left = pivot + 1

    if ans > -10 ** 9 -1:
        return ans
    else:
        #初期値のままの場合はnot exist を返す
        return 'not exist'