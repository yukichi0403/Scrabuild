#A以下B以上の非負整数のうち、「3が付くまたは3の倍数」かつ「8の倍数でない」数の総数を求めるコード
from itertools import product

a = int(input())
b = int(input())

def count(x):
    a = str(x)
    n = len(a)
    #配列は末から
    dp=[[[[[0] * 8 for _ in range(3)] for _ in range(2)] for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0][0][0] = 1

    #条件に合わせてDP
    for i, less, has3, mod3, mod8 in product(range(n), (0,1), (0,1), range(3), range(8)):
        max_d = 9 if less else int(a[i])
        for d in range(max_d+1):
            less_ = less or d < max_d
            has3_ = has3 or d == 3
            mod3_ = (mod3 + d) % 3
            mod8_ = (mod8*10 + d) % 8
            dp[i + 1][less_][has3_][mod3_][mod8_] += dp[i][less][has3][mod3][mod8]
    
    #合致するものを合算
    ret = 0
    for less, mod8 in product((0,1), range(1,8)):
            ret += dp[n][less][1][0][mod8]
            ret += dp[n][less][1][1][mod8]
            ret += dp[n][less][1][2][mod8]
            ret += dp[n][less][0][0][mod8]
    return ret

print(count(a) - count(b-1))

