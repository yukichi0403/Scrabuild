#条件付き二分探索
def is_ok(arg):
    #条件を満たすか問題ごとに定義
    return True,False

def binary_search(left,right):
    while right - left >= 1:
        mid = (right + left) // 2

        if is_ok(mid):
            right = mid
        else:
            left = mid
            
    #対象の値が単調増加する場合最終的にはright（大きい方）が条件を満たす最小値となる
    return right