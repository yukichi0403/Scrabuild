#　条件付き二分探索
#　keyより大きい最小の値を答える
def binary_search(line,key):
    left = 0
    right = len(line) - 1

    #　回答の値を最小値で定義
    ans = -10 ** 9 - 1

    #　rightがleftを下回るまでループ
    while right >= left:
        pivot = (left + right) // 2
        if key < line[pivot]:
            right = pivot - 1
            #　ターゲットより大きい場合は、その値をansに保持
            ans = line[pivot]
            
        # pivotの値がkeyとイコールになった場合もこっちに流れる
        # この場合leftがpivot+1となり、pivotの値がkey以下となることはない
        # よってこれ以上左側は探索されずいずれright<leftとなるため答えが戻る
        else:
            left = pivot + 1

    if ans > -10 ** 9 - 1:
        return ans
    else:
        #　初期値のままの場合はnot exist を返す
        return 'not exist'
