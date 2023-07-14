#繰り返し自乗法
MOD = 998244353 

def power(x,n):
    #0乗は1
    if n == 0:
        return 1
    
    #再帰で呼び出し
    tmp = power(x**2 % MOD,n // 2)
    
    #nが奇数の場合はさらにnをかけて余剰をとる
    if n % 2 == 1:
        tmp = (tmp * x) % MOD
    return tmp