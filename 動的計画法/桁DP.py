#A以下B以上の非負整数のうち、「3が付くまたは3の倍数」かつ「8の倍数でない」数の総数を求めるコード
from itertools import product

a = int(input())
b = int(input())

def count(x):
    a = str(x)
    n = len(a)
    #内包表記上、配列は末から書く
    dp=[[[[[0] * 8 for _ in range(3)] for _ in range(2)] for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0][0][0] = 1

    #条件に合わせてDP
    for i, less, has3, mod3, mod8 in product(range(n), (0,1), (0,1), range(3), range(8)):
        #lessフラグがない場合は９まで、ある場合は指定された数のi桁目までの数字を上限にループ
        max_d = 9 if less else int(a[i])
        for d in range(max_d+1):
            less_ = less or d < max_d
            has3_ = has3 or d == 3
            mod3_ = (mod3 + d) % 3
            #8の倍数は下2桁が8で割り切れるかどうかで見分けられるため、mod8の値を10で乗じてd足し上げることで2桁の数字にして判定。
            mod8_ = (mod8*10 + d) % 8
            dp[i + 1][less_][has3_][mod3_][mod8_] += dp[i][less][has3][mod3][mod8]
    
    #合致するものを合算
    ret = 0
    #lessフラグは両方足し上げる、mod８フラグは1~7まで（余りあり）を足し上げる
    for less, mod8 in product((0,1), range(1,8)):
            ret += dp[n][less][1][0][mod8]
            ret += dp[n][less][1][1][mod8]
            ret += dp[n][less][1][2][mod8]
            ret += dp[n][less][0][0][mod8]
    return ret

#a以上b以下の条件に当てはまる数を出力（以下なので、b-1)
print(count(a) - count(b-1))

