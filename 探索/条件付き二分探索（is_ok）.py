#条件付き二分探索
def is_ok(arg):
    #条件を満たすか問題ごとに定義
    return True,False

def binary_search(left,right):
    while abs(right - left) > 1:
        mid = (right + left) // 2

        if is_ok(mid):
            right = mid
        else:
            left = mid

    return right