#条件付き二分探索
def is_ok(arg):
    #条件を満たすか問題ごとに定義
    return True,False

#修正
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
            
    #対象の値が単調増加する場合最終的にはokが条件を満たす最小値となる
    return ok

    
